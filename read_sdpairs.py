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

def read_data(PATH):
	# ```
	# 1. Read the file from PATH 
	# 2. Return the integer pairs (sd).
	# ```
	with open(PATH) as rfile:
		array = []
		array.append([int(x) for x in next(rfile).split()]) ## read first line
		array.extend([[int(x) for x in line.split()] 		## read rest of lines
					for line in rfile])
	return array

## for testing
## function call
# INPUT_NETWORK_PATH = 'results_hybrid_local_links/topoA_hybridlinks_sync_015_size8x8_normalize.txt'
# print read_data(INPUT_NETWORK_PATH)
