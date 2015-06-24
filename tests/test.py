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

        Buffer = b'\x66\x0f\x38\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
        Instruction = DISASM()
        Target = create_string_buffer(Buffer,len(Buffer))
        Instruction.EIP = addressof(Target)
        InstrLength = Disasm(addressof(Instruction))
        assert_equal(Instruction.CompleteInstr, 'adcx dx, word ptr [eax-6F6F6F70h]')

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
        assert_equal(myDisasm.CompleteInstr, 'imul eax, dword ptr [rdx], 9090F683h')


    def test_VEX3Bytes(self):
        Buffer = b'\xc4\x02\x83\xf6\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90'
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
        assert_equal(myDisasm.CompleteInstr, 'mulx r10, rdi, qword ptr [r8-6F6F6F70h]')


