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


        # EVEX.128.66.0F3A.W0 3e /r ib
        # VPCMPub k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequb ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequb k?, xmm16, xmmword ptr [r8], 10h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpltub ')
        assert_equal(myDisasm.infos.repr, 'vpcmpltub k?, xmm16, xmmword ptr [r8], 11h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2012'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpleub ')
        assert_equal(myDisasm.infos.repr, 'vpcmpleub k?, xmm16, xmmword ptr [r8], 12h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2013'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpfalseub ')
        assert_equal(myDisasm.infos.repr, 'vpcmpfalseub k?, xmm16, xmmword ptr [r8], 13h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2014'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpnequb ')
        assert_equal(myDisasm.infos.repr, 'vpcmpnequb k?, xmm16, xmmword ptr [r8], 14h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2015'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpnltub ')
        assert_equal(myDisasm.infos.repr, 'vpcmpnltub k?, xmm16, xmmword ptr [r8], 15h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2016'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpnleub ')
        assert_equal(myDisasm.infos.repr, 'vpcmpnleub k?, xmm16, xmmword ptr [r8], 16h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3e2017'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmptrueub ')
        assert_equal(myDisasm.infos.repr, 'vpcmptrueub k?, xmm16, xmmword ptr [r8], 17h')

        # EVEX.256.66.0F3A.W0 3e /r ib
        # VPCMPub k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W0')
        Buffer = '{}3e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequb ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequb k?, ymm16, ymmword ptr [r8], 10h')

        # EVEX.512.66.0F3A.W0 3e /r ib
        # VPCMPub k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}3e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequb ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequb k?, zmm16, zmmword ptr [r8], 10h')



        # EVEX.128.66.0F3A.W1 3e /r ib
        # VPCMPuw k1 {k2}, xmm2, xmm3/m128/m64bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W1')
        Buffer = '{}3e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequw ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequw k?, xmm16, xmmword ptr [r8], 10h')

        # EVEX.256.66.0F3A.W1 3e /r ib
        # VPCMPuw k1 {k2}, ymm2, ymm3/m256/m64bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W1')
        Buffer = '{}3e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequw ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequw k?, ymm16, ymmword ptr [r8], 10h')

        # EVEX.512.66.0F3A.W1 3e /r ib
        # VPCMPuw k1 {k2}, zmm2, zmm3/m512/m64bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}3e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequw ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequw k?, zmm16, zmmword ptr [r8], 10h')
