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

# from file import function
from create_cpu_config import create_cpuconfig
from create_southern_islands_gpuconfig import create_southern_islands_gpuconfig
from create_memconfig import create_memconfig
from create_netconfig import create_netconfig
from create_shell_script import create_shell_script

# [cpu gpu mc]
# [16 16 4] : 16 nodes/switches on the interconnect
# [48 96 16] : 64 nodes/switches
## CPU Parameters
#### Note: 	a set of CPU includes two cores.
#### 		Each core in the set can have its own L1$ (Data&Instr) 
#### 		or it can share the Instruction-L1$ with the other core in that set.
####		by enabling `L1_Inst_shared` flag in the CPU Memory Parameters settings.
num_of_cpu_cores = 48 
cpu_frequency = 2400 ## 2.4GHz
num_of_threads = 1
ROB_size = 128
pipelines_size = 4
bimod_size = 4*1024
bpred_size = 1*1024
x86_max_inst = 100000000

## GPU Parameters
#### Note: 	a set of GPU includes four compute units. 
#### 		Each two units share with one L1$. 
#### 		Each two L1$ shares with one L2$.
num_of_gpu_cores 	= 96 	## the number of compute units of GPUs. (each GPU has 4 units.)
type_of_gpu = 'SouthernIslands' ## Note, multi2sim-5.0 does support different types of GPUs, see in Manual.

## CPU Memory Parameters 	
num_of_MC = 16 			# number of memory controllers; [2, 4, 8, 16]
L1_Inst_shared = 0		# enable/disable (1/0) shared Instruction L1$
L1_size = 32			# size of L1$ (kB); [16, 32, 64]
L1_assoc = 1			# associativity of L1$ (#-way) full-assoc
L2_size = 512			# size of L2$ (kB); [256, 512, 1024]
L2_assoc = 8			# associativity of L2$ (#-way); [4, 8, 16]
L1_latency = 1			# latency of L1$ (cycles)
L2_latency = 4			# latency of L2$ (cycles)
L1_blocksize = 64		# blocksize of L1$ (Bytes)
L2_blocksize = 64		# blocksize of L2$ (Bytes)
Memory_latency = 100	# latency of DRAM main memory

## GPU Memory Parameters (iiswc16: Victor Garcia)	
GPU_L1_size = 64		# size of L1$ (kB)
GPU_L1_assoc = 4		# associativity of L1$ (kB)
GPU_L2_size = 512		# size of L2$ (kB)
GPU_L2_assoc = 16		# associativity of L2$ (kB)
GPU_L1_latency = 22 	# latency of L1$ (ns)
GPU_L2_latency = 63 	# latency of L2$ (ns)
GPU_L1_blocksize = 64 	# blocksize of L1$ (Bytes)
GPU_L2_blocksize = 64 	# blocksize of L2$ (Bytes) 

## Note: L3$ shared caches for CPUs and GPUs can be extended if needed. (need a little more work!)

## List of benchmarks:
# splash2-benchmark = ['radix', 'fmm', 'barnes', 'cholesky', 'fft', 'lu', 'ocean', 'radiosity', 'raytrace', 'water-nsquared', 'water-spatial']
# hetero-mark-benchmark = ['aes', 'fir', 'histogram', 'kmeans', 'page_rank']
# amdsdk2.5-benchmark = ['BinarySearch']

benchmark = 'aes'
if benchmark == '':
		benchmark = 'default_mm'

## [0] disable synthetic workload (using benchmarks), 		
## [1] enable synthetic workload (not using benchmarks). 
# synthetic_workload = 1 

## injection rate for synthetic traffic
injection_rate = '0.1'
# numThreads = [8, 16, 32, 48, 56, 64, 128, 256]
numThreads = 8
## Network Parameters
#### Notice: source-destination nodes' id from the input files should start at 1, not zero.
## For a customized 2D-Mesh network
# HYBRIDLINKS_PATH = 'results_hybrid_local_links/test_topoA_hybridlinks_4x4.txt'
# LOCALLINKS_PATH = 'results_hybrid_local_links/test_topoA_locallinks_4x4.txt'

HYBRIDLINKS_PATH = 'results_hybrid_local_links/topoA_hybridlinks_sync_025_size8x8_normalize_cplex.txt'
# HYBRIDLINKS_PATH = 'results_hybrid_local_links/topoA_hybridlinks_sync_025_size8x8_normalize_Regression.txt'
LOCALLINKS_PATH = 'results_hybrid_local_links/topoA_locallinks_8x8.txt'

## network_mode: 
# [0] default 2D-mesh; 
# [1]: Customized 2D-Mesh Network; 
# [2]: Torus; 
# (optional) [3]: Ring
network_mode = 0
net_max_inst = 100000
network_only = 1 ## 1 for network-only, else 0 (full-system).

#### Base conversion 
# link_width = 8 Bytes per cycle
# frequency = 1 GHz
# bandwidth = link_width * frequency = 8 GBps
# For example: If you need a link bandwidth capacity = 40 GBps, you need to update the link_width appropriately.
# link_width = bandwidth/frequency = 40GBps/1GHz = 40 Bytes
# Linkwidth's Range: [8, 16, 32, 40, 48, 56, 64, ...]
## for 64-node	
HYBRID_LINKWIDTH 	= 32 	## Bytes per cycle (frequency*bandwidth(= 2.4GHz * 32Bytes/cyc ~ 80GBps)) 
LOCAL_LINKWIDTH 	= 16 	## Bytes per cycle (frequency*bandwidth(= 2.4GHz * 16Bytes/cyc ~ 40GBps))

## main()
def main():
	# Caches and memory latency calculation for memconfig
	#### for more specific on latency, a user might run offline CACTI to obtain these parameters.

	# Methods for creating the configuration files
	create_cpuconfig(num_of_cpu_cores, cpu_frequency, num_of_threads, ROB_size, pipelines_size, bimod_size, bpred_size);
	if type_of_gpu == 'SouthernIslands':
		create_southern_islands_gpuconfig(num_of_gpu_cores);
	
	num_nodes = create_memconfig(num_of_cpu_cores, \
								num_of_gpu_cores, \
								type_of_gpu, \
								num_of_MC, \
								L1_Inst_shared, \
								L1_size, \
								L1_assoc, \
								L2_size, \
								L2_assoc, \
								L1_latency, \
								L2_latency, \
								L1_blocksize, \
								L2_blocksize, \
								Memory_latency, \
								GPU_L1_size, \
								GPU_L1_assoc, \
								GPU_L2_size, \
								GPU_L2_assoc, \
								GPU_L1_latency, \
								GPU_L2_latency, \
								GPU_L1_blocksize, \
								GPU_L2_blocksize);

	create_netconfig(num_nodes, L2_blocksize, network_mode, LOCALLINKS_PATH, HYBRIDLINKS_PATH, \
															LOCAL_LINKWIDTH, HYBRID_LINKWIDTH)

	create_shell_script(num_of_cpu_cores, num_of_gpu_cores, type_of_gpu, \
						x86_max_inst, benchmark, net_max_inst, network_only, numThreads)


if __name__ == "__main__": main()
