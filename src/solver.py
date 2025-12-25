from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple


@dataclass(frozen=True)
class Flight:
    frm: int
    to: int
    price: int


def cheapest_price_within_k_stops(
    n: int,
    flights: Sequence[Tuple[int, int, int]] | Sequence[Flight],
    src: int,
    dst: int,
    k: int,
) -> int:
    if n <= 0:
        raise ValueError("n must be > 0")
    if not (0 <= src < n) or not (0 <= dst < n):
        raise ValueError("src and dst must be within [0, n)")
    if k < 0:
        return -1

    edges: List[Flight] = []
    for f in flights:
        if isinstance(f, Flight):
            edges.append(f)
        else:
            if len(f) != 3:
                raise ValueError("Each flight must have 3 elements: [from, to, price]")
            a, b, p = f
            edges.append(Flight(int(a), int(b), int(p)))

    INF = 10**18
    prev = [INF] * n
    prev[src] = 0

    for _ in range(k + 1):
        curr = prev[:]
        for e in edges:
            if prev[e.frm] == INF:
                continue
            new_cost = prev[e.frm] + e.price
            if new_cost < curr[e.to]:
                curr[e.to] = new_cost
        prev = curr

    return -1 if prev[dst] >= INF else int(prev[dst])
