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


        # NP 0F 14 /r
        # UNPCKLPS xmm1, xmm2/m128

        Buffer = '0f14e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'unpcklps ')
        assert_equal(myDisasm.infos.repr, 'unpcklps xmm4, xmm0')

        # VEX.NDS.128.0F.WIG 14 /r
        # VUNPCKLPS xmm1,xmm2,xmm3/m128

        myVEX = VEX('VEX.NDS.128.0F.WIG')
        Buffer = '{}14e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklps ')
        assert_equal(myDisasm.infos.repr, 'vunpcklps xmm12, xmm15, xmm8')

        # VEX.NDS.256.0F.WIG 14 /r
        # VUNPCKLPS ymm1,ymm2,ymm3/m256

        myVEX = VEX('VEX.NDS.256.0F.WIG')
        Buffer = '{}14e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklps ')
        assert_equal(myDisasm.infos.repr, 'vunpcklps ymm12, ymm15, ymm8')

        # EVEX.NDS.128.0F.W0 14 /r
        # VUNPCKLPS xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        myEVEX = EVEX('EVEX.NDS.128.0F.W0')
        Buffer = '{}1490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklps ')
        assert_equal(myDisasm.infos.repr, 'vunpcklps xmm2, xmm15, xmmword ptr [rax+00000000h]')

        # EVEX.NDS.256.0F.W0 14 /r
        # VUNPCKLPS ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        myEVEX = EVEX('EVEX.NDS.256.0F.W0')
        Buffer = '{}1490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklps ')
        assert_equal(myDisasm.infos.repr, 'vunpcklps ymm2, ymm15, ymmword ptr [rax+00000000h]')

        # EVEX.NDS.512.0F.W0 14 /r
        # VUNPCKLPS zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        myEVEX = EVEX('EVEX.NDS.512.0F.W0')
        Buffer = '{}1490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklps ')
        assert_equal(myDisasm.infos.repr, 'vunpcklps zmm2, zmm15, zmmword ptr [rax+00000000h]')

        # 66 0F 14 /r
        # UNPCKLPD xmm1, xmm2/m128

        Buffer = '660f14e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'unpcklpd ')
        assert_equal(myDisasm.infos.repr, 'unpcklpd xmm4, xmm0')

        # VEX.NDS.128.66.0F.WIG 14 /r
        # VUNPCKLPD xmm1,xmm2, xmm3/m128

        myVEX = VEX('VEX.NDS.128.66.0F.WIG')
        Buffer = '{}14e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklpd ')
        assert_equal(myDisasm.infos.repr, 'vunpcklpd xmm12, xmm15, xmm8')

        # VEX.NDS.256.66.0F.WIG 14 /r
        # VUNPCKLPD ymm1,ymm2, ymm3/m256

        myVEX = VEX('VEX.NDS.256.66.0F.WIG')
        Buffer = '{}14e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklpd ')
        assert_equal(myDisasm.infos.repr, 'vunpcklpd ymm12, ymm15, ymm8')

        # EVEX.NDS.128.66.0F.W1 14 /r
        # VUNPCKLPD xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst

        myEVEX = EVEX('EVEX.NDS.128.66.0F.W1')
        Buffer = '{}1490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklpd ')
        assert_equal(myDisasm.infos.repr, 'vunpcklpd xmm2, xmm15, xmmword ptr [rax+00000000h]')

        # EVEX.NDS.256.66.0F.W1 14 /r
        # VUNPCKLPD ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst

        myEVEX = EVEX('EVEX.NDS.256.66.0F.W1')
        Buffer = '{}1490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklpd ')
        assert_equal(myDisasm.infos.repr, 'vunpcklpd ymm2, ymm15, ymmword ptr [rax+00000000h]')

        # EVEX.NDS.512.66.0F.W1 14 /r
        # VUNPCKLPD zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst

        myEVEX = EVEX('EVEX.NDS.512.66.0F.W1')
        Buffer = '{}1490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x14')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vunpcklpd ')
        assert_equal(myDisasm.infos.repr, 'vunpcklpd zmm2, zmm15, zmmword ptr [rax+00000000h]')
