![beaengine](./doc/beaengine-logo.png)
# BeaEngine 5

BeaEngine is a library coded in C respecting ISO C99 norm. It has been designed to decode instructions from 16 bits, 32 bits and 64 bits intel architectures. Actually, the main function available is called Disasm. It includes standard instruction set and instruction set from FPU, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, VMX, CLMUL, AES, MPX, AVX, AVX2, AVX512 (VEX & EVEX prefixes), CET, BMI1, BMI2, SGX technologies. For those who like analyzing malicious codes and more generally obfuscated codes, BeaEngine even decodes undocumented instructions called "alias" on the web site sandpile. In all scenarios, it sends back a complex structure that describes precisely the analyzed instructions.

You can use it in C/C++ (usable and compilable with Visual Studio, GCC, MinGW, DigitalMars, BorlandC, WatcomC, SunForte, Pelles C, LCC), in assembler (usable with masm32 and masm64, nasm, fasm, GoAsm) in C#, in Python, in Delphi, in PureBasic and in WinDev. You can use it in user mode and kernel mode. It has been thought to do a lot of tasks.

First, you can retrieve mnemonic and operands according to the specified syntax : intel syntax for Nasm, masm32 and masm64, GoAsm32 and GoAsm64, fasm (no AT&T syntax actually).
Next, you can realize accurate analysis on data-flow and control-flow to generate slices or obfuscation patterns.

Its source code is under LGPL3 license with a "Makefile builder" and headers for following languages : C/C++, C#, Python, Delphi, PureBasic, masm32, masm64, nasm(x86 and x64), fasm(x86 and x64), GoAsm(x86 and x64).

BeaEngine has been implemented using opcode tables from the intel documentation and tables from Christian Ludloff website [www.sandpile.org](http://www.sandpile.org)

## LICENSE

This software is distributed under the LGPL license.
See the COPYING and COPYING.LESSER files for more details.


## quick start

### 1. How to use it with Python :
```
from BeaEnginePython import *
buffer = '6202054000443322'.decode('hex')
target = Disasm(buffer)
target.read()
print(target.repr())
```
Output is :

```
vpshufb zmm24, zmm31, zmmword ptr [r11+r14+0880h]
```

### 2. Releases

https://github.com/BeaEngine/beaengine/releases

### 3. How to Compile :

```
apt install cmake
git clone https://github.com/BeaEngine/beaengine.git
cmake beaengine
make
```

### 4. Compile shared library :
```
cmake -DoptBUILD_DLL=ON beaengine
make

```

### 5. Documentation

Current documentation [HERE](./doc/beaengine.md) explains how are working structures from BeaEngine.

*old documentation can be read here :* http://beatrix2004.free.fr/BeaEngine/index1.php

### 6. Examples

Some basic examples to show how BeaEngine is working [HERE](./doc/examples.md)

### 7. Dev corner

If you want to improve BeaEngine or just add some private features, here are some links :
 - [Adding new instructions](./doc/dev_corner.md)
