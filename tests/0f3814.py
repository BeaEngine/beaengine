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
    """
    Variable Blend Packed Bytes
    """

    def test(self):

        # 66 0F 38 14 /r
        # BLENDVPS xmm1, xmm2/m128, <XMM0>

        Buffer = '660f381427'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.repr, 'blendvps xmm4, xmmword ptr [rdi], xmm0')

        # VEX.NDS.128.66.0F.W0 38 /r /is4
        # VBLENDVPS xmm1, xmm2, xmm3/m128, xmm4

        myVEX = VEX('VEX.NDS.128.66.0F38.W0')
        Buffer = '{}142b'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        #assert_equal(myDisasm.infos.Instruction.Opcode, 0x0f38)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vblendvps ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)



        # EVEX.NDS.128.66.0F38.W0 14 /r
        # VPRORVD xmm1 {k1}{z}, xmm2, xmm3/m128/m32bcst

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vprorvd ')
        assert_equal(myDisasm.infos.repr, 'vprorvd xmm2, xmm0, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W0 14 /r
        # VPRORVD ymm1 {k1}{z}, ymm2, ymm3/m256/m32bcst

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vprorvd ')
        assert_equal(myDisasm.infos.repr, 'vprorvd ymm2, ymm0, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W0 14 /r
        # VPRORVD zmm1 {k1}{z}, zmm2, zmm3/m512/m32bcst

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vprorvd ')
        assert_equal(myDisasm.infos.repr, 'vprorvd zmm2, zmm0, zmmword ptr [rsi]')

        # EVEX.NDS.128.66.0F38.W1 14 /r
        # VPRORVQ xmm1 {k1}{z}, xmm2, xmm3/m128/m64bcst

        myEVEX = EVEX('EVEX.NDS.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vprorvq ')
        assert_equal(myDisasm.infos.repr, 'vprorvq xmm2, xmm0, xmmword ptr [rsi]')

        # EVEX.NDS.256.66.0F38.W1 14 /r
        # VPRORVQ ymm1 {k1}{z}, ymm2, ymm3/m256/m64bcst

        myEVEX = EVEX('EVEX.NDS.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vprorvq ')
        assert_equal(myDisasm.infos.repr, 'vprorvq ymm2, ymm0, ymmword ptr [rsi]')

        # EVEX.NDS.512.66.0F38.W1 14 /r
        # VPRORVQ zmm1 {k1}{z}, zmm2, zmm3/m512/m64bcst

        myEVEX = EVEX('EVEX.NDS.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vprorvq ')
        assert_equal(myDisasm.infos.repr, 'vprorvq zmm2, zmm0, zmmword ptr [rsi]')

        # EVEX.128.F3.0F38.W0 14 /r
        # VPMOVUSQW xmm1/m32 {k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusqw dword ptr [rsi], xmm2')

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}14ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusqw xmm2, xmm1')

        # EVEX.256.F3.0F38.W0 14 /r
        # VPMOVUSQW xmm1/m64 {k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusqw qword ptr [rsi], ymm2')

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}14ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusqw xmm2, ymm1')

        # EVEX.512.F3.0F38.W0 14 /r
        # VPMOVUSQW xmm1/m128 {k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1416'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusqw xmmword ptr [rsi], zmm2')

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}14ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusqw xmm2, zmm1')


        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1110
        Buffer = '{}14ca'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x14)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusqw ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
