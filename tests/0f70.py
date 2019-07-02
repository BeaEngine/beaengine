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


        # NP 0F 70 /r ib
        # PSHUFW mm1, mm2/m64, imm8

        Buffer = '0f702011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufw ')
        assert_equal(myDisasm.instr.repr, 'pshufw mm4, qword ptr [rax], 11h')

        # F2 0F 70 /r ib
        # PSHUFLW xmm1, xmm2/m128, imm8

        Buffer = 'f20f702011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshuflw ')
        assert_equal(myDisasm.instr.repr, 'pshuflw xmm4, xmmword ptr [rax], 11h')

        # VEX.128.F2.0F.WIG 70 /r ib
        # VPSHUFLW xmm1, xmm2/m128, imm8

        myVEX = VEX('VEX.128.F2.0F.WIG')
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshuflw ')
        assert_equal(myDisasm.instr.repr, 'vpshuflw xmm12, xmmword ptr [r8], 11h')

        # VEX.256.F2.0F.WIG 70 /r ib
        # VPSHUFLW ymm1, ymm2/m256, imm8

        myVEX = VEX('VEX.256.F2.0F.WIG')
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshuflw ')
        assert_equal(myDisasm.instr.repr, 'vpshuflw ymm12, ymmword ptr [r8], 11h')

        # EVEX.128.F2.0F.WIG 70 /r ib
        # VPSHUFLW xmm1 {k1}{z}, xmm2/m128, imm8

        myEVEX = EVEX('EVEX.128.F2.0F.WIG')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshuflw ')
        assert_equal(myDisasm.instr.repr, 'vpshuflw xmm4, xmmword ptr [rax], 11h')

        # EVEX.256.F2.0F.WIG 70 /r ib
        # VPSHUFLW ymm1 {k1}{z}, ymm2/m256, imm8

        myEVEX = EVEX('EVEX.256.F2.0F.WIG')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshuflw ')
        assert_equal(myDisasm.instr.repr, 'vpshuflw ymm4, ymmword ptr [rax], 11h')

        # EVEX.512.F2.0F.WIG 70 /r ib
        # VPSHUFLW zmm1 {k1}{z}, zmm2/m512, imm8

        myEVEX = EVEX('EVEX.512.F2.0F.WIG')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshuflw ')
        assert_equal(myDisasm.instr.repr, 'vpshuflw zmm4, zmmword ptr [rax], 11h')

        # F3 0F 70 /r ib
        # PSHUFHW xmm1, xmm2/m128, imm8

        Buffer = 'f30f702011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufhw ')
        assert_equal(myDisasm.instr.repr, 'pshufhw xmm4, xmmword ptr [rax], 11h')

        # VEX.128.F3.0F.WIG 70 /r ib
        # VPSHUFHW xmm1, xmm2/m128, imm8

        myVEX = VEX('VEX.128.F3.0F.WIG')
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufhw ')
        assert_equal(myDisasm.instr.repr, 'vpshufhw xmm12, xmmword ptr [r8], 11h')

        # VEX.256.F3.0F.WIG 70 /r ib
        # VPSHUFHW ymm1, ymm2/m256, imm8

        myVEX = VEX('VEX.256.F3.0F.WIG')
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufhw ')
        assert_equal(myDisasm.instr.repr, 'vpshufhw ymm12, ymmword ptr [r8], 11h')

        # EVEX.128.F3.0F.WIG 70 /r ib
        # VPSHUFHW xmm1 {k1}{z}, xmm2/m128, imm8

        myEVEX = EVEX('EVEX.128.F3.0F.WIG')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufhw ')
        assert_equal(myDisasm.instr.repr, 'vpshufhw xmm4, xmmword ptr [rax], 11h')

        # EVEX.256.F3.0F.WIG 70 /r ib
        # VPSHUFHW ymm1 {k1}{z}, ymm2/m256, imm8

        myEVEX = EVEX('EVEX.256.F3.0F.WIG')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufhw ')
        assert_equal(myDisasm.instr.repr, 'vpshufhw ymm4, ymmword ptr [rax], 11h')

        # EVEX.512.F3.0F.WIG 70 /r ib
        # VPSHUFHW zmm1 {k1}{z}, zmm2/m512, imm8

        myEVEX = EVEX('EVEX.512.F3.0F.WIG')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufhw ')
        assert_equal(myDisasm.instr.repr, 'vpshufhw zmm4, zmmword ptr [rax], 11h')

        # 66 0F 70 /r ib
        # PSHUFD xmm1, xmm2/m128, imm8

        Buffer = '660f702011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pshufd ')
        assert_equal(myDisasm.instr.repr, 'pshufd xmm4, xmmword ptr [rax], 11h')

        # VEX.128.66.0F.WIG 70 /r ib
        # VPSHUFD xmm1, xmm2/m128, imm8

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.repr, 'vpshufd xmm12, xmmword ptr [r8], 11h')

        # VEX.256.66.0F.WIG 70 /r ib
        # VPSHUFD ymm1, ymm2/m256, imm8

        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.repr, 'vpshufd ymm12, ymmword ptr [r8], 11h')

        # EVEX.128.66.0F.W0 70 /r ib
        # VPSHUFD xmm1 {k1}{z}, xmm2/m128/m32bcst,imm8

        myEVEX = EVEX('EVEX.128.66.0F.W0')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.repr, 'vpshufd xmm4, xmmword ptr [rax], 11h')

        # EVEX.256.66.0F.W0 70 /r ib
        # VPSHUFD ymm1 {k1}{z}, ymm2/m256/m32bcst,imm8

        myEVEX = EVEX('EVEX.256.66.0F.W0')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.repr, 'vpshufd ymm4, ymmword ptr [rax], 11h')

        # EVEX.512.66.0F.W0 70 /r ib
        # VPSHUFD zmm1 {k1}{z}, zmm2/m512/m32bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F.W0')
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.repr, 'vpshufd zmm4, zmmword ptr [rax], 11h')

        # If VEX.vvvv ≠ 1111B or EVEX.vvvv ≠ 1111B , #UD

        myEVEX = EVEX('EVEX.512.66.0F.W0')
        myEVEX.vvvv = 0b1110
        Buffer = '{}702011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)

        myVEX = VEX('VEX.256.66.0F.WIG')
        myVEX.vvvv = 0b1110
        Buffer = '{}702011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x70)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpshufd ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
