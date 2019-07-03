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

        # NP 0F 52 /r
        # RSQRTPS xmm1, xmm2/m128

        Buffer = '0f5213'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf52')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rsqrtps ')
        assert_equal(myDisasm.instr.repr, 'rsqrtps xmm2, xmmword ptr [rbx]')

        # VEX.128.0F.WIG 52 /r
        # VRSQRTPS xmm1, xmm2/m128

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}52e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vrsqrtps ')
        assert_equal(myDisasm.instr.repr, 'vrsqrtps xmm12, xmm8')

        # VEX.256.0F.WIG 52 /r
        # VRSQRTPS ymm1, ymm2/m256

        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}52e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vrsqrtps ')
        assert_equal(myDisasm.instr.repr, 'vrsqrtps ymm12, ymm8')

        # F3 0F 52 /r
        # RSQRTSS xmm1, xmm2/m32

        Buffer = 'f30f5213'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf52')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rsqrtss ')
        assert_equal(myDisasm.instr.repr, 'rsqrtss xmm2, dword ptr [rbx]')

        # VEX.NDS.LIG.F3.0F.WIG 52 /r
        # VRSQRTSS xmm1, xmm2, xmm3/m32

        myVEX = VEX('VEX.NDS.LIG.F3.0F.WIG')
        Buffer = '{}5230'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x52)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vrsqrtss ')
        assert_equal(myDisasm.instr.repr, 'vrsqrtss xmm6, xmm15, dword ptr [r8]')
