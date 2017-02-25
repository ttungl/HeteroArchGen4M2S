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

def create_shell_script(num_CPU, num_GPU, gpu_type, cpu_max_inst, benchmark, net_max_inst, injection_rate):
	## check benchmark
	# if benchmark == '':
	# 	benchmark = 'default_mm'

	## create a shell script in runsimulations folder.
	# File name
	f = open('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-benchmark-%s.sh' % (num_CPU, num_GPU, gpu_type, benchmark), 'w');
	## content
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
	
	## splash2 benchmarks
	if benchmark == 'fft':
		f.write('benchmarks/m2s-bench-splash2/fft/fft -m18 -p8 -n65536 -l4')
	if benchmark == 'fmm':
		f.write('benchmarks/m2s-bench-splash2/fmm/fmm.i386 8 benchmarks/m2s-bench-splash2/fmm/input')
	if benchmark == 'lu':
		f.write('benchmarks/m2s-bench-splash2/lu/lu.i386 -p8 -n512 -b16')
	if benchmark == 'cholesky':
		f.write('benchmarks/m2s-bench-splash2/cholesky/cholesky.i386 -p8 benchmarks/m2s-bench-splash2/cholesky/tk14.0')
	if benchmark == 'barnes':
		f.write('benchmarks/m2s-bench-splash2/barnes/barnes.i386 8 benchmarks/m2s-bench-splash2/barnes/input')
	if benchmark == 'ocean':
		f.write('benchmarks/m2s-bench-splash2/ocean/ocean.i386 -n130 -p8 -e1e-07 -r20000 -t28800')
	if benchmark == 'raytrace':
		f.write('benchmarks/m2s-bench-splash2/raytrace/raytrace.i386 -p8 balls4.env')
	if benchmark == 'water-nsquared':
		f.write('benchmarks/m2s-bench-splash2/water-nsquared/water-nsquared.i386 8 benchmarks/m2s-bench-splash2/water-nsquared/input')
	if benchmark == 'water-spatial':
		f.write('benchmarks/m2s-bench-splash2/water-spatial/water-spatial.i386 8 benchmarks/m2s-bench-splash2/water-spatial/input')
	if benchmark == 'radiosity':
		f.write('benchmarks/m2s-bench-splash2/radiosity/radiosity.i386 -batch -p 8 -en 0.5')
	
	## test benchmark
	if benchmark == 'default_mm':
		f.write('HeteroArchGen4M2S/mm_multi/mm_multi_serial 8')
		
	## close
	f.close()

	## granted `chmod +x` for this file
	st = os.stat('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-benchmark-%s.sh' % (num_CPU, num_GPU, gpu_type, benchmark))
	os.chmod('run_simulation_files/run-sim-%0.f-CPU-%0.f-%s-GPU-benchmark-%s.sh' % (num_CPU, num_GPU, gpu_type, benchmark), st.st_mode | stat.S_IEXEC)

## tested
# create_shell_script(16, 16, 1, 10000000, 'fft', 0)
