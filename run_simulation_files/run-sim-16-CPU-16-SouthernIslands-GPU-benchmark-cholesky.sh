m2s --x86-sim detailed --x86-report HeteroArchGen4M2S/results/cholesky_pipeline.out --mem-report HeteroArchGen4M2S/results/cholesky_mem.out --x86-config ./HeteroArchGen4M2S/configs/x86_cpuconfig --si-sim detailed --si-config ./HeteroArchGen4M2S/configs/si_gpuconfig --mem-config ./HeteroArchGen4M2S/configs/memconfig --net-config ./HeteroArchGen4M2S/configs/netconfig --x86-max-inst 100000000 --net-report cholesky_net_report.out benchmarks/m2s-bench-splash2/cholesky/cholesky.i386 -p8 benchmarks/m2s-bench-splash2/cholesky/tk14.0