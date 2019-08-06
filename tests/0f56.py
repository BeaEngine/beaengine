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

        # NP 0F 56 /r
        # orpS xmm1, xmm2/m128

        Buffer = '0f5690'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf56')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'orps ')
        assert_equal(myDisasm.infos.repr, 'orps xmm2, xmmword ptr [rax+00000000h]')

        # VEX.NDS.128.0F 56 /r
        # VorpS xmm1,xmm2, xmm3/m128

        myVEX = VEX('VEX.NDS.128.0F')
        Buffer = '{}5690'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x56')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorps ')
        assert_equal(myDisasm.infos.repr, 'vorps xmm10, xmm15, xmmword ptr [r8+00000000h]')

        # VEX.NDS.256.0F 56 /r
        # VorpS ymm1, ymm2, ymm3/m256

        myVEX = VEX('VEX.NDS.256.0F')
        Buffer = '{}5690'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x56')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorps ')
        assert_equal(myDisasm.infos.repr, 'vorps ymm10, ymm15, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.128.0F.W0 56 /r
        # VorpS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        myEVEX = EVEX('EVEX.NDS.128.0F.W0')
        Buffer = '{}5690'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x56)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorps ')
        assert_equal(myDisasm.infos.repr, 'vorps xmm26, xmm31, xmmword ptr [r8+00000000h]')

        # EVEX.NDS.256.0F.W0 56 /r
        # VorpS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        myEVEX = EVEX('EVEX.NDS.256.0F.W0')
        Buffer = '{}5690'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x56)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorps ')
        assert_equal(myDisasm.infos.repr, 'vorps ymm26, ymm31, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.512.0F.W0 56 /r
        # VorpS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        myEVEX = EVEX('EVEX.NDS.512.0F.W0')
        Buffer = '{}5690'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x56)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorps ')
        assert_equal(myDisasm.infos.repr, 'vorps zmm26, zmm31, zmmword ptr [r8+00000000h]')

        # 66 0F 56 /r
        # orpD xmm1, xmm2/m128

        Buffer = '660f5690'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf56')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'orpd ')
        assert_equal(myDisasm.infos.repr, 'orpd xmm2, xmmword ptr [rax+00000000h]')

        # VEX.NDS.128.66.0F 56 /r
        # VorpD xmm1, xmm2, xmm3/m128

        myVEX = VEX('VEX.NDS.128.66.0F')
        Buffer = '{}5690'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x56')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorpd ')
        assert_equal(myDisasm.infos.repr, 'vorpd xmm10, xmm15, xmmword ptr [r8+00000000h]')

        # VEX.NDS.256.66.0F 56 /r
        # VorpD ymm1, ymm2, ymm3/m256

        myVEX = VEX('VEX.NDS.256.66.0F')
        Buffer = '{}5690'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x56')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorpd ')
        assert_equal(myDisasm.infos.repr, 'vorpd ymm10, ymm15, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.128.66.0F.W1 56 /r
        # VorpD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst

        myEVEX = EVEX('EVEX.NDS.128.66.0F.W1')
        Buffer = '{}5690'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x56)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorpd ')
        assert_equal(myDisasm.infos.repr, 'vorpd xmm26, xmm31, xmmword ptr [r8+00000000h]')

        # EVEX.NDS.256.66.0F.W1 56 /r
        # VorpD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst

        myEVEX = EVEX('EVEX.NDS.256.66.0F.W1')
        Buffer = '{}5690'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x56)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorpd ')
        assert_equal(myDisasm.infos.repr, 'vorpd ymm26, ymm31, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.512.66.0F.W1 56 /r
        # VorpD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst

        myEVEX = EVEX('EVEX.NDS.512.66.0F.W1')
        Buffer = '{}5690'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x56)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vorpd ')
        assert_equal(myDisasm.infos.repr, 'vorpd zmm26, zmm31, zmmword ptr [r8+00000000h]')
