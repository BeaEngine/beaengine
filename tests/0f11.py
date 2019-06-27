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

        # F2 0F 11 /r
        # MOVSD xmm1, xmm2

        Buffer = 'f20f11e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movsd ')
        assert_equal(myDisasm.instr.repr, 'movsd xmm0, xmm4')

        # F2 0F 11 /r
        # MOVSD m64, xmm1
        Buffer = 'f20f1190'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movsd ')
        assert_equal(myDisasm.instr.repr, 'movsd qword ptr [rax+00000000h], xmm2')

        # VEX.NDS.LIG.F2.0F.WIG 11 /r
        # VMOVSD xmm1, xmm2, xmm3

        myVEX = VEX('VEX.NDS.LIG.F2.0F.WIG')
        Buffer = '{}11e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.instr.repr, 'vmovsd xmm8, xmm15, xmm12')

        # VEX.LIG.F2.0F.WIG 11 /r
        # VMOVSD m64, xmm1

        myVEX = VEX('VEX.LIG.F2.0F.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}1190'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Reserved_.VEX.vvvv, 0xF)
        assert_equal(myDisasm.instr.Reserved_.VEX.pp, 0x3)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.instr.repr, 'vmovsd qword ptr [r8+00000000h], xmm10')

        # EVEX.NDS.LIG.F2.0F.W1 11 /r
        # VMOVSD xmm3, xmm2, xmm1 {k1}{z}

        myEVEX = EVEX('EVEX.NDS.LIG.F2.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.instr.repr, 'vmovsd xmmword ptr [rax+00000000h], xmm15, xmm2')

        # EVEX.LIG.F2.0F.W1 11 /r
        # VMOVSD m64, xmm1 {k1}{z}

        myEVEX = EVEX('EVEX.LIG.F2.0F.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.instr.Reserved_.EVEX.vvvv, 0xF)
        assert_equal(myDisasm.instr.Reserved_.VEX.vvvv, 0xF)
        assert_equal(myDisasm.instr.Reserved_.VEX.pp, 0x3)
        assert_equal(myDisasm.instr.repr, 'vmovsd qword ptr [rax+00000000h], xmm2')

        # F3 0F 11 /r
        # MOVSS xmm1, xmm2

        Buffer = 'f30f11e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movss ')
        assert_equal(myDisasm.instr.repr, 'movss xmm0, xmm4')

        # F3 0F 11 /r
        # MOVSS m32, xmm1

        Buffer = 'f30f1190'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movss ')
        assert_equal(myDisasm.instr.repr, 'movss dword ptr [rax+00000000h], xmm2')

        # VEX.NDS.LIG.F3.0F.WIG 11 /r
        # VMOVSS xmm1, xmm2, xmm3

        myVEX = VEX('VEX.NDS.LIG.F3.0F.WIG')
        Buffer = '{}11e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.instr.repr, 'vmovss xmm8, xmm15, xmm12')

        # VEX.LIG.F3.0F.WIG 11 /r
        # VMOVSS m32, xmm1

        myVEX = VEX('VEX.LIG.F3.0F.WIG')
        Buffer = '{}1190'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.instr.repr, 'vmovss dword ptr [r8+00000000h], xmm10')

        # EVEX.NDS.LIG.F3.0F.W0 11 /r
        # VMOVSS xmm3, xmm2, xmm1 {k1}{z}

        myEVEX = EVEX('EVEX.NDS.LIG.F3.0F.W1')
        Buffer = '{}11e0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.instr.repr, 'vmovss xmm0, xmm15, xmm4')

        # EVEX.LIG.F3.0F.W0 11 /r
        # VMOVSS  m32, xmm1 {k1}{z}

        myEVEX = EVEX('EVEX.LIG.F3.0F.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.instr.repr, 'vmovss dword ptr [rax+00000000h], xmm2')

        # 66 0F 11 /r
        # MOVUPD xmm2/m128, xmm1

        Buffer = '660f1190'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movupd ')
        assert_equal(myDisasm.instr.repr, 'movupd xmmword ptr [rax+00000000h], xmm2')

        # VEX.128.66.0F.WIG 11 /r
        # VMOVUPD xmm2/m128, xmm1

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}1190'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.instr.repr, 'vmovupd xmmword ptr [r8+00000000h], xmm10')

        # VEX.256.66.0F.WIG 11 /r
        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}1190'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.instr.repr, 'vmovupd ymmword ptr [r8+00000000h], ymm10')

        # EVEX.128.66.0F.W1 11 /r
        # VMOVUPD xmm2/m128, xmm1 {k1}{z}

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.instr.repr, 'vmovupd xmmword ptr [rax+00000000h], xmm2')

        # EVEX.256.66.0F.W1 11 /r
        # VMOVUPD ymm2/m256, ymm1 {k1}{z}

        myEVEX = EVEX('EVEX.256.66.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.instr.repr, 'vmovupd ymmword ptr [rax+00000000h], ymm2')

        # EVEX.512.66.0F.W1 11 /r
        # VMOVUPD zmm2/m512, zmm1 {k1}{z}

        myEVEX = EVEX('EVEX.512.66.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.instr.repr, 'vmovupd zmmword ptr [rax+00000000h], zmm2')


        # 0F 11 /r
        # MOVUPS xmm2/m128, xmm1

        Buffer = '0f1190'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'movups ')
        assert_equal(myDisasm.instr.repr, 'movups xmmword ptr [rax+00000000h], xmm2')

        # VEX.128.0F.WIG 11 /r
        # VMOVUPD xmm2/m128, xmm1

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}1190'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.instr.repr, 'vmovups xmmword ptr [r8+00000000h], xmm10')

        # VEX.256.0F.WIG 11 /r
        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}1190'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.instr.repr, 'vmovups ymmword ptr [r8+00000000h], ymm10')

        # EVEX.128.0F.W1 11 /r
        # VMOVUPD xmm2/m128, xmm1 {k1}{z}

        myEVEX = EVEX('EVEX.128.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.instr.repr, 'vmovups xmmword ptr [rax+00000000h], xmm2')

        # EVEX.256.0F.W1 11 /r
        # VMOVUPD ymm2/m256, ymm1 {k1}{z}

        myEVEX = EVEX('EVEX.256.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.instr.repr, 'vmovups ymmword ptr [rax+00000000h], ymm2')

        # EVEX.512.0F.W1 11 /r
        # VMOVUPD zmm2/m512, zmm1 {k1}{z}

        myEVEX = EVEX('EVEX.512.0F.W1')
        Buffer = '{}1190'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x11')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.instr.repr, 'vmovups zmmword ptr [rax+00000000h], zmm2')
