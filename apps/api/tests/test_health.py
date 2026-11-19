from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

from rulebound import __version__
from rulebound.main import app


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


async def test_healthz_returns_ok_without_dependencies(client: AsyncClient) -> None:
    resp = await client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "version": __version__}


@pytest.mark.integration
async def test_readyz_reports_database_up(client: AsyncClient) -> None:
    resp = await client.get("/readyz")
    assert resp.status_code == 200
    assert resp.json()["database"] == "up"
