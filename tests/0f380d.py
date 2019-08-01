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
    - vpermilpd Vx, Hx, Wx
    """
    def test(self):
        # VEX.NDS.128.66.0F38.W0 0d /r
        # VPERmilpd xmm1, xmm2, xmm3/m128

        Buffer = 'c402010d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermilpd ')
        assert_equal(myDisasm.infos.repr, 'vpermilpd xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.W0 0d /r
        # VPERmilpd ymm1, ymm2, ymm3/m256

        Buffer = 'c402050d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermilpd ')
        assert_equal(myDisasm.infos.repr, 'vpermilpd ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.W0 0d /r
        # VPERmilpd xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        Buffer = '620205060d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xd)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermilpd ')
        assert_equal(myDisasm.infos.repr, 'vpermilpd xmm1, xmm15, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W0 0d /r
        # VPERmilpd ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        Buffer = '620205200d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xd)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermilpd ')
        assert_equal(myDisasm.infos.repr, 'vpermilpd ymm1, ymm15, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W0 0d /r
        # VPERmilpd zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        Buffer = '620205400d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xd)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpermilpd ')
        assert_equal(myDisasm.infos.repr, 'vpermilpd zmm1, zmm15, zmmword ptr [rsi]')

        # No VEX.66 prefix

        Buffer = 'c402000d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, '??? ')

        # No VEX Prefix

        Buffer = '0f380d9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, '??? ')

        # If VEX.W = 1 #UD

        Buffer = 'c402810d0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.REX.W_, 1)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
