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

        # 66 0f 38 33 /r
        # PMOVSXBW xmm1, xmm2/m64

        Buffer = '660f383390'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f3833)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmovzxwd ')
        assert_equal(myDisasm.instr.repr, 'pmovzxwd xmm2, qword ptr [rax+00000000h]')

        # VEX.128.66.0F38.WIG 33 /r
        # vpmovzxwd xmm1, xmm2/m64

        myVEX = VEX('VEX.128.66.0F38.WIG')
        Buffer = '{}3390'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovzxwd ')
        assert_equal(myDisasm.instr.repr, 'vpmovzxwd xmm10, qword ptr [r8+00000000h]')

        # VEX.256.66.0F38.WIG 33 /r
        # vpmovzxwd ymm1, xmm2/m128

        myVEX = VEX('VEX.256.66.0F38.WIG')
        Buffer = '{}3390'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovzxwd ')
        assert_equal(myDisasm.instr.repr, 'vpmovzxwd ymm10, xmmword ptr [r8+00000000h]')

        # EVEX.128.66.0F38.WIG 33 /r
        # vpmovzxwd xmm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.128.66.0F38.WIG')
        Buffer = '{}3390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovzxwd ')
        assert_equal(myDisasm.instr.repr, 'vpmovzxwd xmm2, qword ptr [rax+00000000h]')

        # EVEX.256.66.0F38.WIG 33 /r
        # vpmovzxwd ymm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.256.66.0F38.WIG')
        Buffer = '{}3390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovzxwd ')
        assert_equal(myDisasm.instr.repr, 'vpmovzxwd ymm2, xmmword ptr [rax+00000000h]')

        # EVEX.512.66.0F38.WIG 33 /r
        # vpmovzxwd zmm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.512.66.0F38.WIG')
        Buffer = '{}3390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovzxwd ')
        assert_equal(myDisasm.instr.repr, 'vpmovzxwd zmm2, ymmword ptr [rax+00000000h]')

        # EVEX.128.F3.0F38.W0 33 /r
        # vpmovdw xmm1/m64 {k1}{z},xmm2

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        Buffer = '{}3390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovdw ')
        assert_equal(myDisasm.instr.repr, 'vpmovdw qword ptr [rax+00000000h], xmm2')

        # EVEX.256.F3.0F38.W0 33 /r
        # vpmovdw xmm1/m128 {k1}{z},ymm2

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        Buffer = '{}3390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovdw ')
        assert_equal(myDisasm.instr.repr, 'vpmovdw xmmword ptr [rax+00000000h], ymm2')

        # EVEX.512.F3.0F38.W0 33 /r
        # vpmovdw ymm1/m256 {k1}{z},zmm2

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}3390'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x33)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovdw ')
        assert_equal(myDisasm.instr.repr, 'vpmovdw ymmword ptr [rax+00000000h], zmm2')
