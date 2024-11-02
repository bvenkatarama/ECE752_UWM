#!/bin/bash
# running DAXPY in gem5 shell script

mkdir m5out

build/X86/gem5.opt -r hw6.py --cpu_type=MinorCPU --binary=iax --options="$1"

tar -czf m5out_iax_minor.tar m5out/

build/X86/gem5.opt -r hw6.py --cpu_type=O3CPU --binary=iax --options="$1"

tar -czf m5out_iax_O3.tar m5out/
