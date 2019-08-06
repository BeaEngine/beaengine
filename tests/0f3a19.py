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

        # VEX.256.66.0F3A.W0 19 /r ib
        # vextractF128 ymm1, ymm2, xmm3/m128, imm8

        myVEX = VEX('VEX.256.66.0F3A.W0')
        Buffer = '{}191033'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractf128 ')
        assert_equal(myDisasm.infos.repr, 'vextractf128 ymm10, ymm0, xmmword ptr [r8], 33h')

        # EVEX.256.66.0F3A.W0 19 /r ib
        # vextractF32X4 ymm1 {k1}{z}, ymm2, xmm3/m128, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W0')
        Buffer = '{}192011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractf32x4 ')
        assert_equal(myDisasm.infos.repr, 'vextractf32x4 ymm28, ymm16, xmmword ptr [r8], 11h')

        # EVEX.512.66.0F3A.W0 19 /r ib
        # vextractF32X4 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}192011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractf32x4 ')
        assert_equal(myDisasm.infos.repr, 'vextractf32x4 zmm28, zmm16, xmmword ptr [r8], 11h')

        # EVEX.256.66.0F3A.W1 19 /r ib
        # vextractF64X2 ymm1 {k1}{z}, ymm2, xmm3/m128, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W1')
        Buffer = '{}192011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractf64x2 ')
        assert_equal(myDisasm.infos.repr, 'vextractf64x2 ymm28, ymm16, xmmword ptr [r8], 11h')

        # EVEX.512.66.0F3A.W1 19 /r ib
        # vextractF64X2 zmm1 {k1}{z}, zmm2, xmm3/m128, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}192011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x19)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractf64x2 ')
        assert_equal(myDisasm.infos.repr, 'vextractf64x2 zmm28, zmm16, xmmword ptr [r8], 11h')
