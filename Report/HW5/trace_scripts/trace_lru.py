# Trace Generation for LFU Replacement Policy

from m5.objects.ReplacementPolicies import LRURP as rp
'''
-------------- Access Pattern -----------------
	LD 0x0	    // Access #0 - Base address = 0x0   = 0     ; Start address = 0
	LD 0x81 	// Access #1 - Base address = 0x80  = 128   ; Start address = 129
	LD 0x100	// Access #2 - Base address = 0x100 = 256   ; Start address = 256
	LD 0x188	// Access #3 - Base address = 0x180 = 384   ; Start address = 392
	LD 0x4	    // Access #4 - Base address = 0x0   = 0     ; Start address = 4
	LD 0x200	// Access #5 - Base address = 0x200 = 512   ; Start address = 512
	LD 0x18C	// Access #6 - Base address = 0x180 = 384   ; Start address = 396
	LD 0x108	// Access #7 - Base address = 0x100 = 256   ; Start address = 264
	LD 0x380	// Access #8 - Base address = 0x380 = 896   ; Start address = 896
	LD 0x8	    // Access #9 - Base address = 0x0   = 0     ; Start address = 8
'''
def python_generator(generator):
    yield generator.createLinear(60000, 0, 63, 64, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 129, 191, 63, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 256, 319, 64, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 392, 447, 56, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 4, 63, 60, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 512, 575, 64, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 396, 447, 52, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 264, 319, 56, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 896, 959, 64, 30000, 30000, 100, 0)
    yield generator.createLinear(60000, 8, 63, 56, 30000, 30000, 100, 0)

    # Synchronization Step
    yield generator.createLinear(30000, 0, 0, 0, 30000, 30000, 100, 0)
    yield generator.createExit(0)
