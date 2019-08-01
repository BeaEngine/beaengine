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


        # F2 0F F0 /r
        # LDDQU xmm1, mem

        Buffer = 'f20ff010'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xff0)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lddqu ')
        assert_equal(myDisasm.infos.repr, 'lddqu xmm2, xmmword ptr [rax]')

        # VEX.128.F2.0F.WIG F0 /r
        # VLDDQU xmm1, m128

        myVEX = VEX('VEX.128.F2.0F.WIG')
        Buffer = '{}f020'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf0)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vlddqu ')
        assert_equal(myDisasm.infos.repr, 'vlddqu xmm12, xmmword ptr [r8]')

        # VEX.256.F2.0F.WIG F0 /r
        # VLDDQU ymm1, m256

        myVEX = VEX('VEX.256.F2.0F.WIG')
        Buffer = '{}f020'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf0)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vlddqu ')
        assert_equal(myDisasm.infos.repr, 'vlddqu ymm12, ymmword ptr [r8]')
