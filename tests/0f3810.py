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
    """
    Variable Blend Packed Bytes
    """

    def test(self):

        # 66 0F 38 10 /r
        # PBLENDVB xmm1, xmm2/m128, <XMM0>

        Buffer = '660f381027'.decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'pblendvb xmm4, xmmword ptr [rdi], xmm0')

        #EVEX.NDS.128.66.0F38.W1 10 /r
        #VPSRLVW xmm1 {k1}{z}, xmm2,xmm3/m128
        myEVEX = EVEX('EVEX.NDS.128.66.0F38.W1')
        Buffer = '{}1027'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpsrlvw xmm4, xmm15, xmmword ptr [rdi]')


        #EVEX.NDS.256.66.0F38.W1 10 /r
        #VPSRLVW ymm1 {k1}{z}, ymm2,ymm3/m256
        myEVEX = EVEX('EVEX.NDS.256.66.0F38.W1')
        Buffer = '{}1027'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpsrlvw ymm4, ymm15, ymmword ptr [rdi]')

        #EVEX.NDS.512.66.0F38.W1 10 /r
        #VPSRLVW zmm1 {k1}{z}, zmm2,zmm3/m512
        myEVEX = EVEX('EVEX.NDS.512.66.0F38.W1')
        Buffer = '{}1027'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpsrlvw zmm4, zmm15, zmmword ptr [rdi]')

        #EVEX.128.F3.0F38.W0 10 /r
        #VPMOVUSWB xmm1/m64 {k1}{z},xmm2
        myEVEX = EVEX('EVEX.128.F3.0F38.W0')
        Buffer = '{}1027'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpmovuswb qword ptr [rdi], xmm4')


        #EVEX.256.F3.0F38.W0 10 /r
        #VPMOVUSWB xmm1/m128 {k1}{z},ymm2
        myEVEX = EVEX('EVEX.256.F3.0F38.W0')
        Buffer = '{}10e0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpmovuswb xmm0, ymm4')


        #EVEX.512.F3.0F38.W0 10 /r
        #VPMOVUSWB ymm1/m256 {k1}{z},zmm2
        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}1027'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpmovuswb xmmword ptr [rdi], zmm4')

        #EVEX.512.F3.0F38.W0 10 /r
        #VPMOVUSWB ymm1/m256 {k1}{z},zmm2
        myEVEX = EVEX('EVEX.512.F3.0F38.W0')
        Buffer = '{}10e0'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.repr, 'vpmovuswb ymm0, zmm4')
