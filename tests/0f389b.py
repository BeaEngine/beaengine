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

        # VEX.NDS.128.66.0F38.W0 9b /r
        # vfmsub132ss xmm1, xmm2, xmm3/m128
        Buffer = 'c402019b0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmsub132ss ')
        assert_equal(myDisasm.instr.repr, 'vfmsub132ss xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.W0 9b /r
        # vfmsub132ss ymm1, ymm2, ymm3/m256
        Buffer = 'c402059b0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmsub132ss ')
        assert_equal(myDisasm.instr.repr, 'vfmsub132ss ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.W0 9b /r
        # vfmsub132ss xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '620205069b0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x9b')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmsub132ss ')
        assert_equal(myDisasm.instr.repr, 'vfmsub132ss xmm1, xmm15, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W0 9b /r
        # vfmsub132ss ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '620205209b0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x9b')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmsub132ss ')
        assert_equal(myDisasm.instr.repr, 'vfmsub132ss ymm1, ymm15, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W0 9b /r
        # vfmsub132ss zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '620205409b0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x9b')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmsub132ss ')
        assert_equal(myDisasm.instr.repr, 'vfmsub132ss zmm1, zmm15, zmmword ptr [rsi]')


        # VEX.NDS.128.66.0F38.W1 9b /r
        # vfmsub132sd xmm1, xmm2, xmm3/m128

        myVEX = VEX()
        myVEX.L = 0
        myVEX.W = 1
        myVEX.pp = 0b1
        myVEX.mmmm = 0b10
        myVEX.vvvv = 0b0

        Buffer = 'c4{:02x}{:02x}9b0e'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vfmsub132sd ')
        assert_equal(myDisasm.instr.repr, 'vfmsub132sd xmm9, xmm15, xmmword ptr [r14]')

        # EVEX.512.F2.0F38.W0 9B /r
        # V4FMADDSS zmm1{k1}{z}, zmm2+3, m128

        myEVEX = EVEX('EVEX.512.F2.0F38.W0')
        myEVEX.vvvv = 0b1011
        Buffer = '{}9b0e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x9b)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'v4fmaddss ')
        assert_equal(myDisasm.instr.Argument2.Registers.zmm, REG4+REG5+REG6+REG7)
        assert_equal(myDisasm.instr.repr, 'v4fmaddss zmm1, zmm4...zmm7, xmmword ptr [rsi]')
