# axrail-backend-test

## Requirements
- Python 3.10+ (3.8+ should also work)

No external libraries are required.

## Project Structure
- `src/main.py`     : Console app entrypoint (reads JSON file, prints answer)
- `src/solver.py`   : Problem solution (limited Bellman-Ford)
- `tests/`          : Unit tests (unittest)
- `inputs/`         : Sample JSON inputs
- `docs/`           : Documentation artifacts (Word doc screenshot template)

## Run the console app
From the repository root:

```bash
cd src
python main.py ../inputs/sample1.json
```

## Run unit tests
From the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Notes for interview
Algorithm: Limited Bellman-Ford / DP by edges.
At most `k` stops => at most `k + 1` flights (edges). We relax edges for `k + 1` rounds, using a snapshot of the previous round to prevent exceeding the edge limit.
