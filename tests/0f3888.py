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

        # EVEX.128.66.0F38.W0 88 /r
        # VEXPANDPS xmm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}880e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x88)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vexpandps ')
        assert_equal(myDisasm.infos.repr, 'vexpandps xmm1, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W0 88 /r
        # VEXPANDPS ymm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}880e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x88)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vexpandps ')
        assert_equal(myDisasm.infos.repr, 'vexpandps ymm1, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W0 88 /r
        # VEXPANDPS zmm1 {k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}880e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x88)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vexpandps ')
        assert_equal(myDisasm.infos.repr, 'vexpandps zmm1, zmmword ptr [rsi]')

        # EVEX.128.66.0F38.W1 88 /r
        # VEXPANDPD xmm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        Buffer = '{}880e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x88)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vexpandpd ')
        assert_equal(myDisasm.infos.repr, 'vexpandpd xmm1, xmmword ptr [rsi]')

        # EVEX.256.66.0F38.W1 88 /r
        # VEXPANDPD ymm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}880e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x88)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vexpandpd ')
        assert_equal(myDisasm.infos.repr, 'vexpandpd ymm1, ymmword ptr [rsi]')

        # EVEX.512.66.0F38.W1 88 /r
        # VEXPANDPD zmm1 {k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}880e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x88)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vexpandpd ')
        assert_equal(myDisasm.infos.repr, 'vexpandpd zmm1, zmmword ptr [rsi]')
