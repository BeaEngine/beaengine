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

        # 0F 03 /r
        # LSL r16, r16/m16

        Buffer = '660f03e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf03)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lsl ')
        assert_equal(myDisasm.infos.repr, 'lsl sp, ax')

        # 0F 03 /r
        # LSL reg, r32/m16

        Buffer = '0f03e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf03)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lsl ')
        assert_equal(myDisasm.infos.repr, 'lsl esp, eax')

        Buffer = '0f0390'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf03)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lsl ')
        assert_equal(myDisasm.infos.repr, 'lsl edx, word ptr [rax+00000000h]')


        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0f0390'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf03)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lsl ')
        assert_equal(myDisasm.infos.repr, 'lsl rdx, word ptr [rax+00000000h]')

        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0f03e0'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf03)
        assert_equal(myDisasm.infos.Reserved_.MOD_, 0x3)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lsl ')
        assert_equal(myDisasm.infos.repr, 'lsl rsp, eax')

        Buffer = 'f00f03e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf03)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'lsl ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
