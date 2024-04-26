"""Prune a network."""
import igraph as ig
import numpy as np
import pandas as pd


class PruneNetwork:
    """Create statistics for communication networks by deletion.

    For a given dataset with sender and receiver information,
    create a weighted network with igraph. For a given number
    of iterations, deletion amounts, and deletion types, the
    algorithm then generates network statistics for randomly
    sampled subnetworks.
    """

    def __init__(self, dataframe:pd.DataFrame) -> None:
        """Initialize pruning."""
        self.inputDF = dataframe

    def makeNet(self, dataframe:pd.DataFrame) -> ig.Graph:
        """Create network from dataframe.

        Assumes the existence of sender, receiver and step
        column names.
        """
        networkdata = dataframe[["sender", "receiver", "step"]]
        networkdata = networkdata.groupby(
            ["sender", "receiver"],
            ).size().reset_index(name="Count")
        return ig.Graph.TupleList(
            networkdata.itertuples(index=False), directed=True, weights=True,
        )

    def netStats(self, G:ig.Graph) -> pd.DataFrame:
        """Generate network statistics.

        Any statistic calculated on the full
        network can be added in principle.
        Currently implemented are:
        average relative degree,
        density
        transitivtiy
        cohesion
        average path length
        modularity
        """
        numVs = len(G.vs)
        avg_rel_deg = np.mean([x/numVs for x in G.degree(mode="all")])
        density = G.density()
        transitivity = G.transitivity_undirected()
        cohesion = G.cohesion()
        avg_path_len = G.average_path_length()
        modularity = G.modularity(G.components())
        return pd.DataFrame(
            [
                {
                    "avg_relative_degree": avg_rel_deg,
                    "avg_path_length": avg_path_len,
                    "density": density,
                    "transitivity": transitivity,
                    "cohesion": cohesion,
                    "modularity": modularity,
                },
            ],
        )

    def generatePruningParameters(self, G:ig.Graph) -> pd.DataFrame:
        """Generate a random set of pruning weights."""
        nodes = G.get_vertex_dataframe()
        id2name = G.get_vertex_dataframe().to_dict()["name"]
        rng = np.random.default_rng()
        del_parameter = pd.DataFrame(
            {
                "ids": nodes.index,
                "degree": G.degree(),
                "unif": rng.uniform(0, 1, len(G.vs)),
                "log_normal": rng.lognormal(0, 1, len(G.vs)),
                "exp": rng.exponential(1, len(G.vs)),
                "beta": rng.beta(a=2, b=3, size=len(G.vs)),
            },
        )

        del_parameter = G.get_edge_dataframe()[["source", "target"]].merge(
            del_parameter, left_on="source", right_on="ids",
        ).merge(
            del_parameter, left_on="target", right_on="ids",
        )
        del_parameter["degree"] = del_parameter.degree_x * del_parameter.degree_y / np.dot(
            del_parameter.degree_x, del_parameter.degree_y,
        )
        del_parameter["unif"] = del_parameter.unif_x * del_parameter.unif_y / np.dot(
            del_parameter.unif_x, del_parameter.unif_y,
        )
        del_parameter["log_normal"] = del_parameter.log_normal_x * del_parameter.log_normal_y / np.dot(
            del_parameter.log_normal_x, del_parameter.log_normal_y,
        )
        del_parameter["exp"] = del_parameter.exp_x * del_parameter.exp_y / np.dot(
            del_parameter.exp_x, del_parameter.exp_y,
        )
        del_parameter["beta"] = del_parameter.beta_x * del_parameter.beta_y / np.dot(
            del_parameter.beta_x, del_parameter.beta_y,
        )
        sender = del_parameter["source"].apply(lambda x: id2name[x])
        receiver = del_parameter["target"].apply(lambda x: id2name[x])
        del_parameter.insert(0, "sender", sender)
        del_parameter.insert(0, "receiver", receiver)
        return del_parameter[
            ["sender", "receiver", "degree", "unif", "log_normal", "exp", "beta"]
        ]


    def deleteFromNetwork(
        self,
        iterations: int = 10,
        delAmounts: tuple = (0.1, 0.25, 0.5, 0.75, 0.9),
        delTypes: tuple = ("degree", "unif", "log_normal", "exp", "beta"),
    ) -> pd.DataFrame:
        """Run the deletion by sampling."""
        results = []
        fullNet = self.makeNet(
            self.inputDF,
        )
        fullStats = self.netStats(fullNet)
        fullStats = fullStats.assign(
            delVal=0, delType="NA", delIteration=0,
        )
        results.append(fullStats)
        for idx in range(1, iterations + 1):
            prunVals = self.generatePruningParameters(
                fullNet,
            )
            tempDF = self.inputDF.merge(
                prunVals,
            )
            for val in list(delAmounts):
                for deltype in list(delTypes):
                    delDF = tempDF.sample(
                        round(len(tempDF) * (1 - val)),
                        weights=deltype,
                    )
                    delNet = self.makeNet(delDF)
                    delStats = self.netStats(delNet)
                    delStats = delStats.assign(
                        delVal=val, delType=deltype, delIteration=idx,
                    )
                    results.append(delStats)
        return pd.concat(results)



def prune(
    modelparameters: dict, network: tuple, columns: list,
    iterations: int = 10, delAmounts: tuple = (0.1, 0.25, 0.5, 0.75, 0.9),
    delTypes: tuple = ("degree", "unif")) -> pd.DataFrame:
    """Generate pruned networks from input.

    Assumes existence of columns "sender", "receiver", and "step".
    """
    runDf = pd.DataFrame(network, columns = columns)
    pruning = PruneNetwork(runDf)
    result = pruning.deleteFromNetwork(
        iterations=iterations,
        delAmounts=delAmounts,
        delTypes=delTypes,
    )
    return result.assign(**modelparameters)
