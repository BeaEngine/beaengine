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

        # F3 0F 53 /r
        # RCPSS xmm1, xmm2/m32

        Buffer = 'f30f5313'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf53)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rcpss ')
        assert_equal(myDisasm.instr.repr, 'rcpss xmm2, dword ptr [rbx]')

        # VEX.NDS.LIG.F3.0F.WIG 53 /r
        # VRCPSS xmm1, xmm2, xmm3/m32

        myVEX = VEX('VEX.NDS.LIG.F3.0F.WIG')
        Buffer = '{}53e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x53)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vrcpss ')
        assert_equal(myDisasm.instr.repr, 'vrcpss xmm12, xmm8')

        # NP 0F 53 /r
        # RCPPS xmm1, xmm2/m128

        Buffer = '0f5313'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf53)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'rcpps ')
        assert_equal(myDisasm.instr.repr, 'rcpps xmm2, xmmword ptr [rbx]')

        # VEX.128.0F.WIG 53 /r
        # VRCPPS xmm1, xmm2/m128

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}53e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x53)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vrcpps ')
        assert_equal(myDisasm.instr.repr, 'vrcpps xmm12, xmm8')

        # VEX.256.0F.WIG 53 /r
        # VRCPPS ymm1, ymm2/m256

        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}53e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x53)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vrcpps ')
        assert_equal(myDisasm.instr.repr, 'vrcpps ymm12, ymm8')
