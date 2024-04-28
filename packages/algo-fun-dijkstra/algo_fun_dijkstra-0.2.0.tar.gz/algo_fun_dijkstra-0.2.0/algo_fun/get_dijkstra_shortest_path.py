#!/!usr/bin/env python
__program__ = "get_dijkstra_shortest_path.py"
__description__ = "Get the shortest path between vertices of a graph using the dijkstra algorithm"
__date__ = "26/04/2024"
__author__ = "Christophe Lagaillarde"
__version__ = "2.0"
__license__ = "MIT License"
__copyright__ = "Copyright 2024 (c) Christophe Lagaillarde"


def get_dijkstra_shortest_path(graph: dict[str, list[tuple]], starting_node: str) -> dict[str, int]: 
	unvisited_nodes: list[str] = list(graph.keys()) 
	shortest_paths: dict[str, int] = {node: 1000 for node in graph}
	unvisited_nodes.remove(starting_node)
	closest_node: str = starting_node
	shortest_paths[starting_node] = 0

	while unvisited_nodes:	
		for paths in graph[closest_node]:
			if (paths[1] + shortest_paths[closest_node]) < shortest_paths[paths[0]]:
				shortest_paths[paths[0]] = paths[1] + shortest_paths[closest_node]
	
		shortest_paths_of_unvisited = {key: value for key, value in shortest_paths.items() \
if key in unvisited_nodes}
	
		closest_node =  min(shortest_paths_of_unvisited, key=shortest_paths_of_unvisited.get) 
		unvisited_nodes.remove(closest_node)


	return shortest_paths
