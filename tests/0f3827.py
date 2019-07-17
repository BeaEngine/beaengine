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


        # EVEX.NDS.128.66.0F38.W0 27 /r
        # vptestmd k2 {k1}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.NDS.128.66.0F38.W0')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestmd ')
        assert_equal(myDisasm.instr.repr, 'vptestmd k4, xmm15, xmmword ptr [rax]')

        # EVEX.NDS.256.66.0F38.W0 27 /r
        # vptestmd k2 {k1}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.NDS.256.66.0F38.W0')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestmd ')
        assert_equal(myDisasm.instr.repr, 'vptestmd k4, ymm15, ymmword ptr [rax]')

        # EVEX.NDS.512.66.0F38.W0 27 /r
        # vptestmd k2 {k1}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.NDS.512.66.0F38.W0')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestmd ')
        assert_equal(myDisasm.instr.repr, 'vptestmd k4, zmm15, zmmword ptr [rax]')

        # EVEX.NDS.128.66.0F38.W1 27 /r
        # vptestmq k2 {k1}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.NDS.128.66.0F38.W1')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestmq ')
        assert_equal(myDisasm.instr.repr, 'vptestmq k4, xmm15, xmmword ptr [rax]')

        # EVEX.NDS.256.66.0F38.W1 27 /r
        # vptestmq k2 {k1}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.NDS.256.66.0F38.W1')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestmq ')
        assert_equal(myDisasm.instr.repr, 'vptestmq k4, ymm15, ymmword ptr [rax]')

        # EVEX.NDS.512.66.0F38.W1 27 /r
        # vptestmq k2 {k1}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.NDS.512.66.0F38.W1')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestmq ')
        assert_equal(myDisasm.instr.repr, 'vptestmq k4, zmm15, zmmword ptr [rax]')

        # EVEX.NDS.128.F3.0F38.W0 27 /r
        # vptestnmd k2 {k1}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.NDS.128.F3.0F38.W0')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestnmd ')
        assert_equal(myDisasm.instr.repr, 'vptestnmd k4, xmm15, xmmword ptr [rax]')

        # EVEX.NDS.256.F3.0F38.W0 27 /r
        # vptestnmd k2 {k1}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.NDS.256.F3.0F38.W0')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestnmd ')
        assert_equal(myDisasm.instr.repr, 'vptestnmd k4, ymm15, ymmword ptr [rax]')

        # EVEX.NDS.512.F3.0F38.W0 27 /r
        # vptestnmd k2 {k1}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.NDS.512.F3.0F38.W0')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestnmd ')
        assert_equal(myDisasm.instr.repr, 'vptestnmd k4, zmm15, zmmword ptr [rax]')

        # EVEX.NDS.128.F3.0F38.W1 27 /r
        # vptestnmq k2 {k1}, xmm2, xmm3/m128

        myEVEX = EVEX('EVEX.NDS.128.F3.0F38.W1')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestnmq ')
        assert_equal(myDisasm.instr.repr, 'vptestnmq k4, xmm15, xmmword ptr [rax]')

        # EVEX.NDS.256.F3.0F38.W1 27 /r
        # vptestnmq k2 {k1}, ymm2, ymm3/m256

        myEVEX = EVEX('EVEX.NDS.256.F3.0F38.W1')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestnmq ')
        assert_equal(myDisasm.instr.repr, 'vptestnmq k4, ymm15, ymmword ptr [rax]')

        # EVEX.NDS.512.F3.0F38.W1 27 /r
        # vptestnmq k2 {k1}, zmm2, zmm3/m512

        myEVEX = EVEX('EVEX.NDS.512.F3.0F38.W1')
        Buffer = '{}2720'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x27)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vptestnmq ')
        assert_equal(myDisasm.instr.repr, 'vptestnmq k4, zmm15, zmmword ptr [rax]')
