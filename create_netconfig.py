#!/usr/bin/env python
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

from read_sdpairs import read_data
from graph_datastructure import Graph

# LOCAL_LINKS_PATH: to file of the optimized results (local links)
# HYBRID_LINKS_PATH: to file of the optimized results (hybrid links)
# network_mode: 
	# 0: 2D-Mesh [Default]
	# 1: Customized 2D-Mesh Network [+PATHS]
	# 2: Torus
	# [Add later] 3: Ring
	
import math # use sqrt


def create_netconfig(num_of_nodes, L2_blocksize, network_mode, LOCAL_LINKS_PATH, HYBRID_LINKS_PATH, LOCAL_LINKWIDTH, HYBRID_LINKWIDTH):
	## check input validation
	assert (num_of_nodes>0), 'Error! number of nodes should be a non-zero number!'
	assert ((math.sqrt(num_of_nodes)*math.sqrt(num_of_nodes))==num_of_nodes), 'Error! number of nodes should be a square number! e.g, 3x3 or 5x5'
	assert (network_mode>=0 & network_mode < 4), 'Error! the number should be greater than zero and less than four!'

	# bandwidth and buffer size	
	if network_mode == 1: ## for customized 2D-Mesh
		bandwidth 	= LOCAL_LINKWIDTH + 8;
		bufferSize 	= bandwidth*num_of_nodes;
	else:
		bandwidth 	= L2_blocksize + 8; # bandwidth = L2_blocksize + 8;
		bufferSize 	= bandwidth * num_of_nodes;
	
	# File name
	# f = open('configs/netconfig', 'w');
	f = open('configs/netconfig_XYrouting', 'w');

	if network_mode == 0: 
		f.write(";; 2D-Mesh Network.\n");
	if network_mode == 1: 
		f.write(";; Customized 2D-Mesh Network.\n");
	if network_mode == 2: 
		f.write(";; 2D-Torus Network.\n");
	if network_mode == 3: 
		f.write(";; Ring Network.\n");

	f.write(";; Interconnection network net-l2-mm.\n");
	f.write("\n");
	f.write("[Network.net-l2-mm]\n");
	f.write("DefaultInputBufferSize = %0.f\n" % bufferSize);
	f.write("DefaultOutputBufferSize = %0.f\n" % bufferSize);
	f.write("DefaultBandwidth = %0.f\n" % bandwidth);
	f.write("\n");
	f.write("\n");

	# Switches
	## Number of switches depends on the topology.
	## If 2D-Mesh, the number of switches is equal to the number of nodes.
	## If Ring, the number of switches > number of nodes.
	## For simplicity, we set the default topology to be 2D-Mesh.
	f.write(";; Switches.\n");
	f.write("\n");
	for i in range(num_of_nodes):
		f.write("[Network.net-l2-mm.Node.sw%0.f]\n" % i);
		f.write("Type = Switch\n");
		f.write("\n");
	f.write("\n");

	# Nodes
	f.write(";; Nodes.\n");
	f.write("\n");
	for i in range(num_of_nodes):
		f.write("[Network.net-l2-mm.Node.n%0.f]\n" % i);
		f.write("Type = EndNode\n");
		f.write("\n");
	f.write("\n");

	# Links
	f.write(";; Links connection between switches and nodes.\n");
	f.write("\n");
	for i in range(num_of_nodes):
		f.write("[Network.net-l2-mm.Link.sw%0.f-n%0.f]\n" % (i, i));
		f.write("Source = sw%0.f\n" % i);
		f.write("Dest = n%0.f\n" % i);
		f.write("Type = Bidirectional\n");
		f.write("\n");
	f.write("\n");

	f.write(";; Links connection among the switches to form the interconnection network.\n");
	f.write("\n");
	## [default] 2D-Mesh network 
	if network_mode == 0:
		###################################################################################
		## 2D-Mesh 
		## num_of_nodes should be a square number in order to create a symmetric network, i.e., 4x4 (in mesh).  
		x_dim = num_of_nodes/math.sqrt(num_of_nodes);
		y_dim = x_dim;
		count = 0;
		# vertical links
		for i in range(num_of_nodes):
			if i<(num_of_nodes-y_dim):
				count = count + 1;
				if count == y_dim: 
					count = 0;
					# vertical
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, y_dim+i));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (y_dim+i));
					f.write("Type = Bidirectional\n");
					f.write("\n");
				else:
					# horizontal
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, i+1));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (i+1));
					f.write("Type = Bidirectional\n");
					f.write("\n");

					# vertical
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, y_dim+i));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (y_dim+i));
					f.write("Type = Bidirectional\n");
					f.write("\n");
			else:
				if i < (num_of_nodes-1):
					# vertical
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, i+1));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (i+1));
					f.write("Type = Bidirectional\n");
					f.write("\n");
		f.write("\n");

		#### XY-routing
		f.write("[Network.mynet.Routes]\n");

		## build the coordinate xy
		countX = 0
		countY = 0
		array3 = [] ## XY coordinate
		for i in range(num_of_nodes):
			if countY % math.sqrt(num_of_nodes) == 0:
				countY = 0
				countX = countX + 1
				array3.extend([[countX-1, countY]])
			else:
				array3.extend([[countX-1, countY]])
			countY = countY + 1

		## build all pairs in the network
		array4 = [] ## all sd-pairs in the network
		for i in range(num_of_nodes):
			for j in range(num_of_nodes):
				if not i==j:
					array4.extend([[i,j]])
		##
		# print array3
		print array4

		# close
		f.close();
		
	## Customized 2D-Mesh network
	if network_mode == 1:
		## Customized 2D-Mesh 
		## num_of_nodes should be a square number in order to create a symmetric network, i.e., 4x4 (in mesh).  
		## XY-routes should be added in this customized network in order to avoid the deadlock.
		
		## For hybrid links
		array =[]
		array.extend(read_data(HYBRID_LINKS_PATH))
		# sort
		array = sorted(array)
		for ePair in array:
			# print ePair
			count = 0;
			for eElem in ePair:
				count = count + 1;
				if count == 1:
					src = eElem-1
				if count == 2:
					count = 0; ## reset
					dst = eElem-1
					## 
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (src, dst));
					f.write("Source = sw%0.f\n" % src);
					f.write("Dest = sw%0.f\n" % dst);
					f.write("Type = Bidirectional\n");
					f.write("Bandwidth = %0.f\n" % HYBRID_LINKWIDTH);
			f.write("\n");

		## For local links
		array1 =[]	
		array1.extend(read_data(LOCAL_LINKS_PATH))
		# sort
		array1 = sorted(array1)
		for ePair in array1:
			# print ePair
			count = 0;
			for eElem in ePair:
				count = count + 1;
				if count == 1:
					src = eElem-1
				if count == 2:
					count = 0; ## reset
					dst = eElem-1
					## 
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (src, dst));
					f.write("Source = sw%0.f\n" % src);
					f.write("Dest = sw%0.f\n" % dst);
					f.write("Type = Bidirectional\n");
					f.write("Bandwidth = %0.f\n" % LOCAL_LINKWIDTH);
			f.write("\n");
		
		###################	Shortest Path Routing protocol 
		f.write("[Network.mynet.Routes]\n");
		
		array2 = [] ## local+hybrid links
		array2.extend(array) ## node id starts from 1.
		array2.extend(array1) 
		
		## build the coordinate xy
		countX = 0
		countY = 0
		array3 = [] ## coordinate
		for i in range(num_of_nodes):
			if countY % math.sqrt(num_of_nodes) == 0:
				countY = 0
				countX = countX + 1
				array3.extend([[countX-1, countY]])
			else:
				array3.extend([[countX-1, countY]])
			countY = countY + 1
		
		## subtract each elem in pairs in the list by 1; 
		##   due to the node IDs start from zero;
		array2[:] = [(x-1,y-1) for (x,y) in array2]

		# array2: customized network (local+hybrid links) 
		# array3: the XY coordinate
		##################################################
		array4 = [] ## all sd-pairs in the network
		for i in range(num_of_nodes):
			for j in range(num_of_nodes):
				if not i==j:
					array4.extend([[i,j]])
		##################################################
		# 1. Find the shortest path from `src` to `dst` using dijkstra's algorithm.
		# 2. Form the routes following the m2s format.

		## 1.
		array2 = sorted(array2)
		gx = Graph(array2, directed=True)
		
		## 2. 
		f.write(";; Bidirectional routes\n\n")
		for (s,d) in array4:
			path = gx.find_shortest_path(s,d)
			if path:
				# print path
				for (index,node) in enumerate(path):
					if index==0:
						f.write("n%d.to.n%d = sw%d\n" % (path[index], path[(len(path)-1)], path[index]));
					else:
						f.write("sw%d.to.n%d = sw%d\n" % (path[index-1], path[(len(path)-1)], path[index]));					
				f.write("\n")
				## 
				revpath = path[::-1] ## reversed path
				# print revpath
				for (index,node) in enumerate(revpath):
					if index==0:
						f.write("n%d.to.n%d = sw%d\n" % (revpath[index], revpath[(len(path)-1)], revpath[index]));
					else:
						f.write("sw%d.to.n%d = sw%d\n" % (revpath[index-1], revpath[(len(path)-1)], revpath[index]));
				f.write("\n")
					
		# close
		f.close();

	## 2D-Torus network 
	if network_mode == 2:
		## Torus (combine between network 1 and 2)
		## num_of_nodes should be a square number in order to create a symmetric network, i.e., 4x4 (in torus).  
		x_dim = num_of_nodes/math.sqrt(num_of_nodes);
		y_dim = x_dim;
		count = 0;
		# network 1: 2D-Mesh
		for i in range(num_of_nodes):
			if i<(num_of_nodes-y_dim):
				count = count + 1;
				if count == y_dim: ## bottom node
					count = 0;
					# vertical
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, y_dim+i));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (y_dim+i));
					f.write("Type = Bidirectional\n");
					f.write("\n");
				else: ## between top and bottom edges.
					# horizontal
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, i+1));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (i+1));
					f.write("Type = Bidirectional\n");
					f.write("\n");

					# vertical
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, y_dim+i));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (y_dim+i));
					f.write("Type = Bidirectional\n");
					f.write("\n");
			else:
				if i < (num_of_nodes-1): 
					# vertical
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, i+1));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (i+1));
					f.write("Type = Bidirectional\n");
					f.write("\n");
		
		count=0 ## reset counter
		## network 2: Torus contour links only
		for i in range(num_of_nodes):
			# if i<(num_of_nodes-y_dim):
			if count==0:
				## node has 2 links
				f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, (y_dim-1)));
				f.write("Source = sw%0.f\n" % i);
				f.write("Dest = sw%0.f\n" % (y_dim-1));
				f.write("Type = Bidirectional\n");
				f.write("\n");


				f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, num_of_nodes-y_dim));
				f.write("Source = sw%0.f\n" % i);
				f.write("Dest = sw%0.f\n" % (num_of_nodes-y_dim));
				f.write("Type = Bidirectional\n");
				f.write("\n");

			else:
				if count < y_dim:
					## node has 1 link
					f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, i+ num_of_nodes-y_dim ));
					f.write("Source = sw%0.f\n" % i);
					f.write("Dest = sw%0.f\n" % (i+ num_of_nodes-y_dim));
					f.write("Type = Bidirectional\n");
					f.write("\n");

				else: ## count > y_dim
					if count % y_dim == 0:
						## node (id+y_dim)
						f.write("[Network.net-l2-mm.Link.sw%0.f-sw%0.f]\n" % (i, (i+ y_dim-1)));
						f.write("Source = sw%0.f\n" % i);
						f.write("Dest = sw%0.f\n" % (i+ y_dim-1));
						f.write("Type = Bidirectional\n");
						f.write("\n");
			## count
			count = count +1;

		f.write("\n");
		# close
		f.close();

	## Ring network
	# if network_mode == 3:
	# 	print 'This will be updated soon!'

# --
## for testing
HYBRIDLINKS_PATH = 'results_hybrid_local_links/test_topoA_hybridlinks_4x4.txt'
LOCALLINKS_PATH = 'results_hybrid_local_links/test_topoA_locallinks_4x4.txt'
HYBRID_LINKWIDTH 	= 32 	## Bytes per cycle (frequency*bandwidth(= 2.4GHz * 32Bytes/cyc ~ 80GBps)) 
LOCAL_LINKWIDTH 	= 16
num_of_nodes = 16
L2_blocksize = 512
network_mode = 0

# create_netconfig(16, 512, 1, LOCALLINKS_PATH, HYBRIDLINKS_PATH,)
create_netconfig(num_of_nodes, L2_blocksize, network_mode, LOCALLINKS_PATH, HYBRIDLINKS_PATH, LOCAL_LINKWIDTH, HYBRID_LINKWIDTH);




