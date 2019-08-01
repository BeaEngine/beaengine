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


        # 66 0F E6 /r
        # CVTTPD2DQ xmm1, xmm2/m128

        Buffer = '660fe620'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xfe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttpd2dq ')
        assert_equal(myDisasm.infos.repr, 'cvttpd2dq xmm4, xmmword ptr [rax]')

        # VEX.128.66.0F.WIG E6 /r
        # VCVTTPD2DQ xmm1, xmm2/m128

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}e610'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvttpd2dq xmm10, xmmword ptr [r8]')

        # VEX.256.66.0F.WIG E6 /r
        # VCVTTPD2DQ xmm1, ymm2/m256

        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}e610'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvttpd2dq xmm10, ymmword ptr [r8]')

        # EVEX.128.66.0F.W1 E6 /r
        # VCVTTPD2DQ xmm1 {k1}{z}, xmm2/m128/m64bcst

        myEVEX = EVEX('EVEX.128.66.0F.W1')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvttpd2dq xmm2, xmmword ptr [rax]')

        # EVEX.256.66.0F.W1 E6 /r
        # VCVTTPD2DQ xmm1 {k1}{z}, ymm2/m256/m64bcst

        myEVEX = EVEX('EVEX.256.66.0F.W1')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvttpd2dq xmm2, ymmword ptr [rax]')

        # EVEX.512.66.0F.W1 E6 /r
        # VCVTTPD2DQ ymm1 {k1}{z}, zmm2/m512/m64bcst{sae}

        myEVEX = EVEX('EVEX.512.66.0F.W1')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvttpd2dq ymm2, zmmword ptr [rax]')


        # F2 0F E6 /r
        # CVTPD2DQ xmm1, xmm2/m128

        Buffer = 'f20fe620'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xfe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvtpd2dq ')
        assert_equal(myDisasm.infos.repr, 'cvtpd2dq xmm4, xmmword ptr [rax]')

        # VEX.128.F2.0F.WIG E6 /r
        # VCVTPD2DQ xmm1, xmm2/m128

        myVEX = VEX('VEX.128.F2.0F.WIG')
        Buffer = '{}e610'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvtpd2dq xmm10, xmmword ptr [r8]')

        # VEX.256.F2.0F.WIG E6 /r
        # VCVTPD2DQ xmm1, ymm2/m256

        myVEX = VEX('VEX.256.F2.0F.WIG')
        Buffer = '{}e610'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvtpd2dq xmm10, ymmword ptr [r8]')

        # EVEX.128.F2.0F.W1 E6 /r
        # VCVTPD2DQ xmm1 {k1}{z}, xmm2/m128/m64bcst

        myEVEX = EVEX('EVEX.128.F2.0F.W1')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvtpd2dq xmm2, xmmword ptr [rax]')

        # EVEX.256.F2.0F.W1 E6 /r
        # VCVTPD2DQ xmm1 {k1}{z}, ymm2/m256/m64bcst

        myEVEX = EVEX('EVEX.256.F2.0F.W1')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvtpd2dq xmm2, ymmword ptr [rax]')

        # EVEX.512.F2.0F.W1 E6 /r
        # VCVTPD2DQ ymm1 {k1}{z}, zmm2/m512/m64bcst{er}

        myEVEX = EVEX('EVEX.512.F2.0F.W1')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtpd2dq ')
        assert_equal(myDisasm.infos.repr, 'vcvtpd2dq ymm2, zmmword ptr [rax]')

        # F3 0F E6 /r
        # CVTDQ2PD xmm1, xmm2/m64

        Buffer = 'f30fe620'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xfe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvtdq2pd ')
        assert_equal(myDisasm.infos.repr, 'cvtdq2pd xmm4, xmmword ptr [rax]')

        # VEX.128.F3.0F.WIG E6 /r
        # VCVTDQ2PD xmm1, xmm2/m64

        myVEX = VEX('VEX.128.F3.0F.WIG')
        Buffer = '{}e610'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtdq2pd ')
        assert_equal(myDisasm.infos.repr, 'vcvtdq2pd xmm10, qword ptr [r8]')

        # VEX.256.F3.0F.WIG E6 /r
        # VCVTDQ2PD ymm1, xmm2/m128

        myVEX = VEX('VEX.256.F3.0F.WIG')
        Buffer = '{}e610'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtdq2pd ')
        assert_equal(myDisasm.infos.repr, 'vcvtdq2pd ymm10, xmmword ptr [r8]')

        # EVEX.128.F3.0F.W0 E6 /r
        # VCVTDQ2PD xmm1 {k1}{z}, xmm2/m128/m32bcst

        myEVEX = EVEX('EVEX.128.F3.0F.W0')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtdq2pd ')
        assert_equal(myDisasm.infos.repr, 'vcvtdq2pd xmm2, xmmword ptr [rax]')

        # EVEX.256.F3.0F.W0 E6 /r
        # VCVTDQ2PD ymm1 {k1}{z}, xmm2/m128/m32bcst

        myEVEX = EVEX('EVEX.256.F3.0F.W0')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtdq2pd ')
        assert_equal(myDisasm.infos.repr, 'vcvtdq2pd ymm2, xmmword ptr [rax]')

        # EVEX.512.F3.0F.W0 E6 /r
        # VCVTDQ2PD zmm1 {k1}{z}, ymm2/m256/m32bcst

        myEVEX = EVEX('EVEX.512.F3.0F.W0')
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtdq2pd ')
        assert_equal(myDisasm.infos.repr, 'vcvtdq2pd zmm2, ymmword ptr [rax]')

        myEVEX = EVEX('EVEX.512.F3.0F.W0')
        myEVEX.vvvv = 0b1110
        Buffer = '{}e610'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xe6)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvtdq2pd ')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
