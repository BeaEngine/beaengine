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

        # F2 0F 10 /r
        # MOVSD xmm1, xmm2

        Buffer = 'f20f10e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movsd ')
        assert_equal(myDisasm.infos.repr, 'movsd xmm4, xmm0')

        # F2 0F 10 /r
        # MOVSD xmm1, m64
        Buffer = 'f20f1090'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movsd ')
        assert_equal(myDisasm.infos.repr, 'movsd xmm2, qword ptr [rax+00000000h]')

        # VEX.NDS.LIG.F2.0F.WIG 10 /r
        # VMOVSD xmm1, xmm2, xmm3

        myVEX = VEX('VEX.NDS.LIG.F2.0F.WIG')
        Buffer = '{}10e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.infos.repr, 'vmovsd xmm12, xmm15, xmm8')

        # VEX.LIG.F2.0F.WIG 10 /r
        # VMOVSD xmm1, m64

        myVEX = VEX('VEX.LIG.F2.0F.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}1090'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Reserved_.VEX.vvvv, 0xF)
        assert_equal(myDisasm.infos.Reserved_.VEX.pp, 0x3)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.infos.repr, 'vmovsd xmm10, qword ptr [r8+00000000h]')

        # EVEX.NDS.LIG.F2.0F.W1 10 /r
        # VMOVSD xmm1 {k1}{z}, xmm2, xmm3

        myEVEX = EVEX('EVEX.NDS.LIG.F2.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.infos.repr, 'vmovsd xmm26, xmm31, xmmword ptr [r8+00000000h]')

        # EVEX.LIG.F2.0F.W1 10 /r
        # VMOVSD xmm1 {k1}{z}, m64

        myEVEX = EVEX('EVEX.LIG.F2.0F.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovsd ')
        assert_equal(myDisasm.infos.Reserved_.EVEX.vvvv, 0xF)
        assert_equal(myDisasm.infos.Reserved_.VEX.vvvv, 0xF)
        assert_equal(myDisasm.infos.Reserved_.VEX.pp, 0x3)
        assert_equal(myDisasm.infos.repr, 'vmovsd xmm26, qword ptr [r8+00000000h]')

        # F3 0F 10 /r
        # MOVSS xmm1, xmm2

        Buffer = 'f30f10e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movss ')
        assert_equal(myDisasm.infos.repr, 'movss xmm4, xmm0')

        # F3 0F 10 /r
        # MOVSS xmm1, m32

        Buffer = 'f30f1090'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movss ')
        assert_equal(myDisasm.infos.repr, 'movss xmm2, dword ptr [rax+00000000h]')

        # VEX.NDS.LIG.F3.0F.WIG 10 /r
        # VMOVSS xmm1, xmm2, xmm3

        myVEX = VEX('VEX.NDS.LIG.F3.0F.WIG')
        Buffer = '{}10e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.infos.repr, 'vmovss xmm12, xmm15, xmm8')

        # VEX.LIG.F3.0F.WIG 10 /r
        # VMOVSS xmm1, m32

        myVEX = VEX('VEX.LIG.F3.0F.WIG')
        Buffer = '{}1090'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.infos.repr, 'vmovss xmm10, dword ptr [r8+00000000h]')

        # EVEX.NDS.LIG.F3.0F.W0 10 /r
        # VMOVSS xmm1 {k1}{z}, xmm2, xmm3

        myEVEX = EVEX('EVEX.NDS.LIG.F3.0F.W1')
        Buffer = '{}10e0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.infos.repr, 'vmovss xmm28, xmm31, xmm24')

        # EVEX.LIG.F3.0F.W0 10 /r
        # VMOVSS xmm1 {k1}{z}, m32

        myEVEX = EVEX('EVEX.LIG.F3.0F.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovss ')
        assert_equal(myDisasm.infos.repr, 'vmovss xmm26, dword ptr [r8+00000000h]')

        # 66 0F 10 /r
        # MOVUPD xmm1, xmm2/m128

        Buffer = '660f1090'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movupd ')
        assert_equal(myDisasm.infos.repr, 'movupd xmm2, xmmword ptr [rax+00000000h]')

        # VEX.128.66.0F.WIG 10 /r
        # VMOVUPD xmm1, xmm2/m128

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}1090'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd xmm10, xmmword ptr [r8+00000000h]')

        # VEX.256.66.0F.WIG 10 /r
        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}1090'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd ymm10, ymmword ptr [r8+00000000h]')

        # EVEX.128.66.0F.W1 10 /r
        # VMOVUPD xmm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd xmm26, xmmword ptr [r8+00000000h]')


        myEVEX = EVEX('EVEX.128.66.0F.W1')
        myEVEX.aaa = 1
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Reserved_.EVEX.aaa, 1)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd xmm26 {k1}{0}, xmmword ptr [r8+00000000h]')

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        myEVEX.aaa = 1
        myEVEX.z = 1
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.infos.Options = ShowEVEXMasking
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Reserved_.EVEX.aaa, 1)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd xmm26 {k1}{1}, xmmword ptr [r8+00000000h]')

        # EVEX.256.66.0F.W1 10 /r
        # VMOVUPD ymm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.66.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd ymm26, ymmword ptr [r8+00000000h]')

        # EVEX.512.66.0F.W1 10 /r
        # VMOVUPD zmm1 {k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.66.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovupd ')
        assert_equal(myDisasm.infos.repr, 'vmovupd zmm26, zmmword ptr [r8+00000000h]')


        # 0F 10 /r
        # MOVUPS xmm1, xmm2/m128

        Buffer = '0f1090'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movups ')
        assert_equal(myDisasm.infos.repr, 'movups xmm2, xmmword ptr [rax+00000000h]')

        # VEX.128.0F.WIG 10 /r
        # VMOVUPD xmm1, xmm2/m128

        myVEX = VEX('VEX.128.0F.WIG')
        Buffer = '{}1090'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.infos.repr, 'vmovups xmm10, xmmword ptr [r8+00000000h]')

        # VEX.256.0F.WIG 10 /r
        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}1090'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.infos.repr, 'vmovups ymm10, ymmword ptr [r8+00000000h]')

        # EVEX.128.0F.W1 10 /r
        # VMOVUPD xmm1 {k1}{z}, xmm2/m128

        myEVEX = EVEX('EVEX.128.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.infos.repr, 'vmovups xmm26, xmmword ptr [r8+00000000h]')

        # EVEX.256.0F.W1 10 /r
        # VMOVUPD ymm1 {k1}{z}, ymm2/m256

        myEVEX = EVEX('EVEX.256.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.infos.repr, 'vmovups ymm26, ymmword ptr [r8+00000000h]')

        # EVEX.512.0F.W1 10 /r
        # VMOVUPD zmm1 {k1}{z}, zmm2/m512

        myEVEX = EVEX('EVEX.512.0F.W1')
        Buffer = '{}1090'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x10')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovups ')
        assert_equal(myDisasm.infos.repr, 'vmovups zmm26, zmmword ptr [r8+00000000h]')
