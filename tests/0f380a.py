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
    Packed Sign
    - psignd Pq, Qq
    - vpsignd Vx, Hx, Wx
    """
    def test(self):
        # NP 0F 38 0a /r1
        # psignd mm1, mm2/m64

        Buffer = '0f380a9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf380a')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psignd ')
        assert_equal(myDisasm.instr.repr, 'psignd mm2, qword ptr [rax+44332211h]')

        # 66 0F 38 0a /r
        # psignd xmm1, xmm2/m128

        Buffer = '660f380a9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf380a')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psignd ')
        assert_equal(myDisasm.instr.repr, 'psignd xmm2, dqword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 0a /r
        # vpsignd xmm1, xmm2, xmm3/m128

        Buffer = 'c402010a443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsignd ')
        assert_equal(myDisasm.instr.repr, 'vpsignd xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F38.WIG 0a /r
        # vpsignd ymm1, ymm2, ymm3/m256

        Buffer = 'c402050a443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsignd ')
        assert_equal(myDisasm.instr.repr, 'vpsignd ymm8, ymm15, ymmword ptr [r11+r14+22h]')

        # EVEX.NDS.128.66.0F38.WIG 0a /r
        # vpsignd xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '6202050a07443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, '??? ')
