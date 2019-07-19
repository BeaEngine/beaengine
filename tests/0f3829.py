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
        # 66 0F 38 29 /r
        # pcmpeqq mm1, mm2/m64
        Buffer = '660f38299011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3829')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pcmpeqq ')
        assert_equal(myDisasm.instr.repr, 'pcmpeqq xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 29 /r
        # vpcmpeqq xmm1, xmm2, xmm3/m128
        Buffer = 'c40201290e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqq ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqq xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.WIG 29 /r
        # vpcmpeqq ymm1, ymm2, ymm3/m256
        Buffer = 'c40205290e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqq ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqq ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.WIG 29 /r
        # vpcmpeqq xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62020506290e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x29')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqq ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqq xmm1, xmm15, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.WIG 29 /r
        # vpcmpeqq ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62020520290e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x29')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqq ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqq ymm1, ymm15, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.WIG 29 /r
        # vpcmpeqq zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62020540290e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x29')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqq ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqq zmm1, zmm15, zmmword ptr [rsi]')
