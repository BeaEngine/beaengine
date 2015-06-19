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
import struct

class TestOpcode1Byte:

    def test_SimpleInstructions(self):
        Instruction = DISASM()
        Buffer = struct.pack('<B', 0x90) 
        Target = create_string_buffer(Buffer,len(Buffer))
        Instruction.EIP = addressof(Target)
        InstrLength = Disasm(addressof(Instruction))
        assert_equal(Instruction.CompleteInstr, "nop ")



