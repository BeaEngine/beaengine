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


        # EVEX.128.66.0F3A.W0 1E /r ib
        # VPCMPUD k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequd ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequd k4, xmm0, xmmword ptr [rax], 10h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpltud ')
        assert_equal(myDisasm.infos.repr, 'vpcmpltud k4, xmm0, xmmword ptr [rax], 11h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2012'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpleud ')
        assert_equal(myDisasm.infos.repr, 'vpcmpleud k4, xmm0, xmmword ptr [rax], 12h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2013'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpfalseud ')
        assert_equal(myDisasm.infos.repr, 'vpcmpfalseud k4, xmm0, xmmword ptr [rax], 13h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2014'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpnequd ')
        assert_equal(myDisasm.infos.repr, 'vpcmpnequd k4, xmm0, xmmword ptr [rax], 14h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2015'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpnltud ')
        assert_equal(myDisasm.infos.repr, 'vpcmpnltud k4, xmm0, xmmword ptr [rax], 15h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2016'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpnleud ')
        assert_equal(myDisasm.infos.repr, 'vpcmpnleud k4, xmm0, xmmword ptr [rax], 16h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}1e2017'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmptrueud ')
        assert_equal(myDisasm.infos.repr, 'vpcmptrueud k4, xmm0, xmmword ptr [rax], 17h')

        # EVEX.256.66.0F3A.W0 1E /r ib
        # VPCMPUD k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W0')
        Buffer = '{}1e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequd ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequd k4, ymm0, ymmword ptr [rax], 10h')

        # EVEX.512.66.0F3A.W0 1E /r ib
        # VPCMPUD k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}1e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequd ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequd k4, zmm0, zmmword ptr [rax], 10h')



        # EVEX.128.66.0F3A.W1 1E /r ib
        # VPCMPUQ k1 {k2}, xmm2, xmm3/m128/m64bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W1')
        Buffer = '{}1e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequq ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequq k4, xmm0, xmmword ptr [rax], 10h')

        # EVEX.256.66.0F3A.W1 1E /r ib
        # VPCMPUQ k1 {k2}, ymm2, ymm3/m256/m64bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W1')
        Buffer = '{}1e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequq ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequq k4, ymm0, ymmword ptr [rax], 10h')

        # EVEX.512.66.0F3A.W1 1E /r ib
        # VPCMPUQ k1 {k2}, zmm2, zmm3/m512/m64bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}1e2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1e)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcmpequq ')
        assert_equal(myDisasm.infos.repr, 'vpcmpequq k4, zmm0, zmmword ptr [rax], 10h')
