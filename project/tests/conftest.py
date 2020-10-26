# -*- coding: utf-8 -*-
import os
from datetime import datetime

import pytest
from app.config import Settings, get_settings
from app.main import create_application
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

urls = [
    (
        "https://lifehacker.com/how-can-i-find-out-if"
        "-my-partner-is-interacting-with-ca-1845461967"
    ),
    (
        "https://vitals.lifehacker.com/"
        "theres-now-an-fda-approved-treatment-for-covid-19-1845465558"
    ),
    (
        "https://vitals.lifehacker.com/"
        "theres-now-an-fda-approved-treatment-for-covid-19-1845465558"
    ),
]


def get_settings_override():
    return Settings(
        testing=1,
        database_url=os.environ.get("DATABASE_TEST_URL"),
    )


@pytest.fixture(scope="module")
def test_app():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:

        # testing
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        yield test_client


@pytest.fixture(scope="function")
def test_data():
    """
    This fixture returns a single mock summary.
    """
    data = {
        "id": 1,
        "url": "https://foo.bar",
        "summary": "summary",
        "created_at": datetime.utcnow().isoformat(),
    }
    return data


@pytest.fixture(scope="function")
def test_data_list():
    """
    This fixture returns a moce list of summaries.
    """
    test_data = [
        {
            "id": 1,
            "url": "https://foo.bar",
            "summary": "summary",
            "created_at": datetime.utcnow().isoformat(),
        },
        {
            "id": 2,
            "url": "https://testdrivenn.io",
            "summary": "summary",
            "created_at": datetime.utcnow().isoformat(),
        },
    ]
    return test_data


@pytest.fixture(scope="function", params=urls)
def test_request_payload(request):
    """
    This is just a dummy payload for a request.
    """
    return request.param


@pytest.fixture(scope="function")
def test_response_payload():
    """
    Dummy payload response.
    """
    return {"id": 1, "url": "https://foo.bar"}


@pytest.fixture(scope="function", params=urls)
def dummy_url(request):
    """
    Dummy URLs for the summerizer to chew on.
    """
    return request.param
