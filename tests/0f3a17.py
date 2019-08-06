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

        # 66 0F 3A 17 /r ib
        # EXTRACTPS reg/m32, xmm1, imm8

        Buffer = '660f3a172011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x0f3a17)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'extractps ')
        assert_equal(myDisasm.infos.repr, 'extractps dword ptr [rax], xmm4, 11h')

        # VEX.128.66.0F3A.WIG 17 /r ib
        # VEXTRACTPS reg/m32, xmm1, imm8

        myVEX = VEX('VEX.128.66.0F3A.WIG')
        Buffer = '{}17e011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x17)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractps ')
        assert_equal(myDisasm.infos.repr, 'vextractps r8d, xmm12, 11h')

        # EVEX.128.66.0F3A.WIG 17 /r ib
        # VEXTRACTPS reg/m32, xmm1, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.WIG')
        Buffer = '{}172011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x17)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vextractps ')
        assert_equal(myDisasm.infos.repr, 'vextractps dword ptr [r8], xmm28, 11h')
