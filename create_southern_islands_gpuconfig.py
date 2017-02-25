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
#
# `create_southern_islands_gpuconfig` is part of M2S configuration files.
# ==========================================================
# Description: This generates `si_gpuconfig` file for M2S
# 	Input: 
# 	Output:
# 	Note: Each core can contain several threads.
# ==========================================================
# E.g.,
	# num_of_cores = 4
# ==========================================================

def create_southern_islands_gpuconfig(num_of_cores):
	# Check inputs validation
	assert(num_of_cores>0), 'Error! Number of cores should be zero (CPU only) or positive integer!';

	# File name
	f = open('configs/si_gpuconfig', 'w');

	# General
	f.write("[ Device ]\n");
	f.write("	NumComputeUnits = %0.f\n" % num_of_cores);

	f.close();

# create_evergreen_gpuconfig(4); 