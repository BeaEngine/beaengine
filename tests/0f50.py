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

        # NP 0F 50 /r
        # MOVMSKPS reg, xmm

        Buffer = '0f50e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf50')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movmskps ')
        assert_equal(myDisasm.infos.repr, 'movmskps rsp, xmm0')

        # VEX.128.0F.WIG 50 /r
        # VMOVMSKPS reg, xmm2

        myVEX = VEX('VEX.128.0F.WIG')
        myVEX.vvvv = 0b1111
        Buffer = '{}50e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x50')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovmskps ')
        assert_equal(myDisasm.infos.repr, 'vmovmskps r12, xmm8')

        # VEX.256.0F.WIG 50 /r
        # VMOVMSKPS reg, ymm2

        myVEX = VEX('VEX.256.0F.WIG')
        Buffer = '{}50e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x50')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovmskps ')
        assert_equal(myDisasm.infos.repr, 'vmovmskps r12, ymm8')

        # 66 0F 50 /r
        # MOVMSKPD reg, xmm

        Buffer = '660f50e0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0xf50')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'movmskpd ')
        assert_equal(myDisasm.infos.repr, 'movmskpd rsp, xmm0')

        # VEX.128.66.0F.WIG 50 /r
        # VMOVMSKPD reg, xmm2

        myVEX = VEX('VEX.128.66.0F.WIG')
        Buffer = '{}50e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x50')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovmskpd ')
        assert_equal(myDisasm.infos.repr, 'vmovmskpd r12, xmm8')

        # VEX.256.66.0F.WIG 50 /r
        # VMOVMSKPD reg, ymm2

        myVEX = VEX('VEX.256.66.0F.WIG')
        Buffer = '{}50e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x50')
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vmovmskpd ')
        assert_equal(myDisasm.infos.repr, 'vmovmskpd r12, ymm8')

        #UD If VEX.vvvv ≠ 1111B.

        myVEX = VEX('VEX.128.0F.WIG')
        myVEX.vvvv = 0b1000
        Buffer = '{}50e0'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.infos.Instruction.Opcode), '0x50')
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
