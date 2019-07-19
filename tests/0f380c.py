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
    """

    - pmulhrsw Pq, Qq
    - vpermilps Vx, Hx, Wx
    """
    def test(self):
        # VEX.NDS.128.66.0F38.W0 0C /r
        # VPERMILPS xmm1, xmm2, xmm3/m128

        Buffer = 'c402010c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermilps ')
        assert_equal(myDisasm.instr.repr, 'vpermilps xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.W0 0C /r
        # VPERMILPS ymm1, ymm2, ymm3/m256

        Buffer = 'c402050c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermilps ')
        assert_equal(myDisasm.instr.repr, 'vpermilps ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.W0 0C /r
        # VPERMILPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        Buffer = '620205060c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xc)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermilps ')
        assert_equal(myDisasm.instr.repr, 'vpermilps xmm1, xmm15, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W0 0C /r
        # VPERMILPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        Buffer = '620205200c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xc)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermilps ')
        assert_equal(myDisasm.instr.repr, 'vpermilps ymm1, ymm15, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W0 0C /r
        # VPERMILPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        Buffer = '620205400c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xc)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpermilps ')
        assert_equal(myDisasm.instr.repr, 'vpermilps zmm1, zmm15, zmmword ptr [rsi]')

        # No VEX.66 prefix

        Buffer = 'c402000c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, '??? ')

        # No VEX Prefix

        Buffer = '0f380c9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, '??? ')

        # If VEX.W = 1 #UD

        Buffer = 'c402810c0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.REX.W_, 1)
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
