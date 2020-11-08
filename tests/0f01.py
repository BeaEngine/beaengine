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

        Buffer = bytes.fromhex('0f01ca')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'clac ')

        # NP 0F 01 CB
        # STAC

        Buffer = bytes.fromhex('0f01cb')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'stac ')

        # NP 0F 01 C5
        # PCONFIG
        # #UD If any of the LOCK/REP/OSIZE/VEX prefixes are used.

        Buffer = bytes.fromhex('0f01c5')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'pconfig ')

        Buffer = bytes.fromhex('f00f01c5')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'pconfig ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = bytes.fromhex('f20f01c5')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'pconfig ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        Buffer = bytes.fromhex('f30f01c5')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'pconfig ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        # NP 0F 01 C0
        # ENCLV

        Buffer = bytes.fromhex('0f01c0')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'enclv ')

        # NP 0F 01 D7
        # ENCLU

        Buffer = bytes.fromhex('0f01d7')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'enclu ')

        # NP 0F 01 CF
        # ENCLS

        Buffer = bytes.fromhex('0f01cf')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'encls ')


        # F3 0F 01 EA (mod=11, /5, RM=010)
        # SAVEPREVSSP

        Buffer = bytes.fromhex('f30f01ea')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'saveprevssp ')

        # 0F 01 EF
        # WRPKRU

        Buffer = bytes.fromhex('0f01ef')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'wrpkru ')
        assert_equal(myDisasm.infos.Operand1.OpType, REGISTER_TYPE)
        assert_equal(myDisasm.infos.Operand1.Registers.special, REG3)
        assert_equal(myDisasm.infos.Operand1.OpSize, 32)
        assert_equal(myDisasm.infos.Operand1.AccessMode, WRITE)
        assert_equal(myDisasm.infos.Operand2.OpType, REGISTER_TYPE)
        assert_equal(myDisasm.infos.Operand2.Registers.gpr, REG0)
        assert_equal(myDisasm.infos.Operand2.OpSize, 32)
        assert_equal(myDisasm.infos.Operand2.AccessMode, READ)

        Buffer = bytes.fromhex('f00f01ef')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf01)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, b'wrpkru ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
