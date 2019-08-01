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


        # EVEX.128.66.0F3A.W1 70 /r /ib
        # VPSHLDW xmm1{k1}{z}, xmm2, xmm3/m128, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W1')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshldw ')
        assert_equal(myDisasm.instr.repr, 'vpshldw xmm4, xmm0, xmmword ptr [rax], 11h')

        # EVEX.256.66.0F3A.W1 70 /r /ib
        # VPSHLDW ymm1{k1}{z}, ymm2, ymm3/m256, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W1')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshldw ')
        assert_equal(myDisasm.instr.repr, 'vpshldw ymm4, ymm0, ymmword ptr [rax], 11h')

        # EVEX.512.66.0F3A.W1 70 /r /ib
        # VPSHLDW zmm1{k1}{z}, zmm2, zmm3/m512, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshldw ')
        assert_equal(myDisasm.instr.repr, 'vpshldw zmm4, zmm0, zmmword ptr [rax], 11h')
