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

        # 66 0F 38 2A /r
        # MOVNTDQA xmm1, m128

        Buffer = '660f382a20'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf382a')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movntdqa ')
        assert_equal(myDisasm.infos.repr, 'movntdqa xmm4, xmmword ptr [rax]')

        # VEX.128.66.0F38.WIG 2A /r
        # VMOVNTDQA xmm1, m128

        myVEX = VEX('VEX.128.66.0F38.WIG')
        Buffer = '{}2a20'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovntdqa ')
        assert_equal(myDisasm.infos.repr, 'vmovntdqa xmm12, xmmword ptr [r8]')

        # VEX.256.66.0F38.WIG 2A /r
        # VMOVNTDQA ymm1, m256

        myVEX = VEX('VEX.256.66.0F38.WIG')
        Buffer = '{}2a20'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovntdqa ')
        assert_equal(myDisasm.infos.repr, 'vmovntdqa ymm12, ymmword ptr [r8]')

        # EVEX.128.66.0F38.W0 2A /r
        # VMOVNTDQA xmm1, m128

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}2a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovntdqa ')
        assert_equal(myDisasm.infos.repr, 'vmovntdqa xmm4, xmmword ptr [rax]')

        # EVEX.256.66.0F38.W0 2A /r
        # VMOVNTDQA ymm1, m256

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}2a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovntdqa ')
        assert_equal(myDisasm.infos.repr, 'vmovntdqa ymm4, ymmword ptr [rax]')

        # EVEX.512.66.0F38.W0 2A /r
        # VMOVNTDQA zmm1, m512

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}2a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovntdqa ')
        assert_equal(myDisasm.infos.repr, 'vmovntdqa zmm4, zmmword ptr [rax]')

        # EVEX.128.F3.0F38.W1 2A /r
        # VPBROADCASTMB2Q xmm1, k1

        myEVEX = EVEX('EVEX.128.F3.0F38.W1')
        Buffer = '{}2ac0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpbroadcastmb2q ')
        assert_equal(myDisasm.infos.repr, 'vpbroadcastmb2q xmm0, k0')


        # EVEX.256.F3.0F38.W1 2A /r
        # VPBROADCASTMB2Q ymm1, k1

        myEVEX = EVEX('EVEX.256.F3.0F38.W1')
        Buffer = '{}2ac0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpbroadcastmb2q ')
        assert_equal(myDisasm.infos.repr, 'vpbroadcastmb2q ymm0, k0')

        # EVEX.512.F3.0F38.W1 2A /r
        # VPBROADCASTMB2Q zmm1, k1

        myEVEX = EVEX('EVEX.512.F3.0F38.W1')
        Buffer = '{}2ac0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpbroadcastmb2q ')
        assert_equal(myDisasm.infos.repr, 'vpbroadcastmb2q zmm0, k0')
