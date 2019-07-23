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

        # SecurityBlock is not useful if equal to buffer length

        Buffer = '0f381c28'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.length, 4)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf381c)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pabsb ')

        # SecurityBlock is disabled if equal to zero

        Buffer = '0f381c28'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 0
        myDisasm.read()
        assert_equal(myDisasm.length, 4)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf381c)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pabsb ')

        # SecurityBlock blocking analysis if < buffer length

        for i in range(1, len(Buffer)):
            myDisasm = Disasm(Buffer)
            myDisasm.instr.SecurityBlock = i
            myDisasm.read()
            assert_equal(myDisasm.length, 0)

        # SecurityBlock if MOD == 0 and RM = 5

        Buffer = '0f381c0501000000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.instr.VirtualAddr = 0x400000
        myDisasm.read()
        assert_equal(myDisasm.length, 8)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf381c)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pabsb ')
        assert_equal(myDisasm.instr.repr, 'pabsb mm0, qword ptr [0000000000400009h]')

        for i in range(1, len(Buffer)):
            myDisasm = Disasm(Buffer)
            myDisasm.instr.SecurityBlock = i
            myDisasm.read()
            assert_equal(myDisasm.length, 0)

        # SecurityBlock if MOD == 1 (disp8)

        Buffer = '660f381c6b11'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.length, 6)

        for i in range(1, len(Buffer)):
            myDisasm = Disasm(Buffer)
            myDisasm.instr.SecurityBlock = i
            myDisasm.read()
            assert_equal(myDisasm.length, 0)

        # SecurityBlock if MOD == 1 (disp8) and RM == 4 (SIB enabled)

        myVEX = VEX('VEX.128.66.0F38.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}1c443322'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer) - 1
        myDisasm.read()
        assert_equal(myDisasm.length, 0)

        myVEX = VEX('VEX.128.66.0F38.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}1c443322'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.length, 7)

        # SecurityBlock if MOD == 2 (disp32)

        myVEX = VEX('VEX.128.66.0F38.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}1c843311223344'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer) - 1
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, myDisasm.instr.SecurityBlock)
        assert_equal(myDisasm.instr.Argument1.Memory.Displacement, 0)

        myVEX = VEX('VEX.128.66.0F38.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}1c843311223344'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.length, 10)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x1c)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpabsb ')
        assert_equal(myDisasm.instr.repr, 'vpabsb xmm8, xmmword ptr [r11+r14+44332211h]')

        Buffer = '40034d03'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 2
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 3)
        assert_equal(myDisasm.instr.Reserved_.MOD_, 0)
        assert_equal(myDisasm.instr.Reserved_.RM_, 0)


        Buffer = '40034d03'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 1
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 0)
        assert_equal(myDisasm.instr.Reserved_.MOD_, 0)
        assert_equal(myDisasm.instr.Reserved_.RM_, 0)

        Buffer = '660f3a14443322'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 4
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.MOD_, 0)
        assert_equal(myDisasm.instr.Reserved_.RM_, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 3)

        Buffer = 'e811223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 4
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 0)

        Buffer = '691011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 5
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 0)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x69)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'imul ')
        assert_equal(myDisasm.instr.Instruction.Immediat, 0)

        Buffer = '6b1011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 2
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 0)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 0)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x6b)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'imul ')
        assert_equal(myDisasm.instr.Instruction.Immediat, 0)

        Buffer = '691011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 6)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 6)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x69)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'imul ')
        assert_equal(myDisasm.instr.Instruction.Immediat, 0x44332211)


        # if SecurityBlock > 15, it is disabled and max size is set to 15
        Buffer = '666666666666666666666666666690'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = 18
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 15)
        assert_equal(myDisasm.instr.Reserved_.EIP_ - offset, 15)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x90)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'nop ')


        Buffer = '0f8001000000'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.instr.SecurityBlock = len(Buffer)
        myDisasm.instr.VirtualAddr = 0x400000
        offset = myDisasm.instr.offset
        myDisasm.read()
        assert_equal(myDisasm.length, 6)
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f80)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'jo ')
