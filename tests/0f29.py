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

        # NP 0F 29 /r
        # MOVAPS xmm2/m128, xmm1

        Buffer = '0f2920'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movaps ')
        assert_equal(myDisasm.instr.repr, 'movaps xmmword ptr [rax], xmm4')

        # VEX.128.0F.WIG 29 /r
        # VMOVAPS xmm2/m128, xmm1

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}2910'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps xmmword ptr [r8], xmm10')

        # VEX.256.0F.WIG 29 /r
        # VMOVAPS ymm2/m256, ymm1

        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}29e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps ymm8, ymm12')

        # EVEX.128.0F.W0 29 /r
        # VMOVAPS xmm2/m128 {k1}{z}, xmm1

        myEVEX = EVEX('EVEX.128.0F.W0')
        Buffer = '{}2916'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Reserved_.EVEX.W, myEVEX.W)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps xmmword ptr [rsi], xmm2')

        # EVEX.256.0F.W0 29 /r
        # VMOVAPS ymm2/m256 {k1}{z}, ymm1

        myEVEX = EVEX('EVEX.256.0F.W0')
        Buffer = '{}2917'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps ymmword ptr [rdi], ymm2')

        # EVEX.512.0F.W0 29 /r
        # VMOVAPS zmm2/m512 {k1}{z}, zmm1

        myEVEX = EVEX('EVEX.512.0F.W0')
        Buffer = '{}2911'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovaps ')
        assert_equal(myDisasm.instr.repr, 'vmovaps zmmword ptr [rcx], zmm2')

        # 66 0F 29 /r
        # MOVAPD xmm2/m128, xmm1

        Buffer = '660f294211'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movapd ')
        assert_equal(myDisasm.instr.repr, 'movapd xmmword ptr [rdx+11h], xmm0')

        # VEX.128.66.0F.WIG 29 /r
        # VMOVAPD xmm2/m128, xmm1

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}2924c012'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd xmmword ptr [r8+r8*8], xmm12')

        # EVEX.128.66.0F.W1 29 /r
        # VMOVAPD xmm2/m128 {k1}{z}, xmm1

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}2944c012'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd xmmword ptr [rax+rax*8+0120h], xmm0')

        # EVEX.256.66.0F.W1 29 /r
        # VMOVAPD ymm2/m256 {k1}{z}, ymm1

        myEVEX = EVEX('EVEX.256.66.0F.W1')
        Buffer = '{}2920'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd ymmword ptr [rax], ymm4')

        # EVEX.512.66.0F.W1 29 /r
        # VMOVAPD zmm2/m512 {k1}{z}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F.W1')
        Buffer = '{}299044332211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd zmmword ptr [rax+11223344h], zmm2')

        # VEX.256.66.0F.WIG 29 /r
        # VMOVAPD ymm2/m256, ymm1

        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}29e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x29)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovapd ')
        assert_equal(myDisasm.instr.repr, 'vmovapd ymm8, ymm12')
