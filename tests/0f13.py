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

        # 0F 13/r
        # MOVLPS m64, xmm1

        Buffer = '0f1390'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf13')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movlps ')
        assert_equal(myDisasm.infos.repr, 'movlps qword ptr [rax+00000000h], xmm2')

        # VEX.128.0F.WIG 13/r
        # VMOVLPS m64, xmm1

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}1390'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x13')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovlps ')
        assert_equal(myDisasm.infos.repr, 'vmovlps qword ptr [r8+00000000h], xmm10')

        # EVEX.128.0F.W0 13/r
        # VMOVLPS m64, xmm1

        myEVEX = EVEX('EVEX.128.0F.W0')
        Buffer = '{}1390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovlps ')
        assert_equal(myDisasm.infos.repr, 'vmovlps qword ptr [r8+00000000h], xmm26')

        # 66 0F 13/r
        # MOVLPD m64, xmm1

        Buffer = '660f1390'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf13')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movlpd ')
        assert_equal(myDisasm.infos.repr, 'movlpd qword ptr [rax+00000000h], xmm2')

        # VEX.128.66.0F.WIG 13/r
        # VMOVLPD m64, xmm1

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}1390'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x13')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovlpd ')
        assert_equal(myDisasm.infos.repr, 'vmovlpd qword ptr [r8+00000000h], xmm10')

        # EVEX.128.66.0F.W1 13/r
        # VMOVLPD m64, xmm1

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}1390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovlpd ')
        assert_equal(myDisasm.infos.repr, 'vmovlpd qword ptr [r8+00000000h], xmm26')
