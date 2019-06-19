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

        # 66 0F 38 F6 /r
        # ADCX r32, r/m32

        Buffer = '660f38f627'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'adcx esp, dword ptr [rdi]')

        # 66 REX.w 0F 38 F6 /r
        # ADCX r64, r/m64

        myREX = REX()
        myREX.W = 1

        Buffer = '66{:02x}0f38f627'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'adcx rsp, qword ptr [rdi]')

        # if LOCK, #UD

        Buffer = 'f0660f38f627'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'adcx ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)

        # F3 0F 38 F6 /r
        # ADCX r32, r/m32

        Buffer = 'f30f38f627'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'adox esp, dword ptr [rdi]')

        # F3 REX.w 0F 38 F6 /r
        # ADCX r64, r/m64

        myREX = REX()
        myREX.W = 1

        Buffer = 'f3{:02x}0f38f627'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'adox rsp, qword ptr [rdi]')

        # if LOCK, #UD

        Buffer = 'f0f30f38f627'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'adox ')
        assert_equal(myDisasm.instr.Reserved_.ERROR_OPCODE, UD_)
