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
          myDisasm.infos.Archi = 32
          myDisasm.read()
          assert_equal(myDisasm.infos.repr, instr['entry'])

    def test_manyPrefixes(self):
        Buffer = b'\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Prefix.Number, 14)
        assert_equal(myDisasm.infos.repr, '')


    def test_adcx(self):
        Buffer = b'\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'wrssd dword ptr [rax-6F6F6F70h], edx')

        Buffer = b'\x66\x0f\x38\xf6\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38f6')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'adcx ')
        assert_equal(myDisasm.infos.Instruction.Category, GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION)
        assert_equal(myDisasm.infos.repr, 'adcx edx, dword ptr [rax+11111111h]')

        Buffer = b'\xf3\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'adox edx, dword ptr [rax-6F6F6F70h]')


    def test_imul(self):
        Buffer = b'\x69\x02\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'imul eax, dword ptr [rdx], 9090F683h')


    def test_VEX3Bytes(self):
        Buffer = b'\xc4\x82\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.VEX.pp, 3)
        assert_equal(myDisasm.infos.Reserved_.VEX.L, 0)
        assert_equal(myDisasm.infos.Reserved_.VEX.mmmmm, 2)
        assert_equal(myDisasm.infos.Reserved_.REX.W_, 1)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf6')
        assert_equal(myDisasm.infos.Reserved_.VEX.vvvv & 0b1111, 0)
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 64)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'mulx rdx, r15, qword ptr [r8-6F6F6F70h]')


    def test_addpd(self):
        # using REX.R to access extended xmm registers
        Buffer = '44660F58909090909090909090909090'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x44\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)

        myDisasm.infos.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'addpd xmm2, m128d [rax-6F6F6F70h]')


        Buffer = b'\x66\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x81\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddpd xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x85\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddpd ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_addps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_addsd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'44F20F589090909090'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addsd xmm2, qword ptr [rax-6F6F6F70h]')

        Buffer = b'\xF2\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addsd xmm2, qword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x83\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 64)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddsd xmm2, xmm15, qword ptr [r8+11111111h]')



    def test_addss(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\xF3\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addss xmm2, dword ptr [rax-6F6F6F70h]')

        Buffer = b'\xF3\x0F\x58\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'addss xmm2, dword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x82\x58\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 32)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddss xmm2, xmm15, dword ptr [r8+11111111h]')

    def test_mov(self):

        Buffer = b'\xB8\x04\x01\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x104)
        assert_equal(myDisasm.infos.repr, 'mov eax, 00000104h')

        Buffer = b'\x41\xB8\x04\x01\x00\x00\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(hex(myDisasm.infos.Operand2.OpType), hex(CONSTANT_TYPE+ABSOLUTE_))
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x104)
        assert_equal(myDisasm.infos.repr, 'mov r8d, 00000104h')

    def test_addsubpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x66\x0F\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xfd0')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'addsubpd ')
        assert_equal(myDisasm.infos.Instruction.Category, SSE3_INSTRUCTION+SIMD_FP_PACKED)
        assert_equal(myDisasm.infos.repr, 'addsubpd xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x01\x01\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddsubpd xmm10, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x01\x05\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddsubpd ymm10, ymm15, ymmword ptr [r8+11111111h]')

    def test_addsubps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\xf2\x0F\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xfd0')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'addsubps ')
        assert_equal(myDisasm.infos.Instruction.Category, SSE3_INSTRUCTION+SIMD_FP_PACKED)
        assert_equal(myDisasm.infos.repr, 'addsubps xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x01\x03\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddsubps xmm10, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x01\x07\xD0\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaddsubps ymm10, ymm15, ymmword ptr [r8+11111111h]')

    def test_aesdec(self):

        Buffer = b'\x66\x0F\x38\xDE\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38de')
        assert_equal(myDisasm.infos.repr, 'aesdec xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDE\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaesdec xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesdeclast(self):

        Buffer = b'\x66\x0F\x38\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38df')
        assert_equal(myDisasm.infos.repr, 'aesdeclast xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaesdeclast xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesenc(self):

        Buffer = b'\x66\x0F\x38\xDC\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38dc')
        assert_equal(myDisasm.infos.repr, 'aesenc xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDC\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaesenc xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesenclast(self):

        Buffer = b'\x66\x0F\x38\xDD\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38dd')
        assert_equal(myDisasm.infos.repr, 'aesenclast xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDD\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaesenclast xmm10, xmm15, xmmword ptr [r8+11111111h]')

    def test_aesimc(self):

        Buffer = b'\x66\x0F\x38\xDB\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf38db')
        assert_equal(myDisasm.infos.repr, 'aesimc xmm2, xmmword ptr [rax+11111111h]')

        Buffer = b'\xc4\x02\x01\xDB\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaesimc xmm10, xmmword ptr [r8+11111111h]')

    def test_aeskeygenassist(self):

        Buffer = b'\x66\x0F\x3A\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, CONSTANT_TYPE + ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x11)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf3adf')
        assert_equal(myDisasm.infos.repr, 'aeskeygenassist xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x01\xDF\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vaeskeygenassist xmm10, xmmword ptr [r8+11111111h], 11h')

    def test_andn(self):

        Buffer = b'\xc4\x02\x00\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 32)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andn r10d, r15d, dword ptr [r8+11111111h]')

        Buffer = b'\xc4\x82\x00\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 32)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andn edx, r15d, dword ptr [r8+11111111h]')

        Buffer = b'\xc4\x82\x80\xf2\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 64)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andn rdx, r15, qword ptr [r8+11111111h]')

    def test_andps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vandps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vandps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_andnps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x0F\x55\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andnps xmm10, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x0F\x55\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andnps xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x80\x55\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vandnps xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x84\x55\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vandnps ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_andpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\x44\x66\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)

        myDisasm.infos.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'andpd xmm2, m128d [rax-6F6F6F70h]')


        Buffer = b'\x66\x0F\x54\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'andpd xmm2, xmmword ptr [rax-6F6F6F70h]')

        Buffer = b'\xc4\x81\x81\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vandpd xmm2, xmm15, xmmword ptr [r8+11111111h]')

        Buffer = b'\xc4\x81\x85\x54\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vandpd ymm2, ymm15, ymmword ptr [r8+11111111h]')

    def test_blendpd(self):
        # using REX.R to access extended xmm registers
        Buffer = b'\x44\x66\x0F\x3A\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blendpd xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\x44\x66\x0F\x3A\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)

        myDisasm.infos.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'blendpd xmm2, m128 [rax+11111111h], 11h')


        Buffer = b'\x66\x0F\x3A\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blendpd xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x81\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.infos.repr, 'vblendpd xmm10, xmmword ptr [r8+11111111h], 11h')

        Buffer = b'\xc4\x03\x85\x0D\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.infos.repr, 'vblendpd ymm10, ymmword ptr [r8+11111111h], 11h')

    def test_blendps(self):
        # using REX.R to access extended xmm registers
        Buffer = b'44660F3A0C9011111111111111111111'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blendps xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\x44\x66\x0F\x3A\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)

        myDisasm.infos.Options = IntrinsicMemSyntax
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'blendps xmm2, m128 [rax+11111111h], 11h')


        Buffer = b'\x66\x0F\x3A\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG2)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blendps xmm2, xmmword ptr [rax+11111111h], 11h')

        Buffer = b'\xc4\x03\x81\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.infos.repr, 'vblendps xmm10, xmmword ptr [r8+11111111h], 11h')

        Buffer = b'\xc4\x03\x85\x0C\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Instruction.Immediat, 0x11)
        assert_equal(myDisasm.infos.repr, 'vblendps ymm10, ymmword ptr [r8+11111111h], 11h')

    def test_bextr(self):

        Buffer = b'\xc4\x02\x04\xf7\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'bextr r10d, dword ptr [r8+11111111h], r15L')

        Buffer = b'\xc4\x02\x80\xf7\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'bextr r10, qword ptr [r8+11111111h], r15L')

    def test_blendvpd(self):

        Buffer = b'\x44\x66\x0F\x38\x15\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blendvpd xmm2, xmmword ptr [rax+11111111h], xmm0')

        Buffer = b'\xc4\x02\x85\x15\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)

        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand4.OpType, REGISTER_TYPE) #AVX_REG) # REG0)
        assert_equal(myDisasm.infos.Operand4.OpSize, 256)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vblendvpd ymm10, ymm15, ymmword ptr [r8+11111111h], ymm0')


        Buffer = b'\xc4\x02\x81\x15\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)

        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand4.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand4.OpSize, 128)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vblendvpd xmm10, xmm15, xmmword ptr [r8+11111111h], xmm0')

    def test_blendvps(self):

        Buffer = b'44660F38149011111111111111111111'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blendvps xmm2, xmmword ptr [rax+11111111h], xmm0')

        Buffer = b'\xc4\x02\x85\x14\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #AVX_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 256)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)

        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #AVX_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 256)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 256)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand4.OpType, REGISTER_TYPE) #AVX_REG) # REG0)
        assert_equal(myDisasm.infos.Operand4.OpSize, 256)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vblendvps ymm10, ymm15, ymmword ptr [r8+11111111h], ymm0')


        Buffer = b'\xc4\x02\x81\x14\x90\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)

        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand3.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)

        assert_equal(myDisasm.infos.Operand4.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand4.OpSize, 128)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vblendvps xmm10, xmm15, xmmword ptr [r8+11111111h], xmm0')

    def test_blsi(self):

        Buffer = b'\xc4\x02\x00\xf3\x18\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blsi r15d, dword ptr [r8]')

        Buffer = b'\xc4\x02\x80\xf3\x18\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blsi r15, qword ptr [r8]')

    def test_blmsk(self):

        Buffer = b'\xc4\x02\x00\xf3\x10\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blmsk r15d, dword ptr [r8]')

        Buffer = b'\xc4\x02\x80\xf3\x10\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blmsk r15, qword ptr [r8]')

    def test_blsr(self):

        Buffer = b'\xc4\x02\x00\xf3\x08\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blsr r15d, dword ptr [r8]')

        Buffer = b'\xc4\x02\x80\xf3\x08\x11\x11\x11\x11\x00\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'blsr r15, qword ptr [r8]')

    def test_bzhi(self):

        Buffer = b'\xc4\x02\x04\xf5\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'bzhi r10d, dword ptr [r8+11111111h], r15L')

        Buffer = b'\xc4\x02\x80\xf5\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.REX.W_, 1)
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #GENERAL_REG) # REG10)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType, REGISTER_TYPE) #GENERAL_REG) # REG15)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'bzhi r10, qword ptr [r8+11111111h], r15L')

    def test_clac(self):

        Buffer = b'\x0F\x01\xCA\x90\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'clac ')

    def test_cmppd(self):

        Buffer = b'\x66\x0F\xC2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpeqpd xmm0, xmmword ptr [rax], 00h')

        Buffer = b'\x66\x0F\xC2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpltpd xmm0, xmmword ptr [rax], 01h')

        Buffer = b'\x66\x0F\xC2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmplepd xmm0, xmmword ptr [rax], 02h')

        Buffer = b'\x66\x0F\xC2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpunordpd xmm0, xmmword ptr [rax], 03h')

        Buffer = b'\x66\x0F\xC2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpneqpd xmm0, xmmword ptr [rax], 04h')

        Buffer = b'\x66\x0F\xC2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpnltpd xmm0, xmmword ptr [rax], 05h')

        Buffer = b'\x66\x0F\xC2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpnlepd xmm0, xmmword ptr [rax], 06h')

        Buffer = b'\x66\x0F\xC2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpordpd xmm0, xmmword ptr [rax], 07h')

        Buffer = b'\xc4\x01\x81\xc2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpeqpd xmm8, xmm15, xmmword ptr [r8], 00h')

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
            assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
            assert_equal(myDisasm.infos.Operand1.OpSize, 128)
            assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
            assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
            assert_equal(myDisasm.infos.Operand2.OpSize, 128)
            assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
            assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
            assert_equal(myDisasm.infos.Operand3.OpSize, 128)
            assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
            assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
            assert_equal(myDisasm.infos.Operand4.OpSize, 8)
            assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
            assert_equal(myDisasm.infos.repr, 'vcmp{}pd xmm8, xmm15, xmmword ptr [r8], {:02X}h'.format(compare[i], i))


    def test_cmpps(self):

        Buffer = b'\x0F\xC2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpeqps xmm0, xmmword ptr [rax], 00h')

        Buffer = b'\x0F\xC2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpltps xmm0, xmmword ptr [rax], 01h')

        Buffer = b'\x0F\xC2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpleps xmm0, xmmword ptr [rax], 02h')

        Buffer = b'\x0F\xC2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpunordps xmm0, xmmword ptr [rax], 03h')

        Buffer = b'\x0F\xC2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpneqps xmm0, xmmword ptr [rax], 04h')

        Buffer = b'\x0F\xC2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpnltps xmm0, xmmword ptr [rax], 05h')

        Buffer = b'\x0F\xC2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpnleps xmm0, xmmword ptr [rax], 06h')

        Buffer = b'\x0F\xC2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpordps xmm0, xmmword ptr [rax], 07h')


    def test_cmpsd(self):

        Buffer = b'\xF2\x0F\xC2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpeqsd xmm0, qword ptr [rax], 00h')

        Buffer = b'\xF2\x0F\xC2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpltsd xmm0, qword ptr [rax], 01h')

        Buffer = b'\xF2\x0F\xC2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmplesd xmm0, qword ptr [rax], 02h')

        Buffer = b'\xF2\x0F\xC2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpunordsd xmm0, qword ptr [rax], 03h')

        Buffer = b'\xF2\x0F\xC2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpneqsd xmm0, qword ptr [rax], 04h')

        Buffer = b'\xF2\x0F\xC2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpnltsd xmm0, qword ptr [rax], 05h')

        Buffer = b'\xF2\x0F\xC2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpnlesd xmm0, qword ptr [rax], 06h')

        Buffer = b'\xF2\x0F\xC2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand3.OpSize, 8)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'cmpordsd xmm0, qword ptr [rax], 07h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'vcmpeqsd xmm8, xmm15, xmmword ptr [r8], 00h')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)


        Buffer = b'\xc4\x01\x83\xc2\x00\x01\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'vcmpltsd xmm8, xmm15, xmmword ptr [r8], 01h')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)


        Buffer = b'\xc4\x01\x83\xc2\x00\x02\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmplesd xmm8, xmm15, xmmword ptr [r8], 02h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x03\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpunordsd xmm8, xmm15, xmmword ptr [r8], 03h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x04\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpneqsd xmm8, xmm15, xmmword ptr [r8], 04h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x05\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpnltsd xmm8, xmm15, xmmword ptr [r8], 05h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x06\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpnlesd xmm8, xmm15, xmmword ptr [r8], 06h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x07\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpordsd xmm8, xmm15, xmmword ptr [r8], 07h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x08\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpeq_uqsd xmm8, xmm15, xmmword ptr [r8], 08h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x09\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpngesd xmm8, xmm15, xmmword ptr [r8], 09h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0a\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpngtsd xmm8, xmm15, xmmword ptr [r8], 0Ah')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpfalsesd xmm8, xmm15, xmmword ptr [r8], 0Bh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0c\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpneq_oqsd xmm8, xmm15, xmmword ptr [r8], 0Ch')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0d\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpgesd xmm8, xmm15, xmmword ptr [r8], 0Dh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0e\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpgtsd xmm8, xmm15, xmmword ptr [r8], 0Eh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x0f\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmptruesd xmm8, xmm15, xmmword ptr [r8], 0Fh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x10\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpeq_ossd xmm8, xmm15, xmmword ptr [r8], 10h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmplt_oqsd xmm8, xmm15, xmmword ptr [r8], 11h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x12\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmple_oqsd xmm8, xmm15, xmmword ptr [r8], 12h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x13\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpunord_ssd xmm8, xmm15, xmmword ptr [r8], 13h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x14\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpneq_ussd xmm8, xmm15, xmmword ptr [r8], 14h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x15\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpnlt_uqsd xmm8, xmm15, xmmword ptr [r8], 15h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x16\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpnle_uqsd xmm8, xmm15, xmmword ptr [r8], 16h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x17\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpord_ssd xmm8, xmm15, xmmword ptr [r8], 17h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x18\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpeq_ussd xmm8, xmm15, xmmword ptr [r8], 18h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x19\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpnge_uqsd xmm8, xmm15, xmmword ptr [r8], 19h')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1a\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpngt_uqsd xmm8, xmm15, xmmword ptr [r8], 1Ah')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1b\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpfalse_ossd xmm8, xmm15, xmmword ptr [r8], 1Bh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1c\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpneq_ossd xmm8, xmm15, xmmword ptr [r8], 1Ch')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1d\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpge_oqsd xmm8, xmm15, xmmword ptr [r8], 1Dh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1e\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmpgt_oqsd xmm8, xmm15, xmmword ptr [r8], 1Eh')

        Buffer = b'\xc4\x01\x83\xc2\x00\x1f\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #SSE_REG) # REG8)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #SSE_REG) # REG15)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand3.OpType,  + MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand3.OpSize, 128)
        assert_equal(myDisasm.infos.Operand3.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand4.OpType,  + CONSTANT_TYPE+ABSOLUTE_)
        assert_equal(myDisasm.infos.Operand4.OpSize, 8)
        assert_equal(myDisasm.infos.Operand4.AccessMode, READ)
        assert_equal(myDisasm.infos.repr, 'vcmptrue_ussd xmm8, xmm15, xmmword ptr [r8], 1Fh')


    def test_mpx(self):

        Buffer = b'\xf3\x41\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndcl bnd1, dword ptr [r11]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf3\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndcl bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf2\x41\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndcu bnd1, dword ptr [r11]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf2\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndcu bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf2\x41\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndcn bnd1, dword ptr [r11]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf2\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndcn bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf3\x41\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndmk bnd1, dword ptr [r11]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\xf3\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndmk bnd1, dword ptr [rbx]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, READ)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)



        Buffer = b'\x66\x0f\x1a\xc0\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 0
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndmov bnd0, bnd0')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) # + REG0)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #MPX_REG) # + REG0)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)


        Buffer = b'\x66\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndmov bnd1, dqword ptr [rbx]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\x66\x0f\x1a\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndmov bnd1, qword ptr [ebx]')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand1.OpSize, 128)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand2.OpSize, 64)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\x66\x0f\x1b\x0b\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndmov qword ptr [ebx], bnd1')
        assert_equal(myDisasm.infos.Operand1.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand1.OpSize, 64)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\x0f\x1b\x0c\x10\x11\x11\x11\x11\x11\x11\x11\x11\x11'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'bndstx dword ptr [rax+rdx], bnd1')
        assert_equal(myDisasm.infos.Operand1.OpType, MEMORY_TYPE)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE) #MPX_REG) #REG1)
        assert_equal(myDisasm.infos.Operand2.OpSize, 128)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = b'\x66\xf3\xa5'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'rep movsw ')

        Buffer = b'\xf3\x66\xa5'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'rep movsw ')

        Buffer = '67654c6973743a'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'imul r14, qword ptr [ebx+74h], 0000003Ah')

        Buffer = '660f73fa02'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'pslldq xmm2, 02h')

        Buffer = '660f73fa02'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 16
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, '??? ')

        Buffer = '820000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'add byte ptr [eax], 00h')

        Buffer = '821000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'adc byte ptr [eax], 00h')

        Buffer = '823000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'xor byte ptr [eax], 00h')

        Buffer = '6ab7'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'push FFFFFFB7h')

        Buffer = '\xf0\x22\xbd\x71\x20\x17\x00'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'lock and bh, byte ptr [rbp+00172071h]')

        Buffer = '\xd3\xb6\x6b\x8f\xac\xa0'
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'sal dword ptr [rsi-5F537095h], cl')

        Buffer = '66F3A7'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'rep cmpsw ')

    def test_lock(self):
        '''Minimal regression tests for https://github.com/BeaEngine/beaengine/issues/9'''

        Buffer = 'f04889ce'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Prefix.LockPrefix, InvalidPrefix)
        assert_equal(myDisasm.infos.repr, 'lock mov rsi, rcx')


        Buffer = '4889ce'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'mov rsi, rcx')

        Buffer = '48'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'dec eax')

        Buffer = 'f048'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'lock dec eax')
        assert_equal(myDisasm.infos.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f0feC9'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'lock dec cl')
        assert_equal(myDisasm.infos.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f0fe8811223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'lock dec byte ptr [rax+44332211h]')
        assert_equal(myDisasm.infos.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, 0)

        Buffer = 'f0ffC9'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'lock dec ecx')
        assert_equal(myDisasm.infos.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f0ff8811223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'lock dec dword ptr [rax+44332211h]')
        assert_equal(myDisasm.infos.Prefix.LockPrefix, 1)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, 0)
