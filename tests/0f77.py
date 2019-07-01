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

        YMM0 = AVX_REG + REG0
        YMM1 = AVX_REG + REG1
        YMM2 = AVX_REG + REG2
        YMM3 = AVX_REG + REG3
        YMM4 = AVX_REG + REG4
        YMM5 = AVX_REG + REG5
        YMM6 = AVX_REG + REG6
        YMM7 = AVX_REG + REG7
        YMM8 = AVX_REG + REG8
        YMM9 = AVX_REG + REG9
        YMM10 = AVX_REG + REG10
        YMM11 = AVX_REG + REG11
        YMM12 = AVX_REG + REG12
        YMM13 = AVX_REG + REG13
        YMM14 = AVX_REG + REG14
        YMM15 = AVX_REG + REG15

        # NP 0F 77
        # EMMS

        Buffer = '0f77'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x0f77)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'emms ')

        # VEX.256.0F.WIG
        # VZEROALL

        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}77'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x77)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vzeroall ')
        assert_equal(myDisasm.instr.Instruction.ImplicitModifiedRegs, YMM1|YMM0
         |YMM2 |YMM3 |YMM4 |YMM5 |YMM6 |YMM7 |YMM8 |YMM9
         |YMM10 |YMM11 |YMM12 |YMM13 |YMM14 |YMM15)

        # VEX.128.0F.WIG 77
        # VZEROUPPER

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}77'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x77)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vzeroupper ')
        assert_equal(myDisasm.instr.Instruction.ImplicitModifiedRegs, YMM1|YMM0
         |YMM2 |YMM3 |YMM4 |YMM5 |YMM6 |YMM7 |YMM8 |YMM9
         |YMM10 |YMM11 |YMM12 |YMM13 |YMM14 |YMM15)


        # VEX.vvvv is reserved and must be 1111b, otherwise instructions will #UD.

        myVEX = VEX('VEX.128.0F.WIG')
        myVEX.vvvv = 0b1000
        Buffer = '{}77'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x77)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vzeroupper ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
