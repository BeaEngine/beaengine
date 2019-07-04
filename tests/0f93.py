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


        # VEX.L0.0F.W0 93 /r
        # KMOVW r32 ,k1

        myVEX = VEX('VEX.L0.0F.W0')
        myVEX.R = 1
        Buffer = '{}93db'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x93)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovw ')
        assert_equal(myDisasm.instr.repr, 'kmovw r11d, k3')

        # VEX.L0.66.0F.W0 93 /r
        # KMOVB r32, k1

        myVEX = VEX('VEX.L0.66.0F.W0')
        myVEX.R = 1
        Buffer = '{}93db'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x93)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovb ')
        assert_equal(myDisasm.instr.repr, 'kmovb r11d, k3')

        # VEX.L0.F2.0F.W0 93 /r
        # KMOVD r32, k1

        myVEX = VEX('VEX.L0.F2.0F.W0')
        myVEX.R = 1
        Buffer = '{}93db'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x93)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovd ')
        assert_equal(myDisasm.instr.Reserved_.REX.W_, 0)
        assert_equal(myDisasm.instr.Reserved_.VEX.pp, 3)
        assert_equal(myDisasm.instr.repr, 'kmovd r11d, k3')

        # VEX.L0.F2.0F.W1 93 /r
        # KMOVQ r64, k1

        myVEX = VEX('VEX.L0.F2.0F.W1')
        myVEX.R = 1
        Buffer = '{}93db'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x93)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kmovq ')
        assert_equal(myDisasm.instr.repr, 'kmovq r11, k3')

        # 0F 93
        # REX + 0F 93
        # SETB r/m8

        Buffer = '0f9300'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f93)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'setnb ')
        assert_equal(myDisasm.instr.repr, 'setnb byte ptr [rax]')
