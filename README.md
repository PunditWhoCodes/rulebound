# Rulebound

An AI booking agent for service businesses. The model works out what the customer wants; deterministic code decides what's allowed.

Work in progress. No results yet. Any numbers that appear here later will come from a committed eval run.

## Why

Most AI receptionists enforce business rules ("no cancellations within 24 hours") through the prompt alone. Push hard enough, or talk long enough, and the model breaks them. Rulebound puts those rules in a policy engine that every booking tool has to go through, then measures how often each approach gets it wrong.

## Running locally

Needs [uv](https://docs.astral.sh/uv/) and Docker.

```bash
docker compose up -d db
cd apps/api
uv sync
uv run pytest
uv run uvicorn rulebound.main:app --reload
```

Checks CI runs:

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy src tests
```

## License

MIT
