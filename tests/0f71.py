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

        # NP 0F 71 /6 ib
        # PSLLW mm1, imm8

        Buffer = '0f71f011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psllw ')
        assert_equal(myDisasm.instr.repr, 'psllw mm0, 11h')

        # 66 0F 71 /6 ib
        # PSLLW xmm1, imm8

        Buffer = '660f71f011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psllw ')
        assert_equal(myDisasm.instr.repr, 'psllw xmm0, 11h')

        # VEX.NDD.128.66.0F.WIG 71 /6 ib
        # VPSLLW xmm1, xmm2, imm8

        myVEX = VEX('VEX.NDD.128.66.0F.WIG')
        myVEX.B = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}71f011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsllw ')
        assert_equal(myDisasm.instr.repr, 'vpsllw xmm0, xmm0, 11h')

        # VEX.NDD.256.66.0F.WIG 71 /6 ib
        # VPSLLW ymm1, ymm2, imm8

        myVEX = VEX('VEX.NDD.256.66.0F.WIG')
        Buffer = '{}71f011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsllw ')
        assert_equal(myDisasm.instr.repr, 'vpsllw ymm15, ymm8, 11h')

        # EVEX.NDD.128.66.0F.WIG 71 /6 ib
        # VPSLLW xmm1 {k1}{z}, xmm2/m128, imm8

        myEVEX = EVEX('EVEX.NDD.128.66.0F.WIG')
        Buffer = '{}713211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsllw ')
        assert_equal(myDisasm.instr.repr, 'vpsllw xmm15, xmmword ptr [rdx], 11h')

        # EVEX.NDD.256.66.0F.WIG 71 /6 ib
        # VPSLLW ymm1 {k1}{z}, ymm2/m256, imm8

        myEVEX = EVEX('EVEX.NDD.256.66.0F.WIG')
        Buffer = '{}713211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsllw ')
        assert_equal(myDisasm.instr.repr, 'vpsllw ymm15, ymmword ptr [rdx], 11h')

        # EVEX.NDD.512.66.0F.WIG 71 /6 ib
        # VPSLLW zmm1 {k1}{z}, zmm2/m512, imm8

        myEVEX = EVEX('EVEX.NDD.512.66.0F.WIG')
        Buffer = '{}713211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x71)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpsllw ')
        assert_equal(myDisasm.instr.repr, 'vpsllw zmm15, zmmword ptr [rdx], 11h')
