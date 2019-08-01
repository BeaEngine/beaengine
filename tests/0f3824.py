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

        # 66 0f 38 24 /r
        # PMOVSXBW xmm1, xmm2/m64

        Buffer = '660f382490'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x0f3824)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pmovsxwq ')
        assert_equal(myDisasm.infos.repr, 'pmovsxwq xmm2, qword ptr [rax+00000000h]')

        # VEX.128.66.0F38.WIG 24 /r
        # vpmovsxwq xmm1, xmm2/m64

        myVEX = VEX('VEX.128.66.0F38.WIG')
        Buffer = '{}2490'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxwq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxwq xmm10, qword ptr [r8+00000000h]')

        # VEX.256.66.0F38.WIG 24 /r
        # vpmovsxwq ymm1, xmm2/m128

        myVEX = VEX('VEX.256.66.0F38.WIG')
        Buffer = '{}2490'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxwq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxwq ymm10, xmmword ptr [r8+00000000h]')

        # EVEX.128.66.0F38.WIG 24 /r
        # vpmovsxwq xmm1 {k1}{z}, xmm2/m64

        myEVEX = EVEX('EVEX.128.66.0F38.WIG')
        Buffer = '{}2490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxwq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxwq xmm2, qword ptr [rax+00000000h]')

        # EVEX.256.66.0F38.WIG 24 /r
        # vpmovsxwq ymm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.256.66.0F38.WIG')
        Buffer = '{}2490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxwq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxwq ymm2, xmmword ptr [rax+00000000h]')

        # EVEX.512.66.0F38.WIG 24 /r
        # vpmovsxwq zmm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.512.66.0F38.WIG')
        Buffer = '{}2490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsxwq ')
        assert_equal(myDisasm.infos.repr, 'vpmovsxwq zmm2, ymmword ptr [rax+00000000h]')

        # EVEX.128.F3.0F38.W0 24 /r
        # vpmovsqw xmm1/m64 {k1}{z},xmm2

        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        Buffer = '{}2490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovsqw qword ptr [rax+00000000h], xmm2')

        # EVEX.256.F3.0F38.W0 24 /r
        # vpmovsqw xmm1/m128 {k1}{z},ymm2

        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        Buffer = '{}2490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovsqw xmmword ptr [rax+00000000h], ymm2')

        # EVEX.512.F3.0F38.W0 24 /r
        # vpmovsqw ymm1/m256 {k1}{z},zmm2

        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}2490'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x24)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpmovsqw ')
        assert_equal(myDisasm.infos.repr, 'vpmovsqw ymmword ptr [rax+00000000h], zmm2')
