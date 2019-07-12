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


        # VEX.NDS.LZ.0F38.W0 F7 /r
        # BEXTR r32a, r/m32, r32b

        myVEX = VEX('VEX.NDS.LZ.0F38.W0')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'bextr ')
        assert_equal(myDisasm.instr.repr, 'bextr eax, dword ptr [r8], cl')

        # VEX.NDS.LZ.0F38.W1 F7 /r
        # BEXTR r64a, r/m64, r64b

        myVEX = VEX('VEX.NDS.LZ.0F38.W1')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'bextr ')
        assert_equal(myDisasm.instr.repr, 'bextr rax, qword ptr [r8], cl')

        # VEX.NDS.LZ.F3.0F38.W0 F7 /r
        # SARX r32a, r/m32, r32b

        myVEX = VEX('VEX.NDS.LZ.F3.0F38.W0')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'sarx ')
        assert_equal(myDisasm.instr.repr, 'sarx eax, dword ptr [r8], cl')

        # VEX.NDS.LZ.66.0F38.W0 F7 /r
        # SHLX r32a, r/m32, r32b

        myVEX = VEX('VEX.NDS.LZ.66.0F38.W0')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'shlx ')
        assert_equal(myDisasm.instr.repr, 'shlx ax, dword ptr [r8], cl')

        # VEX.NDS.LZ.F2.0F38.W0 F7 /r
        # SHRX r32a, r/m32, r32b

        myVEX = VEX('VEX.NDS.LZ.F2.0F38.W0')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'shrx ')
        assert_equal(myDisasm.instr.repr, 'shrx eax, dword ptr [r8], cl')

        # VEX.NDS.LZ.F3.0F38.W1 F7 /r
        # SARX r64a, r/m64, r64b

        myVEX = VEX('VEX.NDS.LZ.F3.0F38.W1')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'sarx ')
        assert_equal(myDisasm.instr.repr, 'sarx rax, qword ptr [r8], cl')

        # VEX.NDS.LZ.66.0F38.W1 F7 /r
        # SHLX r64a, r/m64, r64b

        myVEX = VEX('VEX.NDS.LZ.66.0F38.W1')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'shlx ')
        assert_equal(myDisasm.instr.repr, 'shlx rax, qword ptr [r8], cl')

        # VEX.NDS.LZ.F2.0F38.W1 F7 /r
        # SHRX r64a, r/m64, r64b

        myVEX = VEX('VEX.NDS.LZ.F2.0F38.W1')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f700'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf7)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'shrx ')
        assert_equal(myDisasm.instr.repr, 'shrx rax, qword ptr [r8], cl')

        # 0F 38 F6
        # WRSSD

        Buffer = '0f38f627'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'wrssd ')
        assert_equal(myDisasm.instr.repr, 'wrssd dword ptr [rdi], esp')

        # REX.W 0F 38 F6
        # WRSSQ

        myREX = REX()
        myREX.W = 1
        Buffer = '{:02x}0f38f627'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'wrssq ')
        assert_equal(myDisasm.instr.repr, 'wrssq qword ptr [rdi], rsp')

        # VEX.NDD.LZ.F2.0F38.W0 F6 /r
        # MULX r32a, r32b, r/m32

        myVEX = VEX('VEX.NDS.LZ.F2.0F38.W0')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f600'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf6)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'mulx ')
        assert_equal(myDisasm.instr.repr, 'mulx eax, ecx, dword ptr [r8]')

        # VEX.NDD.LZ.F2.0F38.W1 F6 /r
        # MULX r64a, r64b, r/m64

        myVEX = VEX('VEX.NDS.LZ.F2.0F38.W1')
        myVEX.vvvv = 0b1110
        myVEX.R = 1
        myVEX.L = 0
        Buffer = '{}f600'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0xf6)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'mulx ')
        assert_equal(myDisasm.instr.repr, 'mulx rax, rcx, qword ptr [r8]')

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
