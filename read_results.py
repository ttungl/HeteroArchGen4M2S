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

from read_total_cycles import read_total_cycles
from read_network_performance import read_network_performance

# Read the results of output files, including mem.out, net.out, pipeline.out.
def read_results(benchmark):
	## Pipeline
	PL_PATH = 'results/%s_pipeline.out' % benchmark
	simtime = read_total_cycles(PL_PATH, benchmark)
	print "Done! `%s_totalCycles.out` in the results directory." % benchmark
	
	## Network
	#### Note that this file is generated under m2s directory (after running the 
	#### simulation from shell script file in run_simulation_files directory)
	#### you need to copy this file into the results directory in order to 
	#### run this `read_results.py` file.
	NET_PATH = 'results/net-l2-mm_%s_net_report.out' % benchmark
	read_network_performance(NET_PATH, simtime, benchmark)
	print "Done! `%s_network_performance.out` in the results directory." % benchmark

##### run 
##benchmark = 'default_mm' ## should be passed down from the main_config file
##read_results(benchmark)
