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

        # NP 0F 01 CA
        # CLAC

        Buffer = '0f01ca'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'clac ')

        # NP 0F 01 CB
        # STAC

        Buffer = '0f01cb'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'stac ')

        # NP 0F 01 C5
        # PCONFIG
        # #UD If any of the LOCK/REP/OSIZE/VEX prefixes are used.

        Buffer = '0f01c5'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pconfig ')

        Buffer = 'f00f01c5'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pconfig ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f20f01c5'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pconfig ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = 'f30f01c5'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pconfig ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        # NP 0F 01 C0
        # ENCLV

        Buffer = '0f01c0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'enclv ')

        # NP 0F 01 D7
        # ENCLU

        Buffer = '0f01d7'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'enclu ')

        # NP 0F 01 CF
        # ENCLS

        Buffer = '0f01cf'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'encls ')


        # F3 0F 01 EA (mod=11, /5, RM=010)
        # SAVEPREVSSP

        Buffer = 'f30f01ea'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'saveprevssp ')
