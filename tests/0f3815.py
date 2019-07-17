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

        # 66 0F 38 15 /r
        # BLENDVPD xmm1, xmm2/m128, <XMM0>

        Buffer = '660f381527'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'blendvpd xmm4, xmmword ptr [rdi], xmm0')


        # VEX.NDS.128.66.0F.W0 38 /r /is4
        # VBLENDvpd xmm1, xmm2, xmm3/m128, xmm4

        myVEX = VEX('VEX.NDS.128.66.0F38.W0')
        Buffer = '{}152b'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        #assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f38)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vblendvpd ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)

        # EVEX.NDS.128.66.0F38.W0 15 /r
        # vprolVD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vprolvd ')
        assert_equal(myDisasm.instr.repr, 'vprolvd xmm2, xmm0, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W0 15 /r
        # vprolVD ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vprolvd ')
        assert_equal(myDisasm.instr.repr, 'vprolvd ymm2, ymm0, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W0 15 /r
        # vprolVD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vprolvd ')
        assert_equal(myDisasm.instr.repr, 'vprolvd zmm2, zmm0, zmmword ptr [rsi]')

        # EVEX.NDS.128.66.0F38.W1 15 /r
        # vprolVQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst

        myEVEX = EVEX('EVEX.NDS.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vprolvq ')
        assert_equal(myDisasm.instr.repr, 'vprolvq xmm2, xmm0, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W1 15 /r
        # vprolVQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst

        myEVEX = EVEX('EVEX.NDS.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vprolvq ')
        assert_equal(myDisasm.instr.repr, 'vprolvq ymm2, ymm0, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W1 15 /r
        # vprolVQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst

        myEVEX = EVEX('EVEX.NDS.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vprolvq ')
        assert_equal(myDisasm.instr.repr, 'vprolvq zmm2, zmm0, zmmword ptr [rsi]')

        # EVEX.128.F3.0F38.W0 15 /r
        # VPMOVusqd xmm1/m32 {k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.repr, 'vpmovusqd dword ptr [rsi], xmm2')

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}15ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.repr, 'vpmovusqd xmm2, xmm1')

        # EVEX.256.F3.0F38.W0 15 /r
        # VPMOVusqd xmm1/m64 {k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.repr, 'vpmovusqd qword ptr [rsi], ymm2')

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}15ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.repr, 'vpmovusqd xmm2, ymm1')

        # EVEX.512.F3.0F38.W0 15 /r
        # VPMOVusqd xmm1/m128 {k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1516'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.repr, 'vpmovusqd xmmword ptr [rsi], zmm2')

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}15ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.repr, 'vpmovusqd xmm2, zmm1')


        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1110
        Buffer = '{}15ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x15)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpmovusqd ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
