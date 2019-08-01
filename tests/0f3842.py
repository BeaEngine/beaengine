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

        # EVEX.128.66.0F38.W0 42 /r
        # VGETEXPPS xmm1 {k1}{z},  xmm2/m128/m32bcst

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}420e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x42)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vgetexpps ')
        assert_equal(myDisasm.infos.repr, 'vgetexpps xmm1, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W0 42 /r
        # VGETEXPPS ymm1 {k1}{z},  ymm2/m256/m32bcst

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}420e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x42)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vgetexpps ')
        assert_equal(myDisasm.infos.repr, 'vgetexpps ymm1, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W0 42 /r
        # VGETEXPPS zmm1 {k1}{z},  zmm2/m512/m32bcst{sae}

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}420e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x42)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vgetexpps ')
        assert_equal(myDisasm.infos.repr, 'vgetexpps zmm1, zmmword ptr [rsi]')

        # EVEX.128.66.0F38.W1 42 /r
        # VGETEXPPD xmm1 {k1}{z},  xmm2/m128/m64bcst

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        Buffer = '{}420e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x42)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vgetexppd ')
        assert_equal(myDisasm.infos.repr, 'vgetexppd xmm1, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W1 42 /r
        # VGETEXPPD ymm1 {k1}{z},  ymm2/m256/m64bcst

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}420e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x42)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vgetexppd ')
        assert_equal(myDisasm.infos.repr, 'vgetexppd ymm1, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W1 42 /r
        # VGETEXPPD zmm1 {k1}{z},  zmm2/m512/m64bcst{sae}

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}420e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x42)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vgetexppd ')
        assert_equal(myDisasm.infos.repr, 'vgetexppd zmm1, zmmword ptr [rsi]')
