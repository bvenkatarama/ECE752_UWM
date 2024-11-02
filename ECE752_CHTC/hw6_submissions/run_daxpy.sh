#!/bin/bash
# running DAXPY in gem5 shell script

mkdir m5out

build/X86/gem5.opt -r hw6.py --cpu_type=MinorCPU --binary=daxpy --options="$1"

tar -czf m5out_daxpy_minor.tar m5out/

build/X86/gem5.opt -r hw6.py --cpu_type=O3CPU --binary=daxpy --options="$1"

tar -czf m5out_daxpy_O3.tar m5out/
