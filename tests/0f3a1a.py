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

        # EVEX.512.66.0F3A.W0 1A /r ib
        # VINSERTF32X8 zmm1 {k1}{z}, zmm2, ymm3/m256, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}1a2011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertf32x8 ')
        assert_equal(myDisasm.infos.repr, 'vinsertf32x8 zmm4, zmm0, ymmword ptr [rax], 11h')

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}1ac011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertf32x8 ')
        assert_equal(myDisasm.infos.repr, 'vinsertf32x8 zmm0, zmm0, ymm0, 11h')

        # EVEX.512.66.0F3A.W1 1A /r ib
        # VINSERTF64X4 zmm1 {k1}{z}, zmm2, ymm3/m256, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}1a2011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertf64x4 ')
        assert_equal(myDisasm.infos.repr, 'vinsertf64x4 zmm4, zmm0, ymmword ptr [rax], 11h')

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}1ac011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x1a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vinsertf64x4 ')
        assert_equal(myDisasm.infos.repr, 'vinsertf64x4 zmm0, zmm0, ymm0, 11h')
