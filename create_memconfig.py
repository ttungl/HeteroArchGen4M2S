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

# Description: This generates `memconfig` file for M2S
# Each core has its own Instruction-L1$ and Data-L1$, or with shared I-L1$.
# ===========================================================

def create_memconfig( 	num_of_cpu_cores, 	# number of CPU cores
						num_of_gpu_cores,	# number of GPU cores
						type_of_gpu,	# type of GPU
						num_of_MC, 		# number of memory controllers
						L1_Inst_shared,	# enable/disable (1/0) shared Instruction L1$
						L1_size,		# size of L1$ (kB)
						L1_assoc,		# associativity of L1$ (#-way) 
						L2_size,		# size of L2$ (kB)
						L2_assoc,		# associativity of L2$ (#-way)
						L1_latency,		# latency of L1$ (cycles)
						L2_latency,		# latency of L2$ (cycles)
						L1_blocksize,	# blocksize of L1$ (Bytes)
						L2_blocksize,	# blocksize of L2$ (Bytes)
						Memory_latency, # latency of DRAM main memory
						GPU_L1_size,	# size of L1$ (kB)
						GPU_L1_assoc,	# associativity of L1$ (kB)
						GPU_L2_size,	# size of L2$ (kB)
						GPU_L2_assoc,	# associativity of L2$ (kB)
						GPU_L1_latency, # latency of L1$ (cycles)
						GPU_L2_latency, # latency of L2$ (cycles)
						GPU_L1_blocksize, # blocksize of L1$ (Bytes)
						GPU_L2_blocksize):# blocksize of L2$ (Bytes) 
	# check inputs validation
	assert (num_of_cpu_cores>=4), "Error! Number of CPU cores must be at least 4; range [4,8,16,32,64];"
	assert (num_of_gpu_cores>=4), "Error! Number of compute units in GPU must be at least 4; range [4,8,16,32,64];"
	assert (num_of_MC>=4), "Error! Number of memory controllers must be at least 4; range [4,8,12,16,20,24,28,30,32];"
	# bandwidth and buffer size
	bandwidth = L2_blocksize + 8;
	bufferSize = bandwidth * 16;

	# Nodes counter
	Nodes_counter = 0;

	# File name
	f = open('configs/memconfig', 'w');

	# Cache Geometry I-L1$ for CPUs
	# f.write(";; Cache Geometry I-L1$ for CPUs.\n");
	f.write(";; Cache Geometry for CPUs and GPUs.\n");
	f.write(";; (Summary at the end of this file)\n");		
	f.write("\n");
	f.write("[CacheGeometry geo-cpu-i-l1]\n");
	f.write("Sets = %0.f\n" % (L1_size*1024/L1_assoc/L1_blocksize));
	f.write("Assoc = %0.f\n" % L1_assoc);
	f.write("BlockSize = %0.f\n" % L1_blocksize);
	f.write("Latency = %0.f\n" % L1_latency);
	f.write("Policy = LRU\n");
	f.write("Ports = 2\n");
	f.write("\n");

	# Cache Geometry D-L1$ for CPUs
	# f.write(";; Cache Geometry D-L1$ for CPUs.\n");
	# f.write("\n");
	f.write("[CacheGeometry geo-cpu-d-l1]\n");
	f.write("Sets = %0.f\n" % (L1_size*1024/L1_assoc/L1_blocksize));
	f.write("Assoc = %0.f\n" % L1_assoc);
	f.write("BlockSize = %0.f\n" % L1_blocksize);
	f.write("Latency = %0.f\n" % L1_latency);
	f.write("Policy = LRU\n");
	f.write("Ports = 2\n");
	f.write("\n");

	# Cache Geometry L2$ for CPUs
	# f.write(";; Cache Geometry L2$ for CPUs.\n");
	# f.write("\n");
	f.write("[CacheGeometry geo-cpu-l2]\n");
	f.write("Sets = %0.f\n" % (L2_size*1024/L2_blocksize/L2_assoc));
	f.write("Assoc = %0.f\n" % L2_assoc);
	f.write("BlockSize = %0.f\n" % L2_blocksize);
	f.write("Latency = %0.f\n" % L2_latency);
	f.write("Policy = LRU\n");
	f.write("Ports = 4\n");
	f.write("\n");

	# Cache Geometry L1$ for GPUs
	# f.write(";; Cache Geometry L1$ for GPUs.\n");
	# f.write("\n");
	f.write("[CacheGeometry geo-gpu-l1]\n");
	f.write("Sets = %0.f\n" % (GPU_L1_size*1024/GPU_L1_blocksize/GPU_L1_assoc));
	f.write("Assoc = %0.f\n" % GPU_L1_assoc);
	f.write("BlockSize = %0.f\n" % GPU_L1_blocksize);
	f.write("Latency = %0.f\n" % GPU_L1_latency);
	f.write("Policy = LRU\n");
	f.write("Ports = 2\n");
	f.write("\n");

	# Cache Geometry L2$ for GPUs
	f.write(";; Cache Geometry L2$ for GPUs.\n");
	f.write("\n");
	f.write("[CacheGeometry geo-gpu-l2]\n");
	f.write("Sets = %0.f\n" % (GPU_L2_size*1024/GPU_L2_blocksize/GPU_L2_assoc));
	f.write("Assoc = %0.f\n" % GPU_L2_assoc);
	f.write("BlockSize = %0.f\n" % GPU_L2_blocksize);
	f.write("Latency = %0.f\n" % GPU_L2_latency);
	f.write("Policy = LRU\n");
	f.write("Ports = 4\n");
	f.write("\n");
	f.write("\n");

	# Data cache (D-L1)
	f.write(";; %0.f Data cache (D-L1$) for CPUs.\n" % num_of_cpu_cores);
	f.write("\n");
	count_L2_cache_inc = 0;
	L2_cache_inc = 0;
	for i in range(num_of_cpu_cores):
		## increase
		count_L2_cache_inc = count_L2_cache_inc + 1;
		## to_file
		f.write("[Module mod-cpu-dl1-%0.f]\n" % i);
		f.write("Type = Cache\n");
		f.write("Geometry = geo-cpu-d-l1\n");
		f.write("LowNetwork = net-cpu-l1-l2-%0.f\n" % L2_cache_inc);
		# f.write("LowNetworkNode = mod-cpu-l2-%0.f\n" % L2_cache_inc); # debugging 020317.v1
		f.write("LowModules = mod-cpu-l2-%0.f\n" % L2_cache_inc); # debugging 020317.v1
		f.write("\n");
		## check increasing and reset
		if count_L2_cache_inc==2:
			count_L2_cache_inc = 0; # reset
			L2_cache_inc = L2_cache_inc + 1;
	f.write("\n");
	
	# Instruction cache (I-L1)
	## Note: if I-L1 is shared, (#cores/2) instead #cores.
	if L1_Inst_shared ==1:
		num_of_cpu_cores_shared = num_of_cpu_cores/2;
	else:
		num_of_cpu_cores_shared = num_of_cpu_cores;

	f.write(";; %0.f Instruction cache (I-L1$) for CPUs.\n" % num_of_cpu_cores_shared);
	f.write("\n");
	count_L2_cache_inc = 0;
	L2_cache_inc = 0;
	for i in range(num_of_cpu_cores_shared):
		## increase
		count_L2_cache_inc = count_L2_cache_inc + 1;
		## to_file
		f.write("[Module mod-cpu-il1-%0.f]\n" % i);
		f.write("Type = Cache\n");
		f.write("Geometry = geo-cpu-i-l1\n");
		f.write("LowNetwork = net-cpu-l1-l2-%0.f\n" % L2_cache_inc);
		# f.write("LowNetworkNode = mod-cpu-l2-%0.f\n" % L2_cache_inc); # debugging 020317.v1
		f.write("LowModules = mod-cpu-l2-%0.f\n" % L2_cache_inc); # debugging 020317.v1
		f.write("\n");
		## check increasing and reset
		if count_L2_cache_inc==2:
			count_L2_cache_inc = 0; # reset
			L2_cache_inc = L2_cache_inc + 1;
	f.write("\n");
	
	## L1-L2-of-GPU-cores
	f.write(";; %0.f L1$ for GPUs.\n" % (num_of_gpu_cores/2));
	f.write(";; Each L1$ is for two compute units.\n");
	f.write(";; Each GPU has 4 compute units.\n");
	f.write("\n");
	count_L1_gpu_inc = 0;
	L1_gpu_cache_inc = 0;
	for i in range(num_of_gpu_cores/2): # num of compute units
		## increase
		count_L1_gpu_inc = count_L1_gpu_inc + 1;
		f.write("[Module mod-gpu-l1-%0.f]\n" % i);
		f.write("Type = Cache\n");
		f.write("Geometry = geo-gpu-l1\n");
		f.write("LowNetwork = net-gpu-l1-l2-%0.f\n" % L1_gpu_cache_inc);
		f.write("LowModules = mod-gpu-l2-%0.f\n" % L1_gpu_cache_inc);
		f.write("\n");	
		## check increasing and reset
		if count_L1_gpu_inc%2==0:
			count_L1_gpu_inc = 0; # reset
			L1_gpu_cache_inc = L1_gpu_cache_inc + 1;
	f.write("\n");

	# L2$-interconnect for CPUs
	f.write(";; %0.f L2$ for CPUs.\n" % (num_of_cpu_cores/2));
	f.write("\n");
	LowModules_MM = "LowModules =";
	for i in range(num_of_MC):
		LowModules_MM = LowModules_MM + " mod-mm-%0.f" % i;
	##
	count_L2_MM_inc = 0;
	L2_cache_inc = 0;
	for i in range(num_of_cpu_cores):
		if count_L2_MM_inc%2 == 0:
			Nodes_counter = Nodes_counter + 1;
			f.write("[Module mod-cpu-l2-%0.f]\n" % L2_cache_inc);
			f.write("Type = Cache\n");
			f.write("Geometry = geo-cpu-l2\n");
			f.write("HighNetwork = net-cpu-l1-l2-%0.f\n" % L2_cache_inc);
			f.write("LowNetwork = net-l2-mm\n");
			f.write("LowNetworkNode = n%0.f\n" % L2_cache_inc);
			f.write("%s\n" % LowModules_MM);
			f.write("\n");
			L2_cache_inc = L2_cache_inc + 1;
		# counting
		count_L2_MM_inc = count_L2_MM_inc + 1;	
	f.write("\n");

	# L2$-interconnect for GPUs
	f.write(";; %0.f L2$ for GPUs.\n" % (num_of_gpu_cores/4));
	f.write("\n");
	Node_Increment_L2_Net_GPU = L2_cache_inc;	
	for i in range(num_of_gpu_cores/4):
		Nodes_counter = Nodes_counter + 1;
		f.write("[Module mod-gpu-l2-%0.f]\n" % i);
		f.write("Type = Cache\n");
		f.write("Geometry = geo-gpu-l2\n");
		f.write("HighNetwork = net-gpu-l1-l2-%0.f\n" % i);
		f.write("LowNetwork = net-l2-mm\n");
		f.write("LowNetworkNode = n%0.f\n" % Node_Increment_L2_Net_GPU);
		f.write("%s\n" % LowModules_MM);
		f.write("\n");
		Node_Increment_L2_Net_GPU = Node_Increment_L2_Net_GPU + 1;
	f.write("\n");

	# Main memory 
	Node_Increment_Memory = Node_Increment_L2_Net_GPU;
	f.write(";; %0.f Memory Banks.\n" % num_of_MC);
	f.write("\n");
	for i in range(num_of_MC):
		Nodes_counter = Nodes_counter + 1;
		f.write("[Module mod-mm-%0.f]\n" % i);
		f.write("Type = MainMemory\n");
		f.write("BlockSize = %0.f\n" % L2_blocksize);
		f.write("Latency = %0.f\n" % Memory_latency);
		f.write("Ports = 1\n");
		f.write("HighNetwork = net-l2-mm\n");
		f.write("HighNetworkNode = n%0.f\n" % Node_Increment_Memory);
		f.write("AddressRange = ADDR DIV %0.f MOD %0.f EQ %0.f\n" % (L2_blocksize, num_of_MC, i) );
		f.write("\n");
		Node_Increment_Memory = Node_Increment_Memory + 1;
	f.write("\n");

	# CPU cores
	f.write(";; %0.f CPU cores.\n" % num_of_cpu_cores);
	f.write("\n");
	count_shared = 0;
	for i in range(num_of_cpu_cores):
		f.write("[Entry core-%0.f]\n" % i);
		f.write("Arch = x86\n");
		f.write("Core = %0.f\n" % i);
		f.write("Thread = 0\n");
		f.write("DataModule = mod-cpu-dl1-%0.f\n" % i);
		f.write("InstModule = mod-cpu-il1-%0.f\n" % i);
		f.write("\n");
	f.write("\n");

	# GPU cores
	f.write(";; %0.f GPU cores.\n"  % num_of_gpu_cores);
	f.write("\n");
	count_L1_gpu_inc1 = 0;
	L1_gpu_cache_inc1 = 0;
	for i in range(num_of_gpu_cores):
		count_L1_gpu_inc1 = count_L1_gpu_inc1 + 1;
		f.write("[Entry gpu-cu-%0.f]\n" % i);
		f.write("Arch = %s\n" % type_of_gpu);
		f.write("ComputeUnit = %0.f\n" % i);
		f.write("Module = mod-gpu-l1-%0.f\n" % L1_gpu_cache_inc1);
		f.write("\n");
		## check increasing and reset
		if count_L1_gpu_inc1%2==0:
			count_L1_gpu_inc1 = 0; # reset
			L1_gpu_cache_inc1 = L1_gpu_cache_inc1 + 1;
	f.write("\n");

	# Networks (create netconfig with external net-l2-mm)
	f.write(";; L1$-L2$ network for CPUs.\n");
	f.write("\n");
	count_L2_cache_inc = 0;
	L2_cache_inc = 0;
	for i in range(num_of_cpu_cores):
		if count_L2_cache_inc%2 == 0:
			f.write("[Network net-cpu-l1-l2-%0.f]\n" % L2_cache_inc);
			f.write("DefaultInputBufferSize = %0.f\n" % bufferSize);
			f.write("DefaultOutputBufferSize = %0.f\n" % bufferSize);
			f.write("DefaultBandwidth = %0.f\n" % bandwidth);
			f.write("\n");
			L2_cache_inc = L2_cache_inc + 1;
		# counting
		count_L2_cache_inc = count_L2_cache_inc + 1;	
	f.write("\n");

	f.write(";; L1$-L2$ network for GPUs.\n");
	f.write("\n");
	count_L2_cache_inc = 0;
	L2_cache_inc = 0;
	for i in range(num_of_gpu_cores):
		if count_L2_cache_inc%4 == 0:
			f.write("[Network net-gpu-l1-l2-%0.f]\n" % L2_cache_inc);
			f.write("DefaultInputBufferSize = %0.f\n" % bufferSize);
			f.write("DefaultOutputBufferSize = %0.f\n" % bufferSize);
			f.write("DefaultBandwidth = %0.f\n" % bandwidth);
			f.write("\n");
			L2_cache_inc = L2_cache_inc + 1;
		# counting
		count_L2_cache_inc = count_L2_cache_inc + 1;	
	f.write("\n");

	f.write(";; Total nodes (Switches): %0.f \n" % Nodes_counter);
	f.write(";; Total memory controllers: %0.f \n" % num_of_MC);
	f.write(";; Total number of CPU cores: %0.f \n" % num_of_cpu_cores);
	f.write(";; Total number of %s GPU cores: %0.f \n" % (type_of_gpu, num_of_gpu_cores));
	f.write(";; Total number of L1$ CPUs: %0.f \n" % (num_of_cpu_cores));
	f.write(";; Total number of L1$ GPUs: %0.f \n" % (num_of_gpu_cores/4));
	f.write(";; Total number of L2$ CPUs: %0.f \n" % (num_of_cpu_cores/2));
	f.write(";; Total number of L2$ GPUs: %0.f \n" % (num_of_gpu_cores/4));
	f.write("\n");

	return Nodes_counter;
	# close
	f.close();

# methods call
# create_memconfig(16,16,2,4,0,32,4,512,8,1,4,64,64,100,64,4,512,16,22,63,128,128);
# create_memconfig(48,96,1,16,0,32,4,512,8,1,4,64,64,100,64,4,512,16,22,63,128,128);
	

