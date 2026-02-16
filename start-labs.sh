#!/bin/bash
# Start all Lab project servers

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting Lab servers..."

# Festival Tracker (port 8000)
cd "$DIR/projects/festival-tracker"
source .venv/bin/activate
uvicorn api:app --host 0.0.0.0 --port 8000 &
echo "  Festival Tracker → http://127.0.0.1:8000"

# Film Stocks (port 8001)
cd "$DIR/projects/film-stocks"
source .venv/bin/activate
uvicorn api:app --host 0.0.0.0 --port 8001 &
echo "  Film Stocks      → http://127.0.0.1:8001"

# NYC Film Scene Map (port 8002)
cd "$DIR/projects/nyc-film-map"
source .venv/bin/activate
uvicorn api:app --host 0.0.0.0 --port 8002 &
echo "  NYC Film Map     → http://127.0.0.1:8002"

echo ""
echo "All servers running. Press Ctrl+C to stop all."
wait
