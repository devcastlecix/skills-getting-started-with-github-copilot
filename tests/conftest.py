import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture()
def original_activities():
    return copy.deepcopy(activities)


@pytest.fixture()
def client(original_activities):
    activities.clear()
    activities.update(copy.deepcopy(original_activities))

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(copy.deepcopy(original_activities))