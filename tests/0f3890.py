
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


        # EVEX.128.66.0F38.W0 90 /vsib
        # VPGATHERDD xmm1 {k1}, vm32x

        myEVEX = EVEX('EVEX.128.66.0F38.W0')
        Buffer = '{}90443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdd ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdd xmm0, dword ptr [rbx+xmm14+22h]')

        # EVEX.256.66.0F38.W0 90 /vsib
        # VPGATHERDD ymm1 {k1}, vm32y

        myEVEX = EVEX('EVEX.256.66.0F38.W0')
        Buffer = '{}90443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdd ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdd ymm0, dword ptr [rbx+ymm14+22h]')

        # EVEX.512.66.0F38.W0 90 /vsib
        # VPGATHERDD zmm1 {k1}, vm32z

        myEVEX = EVEX('EVEX.512.66.0F38.W0')
        Buffer = '{}90443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdd ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdd zmm0, dword ptr [rbx+zmm14+22h]')

        # EVEX.128.66.0F38.W1 90 /vsib
        # VPGATHERDQ xmm1 {k1}, vm32x

        myEVEX = EVEX('EVEX.128.66.0F38.W1')
        Buffer = '{}90443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdq ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdq xmm0, dword ptr [rbx+xmm14+22h]')

        # EVEX.256.66.0F38.W1 90 /vsib
        # VPGATHERDQ ymm1 {k1}, vm32x

        myEVEX = EVEX('EVEX.256.66.0F38.W1')
        Buffer = '{}90443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdq ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdq ymm0, dword ptr [rbx+ymm14+22h]')

        # EVEX.512.66.0F38.W1 90 /vsib
        # VPGATHERDQ zmm1 {k1}, vm32y

        myEVEX = EVEX('EVEX.512.66.0F38.W1')
        Buffer = '{}90443322'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdq ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdq zmm0, dword ptr [rbx+zmm14+22h]')

        # VEX.DDS.128.66.0F38.W0 90 /r
        # VPGATHERDD xmm1, vm32x, xmm2

        myVEX = VEX('VEX.DDS.128.66.0F38.W0')
        Buffer = '{}90443322'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdd ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdd xmm8, dword ptr [r11+xmm14+22h], xmm15')

        # VEX.DDS.256.66.0F38.W0 90 /r
        # VPGATHERDD ymm1, vm32y, ymm2

        myVEX = VEX('VEX.DDS.256.66.0F38.W0')
        Buffer = '{}90443322'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpgatherdd ')
        assert_equal(myDisasm.instr.repr, 'vpgatherdd ymm8, dword ptr [r11+ymm14+22h], ymm15')
