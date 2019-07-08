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



        # NP 0F E7 /r
        # MOVNTQ m64, mm

        Buffer = '0fe720'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movntq ')
        assert_equal(myDisasm.instr.repr, 'movntq qword ptr [rax], mm4')

        # 66 0F E7 /r
        # MOVNTDQ m128, xmm1

        Buffer = '660fe720'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xfe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movntdq ')
        assert_equal(myDisasm.instr.repr, 'movntdq xmmword ptr [rax], xmm4')

        # VEX.128.66.0F.WIG E7 /r
        # VMOVNTDQ m128, xmm1

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}e710'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovntdq ')
        assert_equal(myDisasm.instr.repr, 'vmovntdq xmmword ptr [r8], xmm10')

        # VEX.256.66.0F.WIG E7 /r
        # VMOVNTDQ m256, ymm1

        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}e710'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovntdq ')
        assert_equal(myDisasm.instr.repr, 'vmovntdq ymmword ptr [r8], ymm10')

        # EVEX.128.66.0F.W0 E7 /r
        # VMOVNTDQ m128, xmm1

        myEVEX = EVEX('EVEX.128.66.0F.W0')
        Buffer = '{}e710'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovntdq ')
        assert_equal(myDisasm.instr.repr, 'vmovntdq xmmword ptr [rax], xmm2')

        # EVEX.256.66.0F.W0 E7 /r
        # VMOVNTDQ m256, ymm1

        myEVEX = EVEX('EVEX.256.66.0F.W0')
        Buffer = '{}e710'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovntdq ')
        assert_equal(myDisasm.instr.repr, 'vmovntdq ymmword ptr [rax], ymm2')

        # EVEX.512.66.0F.W0 E7 /r
        # VMOVNTDQ m512, zmm1

        myEVEX = EVEX('EVEX.512.66.0F.W0')
        Buffer = '{}e710'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xe7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovntdq ')
        assert_equal(myDisasm.instr.repr, 'vmovntdq zmmword ptr [rax], zmm2')
