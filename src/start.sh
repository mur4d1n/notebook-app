#!/bin/bash

cd /app && alembic upgrade head
python3 -m uvicorn src.app:app --host 0.0.0.0 --port 8080
