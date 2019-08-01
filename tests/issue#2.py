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

        # MOD == 1

        Buffer = '8f442401'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop qword ptr [rsp+09h]')

        Buffer = '8f442401'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop dword ptr [esp+05h]')

        Buffer = '8f4301'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop qword ptr [rbx+01h]')


        # MOD == 00

        Buffer = '8f042400'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop qword ptr [rsp+08h]')

        Buffer = '8f042400'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Archi = 32
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop dword ptr [esp+04h]')


        Buffer = '8f03'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop qword ptr [rbx]')

        # MOD == 2

        Buffer = '8f842401000000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop qword ptr [rsp+00000009h]')

        Buffer = '8f8301000000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop qword ptr [rbx+00000001h]')

        # MOD == 3

        Buffer = '8fc4'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x8f)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pop ')
        assert_equal(myDisasm.infos.repr, 'pop rsp')
