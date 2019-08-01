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

        # EVEX.128.66.0F38.W0 63 /r
        # VPCOMPRESSB m128{k1}, xmm1

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}630e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressb ')
        assert_equal(myDisasm.infos.repr, 'vpcompressb xmmword ptr [rsi], xmm1')

        # EVEX.128.66.0F38.W0 63 /r
        # VPCOMPRESSB xmm1{k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}63c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressb ')
        assert_equal(myDisasm.infos.repr, 'vpcompressb xmm0, xmm0')

        # EVEX.256.66.0F38.W0 63 /r
        # VPCOMPRESSB m256{k1}, ymm1

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}630e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressb ')
        assert_equal(myDisasm.infos.repr, 'vpcompressb ymmword ptr [rsi], ymm1')

        # EVEX.256.66.0F38.W0 63 /r
        # VPCOMPRESSB ymm1{k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}63c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressb ')
        assert_equal(myDisasm.infos.repr, 'vpcompressb ymm0, ymm0')

        # EVEX.512.66.0F38.W0 63 /r
        # VPCOMPRESSB m512{k1}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}630e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressb ')
        assert_equal(myDisasm.infos.repr, 'vpcompressb zmmword ptr [rsi], zmm1')

        # EVEX.512.66.0F38.W0 63 /r
        # VPCOMPRESSB zmm1{k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        myEVEX.vvvv = 0b1111
        Buffer = '{}63c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressb ')
        assert_equal(myDisasm.infos.repr, 'vpcompressb zmm0, zmm0')

        # EVEX.128.66.0F38.W1 63 /r
        # VPCOMPRESSW m128{k1}, xmm1

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}630e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressw ')
        assert_equal(myDisasm.infos.repr, 'vpcompressw xmmword ptr [rsi], xmm1')

        # EVEX.128.66.0F38.W1 63 /r
        # VPCOMPRESSW xmm1{k1}{z}, xmm2

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}63c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressw ')
        assert_equal(myDisasm.infos.repr, 'vpcompressw xmm0, xmm0')

        # EVEX.256.66.0F38.W1 63 /r
        # VPCOMPRESSW m256{k1}, ymm1

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}630e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressw ')
        assert_equal(myDisasm.infos.repr, 'vpcompressw ymmword ptr [rsi], ymm1')

        # EVEX.256.66.0F38.W1 63 /r
        # VPCOMPRESSW ymm1{k1}{z}, ymm2

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}63c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressw ')
        assert_equal(myDisasm.infos.repr, 'vpcompressw ymm0, ymm0')

        # EVEX.512.66.0F38.W1 63 /r
        # VPCOMPRESSW m512{k1}, zmm1

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}630e'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressw ')
        assert_equal(myDisasm.infos.repr, 'vpcompressw zmmword ptr [rsi], zmm1')

        # EVEX.512.66.0F38.W1 63 /r
        # VPCOMPRESSW zmm1{k1}{z}, zmm2

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        myEVEX.vvvv = 0b1111
        Buffer = '{}63c0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x63)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vpcompressw ')
        assert_equal(myDisasm.infos.repr, 'vpcompressw zmm0, zmm0')
