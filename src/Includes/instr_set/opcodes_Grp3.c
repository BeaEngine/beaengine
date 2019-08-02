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
 *      0f6h
 * ==================================================================== */
void __bea_callspec__ G3_Eb(PDISASM pMyDisasm)
{
    if (!Security(1, pMyDisasm)) return;
    GV.REGOPCODE = ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 3) & 0x7;
    if (GV.REGOPCODE == 0) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+BIT_UInt8;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "test ");
        #endif
        EbIb(pMyDisasm);
        (*pMyDisasm).Operand1.AccessMode = READ;
        FillFlags(pMyDisasm, 104);
    }
    else if (GV.REGOPCODE == 1) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+BIT_UInt8;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "test ");
        #endif
        EbIb(pMyDisasm);
        (*pMyDisasm).Operand1.AccessMode = READ;
        FillFlags(pMyDisasm, 104);
    }
    else if (GV.REGOPCODE == 2) {
        if ((*pMyDisasm).Prefix.LockPrefix == InvalidPrefix) {
            (*pMyDisasm).Prefix.LockPrefix = InUsePrefix;
        }
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+LOGICAL_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "not ");
        #endif
        Eb(pMyDisasm);
        FillFlags(pMyDisasm, 73);
    }
    else if (GV.REGOPCODE == 3) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "neg ");
        #endif
        Eb(pMyDisasm);
        FillFlags(pMyDisasm, 71);
    }
    else if (GV.REGOPCODE == 4) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mul ");
        #endif
        GV.MemDecoration = Arg2byte;
        GV.OperandSize = 8;
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.OperandSize = 32;
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0+REG2;
        (*pMyDisasm).Operand1.OpSize = 8;
        (*pMyDisasm).Instruction.ImplicitModifiedRegs.type = GENERAL_REG; (*pMyDisasm).Instruction.ImplicitModifiedRegs.gpr = REG0;
        FillFlags(pMyDisasm, 70);
    }
    else if (GV.REGOPCODE == 5) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "imul ");
        #endif
        GV.MemDecoration = Arg2byte;
        GV.OperandSize = 8;
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.OperandSize = 32;
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0+REG2;
        (*pMyDisasm).Operand1.OpSize = 8;
        FillFlags(pMyDisasm, 38);
    }
    else if (GV.REGOPCODE == 6) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "div ");
        #endif
        GV.MemDecoration = Arg2byte;
        GV.OperandSize = 8;
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.OperandSize = 32;
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0+REG2;
        (*pMyDisasm).Operand1.OpSize = 8;
        FillFlags(pMyDisasm, 31);
    }
    else if (GV.REGOPCODE == 7) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "idiv ");
        #endif
        GV.MemDecoration = Arg2byte;
        GV.OperandSize = 8;
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.OperandSize = 32;
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0+REG2;
        (*pMyDisasm).Operand1.OpSize = 8;
        (*pMyDisasm).Instruction.ImplicitModifiedRegs.type = GENERAL_REG; (*pMyDisasm).Instruction.ImplicitModifiedRegs.gpr = REG0;
        FillFlags(pMyDisasm, 37);
    }
}

/* ====================================================================
 *      0f7h
 * ==================================================================== */
void __bea_callspec__ G3_Ev(PDISASM pMyDisasm)
{
    if (!Security(1, pMyDisasm)) return;
    GV.REGOPCODE = ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 3) & 0x7;
    if (GV.REGOPCODE == 0) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+BIT_UInt8;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "test ");
        #endif
        EvIv(pMyDisasm);
        (*pMyDisasm).Operand1.AccessMode = READ;
        FillFlags(pMyDisasm, 104);
    }
    else if (GV.REGOPCODE == 1) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+BIT_UInt8;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "test ");
        #endif
        EvIv(pMyDisasm);
        (*pMyDisasm).Operand1.AccessMode = READ;
        FillFlags(pMyDisasm, 104);
    }
    else if (GV.REGOPCODE == 2) {
        if ((*pMyDisasm).Prefix.LockPrefix == InvalidPrefix) {
            (*pMyDisasm).Prefix.LockPrefix = InUsePrefix;
        }
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+LOGICAL_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "not ");
        #endif
        Ev(pMyDisasm);
        FillFlags(pMyDisasm, 73);
    }
    else if (GV.REGOPCODE == 3) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "neg ");
        #endif
        Ev(pMyDisasm);
        FillFlags(pMyDisasm, 71);
    }
    else if (GV.REGOPCODE == 4) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mul ");
        #endif
        if (GV.OperandSize == 64) {
            GV.MemDecoration = Arg2qword;
			(*pMyDisasm).Operand1.OpSize = 64;
        }
        else if (GV.OperandSize == 32) {
            GV.MemDecoration = Arg2dword;
			(*pMyDisasm).Operand1.OpSize = 32;
        }
        else {
            GV.MemDecoration = Arg2word;
			(*pMyDisasm).Operand1.OpSize = 16;
        }
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0;
        (*pMyDisasm).Instruction.ImplicitModifiedRegs.type = GENERAL_REG; (*pMyDisasm).Instruction.ImplicitModifiedRegs.gpr = REG0+REG2;
        FillFlags(pMyDisasm, 70);
    }
    else if (GV.REGOPCODE == 5) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "imul ");
        #endif
        if (GV.OperandSize == 64) {
            GV.MemDecoration = Arg2qword;
			(*pMyDisasm).Operand1.OpSize = 64;
        }
        else if (GV.OperandSize == 32) {
            GV.MemDecoration = Arg2dword;
			(*pMyDisasm).Operand1.OpSize = 32;
        }
        else {
            GV.MemDecoration = Arg2word;
			(*pMyDisasm).Operand1.OpSize = 16;
        }
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0;
        (*pMyDisasm).Instruction.ImplicitModifiedRegs.type = GENERAL_REG; (*pMyDisasm).Instruction.ImplicitModifiedRegs.gpr = REG0+REG2;
        FillFlags(pMyDisasm, 38);
    }
    else if (GV.REGOPCODE == 6) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "div ");
        #endif
        if (GV.OperandSize == 64) {
            GV.MemDecoration = Arg2qword;
			(*pMyDisasm).Operand1.OpSize = 64;
        }
        else if (GV.OperandSize == 32) {
            GV.MemDecoration = Arg2dword;
			(*pMyDisasm).Operand1.OpSize = 32;
        }
        else {
            GV.MemDecoration = Arg2word;
			(*pMyDisasm).Operand1.OpSize = 16;
        }
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0+REG2;
        (*pMyDisasm).Instruction.ImplicitModifiedRegs.type = GENERAL_REG; (*pMyDisasm).Instruction.ImplicitModifiedRegs.gpr = REG0+REG2;
        FillFlags(pMyDisasm, 31);
    }
    else if (GV.REGOPCODE == 7) {
        (*pMyDisasm).Instruction.Category = GENERAL_PURPOSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "idiv ");
        #endif
        if (GV.OperandSize == 64) {
            GV.MemDecoration = Arg2qword;
			(*pMyDisasm).Operand1.OpSize = 64;
        }
        else if (GV.OperandSize == 32) {
            GV.MemDecoration = Arg2dword;
			(*pMyDisasm).Operand1.OpSize = 32;
        }
        else {
            GV.MemDecoration = Arg2word;
			(*pMyDisasm).Operand1.OpSize = 16;
        }
        MOD_RM(&(*pMyDisasm).Operand2, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;
        (*pMyDisasm).Operand1.OpType = REGISTER_TYPE;(*pMyDisasm).Operand1.Registers.type = GENERAL_REG;
        (*pMyDisasm).Operand1.Registers.gpr = REG0+REG2;
        (*pMyDisasm).Instruction.ImplicitModifiedRegs.type = GENERAL_REG; (*pMyDisasm).Instruction.ImplicitModifiedRegs.gpr = REG0+REG2;
        FillFlags(pMyDisasm, 37);
    }
}
