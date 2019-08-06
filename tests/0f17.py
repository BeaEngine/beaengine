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

        # 0F 17/r
        # MOvhpS m64, xmm1

        Buffer = '0f1790'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf17')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movhps ')
        assert_equal(myDisasm.infos.repr, 'movhps qword ptr [rax+00000000h], xmm2')

        # VEX.128.0F.WIG 17/r
        # VMOvhpS m64, xmm1

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}1790'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x17')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovhps ')
        assert_equal(myDisasm.infos.repr, 'vmovhps qword ptr [r8+00000000h], xmm10')

        # EVEX.128.0F.W0 17/r
        # VMOvhpS m64, xmm1

        myEVEX = EVEX('EVEX.128.0F.W0')
        Buffer = '{}1790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x17)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovhps ')
        assert_equal(myDisasm.infos.repr, 'vmovhps qword ptr [r8+00000000h], xmm26')

        # 66 0F 17/r
        # MOvhpD m64, xmm1

        Buffer = '660f1790'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf17')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movhpd ')
        assert_equal(myDisasm.infos.repr, 'movhpd qword ptr [rax+00000000h], xmm2')

        # VEX.128.66.0F.WIG 17/r
        # VMOvhpD m64, xmm1

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}1790'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x17')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovhpd ')
        assert_equal(myDisasm.infos.repr, 'vmovhpd qword ptr [r8+00000000h], xmm10')

        # EVEX.128.66.0F.W1 17/r
        # VMOvhpD m64, xmm1

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}1790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x17)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovhpd ')
        assert_equal(myDisasm.infos.repr, 'vmovhpd qword ptr [r8+00000000h], xmm26')
