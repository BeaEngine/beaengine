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
        # 66 0F 38 28 /r
        # pmuldq mm1, mm2/m64
        Buffer = '660f38289011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf3828')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pmuldq ')
        assert_equal(myDisasm.infos.repr, 'pmuldq xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 28 /r
        # vpmuldq xmm1, xmm2, xmm3/m128
        Buffer = 'c40201280e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmuldq ')
        assert_equal(myDisasm.infos.repr, 'vpmuldq xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.WIG 28 /r
        # vpmuldq ymm1, ymm2, ymm3/m256
        Buffer = 'c40205280e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmuldq ')
        assert_equal(myDisasm.infos.repr, 'vpmuldq ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.WIG 28 /r
        # vpmuldq xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62020506280e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x28')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmuldq ')
        assert_equal(myDisasm.infos.repr, 'vpmuldq xmm25, xmm31, xmmword ptr [r14]')

        # EVEX.NDS.256.66.0F38.WIG 28 /r
        # vpmuldq ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62020520280e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x28')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmuldq ')
        assert_equal(myDisasm.infos.repr, 'vpmuldq ymm25, ymm31, ymmword ptr [r14]')

        # EVEX.NDS.512.66.0F38.WIG 28 /r
        # vpmuldq zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62020540280e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x28')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmuldq ')
        assert_equal(myDisasm.infos.repr, 'vpmuldq zmm25, zmm31, zmmword ptr [r14]')


        # EVEX.128.F3.0F38.W0 28 /r
        # VPMOVM2B xmm1, k1

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        Buffer = '{}28c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2b ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2b xmm24, k1')

        # EVEX.256.F3.0F38.W0 28 /r
        # VPMOVM2B ymm1, k1

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        Buffer = '{}28c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2b ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2b ymm24, k1')

        # EVEX.512.F3.0F38.W0 28 /r
        # VPMOVM2B zmm1, k1

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}28c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2b ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2b zmm24, k1')

        # EVEX.128.F3.0F38.W1 28 /r
        # VPMOVM2W xmm1, k1

        myEVEX = EVEX('EVEX.128.F3.0F38.W1')
        Buffer = '{}28c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2w ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2w xmm24, k1')

        # EVEX.256.F3.0F38.W1 28 /r
        # VPMOVM2W ymm1, k1

        myEVEX = EVEX('EVEX.256.F3.0F38.W1')
        Buffer = '{}28c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2w ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2w ymm24, k1')

        # EVEX.512.F3.0F38.W1 28 /r
        # VPMOVM2W zmm1, k1

        myEVEX = EVEX('EVEX.512.F3.0F38.W1')
        Buffer = '{}28c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x28)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2w ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2w zmm24, k1')
