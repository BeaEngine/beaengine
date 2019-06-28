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

void __bea_callspec__ emms_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    FailDecode(pMyDisasm);
    return;
  }  
	(*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+STATE_MANAGEMENT;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "emms ");
    #endif
	GV.EIP_++;
}

/* ====================================================================
 *      0x 0f 7e
 * ==================================================================== */
void __bea_callspec__ movd_EP(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+DATA_TRANSFER;
    /* ========= 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
        #endif
        GV.Register_ = SSE_REG;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.Register_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg1qword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = SSE_REG;
            Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg1dword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movd ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = SSE_REG;
            Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    else {
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg1qword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = MMX_REG;
            Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg1dword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movd ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = MMX_REG;
            Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
}


/* ====================================================================
 *      0x 0f 6e
 * ==================================================================== */
void __bea_callspec__ movd_PE(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+DATA_TRANSFER;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2qword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = SSE_REG;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2dword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movd ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = SSE_REG;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    else {
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2qword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = MMX_REG;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2dword;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movd ");
            #endif
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.Register_ = MMX_REG;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.Register_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
}



/* ====================================================================
 *      0x 0f 6f
 * ==================================================================== */
void __bea_callspec__ movq_PQ(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+DATA_TRANSFER;
    /* ========= 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dqword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movdqu ");
        #endif
        GV.Register_ = SSE_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movdqa ");
        #endif
        GV.Register_ = SSE_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
    else {
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
        #endif
        GV.Register_ = MMX_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 7f
 * ==================================================================== */
void __bea_callspec__ movq_QP(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+DATA_TRANSFER;
    /* ========= 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg1_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movdqu ");
        #endif
        GV.Register_ = SSE_REG;
        ExGx(pMyDisasm);
        GV.Register_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movdqa ");
        #endif
        GV.Register_ = SSE_REG;
        ExGx(pMyDisasm);
        GV.Register_ = 0;
    }
    else {
        GV.MemDecoration = Arg1qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
        #endif
        GV.Register_ = MMX_REG;
        ExGx(pMyDisasm);
        GV.Register_ = 0;
    }
}

/* ====================================================================
 *      0x 0f d6
 * ==================================================================== */
void __bea_callspec__ movq_WV(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+DATA_TRANSFER;
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dqword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movdq2q ");
        #endif
        GV.Register_ = MMX_REG;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.Register_ = 0;
        GV.Register_ = SSE_REG;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.Register_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;

    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq2dq ");
        #endif
        GV.Register_ = SSE_REG;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.Register_ = 0;
        GV.Register_ = MMX_REG;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.Register_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movq ");
        #endif
        GV.Register_ = SSE_REG;
        ExGx(pMyDisasm);
        GV.Register_ = 0;
    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 38 1c
 * ==================================================================== */
void __bea_callspec__ pabsb_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pabsb ");
        #endif
        GV.Register_ = SSE_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
    else {
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pabsb ");
        #endif
        GV.Register_ = MMX_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 38 1e
 * ==================================================================== */
void __bea_callspec__ pabsd_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pabsd ");
        #endif
        GV.Register_ = SSE_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
    else {
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pabsd ");
        #endif
        GV.Register_ = MMX_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 38 1d
 * ==================================================================== */
void __bea_callspec__ pabsw_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = MMX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pabsw ");
        #endif
        GV.Register_ = SSE_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
    else {
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pabsw ");
        #endif
        GV.Register_ = MMX_REG;
        GxEx(pMyDisasm);
        GV.Register_ = 0;
    }
}
