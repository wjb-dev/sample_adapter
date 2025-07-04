import pytest
from haraka_runtime.orchestrator.orchestrator import Orchestrator

from app.main import SampleAdapter


@pytest.fixture
def orchestrator():
    """
    Provides a fresh Orchestrator instance for each test.
    """
    return Orchestrator()


@pytest.fixture
def adapter(orchestrator):
    """
    Provides a SampleAdapter already registered with the orchestrator.
    """
    adapter = SampleAdapter()
    orchestrator.use(adapter, priority=1)
    return adapter
