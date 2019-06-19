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
    Packed Shuffle Bytes
    - pshufb Pq, Qq
    - vpshufb Vx, Hx, Wx
    """
    def test(self):
        # NP 0F 38 00 /r 1
        # PSHUFB mm1, mm2/m64
        Buffer = '0f38009011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3800')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufb ')
        assert_equal(myDisasm.instr.repr, 'pshufb mm2, qword ptr [rax+44332211h]')

        # 66 0F 38 00 /r
        # PSHUFB xmm1, xmm2/m128
        Buffer = '660f38009011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3800')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufb ')
        assert_equal(myDisasm.instr.repr, 'pshufb xmm2, dqword ptr [rax+44332211h]')

        # NP 0F 38 00 /r 1
        # PSHUFB mm1, mm2/m64
        Buffer = 'f20f38009011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3800')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufb ')
        assert_equal(myDisasm.instr.repr, 'pshufb mm2, qword ptr [rax+44332211h]')

        # NP 0F 38 00 /r 1
        # PSHUFB mm1, mm2/m64
        Buffer = 'f30f38009011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf3800')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufb ')
        assert_equal(myDisasm.instr.repr, 'pshufb mm2, qword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 00 /r
        # VPSHUFB xmm1, xmm2, xmm3/m128
        Buffer = 'c4020100443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufb ')
        assert_equal(myDisasm.instr.repr, 'vpshufb xmm8, xmm15, xmmword ptr [r11+r14+22h]')

        # VEX.NDS.256.66.0F38.WIG 00 /r
        # VPSHUFB ymm1, ymm2, ymm3/m256
        Buffer = 'c4020500443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufb ')
        assert_equal(myDisasm.instr.repr, 'vpshufb ymm8, ymm15, ymmword ptr [r11+r14+22h]')

        # EVEX.NDS.128.66.0F38.WIG 00 /r
        # VPSHUFB xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '6202050600443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufb ')
        assert_equal(myDisasm.instr.repr, 'vpshufb xmm0, xmm15, xmmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.256.66.0F38.WIG 00 /r
        # VPSHUFB ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '6202052000443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufb ')
        assert_equal(myDisasm.instr.repr, 'vpshufb ymm0, ymm15, ymmword ptr [rbx+rsi+22h]')

        # EVEX.NDS.512.66.0F38.WIG 00 /r
        # VPSHUFB zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '6202054000443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.instr.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.instr.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.instr.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x0')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufb ')
        assert_equal(myDisasm.instr.repr, 'vpshufb zmm0, zmm15, zmmword ptr [rbx+rsi+22h]')
