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
import struct
import yaml

class TestSuite:

    def test_SimpleInstructions(self):
        stream = open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'opcode1byte.yml')), "r")
        instructions = yaml.load(stream)

        for instr in instructions:
          Buffer = struct.pack('<B', instr['seq'])
          myDisasm = Disasm(Buffer)
          myDisasm.instr.Archi = 32
          myDisasm.read()
          assert_equal(myDisasm.instr.repr, instr['entry'])

    def test_manyPrefixes(self):
        Buffer = b'\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Prefix.Number, 15)
        assert_equal(myDisasm.instr.repr, '')


    def test_adcx(self):
        Buffer = b'\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, '??? ')

        Buffer = b'\x66\x0f\x38\xf6\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf38f6')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'adcx ')
        assert_equal(myDisasm.instr.Instruction.Category, GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION)
        assert_equal(myDisasm.instr.repr, 'adcx edx, dword ptr [rax+11111111h]')

        Buffer = b'\xf3\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'adox edx, dword ptr [rax-6F6F6F70h]')


    def test_imul(self):
        Buffer = b'\x69\x02\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'imul eax, dword ptr [rdx], 9090F683h')


    def test_VEX3Bytes(self):
        Buffer = b'\xc4\x82\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.VEX.pp, 3)
        assert_equal(myDisasm.instr.Reserved_.VEX.L, 0)
        assert_equal(myDisasm.instr.Reserved_.VEX.mmmmm, 2)
        assert_equal(myDisasm.instr.Reserved_.REX.W_, 1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf6')
        assert_equal(myDisasm.instr.Reserved_.VEX.vvvv & 0b1111, 0)
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'mulx rdx, r15, qword ptr [r8-6F6F6F70h]')


    def test_addpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addpd xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x44\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)

        myDisasm.instr.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'addpd xmm10, m128d [rax-6F6F6F70h]')


        Buffer = b'\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x81\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddpd xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x85\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddpd ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_addps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_addsd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\xF2\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addsd xmm10, qword ptr [rax-6F6F6F70h]')

        Buffer = b'\xF2\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addsd xmm2, qword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x83\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddsd xmm2, xmm15, qword ptr [r8+11111111h]')



    def test_addss(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\xF3\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addss xmm10, dword ptr [rax-6F6F6F70h]')

        Buffer = b'\xF3\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'addss xmm2, dword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x82\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddss xmm2, xmm15, dword ptr [r8+11111111h]')

    def test_mov(self):

        Buffer = b'\xB8\x04\x01\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x104)
        assert_equal(myDisasm.instr.repr, 'mov eax, 00000104h')

        Buffer = b'\x41\xB8\x04\x01\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(hex(myDisasm.instr.Argument2.ArgType), hex(CONSTANT_TYPE+ABSOLUTE_))
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x104)
        assert_equal(myDisasm.instr.repr, 'mov r8d, 00000104h')

    def test_addsubpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x66\x0F\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfd0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'addsubpd ')
        assert_equal(myDisasm.instr.Instruction.Category, SSE3_INSTRUCTION+SIMD_FP_PACKED)
        assert_equal(myDisasm.instr.repr, 'addsubpd xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x01\x01\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddsubpd xmm10, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x01\x05\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddsubpd ymm10, ymm15, ymmword ptr [r8+11111111h]')

    def test_addsubps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\xf2\x0F\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfd0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'addsubps ')
        assert_equal(myDisasm.instr.Instruction.Category, SSE3_INSTRUCTION+SIMD_FP_PACKED)
        assert_equal(myDisasm.instr.repr, 'addsubps xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x01\x03\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddsubps xmm10, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x01\x07\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaddsubps ymm10, ymm15, ymmword ptr [r8+11111111h]')

    def test_aesdec(self):

        Buffer = b'\x66\x0F\x38\xDE\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf38de')
        assert_equal(myDisasm.instr.repr, 'aesdec xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDE\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaesdec xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesdeclast(self):

        Buffer = b'\x66\x0F\x38\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf38df')
        assert_equal(myDisasm.instr.repr, 'aesdeclast xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaesdeclast xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesenc(self):

        Buffer = b'\x66\x0F\x38\xDC\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf38dc')
        assert_equal(myDisasm.instr.repr, 'aesenc xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDC\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaesenc xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesenclast(self):

        Buffer = b'\x66\x0F\x38\xDD\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf38dd')
        assert_equal(myDisasm.instr.repr, 'aesenclast xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDD\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaesenclast xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesimc(self):

        Buffer = b'\x66\x0F\x38\xDB\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf38db')
        assert_equal(myDisasm.instr.repr, 'aesimc xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDB\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaesimc xmm10, xmmword ptr [r8+11111111h]')

    def test_aeskeygenassist(self):

        Buffer = b'\x66\x0F\x3A\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, CONSTANT_TYPE + ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x11)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3adf')
        assert_equal(myDisasm.instr.repr, 'aeskeygenassist xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x01\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vaeskeygenassist xmm10, xmmword ptr [r8+11111111h], 11h')

    def test_andn(self):

        Buffer = b'\xc4\x02\x00\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andn r10d, r15d, dword ptr [r8+11111111h]')

        Buffer = b'\xc4\x82\x00\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andn edx, r15d, dword ptr [r8+11111111h]')

        Buffer = b'\xc4\x82\x80\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andn rdx, r15, qword ptr [r8+11111111h]')

    def test_andps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vandps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vandps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_andnps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x55\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andnps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x55\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andnps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x55\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vandnps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x55\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vandnps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_andpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andpd xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x44\x66\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)

        myDisasm.instr.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'andpd xmm10, m128d [rax-6F6F6F70h]')


        Buffer = b'\x66\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'andpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x81\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vandpd xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x85\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vandpd ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_blendpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x3A\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blendpd xmm10, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\x44\x66\x0F\x3A\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)

        myDisasm.instr.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'blendpd xmm10, m128 [rax+11111111h], 11h')


        Buffer = b'\x66\x0F\x3A\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blendpd xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x81\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.instr.repr, 'vblendpd xmm10, xmmword ptr [r8+11111111h], 11h')

        Buffer = b'\xc4\x03\x85\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.instr.repr, 'vblendpd ymm10, ymmword ptr [r8+11111111h], 11h')

    def test_blendps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x3A\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blendps xmm10, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\x44\x66\x0F\x3A\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)

        myDisasm.instr.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'blendps xmm10, m128 [rax+11111111h], 11h')


        Buffer = b'\x66\x0F\x3A\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG2)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blendps xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x81\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.instr.repr, 'vblendps xmm10, xmmword ptr [r8+11111111h], 11h')

        Buffer = b'\xc4\x03\x85\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.instr.repr, 'vblendps ymm10, ymmword ptr [r8+11111111h], 11h')

    def test_bextr(self):

        Buffer = b'\xc4\x02\x04\xf7\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'bextr r10d, dword ptr [r8+11111111h], r15d')

        Buffer = b'\xc4\x02\x80\xf7\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'bextr r10, qword ptr [r8+11111111h], r15')

    def test_blendvpd(self):

        Buffer = b'\x44\x66\x0F\x38\x15\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blendvpd xmm10, xmmword ptr [rax+11111111h], xmm0')

        Buffer = b'\xc4\x02\x85\x15\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument4.ArgType, REGISTER_TYPE + AVX_REG) # REG0)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vblendvpd ymm10, ymm15, ymmword ptr [r8+11111111h], ymm0')


        Buffer = b'\xc4\x02\x81\x15\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument4.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vblendvpd xmm10, xmm15, xmmword ptr [r8+11111111h], xmm0')

    def test_blendvps(self):

        Buffer = b'\x44\x66\x0F\x38\x14\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blendvps xmm10, xmmword ptr [rax+11111111h], xmm0')

        Buffer = b'\xc4\x02\x85\x14\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + AVX_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + AVX_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument4.ArgType, REGISTER_TYPE + AVX_REG) # REG0)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 256)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vblendvps ymm10, ymm15, ymmword ptr [r8+11111111h], ymm0')


        Buffer = b'\xc4\x02\x81\x14\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)

        assert_equal(myDisasm.instr.Argument4.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vblendvps xmm10, xmm15, xmmword ptr [r8+11111111h], xmm0')

    def test_blsi(self):

        Buffer = b'\xc4\x02\x00\xf3\x18\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blsi r15d, dword ptr [r8]')

        Buffer = b'\xc4\x02\x80\xf3\x18\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blsi r15, qword ptr [r8]')

    def test_blmsk(self):

        Buffer = b'\xc4\x02\x00\xf3\x10\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blmsk r15d, dword ptr [r8]')

        Buffer = b'\xc4\x02\x80\xf3\x10\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blmsk r15, qword ptr [r8]')

    def test_blsr(self):

        Buffer = b'\xc4\x02\x00\xf3\x08\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blsr r15d, dword ptr [r8]')

        Buffer = b'\xc4\x02\x80\xf3\x08\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'blsr r15, qword ptr [r8]')

    def test_bzhi(self):

        Buffer = b'\xc4\x02\x04\xf5\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'bzhi r10d, dword ptr [r8+11111111h], r15L')

        Buffer = b'\xc4\x02\x80\xf5\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG) # REG10)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType, REGISTER_TYPE + GENERAL_REG) # REG15)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'bzhi r10, qword ptr [r8+11111111h], r15L')

    def test_clac(self):

        Buffer = b'\x0F\x01\xCA\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'clac ')

    def test_cmppd(self):

        Buffer = b'\x66\x0F\xC2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpeqpd xmm0, xmmword ptr [rax], 00h')

        Buffer = b'\x66\x0F\xC2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpltpd xmm0, xmmword ptr [rax], 01h')

        Buffer = b'\x66\x0F\xC2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmplepd xmm0, xmmword ptr [rax], 02h')

        Buffer = b'\x66\x0F\xC2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpunordpd xmm0, xmmword ptr [rax], 03h')

        Buffer = b'\x66\x0F\xC2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpneqpd xmm0, xmmword ptr [rax], 04h')

        Buffer = b'\x66\x0F\xC2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpnltpd xmm0, xmmword ptr [rax], 05h')

        Buffer = b'\x66\x0F\xC2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpnlepd xmm0, xmmword ptr [rax], 06h')

        Buffer = b'\x66\x0F\xC2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpordpd xmm0, xmmword ptr [rax], 07h')

        Buffer = b'\xc4\x01\x81\xc2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpeqpd xmm8, xmm15, xmmword ptr [r8], 00h')

        compare = [
            'eq', 'lt', 'le', 'unord', 'neq', 'nlt', 'nle', 'ord',
            "eq_uq", "nge", "ngt", "false", "neq_oq",  "ge", "gt",
            "true", "eq_os", "lt_oq", "le_oq", "unord_s", "neq_us",
            "nlt_uq", "nle_uq", "ord_s", "eq_us", "nge_uq", "ngt_uq",
            "false_os", "neq_os", "ge_oq", "gt_oq", "true_us"
        ]

        for i in range(0,0x20):
            Buffer = b'c40181c200{:02x}'.format(i).decode('hex')
            myDisasm = Disasm(Buffer)
            myDisasm.read()
            assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
            assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
            assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
            assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
            assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
            assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
            assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
            assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
            assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
            assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
            assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
            assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
            assert_equal(myDisasm.instr.repr, 'vcmp{}pd xmm8, xmm15, xmmword ptr [r8], {:02X}h'.format(compare[i], i))


    def test_cmpps(self):

        Buffer = b'\x0F\xC2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpeqps xmm0, xmmword ptr [rax], 00h')

        Buffer = b'\x0F\xC2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpltps xmm0, xmmword ptr [rax], 01h')

        Buffer = b'\x0F\xC2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpleps xmm0, xmmword ptr [rax], 02h')

        Buffer = b'\x0F\xC2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpunordps xmm0, xmmword ptr [rax], 03h')

        Buffer = b'\x0F\xC2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpneqps xmm0, xmmword ptr [rax], 04h')

        Buffer = b'\x0F\xC2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpnltps xmm0, xmmword ptr [rax], 05h')

        Buffer = b'\x0F\xC2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpnleps xmm0, xmmword ptr [rax], 06h')

        Buffer = b'\x0F\xC2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpordps xmm0, xmmword ptr [rax], 07h')


    def test_cmpsd(self):

        Buffer = b'\xF2\x0F\xC2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpeqsd xmm0, qword ptr [rax], 00h')

        Buffer = b'\xF2\x0F\xC2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpltsd xmm0, qword ptr [rax], 01h')

        Buffer = b'\xF2\x0F\xC2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmplesd xmm0, qword ptr [rax], 02h')

        Buffer = b'\xF2\x0F\xC2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpunordsd xmm0, qword ptr [rax], 03h')

        Buffer = b'\xF2\x0F\xC2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpneqsd xmm0, qword ptr [rax], 04h')

        Buffer = b'\xF2\x0F\xC2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpnltsd xmm0, qword ptr [rax], 05h')

        Buffer = b'\xF2\x0F\xC2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpnlesd xmm0, qword ptr [rax], 06h')

        Buffer = b'\xF2\x0F\xC2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'cmpordsd xmm0, qword ptr [rax], 07h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vcmpeqsd xmm8, xmm15, xmmword ptr [r8], 00h')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)


        Buffer = b'\xc4\x01\x83\xc2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vcmpltsd xmm8, xmm15, xmmword ptr [r8], 01h')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)


        Buffer = b'\xc4\x01\x83\xc2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmplesd xmm8, xmm15, xmmword ptr [r8], 02h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpunordsd xmm8, xmm15, xmmword ptr [r8], 03h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpneqsd xmm8, xmm15, xmmword ptr [r8], 04h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpnltsd xmm8, xmm15, xmmword ptr [r8], 05h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpnlesd xmm8, xmm15, xmmword ptr [r8], 06h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpordsd xmm8, xmm15, xmmword ptr [r8], 07h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x08\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpeq_uqsd xmm8, xmm15, xmmword ptr [r8], 08h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x09\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpngesd xmm8, xmm15, xmmword ptr [r8], 09h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0a\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpngtsd xmm8, xmm15, xmmword ptr [r8], 0Ah')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpfalsesd xmm8, xmm15, xmmword ptr [r8], 0Bh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0c\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpneq_oqsd xmm8, xmm15, xmmword ptr [r8], 0Ch')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0d\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpgesd xmm8, xmm15, xmmword ptr [r8], 0Dh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0e\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpgtsd xmm8, xmm15, xmmword ptr [r8], 0Eh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0f\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmptruesd xmm8, xmm15, xmmword ptr [r8], 0Fh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x10\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpeq_ossd xmm8, xmm15, xmmword ptr [r8], 10h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmplt_oqsd xmm8, xmm15, xmmword ptr [r8], 11h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x12\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmple_oqsd xmm8, xmm15, xmmword ptr [r8], 12h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x13\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpunord_ssd xmm8, xmm15, xmmword ptr [r8], 13h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x14\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpneq_ussd xmm8, xmm15, xmmword ptr [r8], 14h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x15\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpnlt_uqsd xmm8, xmm15, xmmword ptr [r8], 15h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x16\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpnle_uqsd xmm8, xmm15, xmmword ptr [r8], 16h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x17\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpord_ssd xmm8, xmm15, xmmword ptr [r8], 17h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x18\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpeq_ussd xmm8, xmm15, xmmword ptr [r8], 18h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x19\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpnge_uqsd xmm8, xmm15, xmmword ptr [r8], 19h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1a\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpngt_uqsd xmm8, xmm15, xmmword ptr [r8], 1Ah')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1b\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpfalse_ossd xmm8, xmm15, xmmword ptr [r8], 1Bh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1c\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpneq_ossd xmm8, xmm15, xmmword ptr [r8], 1Ch')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1d\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpge_oqsd xmm8, xmm15, xmmword ptr [r8], 1Dh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1e\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmpgt_oqsd xmm8, xmm15, xmmword ptr [r8], 1Eh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1f\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + SSE_REG) # REG8)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + SSE_REG) # REG15)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument3.ArgType,  + MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument3.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument3.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument4.ArgType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.instr.Argument4.ArgSize, 8)
        assert_equal(myDisasm.instr.Argument4.AccessMode, READ)
        assert_equal(myDisasm.instr.repr, 'vcmptrue_ussd xmm8, xmm15, xmmword ptr [r8], 1Fh')


    def test_mpx(self):

        Buffer = b'\xf3\x41\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndcl bnd1, dword ptr [r11]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf3\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndcl bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf2\x41\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndcu bnd1, dword ptr [r11]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf2\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndcu bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf2\x41\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndcn bnd1, dword ptr [r11]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf2\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndcn bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf3\x41\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndmk bnd1, dword ptr [r11]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\xf3\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndmk bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, READ)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)



        Buffer = b'\x66\x0f\x1a\xc0\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 0
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndmov bnd0, bnd0')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) # + REG0)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + MPX_REG) # + REG0)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)


        Buffer = b'\x66\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndmov bnd1, dqword ptr [rbx]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\x66\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndmov bnd1, qword ptr [ebx]')
        assert_equal(myDisasm.instr.Argument1.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\x66\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndmov qword ptr [ebx], bnd1')
        assert_equal(myDisasm.instr.Argument1.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 64)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\x0f\x1b\x0c\x10\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'bndstx dword ptr [rax+rdx], bnd1')
        assert_equal(myDisasm.instr.Argument1.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 32)
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + MPX_REG) #REG1)
        assert_equal(myDisasm.instr.Argument2.ArgSize, 128)
        assert_equal(myDisasm.instr.Argument2.AccessMode, READ)

        Buffer = b'\x66\xf3\xa5'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'rep movsw ')

        Buffer = b'\xf3\x66\xa5'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'rep movsw ')

        Buffer = '67654c6973743a'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'imul r14, qword ptr [ebx+74h], 0000003Ah')

        Buffer = '660f73fa02'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'pslldq xmm2, 02h')

        Buffer = '660f73fa02'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 16
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, '??? ')

        Buffer = '820000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'add byte ptr [eax], 00h')

        Buffer = '821000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'adc byte ptr [eax], 00h')

        Buffer = '823000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'xor byte ptr [eax], 00h')

        Buffer = '6ab7'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'push FFFFFFB7h')

        Buffer = '\xf0\x22\xbd\x71\x20\x17\x00'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'lock and bh, byte ptr [rbp+00172071h]')

        Buffer = '\xd3\xb6\x6b\x8f\xac\xa0'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'sal dword ptr [rsi-5F537095h], cl')

        Buffer = '66F3A7'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'rep cmpsw ')

    def test_lock(self):
        '''Minimal regression tests for https://github.com/BeaEngine/beaengine/issues/9'''

        Buffer = 'f04889ce'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Prefix.LockPrefix, InvalidPrefix)
        assert_equal(myDisasm.instr.repr, 'lock mov rsi, rcx')


        Buffer = '4889ce'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'mov rsi, rcx')

        Buffer = '48'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'dec eax')

        Buffer = 'f048'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'lock dec eax')
        assert_equal(myDisasm.instr.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f0feC9'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'lock dec cl')
        assert_equal(myDisasm.instr.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f0fe8811223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'lock dec byte ptr [rax+44332211h]')
        assert_equal(myDisasm.instr.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, 0)

        Buffer = 'f0ffC9'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'lock dec ecx')
        assert_equal(myDisasm.instr.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f0ff8811223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'lock dec dword ptr [rax+44332211h]')
        assert_equal(myDisasm.instr.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, 0)
