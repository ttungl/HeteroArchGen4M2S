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
# from write_to_File import write_to_File

# Read network performance
# Input: net_report.out
# Output: network throughput and latency;
# Description:
	# This program calculates the network throughput and latency, from `net_report.out` file,
	# which is generated under multi2sim directory after running the shell script in 
	# the run_simulation_files directory. 

def read_network_performance(net_file, simtime, benchmark):
	with open(net_file) as fopen:
		for line in fopen: 
			if "AverageLatency" in line:
				avg_lat = line.split()
				latency = avg_lat[2]

			if "Cycles" in line:
				Cycles = line.split()
				Cycles = Cycles[2]
				break

		## throughput
		throughput = float(Cycles) / float(simtime)	
	## Write tofile
	writeToFile(throughput, latency, benchmark)

def writeToFile(wthroughput, wlatency, benchmark):
	fw = open('results/%s_network_performance.out' % benchmark, 'w');
	fw.write('Network Throughput (MBps): %03.2f \n' % wthroughput);
	fw.write('Network Latency (cycles): ');
	fw.write(wlatency);
	fw.close()








