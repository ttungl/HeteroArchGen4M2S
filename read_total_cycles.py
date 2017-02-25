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
from write_to_File import write_to_File

# Read total cycles
# Input: pipeline.out
# Output: total cycles 
# Description: This program reads the total number of cycles in the pipeline.out file;

def read_total_cycles(pipeline_file_path, benchmark):
	with open(pipeline_file_path) as fopen:
		for line in fopen: 
			if "Cycles" in line:
				if "CyclesPerSecond" in line:
					CyclesPerSecond = line.split()
					CyclesperSec = CyclesPerSecond[2]
				else: ## Cycles
					Cycles = line.split()
					TotalCycles = Cycles[2]
		simtime = float(TotalCycles) / float(CyclesperSec)		
	## Write tofile
	writeToFile(TotalCycles, simtime, benchmark)
	## return
	return simtime

def writeToFile(wcycles, wsimtime, benchmark):
	fw = open('results/%s_totalCycles.out' % benchmark, 'w');
	fw.write('Cycles: ');
	fw.write(wcycles);
	fw.write('\n');
	fw.write('Time (seconds): %03.2f' % wsimtime);
	fw.close()
