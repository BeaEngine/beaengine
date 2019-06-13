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
import yaml

class TestSuite:
    """
    https://github.com/BeaEngine/beaengine/issues/3
    """
    def test(self):

        Buffer = '0fef08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pxor ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fef08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pxor ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0f6208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckldq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660f6208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckldq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0f6108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpcklwd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660f6108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpcklwd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0f6008'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpcklbw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660f6008'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpcklbw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0f6a08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckhdq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660f6a08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckhdq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0f6908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckhwd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660f6908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckhwd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0f6808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckhbw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660f6808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'punpckhbw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fd908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubusw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fd908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubusw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fd808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubusb ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fd808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubusb ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fe908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubsw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fe908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubsw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fe808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubsb ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fe808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubsb ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ffa08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ffa08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ff908'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubb ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ff808'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubb ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fe208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrad ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fe208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrad ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fe108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psraw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fe108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psraw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fd308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrlq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fd308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrlq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fd208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrld ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fd208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrld ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fd108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrlw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fd108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psrlw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psllq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ff308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psllq ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pslld ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ff208'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pslld ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psllw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ff108'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psllw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0feb08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'por ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660fe508'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmulhw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fe508'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmulhw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff508'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmaddwd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '660ff508'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'pmaddwd ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fa308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'bt ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fab08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'bts ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fb308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'btr ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fa308'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'bt ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fbb08'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'btc ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0fc708'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'cmpxchg8b ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)

        Buffer = '0ff911'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'psubw ')
        assert_equal(myDisasm.instr.Argument1.AccessMode, WRITE)
