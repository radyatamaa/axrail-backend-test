from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from solver import cheapest_price_within_k_stops


def _lower_keys(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k).lower(): _lower_keys(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_lower_keys(x) for x in obj]
    return obj


def load_input_json(path: Union[str, Path]) -> Dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input JSON not found: {p}")

    data = json.loads(p.read_text(encoding="utf-8"))
    data = _lower_keys(data)

    n = int(data["n"])
    src = int(data["src"])
    dst = int(data["dst"])
    k = int(data["k"])

    flights_raw = data["flights"]
    flights: List[Tuple[int, int, int]] = []

    if isinstance(flights_raw, list) and (len(flights_raw) == 0 or isinstance(flights_raw[0], list)):
        for item in flights_raw:
            if not (isinstance(item, list) and len(item) == 3):
                raise ValueError("Invalid flights format. Expected list of [from,to,price].")
            flights.append((int(item[0]), int(item[1]), int(item[2])))
    elif isinstance(flights_raw, list) and (len(flights_raw) == 0 or isinstance(flights_raw[0], dict)):
        for item in flights_raw:
            if not isinstance(item, dict):
                raise ValueError("Invalid flights format. Expected list of objects.")
            item = _lower_keys(item)
            flights.append((int(item["from"]), int(item["to"]), int(item["price"])))
    else:
        raise ValueError("Invalid flights format. Expected list.")

    return {"n": n, "flights": flights, "src": src, "dst": dst, "k": k}


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("Usage: python main.py <input.json>")
        return 2

    try:
        inp = load_input_json(argv[1])
        ans = cheapest_price_within_k_stops(**inp)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    print(f"Input: n={inp['n']}, src={inp['src']}, dst={inp['dst']}, k={inp['k']}")
    print(f"Flights: {inp['flights']}")
    print(f"Result: {ans}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
