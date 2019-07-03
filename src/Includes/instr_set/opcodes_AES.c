/* Copyright 2006-2009, BeatriX
 * File coded by BeatriX
 *
 * This file is part of BeaEngine.
 *
 *    BeaEngine is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU Lesser General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    BeaEngine is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU Lesser General Public License for more details.
 *
 *    You should have received a copy of the GNU Lesser General Public License
 *    along with BeaEngine.  If not, see <http://www.gnu.org/licenses/>. */

/* ====================================================================
 *      0x 0f 38 db
 * ==================================================================== */
void __bea_callspec__ aesimc(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaesimc ");
            #endif
            if (GV.VEX.vvvv != 15) {
              GV.ERROR_OPCODE = UD_;
            }
            GV.Register_ = SSE_REG;
            GV.MemDecoration = Arg2_m128i_xmm;
            GxEx(pMyDisasm);
        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128i_xmm;
            (*pMyDisasm).Instruction.Category = AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "aesimc ");
            #endif
            GV.Register_ = SSE_REG;
            GxEx(pMyDisasm);
            (*pMyDisasm).Argument2.ArgSize = 128;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 dc
 * ==================================================================== */
void __bea_callspec__ aesenc(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaesenc ");
            #endif
            if (GV.VEX.vvvv != 15) {
              GV.ERROR_OPCODE = UD_;
            }
            GV.Register_ = SSE_REG;
            GV.MemDecoration = Arg3_m128i_xmm;
            GyEy(pMyDisasm);
        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128i_xmm;
            (*pMyDisasm).Instruction.Category = AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "aesenc ");
            #endif
            GV.Register_ = SSE_REG;
            GxEx(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 dd
 * ==================================================================== */
void __bea_callspec__ aesenclast(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaesenclast ");
            #endif
            if (GV.VEX.vvvv != 15) {
              GV.ERROR_OPCODE = UD_;
            }
            GV.Register_ = SSE_REG;
            GV.MemDecoration = Arg3_m128i_xmm;
            GyEy(pMyDisasm);
        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128i_xmm;
            (*pMyDisasm).Instruction.Category = AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "aesenclast ");
            #endif
            GV.Register_ = SSE_REG;
            GxEx(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 de
 * ==================================================================== */
void __bea_callspec__ aesdec(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaesdec ");
            #endif
            if (GV.VEX.vvvv != 15) {
              GV.ERROR_OPCODE = UD_;
            }
            GV.Register_ = SSE_REG;
            GV.MemDecoration = Arg3_m128i_xmm;
            GyEy(pMyDisasm);
        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128i_xmm;
            (*pMyDisasm).Instruction.Category = AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "aesdec ");
            #endif
            GV.Register_ = SSE_REG;
            GxEx(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 df
 * ==================================================================== */
void __bea_callspec__ aesdeclast(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaesdeclast ");
            #endif
            if (GV.VEX.vvvv != 15) {
              GV.ERROR_OPCODE = UD_;
            }
            GV.Register_ = SSE_REG;
            GV.MemDecoration = Arg3_m128i_xmm;
            GyEy(pMyDisasm);
        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128i_xmm;
            (*pMyDisasm).Instruction.Category = AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "aesdeclast ");
            #endif
            GV.Register_ = SSE_REG;
            GxEx(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 3a df
 * ==================================================================== */
void __bea_callspec__ aeskeygen(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaeskeygenassist ");
            #endif

            GV.Register_ = SSE_REG;
            GV.MemDecoration = Arg2_m128i_xmm;
            GxEx(pMyDisasm);
            GV.ImmediatSize = 8;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
            #endif
            (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument3.ArgSize = 8;
        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128i_xmm;
            (*pMyDisasm).Instruction.Category = AES_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "aeskeygenassist ");
            #endif
            GV.ImmediatSize = 8;
            GV.Register_ = SSE_REG;
            GxEx(pMyDisasm);
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
            #endif
            (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument3.ArgSize = 8;
        }

    }
    else {
        FailDecode(pMyDisasm);
    }

}
