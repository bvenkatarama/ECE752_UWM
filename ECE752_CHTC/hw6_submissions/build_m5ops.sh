#!/bin/bash

cd util/m5/
scons build/x86/out/m5
tar -czf m5_build.tar build/
