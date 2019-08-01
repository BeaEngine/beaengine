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
        # 66 0F df /r
        # pandn mm1, mm2/m64
        Buffer = '660fdf9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xfdf')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pandn ')
        assert_equal(myDisasm.infos.repr, 'pandn xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F.WIG df /r
        # vpandn xmm1, xmm2, xmm3/m128
        Buffer = 'c40101df0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpandn ')
        assert_equal(myDisasm.infos.repr, 'vpandn xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F.WIG df /r
        # vpandn ymm1, ymm2, ymm3/m256
        Buffer = 'c40105df0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpandn ')
        assert_equal(myDisasm.infos.repr, 'vpandn ymm9, ymm15, ymmword ptr [r14]')


        # EVEX.NDS.128.66.0F.W0 DF /r
        # VPANDND xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        Buffer = '62010506df0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xdf')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpandnd ')
        assert_equal(myDisasm.infos.repr, 'vpandnd xmm1, xmm15, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F.W0 DF /r
        # VPANDND ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        Buffer = '62010520df0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xdf')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpandnd ')
        assert_equal(myDisasm.infos.repr, 'vpandnd ymm1, ymm15, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F.W0 DF /r
        # VPANDND zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        Buffer = '62010540df0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xdf')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpandnd ')
        assert_equal(myDisasm.infos.repr, 'vpandnd zmm1, zmm15, zmmword ptr [rsi]')

        # EVEX.NDS.128.66.0F.W1 DF /r
        # VPANDNQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst

        # EVEX.NDS.256.66.0F.W1 DF /r
        # VPANDNQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst

        # EVEX.NDS.512.66.0F.W1 DF /r
        # VPANDNQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst
