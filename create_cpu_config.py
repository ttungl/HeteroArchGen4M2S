#!/usr/bin/env python
# ===========================================================================
# Copyright 2017 `Tung Thanh Le` 
# Email: ttungl at gmail dot com

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
# `create_cpuconfig` is part of M2S configuration files.
# ==========================================================
# Description: This generates `x86_cpuconfig` file for M2S
# 	Input: 
# 	Output:
# 	Note: Each core can contain several threads.
# ==========================================================
# E.g.,
	# num_of_cores = 16 : number of cores in the CPUs
	# num_of_threads = 1 : number of threads in each core
	# ROB_size = 128 : number of in-flight instructions allowed
	# pipelines_size = 4: decode/dispatch/issue/commit width
	# bimod_size = 4096 : Size of local predictor (larger size means less aliasing in history table)
	# bpred_size = 1024 : Size of global predictor (larger size means longer global history register)
# ==========================================================
import math # to roundup the float numbers.
# benchmark, fast_forward: binary flag, enables fastforward past sequential portion of benchmark
def create_cpuconfig(	num_of_cores, 
						cpu_frequency,
						num_of_threads, 
						ROB_size,
						pipelines_size, 
						bimod_size, 
						bpred_size):

	# Check inputs validation
	assert(num_of_cores>=4), "Error! Number of CPU cores must be at least 4."
	assert(num_of_threads>=0), "Error! Number of threads should be at least zero."
	
	# Adapted the additional parameters from M2StoMcPAT of Caleb (Univ. Maryland College Park)
	IQ_ratio = 0.4; # size of instruction (issue) queue w.r.t. ROB
	LSQ_ratio = 0.5; # size of LSQ w.r.t. ROB
	RF_ratio = 1; # size of register file w.r.t. ROB
	RF_int_ratio = 0.666666;# (2/3) ratio of int vs FP regissters in the RF
	Fetch_Queue_size = 64; # queue holding instructions fetched from I$ waiting to be decoded
	history_size = 8; # size of the local histroy table entries
	
	# File name
	f = open('configs/x86_cpuconfig', 'w');

	# General
	f.write("[ General ]\n");
	f.write("	Cores = %0.f\n" % num_of_cores);
	f.write("	Threads = %0.f\n" % num_of_threads);
	f.write("	Frequency = %0.f\n" % cpu_frequency);
	f.write("\n");

	# Pipeline
	f.write("[ Pipeline ]\n");
	f.write("	DecodeWidth = %0.f\n" % pipelines_size);
	f.write("	DispatchWidth = %0.f\n" % pipelines_size);
	f.write("	IssueWidth = %0.f\n" % pipelines_size);
	f.write("	CommitWidth = %0.f\n" % pipelines_size);
	f.write("\n");

	# Queues
	f.write("[ Queues ]\n");
	f.write("	FetchQueueSize = %0.f\n" % Fetch_Queue_size);
	f.write("	RobSize = %0.f\n" % ROB_size);
	f.write("	IqSize = %0.f\n" % (IQ_ratio*ROB_size));
	f.write("	LsqSize = %0.f\n" % (LSQ_ratio*ROB_size));
	f.write("	RfIntSize = %0.f\n" % (RF_ratio*(RF_int_ratio)*ROB_size));
	f.write("	RfFpSize = %0.f\n" % (RF_ratio*(1-RF_int_ratio)*ROB_size));
	f.write("\n");

	# FunctionalUnits
	f.write("[ FunctionalUnits ]\n");
	f.write("	IntAdd.Count = %0.f\n" % pipelines_size);
	f.write("	IntMult.Count = %0.f\n" % (pipelines_size/4));
	f.write("	IntDiv.Count = %0.f\n" % math.ceil(pipelines_size/8+0.55)); # added 0.55 to roundup the float number.
	f.write("	EffAddr.Count = %0.f\n" % pipelines_size);
	f.write("	Logic.Count = %0.f\n" % pipelines_size);
	f.write("	FpSimple.Count = %0.f\n" % pipelines_size);
	f.write("	FpAdd.Count = %0.f\n" % pipelines_size);
	f.write("	FpMult.Count = %0.f\n" % (pipelines_size/4));
	f.write("	FpDiv.Count = %0.f\n" % math.ceil(pipelines_size/8+0.55)); # added 0.55 to roundup the float number.
	f.write("	FpComplex.Count = %0.f\n" % math.ceil(pipelines_size/8+0.55)); # added 0.55 to roundup the float number.
	f.write("\n");

	# BranchPredictor
	f.write("[ BranchPredictor ]\n");
	f.write("	Kind = Combined\n");
	f.write("	Bimod.Size = %0.f\n" % bimod_size);
	f.write("	Choice.Size = %0.f\n" % bimod_size);
	f.write("	TwoLevel.L1Size = %0.f\n" % bpred_size);
	f.write("	TwoLevel.L2Size = 1\n");
	f.write("	TwoLevel.HistorySize = %0.f\n" % history_size);
	f.write("	BTB.Sets = 1024\n"); 
	f.write("	BTB.Assoc = 1");

	# close
	f.close();

## Tested
# def main():
# 	create_cpuconfig(16, 1, 128, 4, 4096, 1024, 1);
# 	print "This %s file is just executed!" % __file__
# if __name__ == "__main__": main()

