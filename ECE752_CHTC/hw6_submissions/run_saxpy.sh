#!/bin/bash
# running DAXPY in gem5 shell script

mkdir m5out

build/X86/gem5.opt -r hw6.py --cpu_type=MinorCPU --binary=saxpy --options="$1"

tar -czf m5out_saxpy_minor.tar m5out/

build/X86/gem5.opt -r hw6.py --cpu_type=O3CPU --binary=saxpy --options="$1"

tar -czf m5out_saxpy_O3.tar m5out/
