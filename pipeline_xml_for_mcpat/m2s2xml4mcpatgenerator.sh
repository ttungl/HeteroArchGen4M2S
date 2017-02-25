#!/bin/bash

# $1  $2  $3  are :
# $1: the output file from the multi2sim, 
# using cmd: m2s --cpu-sim detailed --report-cpu-pipeline report.pipeline(report file) ~/Apply_Calibration/Apply_Cali(benchmark);
# $2: any template xml file of mcpat;
# $3: a new xml file for mcpat. 
# So the first two are input file names and the third is the output file name

echo "Type in the pipeline report from multi2sim:"
read -e IN_M2S
echo "Type in any template xml file of mcpat:"
read -e IN_XML
echo "Name a new xml file for input of mcpat:"
read -e OUT_XML
# IN_M2S=$1
# IN_XML=$2
# OUT_XML=$3
OUT_TEMP=tungconfigs/mcpatxml/test1_mcpat.xml

m2s_data=$(grep -m 1 "Cycles"   $IN_M2S | sed "s;Cycles = \(.*\);\1;")
sed "s;\(.*\)total_cycles\"\(.*\)\"\(.*\)\"\(.*\);\1total_cycles\"\2\"$m2s_data\"\4;"  $IN_XML  > $OUT_XML 
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)busy_cycles\"\(.*\)\"\(.*\)\"\(.*\);\1busy_cycles\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.Total"   $IN_M2S | sed "s;Dispatch.Total = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)total_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1total_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.Integer"   $IN_M2S | sed "s;Dispatch.Integer = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)int_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1int_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.FloatingPoint"   $IN_M2S | sed "s;Dispatch.FloatingPoint = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)fp_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1fp_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.Ctrl"   $IN_M2S | sed "s;Dispatch.Ctrl = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)branch_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1branch_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Commit.Mispred"   $IN_M2S | sed "s;Commit.Mispred = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)branch_mispredictions\"\(.*\)\"\(.*\)\"\(.*\);\1branch_mispredictions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.Uop.load"   $IN_M2S | sed "s;Dispatch.Uop.load = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)load_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1load_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.Uop.store"   $IN_M2S | sed "s;Dispatch.Uop.store = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)store_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1store_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Commit.Total"   $IN_M2S | sed "s;Commit.Total = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)committed_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1committed_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Commit.Integer"   $IN_M2S | sed "s;Commit.Integer = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)committed_int_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1committed_int_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Commit.FloatingPoint"   $IN_M2S | sed "s;Commit.FloatingPoint = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)committed_fp_instructions\"\(.*\)\"\(.*\)\"\(.*\);\1committed_fp_instructions\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Commit.DutyCycle"   $IN_M2S | sed "s;Commit.DutyCycle = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)pipeline_duty_cycle\"\(.*\)\"\(.*\)\"\(.*\);\1pipeline_duty_cycle\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "ROB.Reads"   $IN_M2S | sed "s;ROB.Reads = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)ROB_reads\"\(.*\)\"\(.*\)\"\(.*\);\1ROB_reads\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "ROB.Writes"   $IN_M2S | sed "s;ROB.Writes = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)ROB_writes\"\(.*\)\"\(.*\)\"\(.*\);\1ROB_writes\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RAT.IntReads"   $IN_M2S | sed "s;RAT.IntReads = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"rename_reads\"\(.*\)\"\(.*\)\"\(.*\);\1\"rename_reads\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RAT.IntWrites"   $IN_M2S | sed "s;RAT.IntWrites = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"rename_writes\"\(.*\)\"\(.*\)\"\(.*\);\1\"rename_writes\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "IQ.Reads"   $IN_M2S | sed "s;IQ.Reads = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"inst_window_reads\"\(.*\)\"\(.*\)\"\(.*\);\1\"inst_window_reads\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "IQ.Writes"   $IN_M2S | sed "s;IQ.Writes = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"inst_window_writes\"\(.*\)\"\(.*\)\"\(.*\);\1\"inst_window_writes\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "IQ.WakeupAccesses"   $IN_M2S | sed "s;IQ.WakeupAccesses = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"inst_window_wakeup_accesses\"\(.*\)\"\(.*\)\"\(.*\);\1\"inst_window_wakeup_accesses\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RF_Int.Reads"   $IN_M2S | sed "s;RF_Int.Reads = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"int_regfile_reads\"\(.*\)\"\(.*\)\"\(.*\);\1\"int_regfile_reads\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RF_Int.Writes"   $IN_M2S | sed "s;RF_Int.Writes = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"int_regfile_writes\"\(.*\)\"\(.*\)\"\(.*\);\1\"int_regfile_writes\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.Uop.call"   $IN_M2S | sed "s;Dispatch.Uop.call = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)function_calls\"\(.*\)\"\(.*\)\"\(.*\);\1function_calls\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Dispatch.WndSwitch"   $IN_M2S | sed "s;Dispatch.WndSwitch = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)context_switches\"\(.*\)\"\(.*\)\"\(.*\);\1context_switches\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

#m2s_data=$(grep -m 1 "Issue.SimpleInteger"   $IN_M2S | sed "s;Issue.SimpleInteger = \(.*\);\1;")
#cp  $OUT_XML  $OUT_TEMP
#sed "s;\(.*\)ialu_accesses\"\(.*\)\"\(.*\)\"\(.*\);\1ialu_accesses\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "Issue.FloatingPoint"   $IN_M2S | sed "s;Issue.FloatingPoint = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)fpu_accesses\"\(.*\)\"\(.*\)\"\(.*\);\1fpu_accesses\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

#m2s_data=$(grep -m 1 "Issue.ComplexInteger"   $IN_M2S | sed "s;Issue.ComplexInteger = \(.*\);\1;")
#cp  $OUT_XML  $OUT_TEMP
#sed "s;\(.*\)mul_accesses\"\(.*\)\"\(.*\)\"\(.*\);\1mul_accesses\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "BTB.Reads"   $IN_M2S | sed "s;BTB.Reads = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)read_accesses\"\(.*\)\"\(.*\)\"\(.*\)BTB\_\(.*\);\1read_accesses\"\2\"$m2s_data\"\4BTB\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "BTB.Writes"   $IN_M2S | sed "s;BTB.Writes = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)write_accesses\"\(.*\)\"\(.*\)\"\(.*\)BTB\_\(.*\);\1write_accesses\"\2\"$m2s_data\"\4BTB\_\5;"  $OUT_TEMP  > $OUT_XML 


#
# itlb
#

m2s_data=$(grep "itlb.0.0"   $IN_M2S | grep "Accesses"  | sed "s;\(.*\)Accesses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)total_accesses\"\(.*\)\"\(.*\)\"\(.*\)itlb\_\(.*\);\1total_accesses\"\2\"$m2s_data\"\4itlb\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "itlb.0.0"   $IN_M2S | grep "Misses"  | sed "s;\(.*\)Misses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)total_misses\"\(.*\)\"\(.*\)\"\(.*\)itlb\_\(.*\);\1total_misses\"\2\"$m2s_data\"\4itlb\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "itlb.0.0"   $IN_M2S | grep "Evictions"  | sed "s;\(.*\)Evictions = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)conflicts\"\(.*\)\"\(.*\)\"\(.*\)itlb\_\(.*\);\1conflicts\"\2\"$m2s_data\"\4itlb\_\5;"  $OUT_TEMP  > $OUT_XML 

#
# il1
#


m2s_data=$(grep "il1-0"   $IN_M2S | grep " Reads "  | sed "s;\(.*\)Reads = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)read_accesses\"\(.*\)\"\(.*\)\"\(.*\)icache\_\(.*\);\1read_accesses\"\2\"$m2s_data\"\4icache\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "il1-0"   $IN_M2S | grep " ReadMisses "  | sed "s;\(.*\)ReadMisses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)read_misses\"\(.*\)\"\(.*\)\"\(.*\)icache\_\(.*\);\1read_misses\"\2\"$m2s_data\"\4icache\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "il1-0"   $IN_M2S | grep " Evictions "  | sed "s;\(.*\)Evictions = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)conflicts\"\(.*\)\"\(.*\)\"\(.*\)icache\_\(.*\);\1conflicts\"\2\"$m2s_data\"\4icache\_\5;"  $OUT_TEMP  > $OUT_XML 

#
# dtlb
#

m2s_data=$(grep "dtlb.0.0"   $IN_M2S | grep " Accesses "  | sed "s;\(.*\)Accesses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)total_accesses\"\(.*\)\"\(.*\)\"\(.*\)dtlb\_\(.*\);\1total_accesses\"\2\"$m2s_data\"\4dtlb\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "dtlb.0.0"   $IN_M2S | grep " Misses "  | sed "s;\(.*\)Misses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)total_misses\"\(.*\)\"\(.*\)\"\(.*\)dtlb\_\(.*\);\1total_misses\"\2\"$m2s_data\"\4dtlb\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "dtlb.0.0"   $IN_M2S | grep " Evictions "  | sed "s;\(.*\)Evictions = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)conflicts\"\(.*\)\"\(.*\)\"\(.*\)dtlb\_\(.*\);\1conflicts\"\2\"$m2s_data\"\4dtlb\_\5;"  $OUT_TEMP  > $OUT_XML 

#
# dl1
#

m2s_data=$(grep "dl1-0"   $IN_M2S | grep " Reads "  | sed "s;\(.*\)Reads = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)read_accesses\"\(.*\)\"\(.*\)\"\(.*\)dcache\_\(.*\);\1read_accesses\"\2\"$m2s_data\"\4dcache\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "dl1-0"   $IN_M2S | grep " Writes "  | sed "s;\(.*\)Writes = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)write_accesses\"\(.*\)\"\(.*\)\"\(.*\)dcache\_\(.*\);\1write_accesses\"\2\"$m2s_data\"\4dcache\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "dl1-0"   $IN_M2S | grep " ReadMisses "  | sed "s;\(.*\)ReadMisses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)read_misses\"\(.*\)\"\(.*\)\"\(.*\)dcache\_\(.*\);\1read_misses\"\2\"$m2s_data\"\4dcache\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "dl1-0"   $IN_M2S | grep " WriteMisses "  | sed "s;\(.*\)WriteMisses = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)write_misses\"\(.*\)\"\(.*\)\"\(.*\)dcache\_\(.*\);\1write_misses\"\2\"$m2s_data\"\4dcache\_\5;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep "dl1-0"   $IN_M2S | grep " Evictions "  | sed "s;\(.*\)Evictions = \(.*\);\2;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)conflicts\"\(.*\)\"\(.*\)\"\(.*\)dcache\_\(.*\);\1conflicts\"\2\"$m2s_data\"\4dcache\_\5;"  $OUT_TEMP  > $OUT_XML 




m2s_data=$(grep -m 1 "Cores"   $IN_M2S | sed "s;Cores = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"number_of_cores\"\(.*\)\"\(.*\)\"\(.*\);\1\"number_of_cores\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "DecodeWidth"   $IN_M2S | sed "s;DecodeWidth = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"decode_width\"\(.*\)\"\(.*\)\"\(.*\);\1\"decode_width\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "IssueWidth"   $IN_M2S | sed "s;IssueWidth = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"issue_width\"\(.*\)\"\(.*\)\"\(.*\);\1\"issue_width\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "CommitWidth"   $IN_M2S | sed "s;CommitWidth = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"commit_width\"\(.*\)\"\(.*\)\"\(.*\);\1\"commit_width\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RAS.Size"   $IN_M2S | sed "s;RAS.Size = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"RAS_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"RAS_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "FetchQueueSize"   $IN_M2S | sed "s;FetchQueueSize = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"instruction_buffer_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"instruction_buffer_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "UopQueueSize"   $IN_M2S | sed "s;UopQueueSize = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"decoded_stream_buffer_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"decoded_stream_buffer_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "ROB.Size"   $IN_M2S | sed "s;ROB.Size = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"ROB_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"ROB_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RfIntSize"   $IN_M2S | sed "s;RfIntSize = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"phy_Regs_IRF_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"phy_Regs_IRF_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "RfFpSize"   $IN_M2S | sed "s;RfFpSize = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"phy_Regs_FRF_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"phy_Regs_FRF_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "IQ.Size"   $IN_M2S | sed "s;IQ.Size = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"instruction_window_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"instruction_window_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

m2s_data=$(grep -m 1 "LSQ.Size"   $IN_M2S | sed "s;LSQ.Size = \(.*\);\1;")
cp  $OUT_XML  $OUT_TEMP
sed "s;\(.*\)\"load_buffer_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"load_buffer_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 
sed "s;\(.*\)\"store_buffer_size\"\(.*\)\"\(.*\)\"\(.*\);\1\"store_buffer_size\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

#m2s_data=$(grep -m 1 "fu.IntAdd.Accesses"   $IN_M2S | sed "s;fu.IntAdd.Accesses = \([1-9]*\)\(.*\);\1;")
#cp  $OUT_XML  $OUT_TEMP
#sed "s;\(.*\)\"ALU_per_core\"\(.*\)\"\(.*\)\"\(.*\);\1\"ALU_per_core\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

#m2s_data=$(grep -m 1 "fu.IntMult.Accesses"   $IN_M2S | sed "s;fu.IntMult.Accesses = \([1-9]*\)\(.*\);\1;")
#cp  $OUT_XML  $OUT_TEMP
#sed "s;\(.*\)\"MUL_per_core\"\(.*\)\"\(.*\)\"\(.*\);\1\"MUL_per_core\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 

#m2s_data=$(grep -m 1 "fu.FPSimple.Accesses"   $IN_M2S | sed "s;fu.FPSimple.Accesses = \([1-9]*\)\(.*\);\1;")
#cp  $OUT_XML  $OUT_TEMP
#sed "s;\(.*\)\"FPU_per_core\"\(.*\)\"\(.*\)\"\(.*\);\1\"FPU_per_core\"\2\"$m2s_data\"\4;"  $OUT_TEMP  > $OUT_XML 



