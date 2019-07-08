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



        # NP 0F D7 /r1
        # PMOVMSKB reg, mm

        Buffer = '0fd7c0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfd7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmovmskb ')
        assert_equal(myDisasm.instr.repr, 'pmovmskb rax, mm0')

        # 66 0F D7 /r
        # PMOVMSKB reg, xmm

        Buffer = '660fd7c0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfd7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmovmskb ')
        assert_equal(myDisasm.instr.repr, 'pmovmskb rax, xmm0')

        # VEX.128.66.0F.WIG D7 /r
        # VPMOVMSKB reg, xmm1

        myVEX = VEX('VEX.128.66.0F.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}d7c0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xd7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovmskb ')
        assert_equal(myDisasm.instr.repr, 'vpmovmskb r8, xmm8')

        # VEX.256.66.0F.WIG D7 /r
        # VPMOVMSKB reg, ymm1

        myVEX = VEX('VEX.256.66.0F.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}d7c0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xd7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovmskb ')
        assert_equal(myDisasm.instr.repr, 'vpmovmskb r8, ymm8')


        myVEX = VEX('VEX.256.66.0F.WIG')
        myVEX.vvvv = 0b1110
        Buffer = '{}d7c0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xd7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovmskb ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
