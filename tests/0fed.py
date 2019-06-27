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
        # 66 0F ed /r
        # paddsw mm1, mm2/m64
        Buffer = '660fed9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfed')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'paddsw ')
        assert_equal(myDisasm.instr.repr, 'paddsw xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F.WIG ed /r
        # vpaddsw xmm1, xmm2, xmm3/m128
        Buffer = 'c40101ed443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpaddsw ')
        assert_equal(myDisasm.instr.repr, 'vpaddsw xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F.WIG ed /r
        # vpaddsw ymm1, ymm2, ymm3/m256
        Buffer = 'c40105ed443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpaddsw ')
        assert_equal(myDisasm.instr.repr, 'vpaddsw ymm8, ymm15, ymmword ptr [r11+r14+22h]')

        # EVEX.NDS.128.66.0F.WIG ed /r
        # vpaddsw xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62010506ed443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xed')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpaddsw ')
        assert_equal(myDisasm.instr.repr, 'vpaddsw xmm0, xmm15, xmmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.256.66.0F.WIG ed /r
        # vpaddsw ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62010520ed443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xed')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpaddsw ')
        assert_equal(myDisasm.instr.repr, 'vpaddsw ymm0, ymm15, ymmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.512.66.0F.WIG ed /r
        # vpaddsw zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62010540ed443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x1)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xed')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpaddsw ')
        assert_equal(myDisasm.instr.repr, 'vpaddsw zmm0, zmm15, zmmword ptr [rbx+rsi+22h]')
