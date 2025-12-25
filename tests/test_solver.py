import unittest

from src.solver import cheapest_price_within_k_stops


class TestCheapestFlightsWithinKStops(unittest.TestCase):
    def test_example_1(self):
        n = 4
        flights = [(0,1,100),(1,2,100),(2,0,100),(1,3,600),(2,3,200)]
        self.assertEqual(cheapest_price_within_k_stops(n, flights, 0, 3, 1), 700)

    def test_example_2(self):
        n = 3
        flights = [(0,1,100),(1,2,100),(0,2,500)]
        self.assertEqual(cheapest_price_within_k_stops(n, flights, 0, 2, 1), 200)

    def test_example_3(self):
        n = 3
        flights = [(0,1,100),(1,2,100),(0,2,500)]
        self.assertEqual(cheapest_price_within_k_stops(n, flights, 0, 2, 0), 500)

    def test_no_route(self):
        n = 3
        flights = [(0,1,100)]
        self.assertEqual(cheapest_price_within_k_stops(n, flights, 0, 2, 1), -1)

    def test_k_large_still_ok(self):
        # Ensure it can use more edges if k allows
        n = 4
        flights = [(0,1,1),(1,2,1),(2,3,1),(0,3,10)]
        self.assertEqual(cheapest_price_within_k_stops(n, flights, 0, 3, 2), 3)

    def test_src_dst_range_validation(self):
        with self.assertRaises(ValueError):
            cheapest_price_within_k_stops(3, [(0,1,5)], -1, 2, 1)
        with self.assertRaises(ValueError):
            cheapest_price_within_k_stops(3, [(0,1,5)], 0, 3, 1)

    def test_n_validation(self):
        with self.assertRaises(ValueError):
            cheapest_price_within_k_stops(0, [], 0, 0, 0)

    def test_negative_k(self):
        n = 3
        flights = [(0,1,100),(1,2,100)]
        self.assertEqual(cheapest_price_within_k_stops(n, flights, 0, 2, -1), -1)


if __name__ == "__main__":
    unittest.main()
