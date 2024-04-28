#!/!usr/bin/env python
__program__ = "test_get_dijkstra_shortest_path.py"
__description__ = "test the function get_dijkstra_shortest_path" 
__date__ = "26/04/24"
__author__ = "Christophe Lagaillarde"
__version__ = "2.0"
__license__ = "MIT License"
__copyright__ = "Copyright (c) 2024 Christophe Lagaillarde"

import sys
sys.path.append('../')
from algo_fun.get_dijkstra_shortest_path import get_dijkstra_shortest_path


def test_get_dijkstra_shortest_path() -> None:

	graph_1: dict[str, list[tuple]] = {
	    'A': [('B', 4), ('H', 8)],
            'B': [('A', 4), ('H', 11), ('C', 8)],
	    'C': [('B', 8), ('D', 7), ('I', 2), ('F', 4)],
	    'D': [('C', 7), ('E', 9), ('F', 14)],
	    'E': [('D', 9), ('F', 10)],
	    'F': [('E', 10), ('D', 14), ('C', 4), ('G', 2)],
	    'G': [('F', 2), ('H', 1), ('I', 6)],
	    'H': [('G', 1), ('I', 7), ('B', 11), ('A', 8)],
	    'I': [('H', 7), ('G', 6), ('C', 2)]
	}
	expected_shortest_path_1: dict[str, int] = {'A': 0, 'B': 4, 'C': 12, 'D': 19, 'E': 21, \
 'F': 11, 'G': 9, 'H': 8, 'I': 14}

	graph_2: dict[str, list[tuple]] = {
	    'A': [('B', 2), ('C', 6)],
	    'B': [('A', 2), ('D', 5)],
	    'C': [('A', 6), ('D', 8)],
	    'D': [('C', 8), ('B', 5), ('E', 10), ('F', 15)],
	    'E': [('D', 10), ('F', 6), ('G', 2)],
	    'F': [('D', 15), ('E', 6), ('G', 6)],
	    'G': [('E', 2), ('F', 6)]
	}
	expected_shortest_path_2: dict[str, int] = {'A': 0, 'B': 2, 'C': 6, 'D': 7, \
 'E': 17, 'F': 22, 'G': 19}

	graph_3: dict[str, list[tuple]] = {
	    'A': [('B', 4), ('C', 5)],
	    'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
	    'C': [('A', 5), ('B', 11), ('E', 3)],
	    'D': [('B', 9), ('E', 13), ('F', 2)],
	    'E': [('B', 7), ('C', 3), ('D', 13), ('F', 6)],
	    'F': [('D', 2), ('E', 6)]
	}
	expected_shortest_path_3: dict[str, int] = {'A': 0, 'B': 4, 'C': 5, 'D': 13, 'E': 8, 'F': 14}	

	assert get_dijkstra_shortest_path(graph_1, 'A') == expected_shortest_path_1
	assert get_dijkstra_shortest_path(graph_2, 'A') == expected_shortest_path_2
	assert get_dijkstra_shortest_path(graph_3, 'A') == expected_shortest_path_3

	return None

if __name__ == '__main__':
	test_get_dijkstra_shortest_path()
