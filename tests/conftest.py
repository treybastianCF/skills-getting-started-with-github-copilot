import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Ensure each test starts from the same in-memory dataset."""
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))

    yield

    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
