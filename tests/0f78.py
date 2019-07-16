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

        # NP 0F 78
        # VMREAD r/m64, r64

        Buffer = '0f7820'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0xf78')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vmread ')
        assert_equal(myDisasm.instr.repr, 'vmread qword ptr [rax], rsp')

        # EVEX.128.0F.W0 78 /r
        # vcvttPS2UDQ xmm1 {k1}{z}, xmm2/m128/m32bcst

        myEVEX = EVEX('EVEX.128.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttps2udq ')
        assert_equal(myDisasm.instr.repr, 'vcvttps2udq xmm4, xmmword ptr [rax]')

        # EVEX.256.0F.W0 78 /r
        # vcvtttPS2UDQ ymm1 {k1}{z}, ymm2/m256/m32bcst

        myEVEX = EVEX('EVEX.256.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttps2udq ')
        assert_equal(myDisasm.instr.repr, 'vcvttps2udq ymm4, ymmword ptr [rax]')

        # EVEX.512.0F.W0 78 /r
        # vcvttPS2UDQ zmm1 {k1}{z}, zmm2/m512/m32bcst{er}

        myEVEX = EVEX('EVEX.512.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttps2udq ')
        assert_equal(myDisasm.instr.repr, 'vcvttps2udq zmm4, zmmword ptr [rax]')

        # EVEX.128.0F.W1 78 /r
        # vcvttPD2UDQ xmm1 {k1}{z}, xmm2/m128/m64bcst

        myEVEX = EVEX('EVEX.128.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttpd2udq ')
        assert_equal(myDisasm.instr.repr, 'vcvttpd2udq xmm4, xmmword ptr [rax]')

        # EVEX.256.0F.W1 78 /r
        # vcvttPD2UDQ xmm1 {k1}{z}, ymm2/m256/m64bcst

        myEVEX = EVEX('EVEX.256.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttpd2udq ')
        assert_equal(myDisasm.instr.repr, 'vcvttpd2udq ymm4, ymmword ptr [rax]')

        # EVEX.512.0F.W1 78 /r
        # vcvttPD2UDQ ymm1 {k1}{z}, zmm2/m512/m64bcst{er}

        myEVEX = EVEX('EVEX.512.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttpd2udq ')
        assert_equal(myDisasm.instr.repr, 'vcvttpd2udq zmm4, zmmword ptr [rax]')

        # EVEX.128.66.0F.W0 78 /r
        # vcvttPS2UQQ xmm1 {k1}{z}, xmm2/m64/m32bcst

        myEVEX = EVEX('EVEX.128.66.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttps2uqq ')
        assert_equal(myDisasm.instr.repr, 'vcvttps2uqq xmm4, qword ptr [rax]')

        # EVEX.256.66.0F.W0 78 /r
        # vcvttPS2UQQ ymm1 {k1}{z}, xmm2/m128/m32bcst

        myEVEX = EVEX('EVEX.256.66.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttps2uqq ')
        assert_equal(myDisasm.instr.repr, 'vcvttps2uqq ymm4, xmmword ptr [rax]')

        # EVEX.512.66.0F.W0 78 /r
        # vcvttPS2UQQ zmm1 {k1}{z}, ymm2/m256/m32bcst{er}

        myEVEX = EVEX('EVEX.512.66.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttps2uqq ')
        assert_equal(myDisasm.instr.repr, 'vcvttps2uqq zmm4, ymmword ptr [rax]')

        # EVEX.128.66.0F.W1 78 /r
        # vcvttPD2UQQ xmm1 {k1}{z}, xmm2/m128/m64bcst

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttpd2uqq ')
        assert_equal(myDisasm.instr.repr, 'vcvttpd2uqq xmm4, xmmword ptr [rax]')

        # EVEX.256.66.0F.W1 78 /r
        # vcvttPD2UQQ ymm1 {k1}{z}, ymm2/m256/m64bcst

        myEVEX = EVEX('EVEX.256.66.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttpd2uqq ')
        assert_equal(myDisasm.instr.repr, 'vcvttpd2uqq ymm4, ymmword ptr [rax]')

        # EVEX.512.66.0F.W1 78 /r
        # vcvttPD2UQQ zmm1 {k1}{z}, zmm2/m512/m64bcst{er}

        myEVEX = EVEX('EVEX.512.66.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttpd2uqq ')
        assert_equal(myDisasm.instr.repr, 'vcvttpd2uqq zmm4, zmmword ptr [rax]')

        # EVEX.LIG.F3.0F.W0 78 /r
        # vcvttSS2USI r32, xmm1/m32{er}

        myEVEX = EVEX('EVEX.LIG.F3.0F.W0')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttss2usi ')
        assert_equal(myDisasm.instr.repr, 'vcvttss2usi esp, dword ptr [rax]')

        myEVEX = EVEX('EVEX.LIG.F3.0F.W0')
        Buffer = '{}78c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttss2usi ')
        assert_equal(myDisasm.instr.repr, 'vcvttss2usi eax, xmm0')

        # EVEX.LIG.F3.0F.W1 78 /r
        # vcvttSS2USI r64, xmm1/m32{er}

        myEVEX = EVEX('EVEX.LIG.F3.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Reserved_.EVEX.W, 1)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttss2usi ')
        assert_equal(myDisasm.instr.repr, 'vcvttss2usi rsp, dword ptr [rax]')

        # EVEX.LIG.F2.0F.W0 78 /r
        # vcvttSD2USI r32, xmm1/m64{er}

        myEVEX = EVEX('EVEX.LIG.F3.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Reserved_.EVEX.W, 1)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttss2usi ')
        assert_equal(myDisasm.instr.repr, 'vcvttss2usi rsp, dword ptr [rax]')

        # EVEX.LIG.F2.0F.W1 78 /r
        # vcvttSD2USI r64, xmm1/m64{er}

        myEVEX = EVEX('EVEX.LIG.F2.0F.W1')
        Buffer = '{}7820'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Reserved_.EVEX.W, 1)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttsd2usi ')
        assert_equal(myDisasm.instr.repr, 'vcvttsd2usi rsp, qword ptr [rax]')

        myEVEX = EVEX('EVEX.LIG.F2.0F.W1')
        Buffer = '{}78c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x78)
        assert_equal(myDisasm.instr.Reserved_.EVEX.W, 1)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vcvttsd2usi ')
        assert_equal(myDisasm.instr.repr, 'vcvttsd2usi rax, xmm0')
