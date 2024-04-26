"""Test model initialization."""
import networkx as nx
from scicom.historicalletters.model import (
    HistoricalLetters,
)

#####
# Test model setup
#####

def test_model_initialization_with_defaults() -> None:
    """Model initialization puts agents on sheduler."""
    # initialize model for 30 agents with defaults
    model = HistoricalLetters(
        population=30,
    )
    # 30 agents should be on the scheduler
    c1 = 30
    assert len(model.schedule.agents) == c1
    model.run(5)


def test_model_initialization_with_debug() -> None:
    """Model initialization puts agents on sheduler."""
    # initialize model for 30 agents with defaults
    model = HistoricalLetters(
        population=30,
        debug=True,
    )
    # 30 agents should be on the scheduler
    c1 = 30
    assert len(model.schedule.agents) == c1
    model.run(5)


def test_model_initialization_with_socialnet() -> None:
    """Model initialization puts agents on sheduler."""
    # initialize model for 30 agents with defaults
    model = HistoricalLetters(
        population=30,
        useSocialNetwork=True,
        debug=True,
    )
    # 30 agents should be on the scheduler
    c1 = 30
    assert len(model.schedule.agents) == c1
    model.run(5)


def test_model_initialization_with_activations() -> None:
    """Model initialization puts agents on sheduler."""
    # initialize model for 30 agents with defaults
    model = HistoricalLetters(
        population=30,
        useActivation=True,
        debug=True,
    )
    # 30 agents should be on the scheduler
    c1 = 30
    assert len(model.schedule.agents) == c1
    model.run(5)


def test_model_initialization_with_pruning() -> None:
    """Model initialization puts agents on sheduler."""
    # initialize model for 30 agents with defaults
    model = HistoricalLetters(
        population=30,
        runPruning=True,
        debug=True,
    )
    # 30 agents should be on the scheduler
    c1 = 30
    assert len(model.schedule.agents) == c1
    model.run(5)


def test_model_smallworldiness() -> None:
    """Test if parameter changes increase smallworldiness."""
    model1 = HistoricalLetters(
        population=30,
        useSocialNetwork=True,
        longRangeNetworkFactor=0.3,
        shortRangeNetworkFactor=0.4,
    )
    model2 = HistoricalLetters(
        population=30,
        useSocialNetwork=True,
        longRangeNetworkFactor=0.1,
        shortRangeNetworkFactor=0.4,
    )
    G1 = nx.Graph(model1.socialNetwork)
    G2 = nx.Graph(model2.socialNetwork)
    om1 = nx.smallworld.omega(G1, niter=1, nrand=1)
    om2 = nx.smallworld.omega(G2, niter=1, nrand=1)
    assert om1 < om2
