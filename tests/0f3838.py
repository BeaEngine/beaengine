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
        # 66 0F 38 38 /r
        # pminsb mm1, mm2/m64
        Buffer = '660f38389011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf3838')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pminsb ')
        assert_equal(myDisasm.infos.repr, 'pminsb xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 38 /r
        # vpminsb xmm1, xmm2, xmm3/m128
        Buffer = 'c40201380e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.infos.repr, 'vpminsb xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.WIG 38 /r
        # vpminsb ymm1, ymm2, ymm3/m256
        Buffer = 'c40205380e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.infos.repr, 'vpminsb ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.WIG 38 /r
        # vpminsb xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '62020506380e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x38')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.infos.repr, 'vpminsb xmm25, xmm31, xmmword ptr [r14]')

        # EVEX.NDS.256.66.0F38.WIG 38 /r
        # vpminsb ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '62020520380e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x38')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.infos.repr, 'vpminsb ymm25, ymm31, ymmword ptr [r14]')

        # EVEX.NDS.512.66.0F38.WIG 38 /r
        # vpminsb zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '62020540380e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x38')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminsb ')
        assert_equal(myDisasm.infos.repr, 'vpminsb zmm25, zmm31, zmmword ptr [r14]')


        # EVEX.128.F3.0F38.W0 38 /r
        # vpmovm2d xmm1, k1

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        Buffer = '{}38c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2d ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2d xmm24, k1')

        # EVEX.256.F3.0F38.W0 38 /r
        # vpmovm2d ymm1, k1

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        Buffer = '{}38c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2d ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2d ymm24, k1')

        # EVEX.512.F3.0F38.W0 38 /r
        # vpmovm2d zmm1, k1

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}38c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2d ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2d zmm24, k1')

        # EVEX.128.F3.0F38.W1 38 /r
        # vpmovm2q xmm1, k1

        myEVEX = EVEX('EVEX.128.F3.0F38.W1')
        Buffer = '{}38c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2q ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2q xmm24, k1')

        # EVEX.256.F3.0F38.W1 38 /r
        # vpmovm2q ymm1, k1

        myEVEX = EVEX('EVEX.256.F3.0F38.W1')
        Buffer = '{}38c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2q ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2q ymm24, k1')

        # EVEX.512.F3.0F38.W1 38 /r
        # vpmovm2q zmm1, k1

        myEVEX = EVEX('EVEX.512.F3.0F38.W1')
        Buffer = '{}38c1'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovm2q ')
        assert_equal(myDisasm.infos.repr, 'vpmovm2q zmm24, k1')
