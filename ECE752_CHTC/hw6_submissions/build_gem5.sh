#build.sh
# gem5 build shell script

scons build/X86/gem5.opt -j$(nproc) CPU_MODELS=AtomicSimpleCPU,TimingSimpleCPU,O3CPU,MinorCPU
tar -czf build.tar build/
