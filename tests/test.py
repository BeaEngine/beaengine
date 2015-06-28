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
        Instruction = DISASM()
        for instr in instructions:
          Buffer = struct.pack('<B', instr['seq']) 
          Target = create_string_buffer(Buffer,len(Buffer))
          Instruction.EIP = addressof(Target)
          InstrLength = Disasm(addressof(Instruction))
          assert_equal(Instruction.CompleteInstr, instr['entry'])

    def test_manyPrefixes(self):
        Buffer = b'\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x90'
        Instruction = DISASM()
        Target = create_string_buffer(Buffer,len(Buffer))
        Instruction.EIP = addressof(Target)
        InstrLength = Disasm(addressof(Instruction))
        assert_equal(Instruction.Prefix.Number, 15)
        assert_equal(Instruction.CompleteInstr, '')


    def test_adcx(self):
        Buffer = b'\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        Instruction = DISASM()
        Target = create_string_buffer(Buffer,len(Buffer))
        Instruction.EIP = addressof(Target)
        InstrLength = Disasm(addressof(Instruction))
        assert_equal(Instruction.CompleteInstr, '??? ')

        Buffer = b'\x66\x0f\x38\xf6\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 32)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf38f6')
        assert_equal(myDisasm.Instruction.Mnemonic, 'adcx ')
        assert_equal(myDisasm.Instruction.Category, GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION)
        assert_equal(myDisasm.CompleteInstr, 'adcx edx, dword ptr [eax+11111111h]')

        Buffer = b'\xf3\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        Instruction = DISASM()
        Target = create_string_buffer(Buffer,len(Buffer))
        Instruction.EIP = addressof(Target)
        InstrLength = Disasm(addressof(Instruction))
        assert_equal(Instruction.CompleteInstr, 'adox edx, dword ptr [eax-6F6F6F70h]')


    def test_imul(self):
        Buffer = b'\x69\x02\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG0)
        assert_equal(myDisasm.Argument1.ArgSize, 32)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'imul eax, dword ptr [rdx], 9090F683h')


    def test_VEX3Bytes(self):
        Buffer = b'\xc4\x82\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Reserved_.VEX.pp, 3)
        assert_equal(myDisasm.Reserved_.VEX.L, 0)
        assert_equal(myDisasm.Reserved_.VEX.mmmmm, 2)
        assert_equal(myDisasm.Reserved_.REX.W_, 1)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf6')
        assert_equal(~myDisasm.Reserved_.VEX.vvvv & 0b00001111, 15)
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 64)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 64)
        assert_equal(myDisasm.Argument2.AccessMode, WRITE)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 64)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'mulx rdx, r15, qword ptr [r8-6F6F6F70h]')


    def test_addpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addpd xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x44\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        myDisasm.Options = IntrinsicMemSyntax
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.CompleteInstr, 'addpd xmm10, __m128d [rax-6F6F6F70h]')


        Buffer = b'\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x81\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddpd xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x85\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + AVX_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 256)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + AVX_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 256)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 256)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddpd ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_addps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + AVX_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 256)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + AVX_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 256)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 256)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_addsd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\xF2\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 64)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addsd xmm10, qword ptr [rax-6F6F6F70h]')

        Buffer = b'\xF2\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 64)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addsd xmm2, qword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x83\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 64)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddsd xmm2, xmm15, qword ptr [r8+11111111h]')



    def test_addss(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\xF3\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addss xmm10, dword ptr [rax-6F6F6F70h]')

        Buffer = b'\xF3\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'addss xmm2, dword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x82\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 32)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddss xmm2, xmm15, dword ptr [r8+11111111h]')

    def test_mov(self):

        Buffer = b'\xB8\x04\x01\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG0)
        assert_equal(myDisasm.Argument1.ArgSize, 32)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Instruction.Immediat, 0x104)
        assert_equal(myDisasm.CompleteInstr, 'mov eax, 00000104h')

        Buffer = b'\x41\xB8\x04\x01\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG8)
        assert_equal(myDisasm.Argument1.ArgSize, 32)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(hex(myDisasm.Argument2.ArgType), hex(CONSTANT_TYPE+ABSOLUTE_))
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Instruction.Immediat, 0x104)
        assert_equal(myDisasm.CompleteInstr, 'mov r8d, 00000104h')

    def test_addsubpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x66\x0F\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xfd0')
        assert_equal(myDisasm.Instruction.Mnemonic, 'addsubpd ')
        assert_equal(myDisasm.Instruction.Category, SSE3_INSTRUCTION+SIMD_FP_PACKED)
        assert_equal(myDisasm.CompleteInstr, 'addsubpd xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x01\x01\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddsubpd xmm10, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x01\x05\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + AVX_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 256)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + AVX_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 256)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 256)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddsubpd ymm10, ymm15, ymmword ptr [r8+11111111h]')

    def test_addsubps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\xf2\x0F\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xfd0')
        assert_equal(myDisasm.Instruction.Mnemonic, 'addsubps ')
        assert_equal(myDisasm.Instruction.Category, SSE3_INSTRUCTION+SIMD_FP_PACKED)
        assert_equal(myDisasm.CompleteInstr, 'addsubps xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x01\x03\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddsubps xmm10, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x01\x07\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + AVX_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 256)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + AVX_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 256)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 256)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaddsubps ymm10, ymm15, ymmword ptr [r8+11111111h]')

    def test_aesdec(self):

        Buffer = b'\x66\x0F\x38\xDE\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf38de')
        assert_equal(myDisasm.CompleteInstr, 'aesdec xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDE\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaesdec xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesdeclast(self):

        Buffer = b'\x66\x0F\x38\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf38df')
        assert_equal(myDisasm.CompleteInstr, 'aesdeclast xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaesdeclast xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesenc(self):

        Buffer = b'\x66\x0F\x38\xDC\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf38dc')
        assert_equal(myDisasm.CompleteInstr, 'aesenc xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDC\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaesenc xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesenclast(self):

        Buffer = b'\x66\x0F\x38\xDD\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf38dd')
        assert_equal(myDisasm.CompleteInstr, 'aesenclast xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDD\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + SSE_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 128)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaesenclast xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesimc(self):

        Buffer = b'\x66\x0F\x38\xDB\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf38db')
        assert_equal(myDisasm.CompleteInstr, 'aesimc xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDB\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaesimc xmm10, xmmword ptr [r8+11111111h]')

    def test_aeskeygenassist(self):

        Buffer = b'\x66\x0F\x3A\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, CONSTANT_TYPE + ABSOLUTE_)
        assert_equal(myDisasm.Argument3.ArgSize, 8)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.Instruction.Immediat, 0x11)
        assert_equal(hex(myDisasm.Instruction.Opcode), '0xf3adf')
        assert_equal(myDisasm.CompleteInstr, 'aeskeygenassist xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x01\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + SSE_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 128)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument2.ArgSize, 128)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'vaeskeygenassist xmm10, xmmword ptr [r8+11111111h], 11h')

    def test_andn(self):

        Buffer = b'\xc4\x02\x00\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG10)
        assert_equal(myDisasm.Argument1.ArgSize, 32)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 32)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'andn r10d, r15d, dword ptr [r8+11111111h]')

        Buffer = b'\xc4\x82\x00\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 32)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 32)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 32)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'andn edx, r15d, dword ptr [r8+11111111h]')

        Buffer = b'\xc4\x82\x80\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = DISASM()
        myDisasm.Archi = 64
        Target = create_string_buffer(Buffer,len(Buffer))
        myDisasm.EIP = addressof(Target)
        InstrLength = Disasm(addressof(myDisasm))
        assert_equal(myDisasm.Argument1.ArgType, REGISTER_TYPE + GENERAL_REG + REG2)
        assert_equal(myDisasm.Argument1.ArgSize, 64)
        assert_equal(myDisasm.Argument1.AccessMode, WRITE)
        assert_equal(myDisasm.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG + REG15)
        assert_equal(myDisasm.Argument2.ArgSize, 64)
        assert_equal(myDisasm.Argument2.AccessMode, READ)
        assert_equal(myDisasm.Argument3.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.Argument3.ArgSize, 64)
        assert_equal(myDisasm.Argument3.AccessMode, READ)
        assert_equal(myDisasm.CompleteInstr, 'andn rdx, r15, qword ptr [r8+11111111h]')
