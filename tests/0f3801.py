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
    Packed Horizontal Add
    - phaddw Pq, Qq
    - vphaddw Vx, Hx, Wx
    """
    def test(self):
        # NP 0F 38 01 /r1
        # PHADDW mm1, mm2/m64

        Buffer = '0f38019011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3801')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'phaddw ')
        assert_equal(myDisasm.instr.repr, 'phaddw mm2, qword ptr [rax+44332211h]')

        # 66 0F 38 01 /r
        # PHADDW xmm1, xmm2/m128

        Buffer = '660f38019011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3801')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'phaddw ')
        assert_equal(myDisasm.instr.repr, 'phaddw xmm2, dqword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 01 /r
        # VPHADDW xmm1, xmm2, xmm3/m128

        Buffer = 'c4020101443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vphaddw ')
        assert_equal(myDisasm.instr.repr, 'vphaddw xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F38.WIG 01 /r
        # VPHADDW ymm1, ymm2, ymm3/m256

        Buffer = 'c4020501443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vphaddw ')
        assert_equal(myDisasm.instr.repr, 'vphaddw ymm8, ymm15, ymmword ptr [r11+r14+22h]')
