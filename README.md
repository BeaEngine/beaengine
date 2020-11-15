![beaengine](./doc/beaengine-logo.png)
# BeaEngine 5

BeaEngine is C library designed to decode instructions from 16 bits, 32 bits and 64 bits intel architectures. It includes standard instructions set and instructions set from FPU, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, VMX, CLMUL, AES, MPX, AVX, AVX2, AVX512 (VEX & EVEX prefixes), CET, BMI1, BMI2, SGX, UINTR, KL and TDX extensions. If you want to analyze malicious codes and more generally obfuscated codes, BeaEngine sends back a complex structure that describes precisely the analyzed instructions.

You can use it in C/C++ (usable and compilable with Visual Studio, GCC, MinGW, DigitalMars, BorlandC, WatcomC, SunForte, Pelles C, LCC), in assembler (usable with masm32 and masm64, nasm, fasm, GoAsm) in C#, in Python3, in Delphi, in PureBasic and in WinDev. You can use it in user mode and kernel mode.

First, you can retrieve mnemonic and operands according to the specified syntax : intel syntax for nasm, masm32 and masm64, GoAsm32 and GoAsm64, fasm (no AT&T syntax actually).
Next, you can realize accurate analysis on data-flow and control-flow to generate slices or obfuscation patterns.

Its source code is under LGPL3 license with a "Makefile builder" and headers for following languages : C/C++, C#, Python3, Delphi, PureBasic, masm32, masm64, nasm(x86 and x64), fasm(x86 and x64), GoAsm(x86 and x64).

BeaEngine has been implemented using opcode tables from the intel documentation and tables from Christian Ludloff website [www.sandpile.org](http://www.sandpile.org)

## LICENSE

This software is distributed under the LGPL license.
See the COPYING and COPYING.LESSER files for more details.


## quick start

### 1. How to use it with Python :

#### 1.1. Very simple example to read one instruction:
```
#!/usr/bin/python3

from BeaEnginePython import *

buffer = bytes.fromhex('6202054000443322')
instr = Disasm(buffer)
instr.read()
print(instr.repr())
```
Output is :

```
vpshufb zmm24, zmm31, zmmword ptr [r11+r14+0880h]
```

#### 1.2. Loop on *instructions flow* and extract instructions modifying `rax` register:  

```
#!/usr/bin/python3

from BeaEnginePython import *

buffer = bytes.fromhex('4831c04889fbffc04989c49031ed66586a005f80c40c')
instr = Disasm(buffer)
while instr.read() > 0:
  if instr.modifies("rax"):
    print(f"{instr.repr():20}rax register is modified")
  else:
    print(instr.repr())
```

Output is:

```
xor rax, rax        rax register is modified
mov rbx, rdi
inc eax             rax register is modified
mov r12, rax
nop
xor ebp, ebp
pop ax              rax register is modified
push 00000000h
pop rdi
add ah, 0Ch         rax register is modified
```

#### 1.3. Loop on *instructions flow* and follow jump instructions:

```
#!/usr/bin/python3

from BeaEnginePython import *

buffer = bytes.fromhex('e90000000090e901000000cc90')
instr = Disasm(buffer)
while instr.read() > 0:
  print(instr.repr())
  if instr.is_jump():
    instr.follow()

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

Each BeaEngine release is provided with pdf documentation:

```
sudo apt install pandoc texlive-latex-extra
cd doc
pandoc --highlight-style tango -V mainfont="Arial" -V geometry:margin=1cm --output=beaengine.pdf beaengine.md
pandoc --highlight-style tango -V mainfont="Arial" -V geometry:margin=1cm --output=examples.pdf examples.md
```


### 6. Examples

Some basic examples to show how BeaEngine is working [HERE](./doc/examples.md)

### 7. Dev corner

If you want to improve BeaEngine or just add some private features, here are some links :
 - [Adding new instructions](./doc/dev_corner.md)
