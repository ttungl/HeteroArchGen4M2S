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
import os ## for chmod
import stat

def create_shell_script(num_CPU, num_GPU, gpu_type, cpu_max_inst, benchmark, net_max_inst, network_only, numThreads):
	# assert (benchmark is not empty), "Error benchmark"
	## create a shell script in runsimulations folder.
	# File name
	f = open('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-benchmark-%s.sh' % (num_CPU, num_GPU, gpu_type, benchmark), 'w');
	## content
	if network_only == 0: ## full system
		f.write('m2s --x86-sim detailed ')
		f.write('--x86-report HeteroArchGen4M2S/results/%s_pipeline.out ' % benchmark)
		f.write('--mem-report HeteroArchGen4M2S/results/%s_mem.out ' % benchmark)
		f.write('--x86-config ./HeteroArchGen4M2S/configs/x86_cpuconfig ')
		f.write('--si-sim detailed ')
		f.write('--si-config ./HeteroArchGen4M2S/configs/si_gpuconfig ')
		f.write('--mem-config ./HeteroArchGen4M2S/configs/memconfig ')
		f.write('--net-config ./HeteroArchGen4M2S/configs/netconfig ')
		f.write('--x86-max-inst %0.f ' % cpu_max_inst)
		## network report: 
		##### Note: This file is generated under m2s directory.
		f.write('--net-report %s_net_report.out ' % benchmark)
	else: ## network_only = 1
		## m2s --net-config net-config --net-sim mynet --net-max-cycles 1000000 --report-net report-net 
		## --net-injection-rate 0.1
		f.write('m2s --net-config ./HeteroArchGen4M2S/configs/netconfig ')
		f.write('--net-sim net-l2-mm ')
		f.write('--net-max-cycles %0.f '% net_max_inst)
		f.write('--net-report %s_net_report.out ' % benchmark)
	
	## benchmarks or synthetic workloads
	# if synthetic_workload == 1:
	# 	f.write('--net-report %0.f_net_report.out ' % injection_rate)
	# 	f.write('--net-injection-rate %0.f '% injection_rate)
	## splash2-benchmarks
	if benchmark == 'fft':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/fft/fft -m18 -p%0.f -n65536 -l4' % numThreads)
	if benchmark == 'fmm':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/fmm/fmm.i386 %0.f HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/fmm/input' % numThreads)
	if benchmark == 'lu':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/lu/lu.i386 -p%0.f -n512 -b16' % numThreads)
	if benchmark == 'cholesky':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/cholesky/cholesky.i386 -p%0.f HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/cholesky/tk14.O' % numThreads)
	if benchmark == 'barnes':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/barnes/barnes.i386 %0.f HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/barnes/input' % numThreads)
	if benchmark == 'ocean':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/ocean/ocean.i386 -n130 -p%0.f -e1e-07 -r20000 -t28800' % numThreads)
	if benchmark == 'raytrace':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/raytrace/raytrace.i386 -p%0.f HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/raytrace/balls4.env' % numThreads)
	if benchmark == 'water-nsquared':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/water-nsquared/water-nsquared.i386 %0.f HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/water-nsquared/input' % numThreads)
	if benchmark == 'water-spatial':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/water-spatial/water-spatial.i386 %0.f HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/water-spatial/input' % numThreads)
	if benchmark == 'radiosity':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/radiosity/radiosity.i386 -batch -p %0.f -en 0.5' % numThreads)
	if benchmark == 'radix':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-splash2/radix/radix.i386 -p%0.f -r4096 -n262144 -m524288' % numThreads)

	## hetero-mark-benchmarks
	if benchmark == 'aes':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/aes/aes_hsa -k HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/aes/data/key.data -i HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/aes/data/small.data')
	# 	# f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/aes/aes_hsa -k key.data -i small.data data')
	# if benchmark == 'fir':
	# 	f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/fir/fir_hsa')
	# if benchmark == 'histogram':
	# 	f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/histogram/hist_hsa')
	# if benchmark == 'kmeans':
	# 	f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/kmeans/kmeans_hsa -k HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/kmeans/small.data HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/kmeans/data')
	# if benchmark == 'page_rank':
	# 	f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/page_rank/pr_hsa -k HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/page_rank/small.data HeteroArchGen4M2S/benchmarks/m2s-bench-heteromark/page_rank/data')
		
	## amd-sdk-2.5-benchmark
	if benchmark == 'BinarySearch':
		f.write('HeteroArchGen4M2S/benchmarks/m2s-bench-amdsdk-2.5/BinarySearch/BinarySearch --load HeteroArchGen4M2S/benchmarks/m2s-bench-amdsdk-2.5/BinarySearch/BinarySearch_Kernels.bin -e')
	


	## Spec2006-benchmarks
	## Parsec-3.0-benchmarks
	## Parboil-benchmarks

	## test benchmark
	if benchmark == 'default_mm':
		f.write('HeteroArchGen4M2S/mm_multi/mm_multi_serial %0.f' % numThreads)

	## close
	f.close()

	## granted `chmod +x` for this file
	# if synthetic_workload ==1:
	# 	st = os.stat('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-synthetic-injection-%0.f.sh' % (num_CPU, num_GPU, gpu_type, injection_rate))
	# 	os.chmod('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-synthetic-injection-%0.f.sh' % (num_CPU, num_GPU, gpu_type, injection_rate), st.st_mode | stat.S_IEXEC)
	# else:
	st = os.stat('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-benchmark-%s.sh' % (num_CPU, num_GPU, gpu_type, benchmark))
	os.chmod('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-benchmark-%s.sh' % (num_CPU, num_GPU, gpu_type, benchmark), st.st_mode | stat.S_IEXEC)

## tested
# create_shell_script(16, 16, 1, 10000000, 'fft', 0)
