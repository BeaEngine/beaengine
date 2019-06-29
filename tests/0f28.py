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

        # NP 0F 28 /r
        # MOVAPS xmm1, xmm2/m128

        Buffer = '0f28e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movaps ')
        assert_equal(myDisasm.instr.repr, 'movaps xmm4, xmm0')

        # VEX.128.0F.WIG 28 /r
        # VMOVAPS xmm1, xmm2/m128

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}28e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps xmm12, xmm8')

        # VEX.256.0F.WIG 28 /r
        # VMOVAPS ymm1, ymm2/m256

        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}28e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps ymm12, ymm8')

        # EVEX.128.0F.W0 28 /r
        # VMOVAPS xmm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.0F.W0')
        Buffer = '{}2890'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Reserved_.EVEX.W, myEVEX.W)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps xmm2, xmmword ptr [rax+00000000h]')

        # EVEX.256.0F.W0 28 /r
        # VMOVAPS ymm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.0F.W0')
        Buffer = '{}2890'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps ymm2, ymmword ptr [rax+00000000h]')

        # EVEX.512.0F.W0 28 /r
        # VMOVAPS zmm1 {k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.0F.W0')
        Buffer = '{}2890'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps zmm2, zmmword ptr [rax+00000000h]')

        # 66 0F 28 /r
        # MOVAPD xmm1, xmm2/m128

        Buffer = '660f28e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movapd ')
        assert_equal(myDisasm.instr.repr, 'movapd xmm4, xmm0')

        # VEX.128.66.0F.WIG 28 /r
        # VMOVAPD xmm1, xmm2/m128

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}28e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd xmm12, xmm8')

        # VEX.256.66.0F.WIG 28 /r
        # VMOVAPD ymm1, ymm2/m256

        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}28e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd ymm12, ymm8')

        # EVEX.128.66.0F.W1 28 /r
        # VMOVAPD xmm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}2890'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd xmm2, xmmword ptr [rax+00000000h]')

        # EVEX.256.66.0F.W1 28 /r
        # VMOVAPD ymm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.66.0F.W1')
        Buffer = '{}2890'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd ymm2, ymmword ptr [rax+00000000h]')

        # EVEX.512.66.0F.W1 28 /r
        # VMOVAPD zmm1 {k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.66.0F.W1')
        Buffer = '{}2820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd zmm4, zmmword ptr [rax]')
