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


        # EVEX.128.66.0F38.W0 8D /r
        # VPERMB xmm1 {k1}{z}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}8d0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8d)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermb ')
        assert_equal(myDisasm.infos.repr, 'vpermb xmm1, xmm0, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W0 8D /r
        # VPERMB ymm1 {k1}{z}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}8d0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8d)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermb ')
        assert_equal(myDisasm.infos.repr, 'vpermb ymm1, ymm0, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W0 8D /r
        # VPERMB zmm1 {k1}{z}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}8d0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8d)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermb ')
        assert_equal(myDisasm.infos.repr, 'vpermb zmm1, zmm0, zmmword ptr [rsi]')

        # EVEX.128.66.0F38.W1 8D /r
        # VPERMW xmm1 {k1}{z}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        Buffer = '{}8d0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8d)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermw ')
        assert_equal(myDisasm.infos.repr, 'vpermw xmm1, xmm0, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W1 8D /r
        # VPERMW ymm1 {k1}{z}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}8d0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8d)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermw ')
        assert_equal(myDisasm.infos.repr, 'vpermw ymm1, ymm0, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W1 8D /r
        # VPERMW zmm1 {k1}{z}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}8d0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8d)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermw ')
        assert_equal(myDisasm.infos.repr, 'vpermw zmm1, zmm0, zmmword ptr [rsi]')
