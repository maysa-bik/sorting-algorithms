import unittest

from app.sorting import get_sorting_algorithm


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([5, 3, 1, 2, 6, 4], [1, 2, 3, 4, 5, 6]),
            ([], []),
            ([1], [1]),
            ([1, 1, 1, 1], [1, 1, 1, 1]),
            ([5, -3, 1, -2, 6, 4], [-3, -2, 1, 4, 5, 6])
        ]
        self.algorithms = ['Selection Sort', 'Bubble Sort', 'Insertion Sort']

    def test_sorting_algorithms(self):
        for algorithm_name in self.algorithms:
            with self.subTest(algorithm_name=algorithm_name):
                sort_function = get_sorting_algorithm(algorithm_name)
                for input_list, expected in self.test_cases:
                    result = list(sort_function(input_list))[-1]
                    self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
