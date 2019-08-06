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

        # NP 0F 57 /r
        # xorpS xmm1, xmm2/m128

        Buffer = '0f5790'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf57')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'xorps ')
        assert_equal(myDisasm.infos.repr, 'xorps xmm2, xmmword ptr [rax+00000000h]')

        # VEX.NDS.128.0F 57 /r
        # VxorpS xmm1,xmm2, xmm3/m128

        myVEX = VEX('VEX.NDS.128.0F')
        Buffer = '{}5790'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x57')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorps ')
        assert_equal(myDisasm.infos.repr, 'vxorps xmm10, xmm15, xmmword ptr [r8+00000000h]')

        # VEX.NDS.256.0F 57 /r
        # VxorpS ymm1, ymm2, ymm3/m256

        myVEX = VEX('VEX.NDS.256.0F')
        Buffer = '{}5790'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x57')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorps ')
        assert_equal(myDisasm.infos.repr, 'vxorps ymm10, ymm15, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.128.0F.W0 57 /r
        # VxorpS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        myEVEX = EVEX('EVEX.NDS.128.0F.W0')
        Buffer = '{}5790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x57)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorps ')
        assert_equal(myDisasm.infos.repr, 'vxorps xmm26, xmm31, xmmword ptr [r8+00000000h]')

        # EVEX.NDS.256.0F.W0 57 /r
        # VxorpS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        myEVEX = EVEX('EVEX.NDS.256.0F.W0')
        Buffer = '{}5790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x57)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorps ')
        assert_equal(myDisasm.infos.repr, 'vxorps ymm26, ymm31, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.512.0F.W0 57 /r
        # VxorpS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        myEVEX = EVEX('EVEX.NDS.512.0F.W0')
        Buffer = '{}5790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x57)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorps ')
        assert_equal(myDisasm.infos.repr, 'vxorps zmm26, zmm31, zmmword ptr [r8+00000000h]')

        # 66 0F 57 /r
        # xorpD xmm1, xmm2/m128

        Buffer = '660f5790'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf57')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'xorpd ')
        assert_equal(myDisasm.infos.repr, 'xorpd xmm2, xmmword ptr [rax+00000000h]')

        # VEX.NDS.128.66.0F 57 /r
        # VxorpD xmm1, xmm2, xmm3/m128

        myVEX = VEX('VEX.NDS.128.66.0F')
        Buffer = '{}5790'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x57')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorpd ')
        assert_equal(myDisasm.infos.repr, 'vxorpd xmm10, xmm15, xmmword ptr [r8+00000000h]')

        # VEX.NDS.256.66.0F 57 /r
        # VxorpD ymm1, ymm2, ymm3/m256

        myVEX = VEX('VEX.NDS.256.66.0F')
        Buffer = '{}5790'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x57')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorpd ')
        assert_equal(myDisasm.infos.repr, 'vxorpd ymm10, ymm15, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.128.66.0F.W1 57 /r
        # VxorpD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst

        myEVEX = EVEX('EVEX.NDS.128.66.0F.W1')
        Buffer = '{}5790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x57)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorpd ')
        assert_equal(myDisasm.infos.repr, 'vxorpd xmm26, xmm31, xmmword ptr [r8+00000000h]')

        # EVEX.NDS.256.66.0F.W1 57 /r
        # VxorpD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst

        myEVEX = EVEX('EVEX.NDS.256.66.0F.W1')
        Buffer = '{}5790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x57)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorpd ')
        assert_equal(myDisasm.infos.repr, 'vxorpd ymm26, ymm31, ymmword ptr [r8+00000000h]')

        # EVEX.NDS.512.66.0F.W1 57 /r
        # VxorpD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst

        myEVEX = EVEX('EVEX.NDS.512.66.0F.W1')
        Buffer = '{}5790'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x57)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vxorpd ')
        assert_equal(myDisasm.infos.repr, 'vxorpd zmm26, zmm31, zmmword ptr [r8+00000000h]')
