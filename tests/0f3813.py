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

        # VEX.128.66.0F38.W0 13 /r
        # VCVTPH2PS xmm1, xmm2/m64

        myVEX = VEX('VEX.128.66.0F38.W0')
        myVEX.R = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}132b'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps xmm5, qword ptr [r11]')

        myVEX = VEX('VEX.128.66.0F38.W0')
        myVEX.R = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps xmm0, xmm8')

        # VEX.256.66.0F38.W0 13 /r
        # VCVTPH2PS ymm1, xmm2/m128

        myVEX = VEX('VEX.256.66.0F38.W0')
        myVEX.R = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}132b'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps ymm5, xmmword ptr [r11]')

        myVEX = VEX('VEX.256.66.0F38.W0')
        myVEX.R = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps ymm0, xmm8')

        # EVEX.128.66.0F38.W0 13 /r
        # VCVTPH2PS xmm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1316'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps xmm2, qword ptr [rsi]')

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps xmm0, xmm0')

        # EVEX.256.66.0F38.W0 13 /r
        # VCVTPH2PS ymm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1316'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps ymm2, xmmword ptr [rsi]')

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps ymm0, xmm0')

        # EVEX.512.66.0F38.W0 13 /r
        # VCVTPH2PS zmm1 {k1}{z}, ymm2/m256 {sae}

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1316'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps zmm2, ymmword ptr [rsi]')

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtph2ps ')
        assert_equal(myDisasm.infos.repr, 'vcvtph2ps zmm0, ymm0')

        # EVEX.128.F3.0F38.W0 13 /r
        # VPMOVUSDW xmm1/m64 {k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1316'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusdw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusdw qword ptr [rsi], xmm2')

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusdw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusdw xmm0, xmm0')


        # EVEX.256.F3.0F38.W0 13 /r
        # VPMOVUSDW xmm1/m128 {k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1316'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusdw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusdw xmmword ptr [rsi], ymm2')

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusdw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusdw xmm0, ymm0')

        # EVEX.512.F3.0F38.W0 13 /r
        # VPMOVUSDW ymm1/m256 {k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1316'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusdw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusdw ymmword ptr [rsi], zmm2')

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}13c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x13)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovusdw ')
        assert_equal(myDisasm.infos.repr, 'vpmovusdw ymm0, zmm0')
