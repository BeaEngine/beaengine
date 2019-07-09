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



        # NP 0F F7 /r
        # MASKMOVQ mm1, mm2

        Buffer = '0ff7c0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xff7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'maskmovq ')
        assert_equal(myDisasm.instr.repr, 'maskmovq mm0, mm0')

        # 66 0F F7 /r
        # MASKMOVDQU xmm1, xmm2

        Buffer = '660ff7c0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xff7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'maskmovdqu ')
        assert_equal(myDisasm.instr.repr, 'maskmovdqu xmm0, xmm0')

        # VEX.128.66.0F.WIG F7 /r
        # VMASKMOVDQU xmm1, xmm2

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}f7e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmaskmovdqu ')
        assert_equal(myDisasm.instr.repr, 'vmaskmovdqu xmm12, xmm8')
