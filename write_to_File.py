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

def write_to_File(function_name, name_1, value_1, name_2, value_2, benchmark):
	fw = open('results/%s_%s.out' % (benchmark, function_name) , 'w');
	# fw.write("%s: %03.2f \n" % (name_1, value_1));
	# fw.write("%s: %03.2f \n" % (name_2, value_2));
	fw.write(name_1);
	fw.write('%0.f', value_1);
	fw.write('\n');
	fw.write(name_2);
	fw.write('%0.f', value_2);
	fw.close()
