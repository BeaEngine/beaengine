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


class VEX:
    def __init__(self):
        self.reset()

    def reset(self):
        self.L = 0
        self.pp = 0
        self.mmmm = 0
        self.W = 0
        self.vvvv = 0
        self.R = 0
        self.X = 0
        self.B = 0

    def byte1(self):
        return self.mmmm + (self.B << 5) + (self.X << 6) + (self.R << 7)

    def byte2(self):
        return self.pp + (self.L << 2) + (self.vvvv << 3) + (self.W << 7)


class TestSuite:
    """
    Variable Blend Packed Bytes
    """

    def test(self):

        # VEX.128.66.0F3A.W0 4C /r /is4
        # VPBLENDVB xmm1, xmm2, xmm3/m128, xmm4

        myVEX = VEX()
        myVEX.L = 0
        myVEX.W = 0
        myVEX.pp = 0b1
        myVEX.mmmm = 0b11
        myVEX.vvvv = 0b0
        myVEX.R = 1
        myVEX.B = 1

        Buffer = 'c4{:02x}{:02x}4c2700'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpblendvb xmm4, xmm15, xmmword ptr [rdi], xmm0')

        # VEX.256.66.0F3A.W0 4C /r /is4
        # VPBLENDVB ymm1, ymm2, ymm3/m256, ymm4

        myVEX.reset()
        myVEX.L = 1
        myVEX.pp = 0b1
        myVEX.mmmm = 0b11
        myVEX.vvvv = 0b0
        myVEX.R = 1
        myVEX.B = 1

        Buffer = 'c4{:02x}{:02x}4c0e50'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpblendvb ymm1, ymm15, ymmword ptr [rsi], ymm5')


        # if VEX.W = 1 #UD

        myVEX.reset()
        myVEX.W = 1
        myVEX.L = 1
        myVEX.pp = 0b1
        myVEX.mmmm = 0b11

        Buffer = 'c4{:02x}{:02x}4c0000'.format(myVEX.byte1(), myVEX.byte2()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpblendvb ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
