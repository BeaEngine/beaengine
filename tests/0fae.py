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

        # Saves the states of x87 FPU, MMX, XMM, YMM, and MXCSR registers to memory, optimizing the save operation if possible.

        # NP 0F AE /6
        # XSAVEOPT mem

        Buffer = '0fae30'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xsaveopt ')
        assert_equal(myDisasm.instr.repr, 'xsaveopt  [rax]')


        # NP REX.W + 0F AE /6
        # XSAVEOPT64 mem

        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0fae30'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xfae')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'xsaveopt64 ')
        assert_equal(myDisasm.instr.repr, 'xsaveopt64  [rax]')
        assert_equal(myDisasm.instr.Argument1.ArgType, MEMORY_TYPE)
        assert_equal(myDisasm.instr.Argument1.ArgSize, 512 * 8)
        assert_equal(myDisasm.instr.Argument2.ArgType, REGISTER_TYPE + GENERAL_REG)
        assert_equal(myDisasm.instr.Argument2.Registers, REG0 + REG2)
