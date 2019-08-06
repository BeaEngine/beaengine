
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
        # 66 0F 38 3a /r
        # pminuw mm1, mm2/m64
        Buffer = '660f383a9011223344'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf383a')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'pminuw ')
        assert_equal(myDisasm.infos.repr, 'pminuw xmm2, xmmword ptr [rax+44332211h]')

        # VEX.NDS.128.66.0F38.WIG 3a /r
        # vpminuw xmm1, xmm2, xmm3/m128
        Buffer = 'c402013a0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminuw ')
        assert_equal(myDisasm.infos.repr, 'vpminuw xmm9, xmm15, xmmword ptr [r14]')

        # VEX.NDS.256.66.0F38.WIG 3a /r
        # vpminuw ymm1, ymm2, ymm3/m256
        Buffer = 'c402053a0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminuw ')
        assert_equal(myDisasm.infos.repr, 'vpminuw ymm9, ymm15, ymmword ptr [r14]')

        # EVEX.NDS.128.66.0F38.WIG 3a /r
        # vpminuw xmm1 {k1}{z}, xmm2, xmm3/m128
        Buffer = '620205063a0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x6)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x3a')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminuw ')
        assert_equal(myDisasm.infos.repr, 'vpminuw xmm25, xmm31, xmmword ptr [r14]')

        # EVEX.NDS.256.66.0F38.WIG 3a /r
        # vpminuw ymm1 {k1}{z}, ymm2, ymm3/m256
        Buffer = '620205203a0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x20)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x3a')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminuw ')
        assert_equal(myDisasm.infos.repr, 'vpminuw ymm25, ymm31, ymmword ptr [r14]')

        # EVEX.NDS.512.66.0F38.WIG 3a /r
        # vpminuw zmm1 {k1}{z}, zmm2, zmm3/m512
        Buffer = '620205403a0e'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Reserved_.EVEX.P0, 0x2)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P1, 0x5)
        assert_equal(myDisasm.infos.Reserved_.EVEX.P2, 0x40)
        assert_equal(myDisasm.infos.Reserved_.EVEX.pp, 0x1)
        assert_equal(myDisasm.infos.Reserved_.EVEX.mm, 0x2)
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x3a')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminuw ')
        assert_equal(myDisasm.infos.repr, 'vpminuw zmm25, zmm31, zmmword ptr [r14]')

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}3a20'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpminuw ')
        assert_equal(myDisasm.infos.repr, 'vpminuw zmm28, zmm16, zmmword ptr [r8]')

        # EVEX.128.F3.0F38.W1 3a /r
        # VPBROADCASTmw2d xmm1, k1

        myEVEX = EVEX('EVEX.128.F3.0F38.W1')
        Buffer = '{}3ac0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpbroadcastmw2d ')
        assert_equal(myDisasm.infos.repr, 'vpbroadcastmw2d xmm24, k0')


        # EVEX.256.F3.0F38.W1 3a /r
        # VPBROADCASTmw2d ymm1, k1

        myEVEX = EVEX('EVEX.256.F3.0F38.W1')
        Buffer = '{}3ac0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpbroadcastmw2d ')
        assert_equal(myDisasm.infos.repr, 'vpbroadcastmw2d ymm24, k0')

        # EVEX.512.F3.0F38.W1 3a /r
        # VPBROADCASTmw2d zmm1, k1

        myEVEX = EVEX('EVEX.512.F3.0F38.W1')
        Buffer = '{}3ac0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x3a)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpbroadcastmw2d ')
        assert_equal(myDisasm.infos.repr, 'vpbroadcastmw2d zmm24, k0')
