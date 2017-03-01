#!/usr/bin/env python
##############################
# Graph data structure
##############################
# ===========================================================================
# Copyright 2017 `Tung Thanh Le` 
# Email: ttungl at gmail dot com
#
# Heterogeneous Architecture Configurations Generator for Multi2Sim simulator
# (aka, `HeteroArchGen4M2S`)
# `HeteroArchGen4M2S` is free software, which is freely to be
# redistributed and modified it under the terms of 
# the GNU General Public License as published by
# the Free Software Foundation. 
# For more details `http://www.gnu.org/licenses`
# `HeteroArchGen4M2S` is written to help you configure M2S 
# easily, but non-warranty and non-mechantability.
# ============================================================================
# sources: 
# http://stackoverflow.com/a/30747003/2881205
# How to import classes: http://stackoverflow.com/a/4142178/2881205
# find paths in graphs: https://www.python.org/doc/essays/graphs/

from collections import defaultdict

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    ## Tung Le added [02/28/17] 
    def find_all_paths(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return [path]
		if start not in self._graph:
			return []
		paths = []
		for node in self._graph[start]:
			if node not in path:
				newpaths = self.find_all_paths(node, end, path)
				for newpath in newpaths:
					paths.append(newpath)
		return paths

    ## Tung Le added [02/28/17]	
    def find_shortest_path(self, start, end, path=[]):
		path = path + [start]
		if start == end:
			return path
		if start not in self._graph:
			return None
		shortest = None
		for node in self._graph[start]:
			if node not in path:
				newpath = self.find_shortest_path(node, end, path)
				if newpath:
					if not shortest or len(newpath) < len(shortest):
						shortest = newpath
		return shortest

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
