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

        # EVEX.128.66.0F38.W0 52 /r
        # vpdpwssd xmm1{k1}{z}, xmm2,  xmm3/m128/m32bcst

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}520e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpdpwssd ')
        assert_equal(myDisasm.infos.repr, 'vpdpwssd xmm1, xmm0, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W0 52 /r
        # vpdpwssd ymm1{k1}{z}, ymm2,  ymm3/m256/m32bcst

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}520e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpdpwssd ')
        assert_equal(myDisasm.infos.repr, 'vpdpwssd ymm1, ymm0, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W0 52 /r
        # vpdpwssd zmm1{k1}{z}, zmm2,  zmm3/m512/m32bcst

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}520e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpdpwssd ')
        assert_equal(myDisasm.infos.repr, 'vpdpwssd zmm1, zmm0, zmmword ptr [rsi]')

        # EVEX.512.F2.0F38.W0 52 /r
        # VP4DPWSSD zmm1{k1}{z}, zmm2+3, m128

        myEVEX = EVEX('EVEX.512.F2.0F38.W0')
        myEVEX.vvvv = 0b1011
        Buffer = '{}520e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vp4dpwssd ')
        assert_equal(myDisasm.infos.Operand2.Registers.zmm, REG4+REG5+REG6+REG7)
        assert_equal(myDisasm.infos.repr, 'vp4dpwssd zmm1, zmm4...zmm7, xmmword ptr [rsi]')
