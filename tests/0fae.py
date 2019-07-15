#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):

        # F3 0F AE /2
        # WRFSBASE r32

        Buffer = 'f30faed0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'wrfsbase ')
        assert_equal(myDisasm.instr.repr, 'wrfsbase eax')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument1.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument1.Registers.segment, REG4)

        # F3 REX.W 0F AE /2
        # WRFSBASE r64

        myREX = REX()
        myREX.W = 1
        Buffer = 'f3{:02x}0faed0'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'wrfsbase ')
        assert_equal(myDisasm.instr.repr, 'wrfsbase rax')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument1.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument1.Registers.segment, REG4)

        # F3 0F AE /3
        # WRGSBASE r32

        Buffer = 'f30faed8'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'wrgsbase ')
        assert_equal(myDisasm.instr.repr, 'wrgsbase eax')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument1.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument1.Registers.segment, REG5)

        # F3 REX.W 0F AE /3
        # WRGSBASE r64

        myREX = REX()
        myREX.W = 1
        Buffer = 'f3{:02x}0faed8'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'wrgsbase ')
        assert_equal(myDisasm.instr.repr, 'wrgsbase rax')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument1.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument1.Registers.segment, REG5)

        # F3 0F AE /0
        # RDFSBASE r32

        Buffer = 'f30faec0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rdfsbase ')
        assert_equal(myDisasm.instr.repr, 'rdfsbase eax')
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument2.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument2.Registers.segment, REG4)

        # F3 REX.W 0F AE /0
        # RDFSBASE r64

        myREX = REX()
        myREX.W = 1
        Buffer = 'f3{:02x}0faec0'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rdfsbase ')
        assert_equal(myDisasm.instr.repr, 'rdfsbase rax')
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument2.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument2.Registers.segment, REG4)

        # F3 0F AE /1
        # RDGSBASE r32

        Buffer = 'f30faec8'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rdgsbase ')
        assert_equal(myDisasm.instr.repr, 'rdgsbase eax')
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument2.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument2.Registers.segment, REG5)

        # F3 REX.W 0F AE /1
        # RDGSBASE r64

        myREX = REX()
        myREX.W = 1
        Buffer = 'f3{:02x}0faec8'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rdgsbase ')
        assert_equal(myDisasm.instr.repr, 'rdgsbase rax')
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument2.Registers.type, SEGMENT_REG)
        assert_equal(myDisasm.instr.Argument2.Registers.segment, REG5)

        # F3 REX.W 0F AE /4
        # PTWRITE r64/m64

        myREX = REX()
        myREX.W = 1
        Buffer = 'f3{:02x}0fae20'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'ptwrite ')
        assert_equal(myDisasm.instr.repr, 'ptwrite qword ptr [rax]')
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)

        # F3 0F AE /4
        # PTWRITE r32/m32

        Buffer = 'f30fae20'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'ptwrite ')
        assert_equal(myDisasm.instr.repr, 'ptwrite dword ptr [rax]')
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)

        # 66 0F AE /6
        # CLWB m8

        Buffer = '660fae30'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'clwb ')
        assert_equal(myDisasm.instr.repr, 'clwb byte ptr [rax]')

        # 66 0F AE /7
        # CLFLUSHOPT m8

        Buffer = '660fae38'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'clflushopt ')
        assert_equal(myDisasm.instr.repr, 'clflushopt byte ptr [rax]')

        # NP 0F AE /0
        # FXSAVE m512byte

        Buffer = '0fae00'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'fxsave ')
        assert_equal(myDisasm.instr.repr, 'fxsave  [rax]')

        # NP REX.W + 0F AE /0
        # FXSAVE64 m512byte

        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0fae00'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'fxsave64 ')
        assert_equal(myDisasm.instr.repr, 'fxsave64  [rax]')
        assert_equal(myDisasm.instr.Argument1.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 512 * 8)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE)


        # NP 0F AE /1
        # FXRSTOR m512byte

        Buffer = '0fae08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'fxrstor ')
        assert_equal(myDisasm.instr.repr, 'fxrstor  [rax]')

        # NP REX.W + 0F AE /1
        # FXRSTOR64 m512byte

        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0fae08'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'fxrstor64 ')
        assert_equal(myDisasm.instr.repr, 'fxrstor64  [rax]')
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 512 * 8)
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE)

        # NP 0F AE /2
        # LDMXCSR m32

        Buffer = '0fae10'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'ldmxcsr ')
        assert_equal(myDisasm.instr.repr, 'ldmxcsr dword ptr [rax]')

        # VEX.LZ.0F.WIG AE /2
        # VLDMXCSR m32

        myVEX = VEX('VEX.LZ.0F.WIG')
        Buffer = '{}ae10'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xae)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vldmxcsr ')
        assert_equal(myDisasm.instr.repr, 'vldmxcsr dword ptr [r8]')


        # Saves the states of x87 FPU, MMX, XMM, YMM, and MXCSR registers to memory,
        # optimizing the save operation if possible.

        # NP 0F AE /6
        # XSAVEOPT mem

        Buffer = '0fae30'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xsaveopt ')
        assert_equal(myDisasm.instr.repr, 'xsaveopt  [rax]')


        # NP REX.W + 0F AE /6
        # XSAVEOPT64 mem

        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0fae30'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xsaveopt64 ')
        assert_equal(myDisasm.instr.repr, 'xsaveopt64  [rax]')
        assert_equal(myDisasm.instr.Argument1.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 512 * 8)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE)
        assert_equal(myDisasm.instr.Argument2.Registers.type, GENERAL_REG)
        assert_equal(myDisasm.instr.Argument2.Registers.gpr, REG0 + REG2)
