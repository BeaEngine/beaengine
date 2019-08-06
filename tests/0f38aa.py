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

        # VEX.NDS.128.66.0F38.W0 aa /r
        # vfmsub213ps xmm1, xmm2, xmm3/m128
        Buffer = 'c40201aa0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vfmsub213ps ')
        assert_equal(myDisasm.infos.repr, 'vfmsub213ps xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.W0 aa /r
        # vfmsub213ps ymm1, ymm2, ymm3/m256
        Buffer = 'c40205aa0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vfmsub213ps ')
        assert_equal(myDisasm.infos.repr, 'vfmsub213ps ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.W0 aa /r
        # vfmsub213ps xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62020506aa0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xaa')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vfmsub213ps ')
        assert_equal(myDisasm.infos.repr, 'vfmsub213ps xmm25, xmm31, xmmword ptr [r14]')

        # EVEX.NDS.256.66.0F38.W0 aa /r
        # vfmsub213ps ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62020520aa0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xaa')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vfmsub213ps ')
        assert_equal(myDisasm.infos.repr, 'vfmsub213ps ymm25, ymm31, ymmword ptr [r14]')

        # EVEX.NDS.512.66.0F38.W0 aa /r
        # vfmsub213ps zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62020540aa0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xaa')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vfmsub213ps ')
        assert_equal(myDisasm.infos.repr, 'vfmsub213ps zmm25, zmm31, zmmword ptr [r14]')


        # VEX.NDS.128.66.0F38.W1 aa /r
        # vfmsub213pd xmm1, xmm2, xmm3/m128

        myVEX = VEX()
        myVEX.L = 0
        myVEX.W = 1
        myVEX.pp = 0b1
        myVEX.mmmm = 0b10
        myVEX.vvvv = 0b0

        Buffer = 'c4{:02x}{:02x}aa0e'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vfmsub213pd ')
        assert_equal(myDisasm.infos.repr, 'vfmsub213pd xmm9, xmm15, xmmword ptr [r14]')

        # EVEX.512.F2.0F38.W0 AA /r
        # V4FNMADDPS zmm1{k1}{z}, zmm2+3, m128

        myEVEX = EVEX('EVEX.512.F2.0F38.W0')
        myEVEX.vvvv = 0b1011
        Buffer = '{}aa0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xaa)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'v4fnmaddps ')
        assert_equal(myDisasm.infos.Operand2.Registers.zmm, REG20+REG21+REG22+REG23)
        assert_equal(myDisasm.infos.repr, 'v4fnmaddps zmm25, zmm20...zmm23, xmmword ptr [r14]')
