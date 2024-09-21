import m5
from m5.objects import *
m5.util.addToPath("../")
from caches import *
from cpu import *

# Default to running 'sieve', use the compiled ISA to find the binary
# grab the specific path to the binary
thispath = os.path.dirname(os.path.realpath(__file__))
default_binary = os.path.join(
        thispath,
        "../../../..",
        "common/HW2/daxpy",
)

import argparse
parser = argparse.ArgumentParser(description='Running the DAXPY program.')
parser.add_argument("--binary", default=default_binary, nargs="?", type=str, help="Path to the binary to execute.")
parser.add_argument("--l1i_size", help=f"L1 instruction cache size. Default: 16kB.")
parser.add_argument("--l1d_size", help="L1 data cache size. Default: 64kB.")
parser.add_argument("--l2_size", help="L2 cache size. Default: 256kB.")
parser.add_argument("--freq",default="1GHz", help="Operating Clock Frequency")
parser.add_argument("--cpu", default="simple", help="CPU type. 1)simple 2)minor 3)mycpu")
parser.add_argument("--mem", default= 1, type= int,
        help="Select type of memory.1)DDR3_1600_8x8 2)DDR3_2133_8x8 3)LPDDR2_S4_1066_1x32 4)HBM_1000_4H_1x64 5)HBM_2000_4H_1x64")
# Adding support for opLat and issueLat
parser.add_argument("--fpu_opLat", default=6, type=int, help="Operation latency for FPU SIMD functional unit")
parser.add_argument("--fpu_issueLat", default=1, type=int, help="Issue latency for FPU SIMD functional unit")
parser.add_argument("--int_opLat", default=1, type=int, help="Operation latency for Int functional unit")

args = parser.parse_args()

# create the system we are going to simulate
system = System()

# Set the clock frequency of the system (and all of its children)
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = args.freq
system.clk_domain.voltage_domain = VoltageDomain()

# Set up the system
system.mem_mode = "timing"  # Use timing accesses
system.mem_ranges = [AddrRange("512MB")]  # Create an address range

# Create a simple CPU
if args.cpu == "simple":
    system.cpu = X86TimingSimpleCPU()
elif args.cpu == "minor":
    system.cpu = X86MinorCPU()
else:
    system.cpu = MyMinorCPU(args)

# Create an L1 instruction and data cache
system.cpu.icache = L1ICache(args)
system.cpu.dcache = L1DCache(args)

# Connect the instruction and data caches to the CPU
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# Create a memory bus, a coherent crossbar, in this case
system.l2bus = L2XBar()

# Hook the CPU ports up to the l2bus
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# Create an L2 cache and connect it to the l2bus
system.l2cache = L2Cache(args)
system.l2cache.connectCPUSideBus(system.l2bus)

# Create a memory bus
system.membus = SystemXBar()

# Connect the L2 cache to the membus
system.l2cache.connectMemSideBus(system.membus)

# create the interrupt controller for the CPU
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

# Connect the system up to the membus
system.system_port = system.membus.cpu_side_ports

# Create a DDR3 memory controller
system.mem_ctrl = MemCtrl()

if args.mem == 1:
    system.mem_ctrl.dram = DDR3_1600_8x8()
if args.mem == 2:
    system.mem_ctrl.dram = DDR3_2133_8x8()
if args.mem == 3:
    system.mem_ctrl.dram = LPDDR2_S4_1066_1x32()
if args.mem == 4:
    system.mem_ctrl.dram = HBM_1000_4H_1x64()
if args.mem == 5:
    system.mem_ctrl.dram = HBM_2000_4H_1x64()

system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

system.workload = SEWorkload.init_compatible(args.binary)

# Create a process for a simple "Hello World" application
process = Process()
# Set the command
# cmd is a list which begins with the executable (like argv)
process.cmd = [args.binary]
# Set the cpu to use the process as its workload and create thread contexts
system.cpu.workload = process
system.cpu.createThreads()

# set up the root SimObject and start the simulation
root = Root(full_system=False, system=system)
# instantiate all of the objects we've created above
m5.instantiate()

print(f"Beginning simulation!")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")
