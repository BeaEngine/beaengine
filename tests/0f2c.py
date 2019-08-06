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

        # 66 0F 2C /r
        # CVTTPD2PI mm, xmm/m128

        Buffer = '660f2c20'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttpd2pi ')
        assert_equal(myDisasm.infos.repr, 'cvttpd2pi mm4, xmmword ptr [rax]')

        # NP 0F 2C /r
        # CVTTPS2PI mm, xmm/m64

        Buffer = '0f2c20'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttps2pi ')
        assert_equal(myDisasm.infos.repr, 'cvttps2pi mm4, qword ptr [rax]')

        # F2 0F 2C /r
        # CVTTSD2SI r32, xmm1/m64

        Buffer = 'f20f2c20'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'cvttsd2si esp, qword ptr [rax]')

        Buffer = 'f20f2ce0'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'cvttsd2si esp, xmm0')


        # F2 REX.W 0F 2C /r
        # CVTTSD2SI r64, xmm1/m64

        myREX = REX()
        myREX.W = 1
        Buffer = 'f2{:02x}0f2c20'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'cvttsd2si rsp, qword ptr [rax]')

        # VEX.LIG.F2.0F.W0 2C /r 1
        # VCVTTSD2SI r32, xmm1/m64

        myVEX = VEX('VEX.LIG.F2.0F.W0')
        Buffer = '{}2c10'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttsd2si r10d, qword ptr [r8]')

        # VEX.LIG.F2.0F.W1 2C /r 1
        # VCVTTSD2SI r64, xmm1/m64

        myVEX = VEX('VEX.LIG.F2.0F.W1')
        Buffer = '{}2c10'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttsd2si r10, qword ptr [r8]')

        # EVEX.LIG.F2.0F.W0 2C /r
        # VCVTTSD2SI r32, xmm1/m64{sae}

        myEVEX = EVEX('EVEX.LIG.F2.0F.W0')
        Buffer = '{}2c16'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttsd2si r10w, qword ptr [r14]')

        # EVEX.LIG.F2.0F.W1 2C /r
        # VCVTTSD2SI r64, xmm1/m64{sae}

        myEVEX = EVEX('EVEX.LIG.F2.0F.W1')
        Buffer = '{}2c16'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttsd2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttsd2si ebp, qword ptr [r14]')

        # F3 0F 2C /r
        # CVTTSS2SI r32, xmm1/m32

        Buffer = 'f30f2c20'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttss2si ')
        assert_equal(myDisasm.infos.repr, 'cvttss2si esp, dword ptr [rax]')

        # F3 REX.W 0F 2C /r
        # CVTTSS2SI r64, xmm1/m32

        myREX = REX()
        myREX.W = 1
        Buffer = 'f3{:02x}0f2c20'.format(myREX.byte()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0xf2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'cvttss2si ')
        assert_equal(myDisasm.infos.repr, 'cvttss2si rsp, dword ptr [rax]')

        # VEX.LIG.F3.0F.W0 2C /r 1
        # VCVTTSS2SI r32, xmm1/m32

        myVEX = VEX('VEX.LIG.F3.0F.W0')
        Buffer = '{}2c10'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttss2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttss2si r10d, dword ptr [r8]')

        # VEX.LIG.F3.0F.W1 2C /r 1
        # VCVTTSS2SI r64, xmm1/m32

        myVEX = VEX('VEX.LIG.F3.0F.W1')
        Buffer = '{}2c10'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttss2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttss2si r10, dword ptr [r8]')

        # EVEX.LIG.F3.0F.W0 2C /r
        # VCVTTSS2SI r32, xmm1/m32{sae}

        myEVEX = EVEX('EVEX.LIG.F3.0F.W0')
        Buffer = '{}2c16'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttss2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttss2si r10w, dword ptr [r14]')

        # EVEX.LIG.F3.0F.W1 2C /r
        # VCVTTSS2SI r64, xmm1/m32{sae}

        myEVEX = EVEX('EVEX.LIG.F3.0F.W1')
        Buffer = '{}2c16'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Instruction.Mnemonic, 'vcvttss2si ')
        assert_equal(myDisasm.infos.repr, 'vcvttss2si ebp, dword ptr [r14]')

        # VEX.vvvv and EVEX.vvvv are reserved and must be 1111b, otherwise instructions will #UD.

        myEVEX = EVEX('EVEX.LIG.F2.0F.W0')
        myEVEX.vvvv = 0b1000
        Buffer = '{}2c16'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)

        myVEX = VEX('VEX.LIG.F2.0F.W0')
        myVEX.vvvv = 0b1000
        Buffer = '{}2c16'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.infos.Instruction.Opcode, 0x2c)
        assert_equal(myDisasm.infos.Reserved_.ERROR_OPCODE, UD_)
