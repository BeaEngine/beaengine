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

        # NP 0F 73 /6 ib
        # psllq mm1, imm8

        Buffer = '0f73f011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'psllq ')
        assert_equal(myDisasm.infos.repr, 'psllq mm0, 11h')

        # 66 0F 73 /6 ib
        # psllq xmm1, imm8

        Buffer = '660f73f011'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'psllq ')
        assert_equal(myDisasm.infos.repr, 'psllq xmm0, 11h')

        # VEX.NDD.128.66.0F.WIG 73 /6 ib
        # Vpsllq xmm1, xmm2, imm8

        myVEX = VEX('VEX.NDD.128.66.0F.WIG')
        myVEX.B = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}73f011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpsllq ')
        assert_equal(myDisasm.infos.repr, 'vpsllq xmm0, xmm0, 11h')

        # VEX.NDD.256.66.0F.WIG 73 /6 ib
        # Vpsllq ymm1, ymm2, imm8

        myVEX = VEX('VEX.NDD.256.66.0F.WIG')
        Buffer = '{}73f011'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpsllq ')
        assert_equal(myDisasm.infos.repr, 'vpsllq ymm15, ymm8, 11h')

        # EVEX.NDD.128.66.0F.WIG 73 /6 ib
        # Vpsllq xmm1 {k1}{z}, xmm2/m128, imm8

        myEVEX = EVEX('EVEX.NDD.128.66.0F.WIG')
        Buffer = '{}733211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpsllq ')
        assert_equal(myDisasm.infos.repr, 'vpsllq xmm15, xmmword ptr [rdx], 11h')

        # EVEX.NDD.256.66.0F.WIG 73 /6 ib
        # Vpsllq ymm1 {k1}{z}, ymm2/m256, imm8

        myEVEX = EVEX('EVEX.NDD.256.66.0F.WIG')
        Buffer = '{}733211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpsllq ')
        assert_equal(myDisasm.infos.repr, 'vpsllq ymm15, ymmword ptr [rdx], 11h')

        # EVEX.NDD.512.66.0F.WIG 73 /6 ib
        # Vpsllq zmm1 {k1}{z}, zmm2/m512, imm8

        myEVEX = EVEX('EVEX.NDD.512.66.0F.WIG')
        Buffer = '{}733211'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpsllq ')
        assert_equal(myDisasm.infos.repr, 'vpsllq zmm15, zmmword ptr [rdx], 11h')

        # VEX.NDD.128.66.0F.WIG 73 /6 ib
        # Vpslldq xmm1, xmm2, imm8

        myVEX = VEX('VEX.NDD.128.66.0F.WIG')
        myVEX.B = 1
        myVEX.vvvv = 0b1111
        Buffer = '{}73f811'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpslldq ')
        assert_equal(myDisasm.infos.repr, 'vpslldq xmm0, xmm0, 11h')

        # VEX.NDD.256.66.0F.WIG 73 /6 ib
        # Vpslldq ymm1, ymm2, imm8

        myVEX = VEX('VEX.NDD.256.66.0F.WIG')
        Buffer = '{}73f811'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpslldq ')
        assert_equal(myDisasm.infos.repr, 'vpslldq ymm15, ymm8, 11h')

        # EVEX.NDD.128.66.0F.WIG 73 /6 ib
        # Vpslldq xmm1 {k1}{z}, xmm2/m128, imm8

        myEVEX = EVEX('EVEX.NDD.128.66.0F.WIG')
        Buffer = '{}733a11'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpslldq ')
        assert_equal(myDisasm.infos.repr, 'vpslldq xmm15, xmmword ptr [rdx], 11h')

        # EVEX.NDD.256.66.0F.WIG 73 /6 ib
        # Vpslldq ymm1 {k1}{z}, ymm2/m256, imm8

        myEVEX = EVEX('EVEX.NDD.256.66.0F.WIG')
        Buffer = '{}733a11'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpslldq ')
        assert_equal(myDisasm.infos.repr, 'vpslldq ymm15, ymmword ptr [rdx], 11h')

        # EVEX.NDD.512.66.0F.WIG 73 /6 ib
        # Vpslldq zmm1 {k1}{z}, zmm2/m512, imm8

        myEVEX = EVEX('EVEX.NDD.512.66.0F.WIG')
        Buffer = '{}733a11'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x73)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpslldq ')
        assert_equal(myDisasm.infos.repr, 'vpslldq zmm15, zmmword ptr [rdx], 11h')
