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


        # 66 0F 3A 21 /r ib
        # INSERTPS xmm1, xmm2/m32, imm8

        Buffer = '660f3a212011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x0f3a21)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'insertps ')
        assert_equal(myDisasm.infos.repr, 'insertps xmm4, dword ptr [rax], 11h')

        Buffer = '660f3a21c011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x0f3a21)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'insertps ')
        assert_equal(myDisasm.infos.repr, 'insertps xmm0, xmm0, 11h')

        # VEX.128.66.0F3A.WIG 21 /r ib
        # VINSERTPS xmm1, xmm2, xmm3/m32, imm8

        myVEX = VEX('VEX.128.66.0F3A.WIG')
        Buffer = '{}21e011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x21)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertps ')
        assert_equal(myDisasm.infos.repr, 'vinsertps xmm12, xmm0, xmm8, 11h')

        myVEX = VEX('VEX.128.66.0F3A.WIG')
        Buffer = '{}212011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x21)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertps ')
        assert_equal(myDisasm.infos.repr, 'vinsertps xmm12, xmm0, dword ptr [r8], 11h')

        # EVEX.128.66.0F3A.W0 21 /r ib
        # VINSERTPS xmm1, xmm2, xmm3/m32, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}212011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x21)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertps ')
        assert_equal(myDisasm.infos.repr, 'vinsertps xmm4, xmm0, dword ptr [rax], 11h')


        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}21c011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x21)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertps ')
        assert_equal(myDisasm.infos.repr, 'vinsertps xmm0, xmm0, xmm0, 11h')
