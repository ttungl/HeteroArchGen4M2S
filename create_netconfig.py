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
	f = open('configs/netconfig', 'w');

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
		array =[]	
		array.extend(read_data(LOCAL_LINKS_PATH))
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
					f.write("Bandwidth = %0.f\n" % LOCAL_LINKWIDTH);
			f.write("\n");
		
		## XY-routing
			# [Network.mynet.Routes]
			# N1.to.N2 = S1
			# S1.to.N2 = S2

			# N1.to.N3 = S1
			# S1.to.N3 = S2
			# S2.to.N3 = S3

			# N1.to.N4 = S1
			# S1.to.N4 = S4
			###################	


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
	# 	##
	# 	##
	# 	print 'You are not expected to be here!'

# --
## for testing
# LOCALLINKS_PATH = 'results_hybrid_local_links/test_topoA_hybridlinks_4x4.txt'
# HYBRIDLINKS_PATH = 'results_hybrid_local_links/test_topoA_locallinks_4x4.txt'
# create_netconfig(16, 512, 2, LOCALLINKS_PATH, HYBRIDLINKS_PATH,)






