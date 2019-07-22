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


        # EVEX.128.66.0F38.W0 62 /r
        # VPEXPANDB xmm1{k1}{z}, m128

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}620e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandb ')
        assert_equal(myDisasm.instr.repr, 'vpexpandb xmm1, xmmword ptr [rsi]')

        # EVEX.128.66.0F38.W0 62 /r
        # VPEXPANDB xmm1{k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}62c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandb ')
        assert_equal(myDisasm.instr.repr, 'vpexpandb xmm0, xmm0')

        # EVEX.256.66.0F38.W0 62 /r
        # VPEXPANDB ymm1{k1}{z}, m256

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}620e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandb ')
        assert_equal(myDisasm.instr.repr, 'vpexpandb ymm1, ymmword ptr [rsi]')

        # EVEX.256.66.0F38.W0 62 /r
        # VPEXPANDB ymm1{k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}62c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandb ')
        assert_equal(myDisasm.instr.repr, 'vpexpandb ymm0, ymm0')

        # EVEX.512.66.0F38.W0 62 /r
        # VPEXPANDB zmm1{k1}{z}, m512

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}620e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandb ')
        assert_equal(myDisasm.instr.repr, 'vpexpandb zmm1, zmmword ptr [rsi]')

        # EVEX.512.66.0F38.W0 62 /r
        # VPEXPANDB zmm1{k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}62c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandb ')
        assert_equal(myDisasm.instr.repr, 'vpexpandb zmm0, zmm0')

        # EVEX.128.66.0F38.W1 62 /r
        # VPEXPANDW xmm1{k1}{z}, m128

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}620e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandw ')
        assert_equal(myDisasm.instr.repr, 'vpexpandw xmm1, xmmword ptr [rsi]')

        # EVEX.128.66.0F38.W1 62 /r
        # VPEXPANDW xmm1{k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}62c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandw ')
        assert_equal(myDisasm.instr.repr, 'vpexpandw xmm0, xmm0')

        # EVEX.256.66.0F38.W1 62 /r
        # VPEXPANDW ymm1{k1}{z}, m256

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}620e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandw ')
        assert_equal(myDisasm.instr.repr, 'vpexpandw ymm1, ymmword ptr [rsi]')

        # EVEX.256.66.0F38.W1 62 /r
        # VPEXPANDW ymm1{k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}62c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandw ')
        assert_equal(myDisasm.instr.repr, 'vpexpandw ymm0, ymm0')

        # EVEX.512.66.0F38.W1 62 /r
        # VPEXPANDW zmm1{k1}{z}, m512

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}620e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandw ')
        assert_equal(myDisasm.instr.repr, 'vpexpandw zmm1, zmmword ptr [rsi]')

        # EVEX.512.66.0F38.W1 62 /r
        # VPEXPANDW zmm1{k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}62c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x62)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpexpandw ')
        assert_equal(myDisasm.instr.repr, 'vpexpandw zmm0, zmm0')
