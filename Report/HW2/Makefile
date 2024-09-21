TARGET_ISA=x86

CODE_PATH=$(realpath ./../common/HW2)
GEM5_HOME=$(realpath ./)

CXX=g++

CFLAGS=-I$(GEM5_HOME)/include
LDFLAGS=-L$(GEM5_HOME)/util/m5/build/$(TARGET_ISA)/out -lm5

DASM_OBJECT=daxpy.s
BIN_OBJECT=daxpy

all: daxpy_dasm daxpy_bin

# To generate the disassembly code
daxpy_dasm:
	$(CXX) -S -O3 -o $(CODE_PATH)/$(DASM_OBJECT) $(CODE_PATH)/daxpy.cpp $(CFLAGS) $(LDFLAGS) -fverbose-asm

# To generate the binary required to run the gem5 sim
daxpy_bin:
	$(CXX) -O3 -o $(CODE_PATH)/$(BIN_OBJECT) $(CODE_PATH)/daxpy.cpp $(CFLAGS) $(LDFLAGS)

# Run the daxpy code with O2 level of optimization
daxpy_O2:
	$(CXX) -S -O2 -o $(CODE_PATH)/$(BIN_OBJECT)_O2 $(CODE_PATH)/daxpy.cpp $(CFLAGS) $(LDFLAGS) -fverbose-asm

# To clean the resultant directory
clean:
	rm -f $(CODE_PATH)/$(BIN_OBJECT)_O2 $(CODE_PATH)/$(BIN_OBJECT) $(CODE_PATH)/$(DASM_OBJECT)
