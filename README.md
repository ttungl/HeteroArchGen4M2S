##Introduction
Heterogeneous Architecture Configurations Generator for Multi2Sim simulator (`HeteroArchGen4M2S`) 

`HeteroArchGen4M2S` is an automatic generator tool for heterogeneous CPU-GPU architectures' configurations for Multi2Sim simulator. This tool runs on top of M2S simulator, it allows us to configure the various heterogeneous CPU-GPU architectures (e.g., number of CPU cores, GPU cores, L1$, L2$, memory (size and latency (via `CACTI 6.5`)), network topologies (currently support 2D-Mesh, customized 2D-Mesh, and Torus networks)...). The output files include the results of network throughput and latency, caches/memory access time, and power consumption of the cores (can be collected after running `McPAT`).

`HeteroArchGen4M2S` is free software, which is freely to be redistributed and modified it under the terms of the GNU General Public License as published by the Free Software Foundation.

For more details `http://www.gnu.org/licenses`.

`HeteroArchGen4M2S` is written to help you configure M2S 
easily, but non-warranty and non-mechantability.

A pdf version of this manual is also available in `HeteroArchGen4M2S_manual.pdf`.

##Download HeteroArchGen4M2S

	git clone https://github.com/HeteroArchGen4M2S.git

##Setup Requirements

1. Currently HeteroArchGen4M2S has been tested on 64-bit platforms:

	* Ubuntu 14.04 (final)

2. Required tools to build and run with HeteroArchGen4M2S:

	* GCC-4.8.0 to build HeteroArchGen4M2S
	* Python 2.7

3. Download and install `multi2sim-5.0` from `https://github.com/Multi2Sim/multi2sim`. 

4. Download McPAT (current ver-1.3) from `https://code.google.com/archive/p/mcpat/`. Unzip under multi2sim-5.0 directory and install it.

5. Required benchmarks to run:
	* Download benchmarks from `https://github.com/Multi2Sim`, then unzip under the installed multi2sim directory, then compile the benchmarks following the README file.
	* Note: In case you want to run CUDA benchmarks, you can download other benchmarks for CPU-GPU interaction such as Rodinia, Parboil, etc. Your desktop should have a NVIDIA graphic card (e.g., NVIDIA Quadro 4000), and you need to install the graphic card driver for running the simulation. (When compiling benchmarks, use `-m32` to make compatible with `multi2sim`). 

##Build configuration files with HeteroArchGen4M2S

Let’s assume you are in the home directory (`$multi2sim-5.0/HeteroArchGen4M2S`)

##Where are the configuration files?
* After running `create_sim_configs_files.py` the output files will be saved in configs directory.
* `cd HeteroArchGen4M2S/configs`	--- note that, it contains many configuration files, i.e., memconfig, netconfig, x86_cpuconfig, si_gpuconfig.

##Where are the output files after simulation?
* `cd HeteroArchGen4M2S/results`	--- note that, it contains many configuration files, i.e., pipeline.out, mem.out.
* Note that, `net_report.out` will be generated under the multi2sim-5.0 directory, you need to copy this file to `HeteroArchGen4M2S/results`.

##Demonstration: How to Run multi2sim-5.0 simulator with a benchmark

Let’s use the mm_multi_serial example for demonstration.

1.	Check:
	* `./run.check.sh`
	

Now you are ready to go. Hack the code and have fun!

##Claims:

We would like to thank the open source multi2sim community.

This work is inspired by [M2StoMcPAT](http://www.ece.umd.edu/~cserafy1/index.htm), but implemented completely in Python. 

		Tung Thanh Le
		ttungl at gmail dot com
		version 1.0

