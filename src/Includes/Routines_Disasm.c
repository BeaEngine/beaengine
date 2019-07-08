/* Copyright 2006-2019, BeatriX
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
 *
 * ==================================================================== */
int __bea_callspec__ Disasm (PDISASM pMyDisasm) {

  if (InitVariables(pMyDisasm)) {
    (void) AnalyzeOpcode(pMyDisasm);
    if (!GV.OutOfBlock) {
      FixArgSizeForMemoryOperand(pMyDisasm);
      FixREXPrefixes(pMyDisasm);
      FillSegmentsRegisters(pMyDisasm);
      CompleteInstructionFields(pMyDisasm);
      #ifndef BEA_LIGHT_DISASSEMBLY
      BuildCompleteInstruction(pMyDisasm);
      #endif
      if (GV.ERROR_OPCODE == UNKNOWN_OPCODE) {
        return -1;
      }
      else {
        return (int) (GV.EIP_-(*pMyDisasm).EIP);
      }
    }
    else {
      return 0;
    }
  }
  else {
    return -1;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ CompleteInstructionFields (PDISASM pMyDisasm) {

  if (((*pMyDisasm).Instruction.BranchType == JmpType) || ((*pMyDisasm).Instruction.BranchType == CallType)) {
    (*pMyDisasm).Argument1.AccessMode = READ;
  }
  if ((*pMyDisasm).Prefix.LockPrefix == InvalidPrefix) {
    GV.ERROR_OPCODE = UD_;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ FailDecode(PDISASM pMyDisasm)
{
	#ifndef BEA_LIGHT_DISASSEMBLY
   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "??? ");
  #endif
	GV.ERROR_OPCODE = UNKNOWN_OPCODE;
}

/* ====================================================================
 *
 * ==================================================================== */
int __bea_callspec__ InitVariables (PDISASM pMyDisasm) {
  (void) memset (&GV, 0, sizeof (InternalDatas));
  GV.EIP_ = (*pMyDisasm).EIP;
  GV.EIP_REAL = GV.EIP_;
  GV.EIP_VA = (*pMyDisasm).VirtualAddr;
  GV.EndOfBlock = GV.EIP_ + 15;
  if ((*pMyDisasm).SecurityBlock != 0) GV.EndOfBlock = GV.EIP_ + (*pMyDisasm).SecurityBlock;
  GV.OperandSize = 32;
  GV.OriginalOperandSize = 32;
  GV.AddressSize = 32;
  GV.Register_ = 0;
  GV.Architecture = (*pMyDisasm).Archi;
  if (GV.Architecture == 0) {
    GV.Architecture = 64;
  }
  (*pMyDisasm).Prefix.Number = 0;
  if (GV.Architecture == 64) {
    GV.AddressSize = 64;
  }
  if (GV.Architecture == 16) {
    GV.OperandSize = 16;
    GV.OriginalOperandSize = 16;
    GV.AddressSize = 16;
  }
  (void) memset (&(*pMyDisasm).Argument1, 0, sizeof (ARGTYPE));
  (void) memset (&(*pMyDisasm).Argument2, 0, sizeof (ARGTYPE));
  (void) memset (&(*pMyDisasm).Argument3, 0, sizeof (ARGTYPE));
  (void) memset (&(*pMyDisasm).Argument4, 0, sizeof (ARGTYPE));
  (void) memset (&(*pMyDisasm).Prefix, 0, sizeof (PREFIXINFO));
  (*pMyDisasm).Argument1.AccessMode = WRITE;
  (*pMyDisasm).Argument1.ArgPosition = LowPosition;
  (*pMyDisasm).Argument2.ArgPosition = LowPosition;
  (*pMyDisasm).Argument3.ArgPosition = LowPosition;
  (*pMyDisasm).Argument4.ArgPosition = LowPosition;
  (*pMyDisasm).Argument1.ArgType = NO_ARGUMENT;
  (*pMyDisasm).Argument2.ArgType = NO_ARGUMENT;
  (*pMyDisasm).Argument3.ArgType = NO_ARGUMENT;
  (*pMyDisasm).Argument4.ArgType = NO_ARGUMENT;
  (*pMyDisasm).Argument2.AccessMode = READ;
  (*pMyDisasm).Argument3.AccessMode = READ;
  (*pMyDisasm).Argument4.AccessMode = READ;
  (void) memset (&(*pMyDisasm).Instruction, 0, sizeof (INSTRTYPE));
  GV.TAB_ = (UInt32)(*pMyDisasm).Options & 0xff;
  GV.SYNTAX_ = (UInt32)(*pMyDisasm).Options & 0xff00;
  GV.FORMATNUMBER = (UInt32)(*pMyDisasm).Options & 0xff0000;
  GV.SEGMENTREGS = (UInt32)(*pMyDisasm).Options & 0xff000000;
  GV.OutOfBlock = 0;
  return 1;
}
/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ FixArgSizeForMemoryOperand (PDISASM pMyDisasm) {

  if ((GV.MemDecoration > 0) && (GV.MemDecoration < 99))
  {
    (*pMyDisasm).Argument1.ArgSize = ArgsSize[GV.MemDecoration - 1];
  }
  else if ((GV.MemDecoration > 100) && (GV.MemDecoration < 199))
  {
    (*pMyDisasm).Argument2.ArgSize = ArgsSize[GV.MemDecoration - 101];
  }
  else if ((GV.MemDecoration > 200) && (GV.MemDecoration < 299))
  {
    (*pMyDisasm).Argument3.ArgSize = ArgsSize[GV.MemDecoration - 201];
  }
  else if ((GV.MemDecoration > 300) && (GV.MemDecoration < 399))
  {
    (*pMyDisasm).Argument4.ArgSize = ArgsSize[GV.MemDecoration - 301];
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ FixREXPrefixes (PDISASM pMyDisasm) {

  (*pMyDisasm).Prefix.REX.W_ = GV.REX.W_;
  (*pMyDisasm).Prefix.REX.R_ = GV.REX.R_;
  (*pMyDisasm).Prefix.REX.X_ = GV.REX.X_;
  (*pMyDisasm).Prefix.REX.B_ = GV.REX.B_;
  (*pMyDisasm).Prefix.REX.state = GV.REX.state;
}

/* ====================================================================
 *
 * ==================================================================== */
int __bea_callspec__ AnalyzeOpcode (PDISASM pMyDisasm) {

  (*pMyDisasm).Instruction.Opcode = *((UInt8*) (UIntPtr)(GV.EIP_));
  (void) opcode_map1[*((UInt8*) (UIntPtr)GV.EIP_)](pMyDisasm);
  return 1;
}
/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ EbGb(PDISASM pMyDisasm)
{
  GV.MemDecoration = Arg1byte;
  GV.OperandSize = 8;
  ExGx(pMyDisasm);
  GV.OperandSize = 32;
  if (
      (GV.MOD_ == 3) &&
      ((*pMyDisasm).Prefix.LockPrefix == InUsePrefix)
    ) {
    GV.ERROR_OPCODE = UD_;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ GbEb(PDISASM pMyDisasm)
{
  GV.MemDecoration = Arg2byte;
  GV.OperandSize = 8;
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
  GV.OperandSize = 32;
  GV.EIP_ += GV.DECALAGE_EIP+2;
}
/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ EvGv(PDISASM pMyDisasm)
{
  if (GV.OperandSize == 64) {
    GV.MemDecoration = Arg1qword;
  }
  else if (GV.OperandSize == 32) {
    GV.MemDecoration = Arg1dword;
  }
  else {
    GV.MemDecoration = Arg1word;
  }
  ExGx(pMyDisasm);
  if ((GV.MOD_ == 3) && ((*pMyDisasm).Prefix.LockPrefix == InUsePrefix)) {
    GV.ERROR_OPCODE = UD_;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ ExGx(PDISASM pMyDisasm)
{
  MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
  Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ EvIv(PDISASM pMyDisasm)
{
  if (GV.OperandSize >= 32) {
    if (GV.OperandSize == 64) {
      GV.MemDecoration = Arg1qword;
    }
    else {
      GV.MemDecoration = Arg1dword;
    }
    GV.ImmediatSize = 32;                       /* place this instruction before MOD_RM routine to inform it there is an immediat value */
    MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
    GV.EIP_ += GV.DECALAGE_EIP+6;
    if (!Security(0, pMyDisasm)) return;
    #ifndef BEA_LIGHT_DISASSEMBLY
    if (GV.OperandSize == 64) {
      (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.16llX",(Int64) *((Int32*)(UIntPtr) (GV.EIP_-4)));
    }
    else {
      (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.8X",(Int64) *((UInt32*)(UIntPtr) (GV.EIP_-4)));
    }
    #endif

    (*pMyDisasm).Argument2.ArgType = CONSTANT_TYPE+ABSOLUTE_;
    (*pMyDisasm).Argument2.ArgSize = 32;
    (*pMyDisasm).Instruction.Immediat = *((UInt32*)(UIntPtr) (GV.EIP_-4));
  }
  else {
    GV.MemDecoration = Arg1word;
    GV.ImmediatSize = 16;
    MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
    GV.EIP_ += GV.DECALAGE_EIP+4;
    if (!Security(0, pMyDisasm)) return;
    #ifndef BEA_LIGHT_DISASSEMBLY
      (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.4X",(Int64)*((UInt16*)(UIntPtr) (GV.EIP_-2)));
    #endif
    (*pMyDisasm).Argument2.ArgType = CONSTANT_TYPE+ABSOLUTE_;
    (*pMyDisasm).Argument2.ArgSize = 16;
    (*pMyDisasm).Instruction.Immediat = *((UInt16*)(UIntPtr) (GV.EIP_-2));
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ EvIb(PDISASM pMyDisasm)
{
  Int8 MyNumber;
  (*pMyDisasm).Argument2.ArgType = CONSTANT_TYPE+ABSOLUTE_;
  (*pMyDisasm).Argument2.ArgSize = 8;
  GV.ImmediatSize = 8;
  if (GV.OperandSize >= 32) {
    if (GV.OperandSize == 64) {
      GV.MemDecoration = Arg1qword;
    }
    else {
      GV.MemDecoration = Arg1dword;
    }
    MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
    GV.EIP_ += GV.DECALAGE_EIP+3;
    if (!Security(0, pMyDisasm)) return;
    if (GV.OperandSize == 32) {
      #ifndef BEA_LIGHT_DISASSEMBLY
      MyNumber = *((Int8*)(UIntPtr) (GV.EIP_-1));
      if (MyNumber > 0) {
        (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.2X",(Int64)*((Int8*)(UIntPtr) (GV.EIP_-1)));
      }
      else {
        (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.8X",(Int64)*((Int8*)(IntPtr) (GV.EIP_-1)));
      }
      #endif
    }
    else {
      #ifndef BEA_LIGHT_DISASSEMBLY
      MyNumber = *((Int8*)(UIntPtr) (GV.EIP_-1));
      if (MyNumber > 0) {
        (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.2X",(Int64)*((Int8*)(UIntPtr) (GV.EIP_-1)));
      }
      else {
        (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.16llX",(Int64)*((Int8*)(IntPtr) (GV.EIP_-1)));
      }
      #endif
    }
  (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_-1));
  }
  else {
    GV.MemDecoration = Arg1word;
    MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
    GV.EIP_ += GV.DECALAGE_EIP+3;
    if (!Security(0, pMyDisasm)) return;
    #ifndef BEA_LIGHT_DISASSEMBLY
      (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.4X",(Int64)*((Int8*)(UIntPtr) (GV.EIP_-1)));
    #endif
    (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_-1));
  }
}
/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ EbIb(PDISASM pMyDisasm)
{
  (*pMyDisasm).Argument2.ArgType = CONSTANT_TYPE+ABSOLUTE_;
  (*pMyDisasm).Argument2.ArgSize = 8;
  GV.ImmediatSize = 8;
  GV.MemDecoration = Arg1byte;
  GV.OperandSize = 8;
  MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.OperandSize = 32;
  GV.EIP_ += GV.DECALAGE_EIP+3;
  if (!Security(0, pMyDisasm)) return;
  #ifndef BEA_LIGHT_DISASSEMBLY
    (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.2X",(Int64)*((Int8*)(UIntPtr) (GV.EIP_-1)));
  #endif
  (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_-1));
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ Eb(PDISASM pMyDisasm)
{
  GV.MemDecoration = Arg1byte;
  GV.OperandSize = 8;
  MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.OperandSize = 32;
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ Ev(PDISASM pMyDisasm)
{
  if (GV.OperandSize == 64) {
    GV.MemDecoration = Arg1qword;
  }
  else if (GV.OperandSize == 32) {
    GV.MemDecoration = Arg1dword;
  }
  else {
    GV.MemDecoration = Arg1word;
  }
  MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ GvEv(PDISASM pMyDisasm)
{
  if (GV.OperandSize == 64) {
    GV.MemDecoration = Arg2qword;
  }
  else if (GV.OperandSize == 32) {
    GV.MemDecoration = Arg2dword;
  }
  else {
    GV.MemDecoration = Arg2word;
  }
  MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 * Used by AVX instructions
 * ==================================================================== */
void __bea_callspec__ GyEy(PDISASM pMyDisasm)
{
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  fillRegister((~GV.VEX.vvvv & 0xF) + 16 * GV.EVEX.V, &(*pMyDisasm).Argument2, pMyDisasm);
  MOD_RM(&(*pMyDisasm).Argument3, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 * Used by AVX instructions
 * ==================================================================== */
void __bea_callspec__ ArgsVEX(PDISASM pMyDisasm)
{
  if (GV.VEX.L == 0) {
    (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
    GV.Register_ = SSE_REG;
    GV.MemDecoration = Arg3_m128_xmm;
    GyEy(pMyDisasm);
    GV.Register_ = 0;
  }
  else if (GV.VEX.L == 0x1) {
    (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
    GV.Register_ = AVX_REG;
    GV.MemDecoration = Arg3_m256_ymm;
    GyEy(pMyDisasm);
    GV.Register_ = 0;
  }
  else if (GV.EVEX.LL == 0x2) {
    (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
    GV.Register_ = AVX512_REG;
    GV.MemDecoration = Arg3_m512_zmm;
    GyEy(pMyDisasm);
    GV.Register_ = 0;
  }
}

void __bea_callspec__ ArgsVEX_CMPPS(PDISASM pMyDisasm)
{
  GV.Register_ = OPMASK_REG;
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  if (GV.VEX.L == 0) {
    (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
    GV.Register_ = SSE_REG;
    GV.MemDecoration = Arg3_m128_xmm;
  }
  else if (GV.VEX.L == 0x1) {
    (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
    GV.Register_ = AVX_REG;
    GV.MemDecoration = Arg3_m256_ymm;
  }
  else if (GV.EVEX.LL == 0x2) {
    (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
    GV.Register_ = AVX512_REG;
    GV.MemDecoration = Arg3_m512_zmm;
  }
  fillRegister((~GV.VEX.vvvv & 0xF) + 16 * GV.EVEX.V, &(*pMyDisasm).Argument2, pMyDisasm);
  MOD_RM(&(*pMyDisasm).Argument3, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}


/* ====================================================================
 * Used by AVX instructions
 * ==================================================================== */
void __bea_callspec__ EyGy(PDISASM pMyDisasm)
{
  GV.third_arg = 1;
  MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
  fillRegister((~GV.VEX.vvvv & 0xF) + 16 * GV.EVEX.V, &(*pMyDisasm).Argument2, pMyDisasm);
  Reg_Opcode(&(*pMyDisasm).Argument3, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 * Used by AVX instructions
 * ==================================================================== */
void __bea_callspec__ ArgsVEX_EyGy(PDISASM pMyDisasm)
{
  if (GV.VEX.L == 0) {
    (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
    GV.Register_ = SSE_REG;
    GV.MemDecoration = Arg1_m128_xmm;
    EyGy(pMyDisasm);
  }
  else if (GV.VEX.L == 0x1) {
    (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
    GV.Register_ = AVX_REG;
    GV.MemDecoration = Arg1_m256_ymm;
    EyGy(pMyDisasm);
  }
  else if (GV.EVEX.LL == 0x2) {
    (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
    GV.Register_ = AVX512_REG;
    GV.MemDecoration = Arg1_m512_zmm;
    EyGy(pMyDisasm);
  }
}

/* ====================================================================
 * Used by AVX instructions
 * ==================================================================== */
void __bea_callspec__ ArgsVEX_ExGx(PDISASM pMyDisasm)
{
  if (GV.VEX.L == 0) {
    (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
    GV.Register_ = SSE_REG;
    GV.MemDecoration = Arg1_m128_xmm;
    ExGx(pMyDisasm);
    GV.Register_ = 0;
  }
  else if (GV.VEX.L == 0x1) {
    (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
    GV.Register_ = AVX_REG;
    GV.MemDecoration = Arg1_m256_ymm;
    ExGx(pMyDisasm);
    GV.Register_ = 0;
  }
  else if (GV.EVEX.LL == 0x2) {
    (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
    GV.Register_ = AVX512_REG;
    GV.MemDecoration = Arg1_m512_zmm;
    ExGx(pMyDisasm);
    GV.Register_ = 0;
  }
}

/* ====================================================================
 * Used by AVX instructions
 * ==================================================================== */
void __bea_callspec__ ArgsVEX_GxEx(PDISASM pMyDisasm)
{
  if (GV.VEX.L == 0) {
    (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
    GV.Register_ = SSE_REG;
    GV.MemDecoration = Arg2_m128_xmm;
    GxEx(pMyDisasm);
    GV.Register_ = 0;
  }
  else if (GV.VEX.L == 0x1) {
    (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
    GV.Register_ = AVX_REG;
    GV.MemDecoration = Arg2_m256_ymm;
    GxEx(pMyDisasm);
    GV.Register_ = 0;
  }
  else if (GV.EVEX.LL == 0x2) {
    (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
    GV.Register_ = AVX512_REG;
    GV.MemDecoration = Arg2_m512_zmm;
    GxEx(pMyDisasm);
    GV.Register_ = 0;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ getImmediat8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  GV.EIP_++;
  GV.ImmediatSize = 8;
  if (!Security(0, pMyDisasm)) return;
  (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
  #ifndef BEA_LIGHT_DISASSEMBLY
     (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
  #endif
  (*pMyArgument).ArgType = CONSTANT_TYPE+ABSOLUTE_;
  (*pMyArgument).ArgSize = 8;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ verifyVEXvvvv(PDISASM pMyDisasm)
{
  if (
      ((GV.EVEX.state != InUsePrefix) && (GV.VEX.vvvv != 15))
      || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.vvvv != 15))
    ) {
    GV.ERROR_OPCODE = UD_;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ GvEb(PDISASM pMyDisasm)
{
  if (GV.OperandSize == 64) {
    GV.MemDecoration = Arg2byte;
    GV.OperandSize = 8;
    MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
    GV.OperandSize = 64;
  }
  else if (GV.OperandSize == 32) {
    GV.MemDecoration = Arg2byte;
    GV.OperandSize = 8;
    MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
    GV.OperandSize = 32;
  }
  else {
    GV.MemDecoration = Arg2byte;
    GV.OperandSize = 8;
    MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
    GV.OperandSize = 16;
  }
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ GxEx(PDISASM pMyDisasm)
{
  MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ GxExVEX(PDISASM pMyDisasm)
{
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
  fillRegister((~GV.VEX.vvvv & 0xF) + 16 * GV.EVEX.V, &(*pMyDisasm).Argument3, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ GvEw(PDISASM pMyDisasm)
{
  GV.MemDecoration = Arg2word;
  GV.OriginalOperandSize = GV.OperandSize;
  GV.OperandSize = 16;
  MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
  GV.OperandSize = GV.OriginalOperandSize;
  Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
  GV.EIP_ += GV.DECALAGE_EIP+2;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ ALIb(PDISASM pMyDisasm)
{
  long MyNumber;
  if (!Security(2, pMyDisasm)) return;
  GV.ImmediatSize = 8;
  MyNumber = *((Int8*)(IntPtr) (GV.EIP_+1));
  #ifndef BEA_LIGHT_DISASSEMBLY
    (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.2X",(Int64) MyNumber);
  #endif
  (*pMyDisasm).Instruction.Immediat = MyNumber;
  #ifndef BEA_LIGHT_DISASSEMBLY
    (void) strcpy((char*) &(*pMyDisasm).Argument1.ArgMnemonic, Registers8Bits[0]);
  #endif
  (*pMyDisasm).Argument1.ArgType = REGISTER_TYPE+GENERAL_REG;
  (*pMyDisasm).Argument1.Registers = REG0;
  (*pMyDisasm).Argument1.ArgSize = 8;
  (*pMyDisasm).Argument2.ArgType = CONSTANT_TYPE+ABSOLUTE_;
  (*pMyDisasm).Argument2.ArgSize = 8;
  GV.EIP_ += 2;
  if (
      ((*pMyDisasm).Prefix.LockPrefix == InUsePrefix)
    ) {
    GV.ERROR_OPCODE = UD_;
  }
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ eAX_Iv(PDISASM pMyDisasm)
{
    UInt32 MyNumber;
    (*pMyDisasm).Argument1.ArgType = REGISTER_TYPE+GENERAL_REG;
    (*pMyDisasm).Argument1.Registers = REG0;
    (*pMyDisasm).Argument2.ArgType = CONSTANT_TYPE+ABSOLUTE_;
    if (GV.OperandSize == 64) {
      if (!Security(5, pMyDisasm)) return;
      GV.ImmediatSize = 32;
      (*pMyDisasm).Argument1.ArgSize = 64;
      (*pMyDisasm).Argument2.ArgSize = 32;
      MyNumber = *((UInt32*)(UIntPtr) (GV.EIP_+1));
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.16llX",(Int64) MyNumber);
      #endif
      (*pMyDisasm).Instruction.Immediat = MyNumber;
       if (GV.REX.B_ == 1) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyDisasm).Argument1.ArgMnemonic, Registers64Bits[0+8]);
          #endif
      }
      else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyDisasm).Argument1.ArgMnemonic, Registers64Bits[0]);
          #endif
      }
      GV.EIP_+= 5;
    }
    else if (GV.OperandSize == 32) {
      if (!Security(5, pMyDisasm)) return;
      GV.ImmediatSize = 32;
      (*pMyDisasm).Argument1.ArgSize = 32;
      (*pMyDisasm).Argument2.ArgSize = 32;
      MyNumber = *((UInt32*)(UIntPtr) (GV.EIP_+1));
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.8X",(Int64) MyNumber);
      #endif
      (*pMyDisasm).Instruction.Immediat = MyNumber;
       if (GV.REX.B_ == 1) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyDisasm).Argument1.ArgMnemonic, Registers32Bits[0+8]);
        #endif
      }
      else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyDisasm).Argument1.ArgMnemonic, Registers32Bits[0]);
        #endif
      }
      GV.EIP_+= 5;
    }
    else {
      if (!Security(3, pMyDisasm)) return;
      GV.ImmediatSize = 16;
      (*pMyDisasm).Argument1.ArgSize = 16;
      (*pMyDisasm).Argument2.ArgSize = 16;
      MyNumber = *((UInt16*)(UIntPtr) (GV.EIP_+1));
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) CopyFormattedNumber(pMyDisasm, (char*) &(*pMyDisasm).Argument2.ArgMnemonic,"%.8X", (Int64) MyNumber);
      #endif
      (*pMyDisasm).Instruction.Immediat = MyNumber;
       if (GV.REX.B_ == 1) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyDisasm).Argument1.ArgMnemonic, Registers16Bits[0+8]);
          #endif
      }
      else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyDisasm).Argument1.ArgMnemonic, Registers16Bits[0]);
          #endif
      }
      GV.EIP_+= 3;
    }
    if (
        ((*pMyDisasm).Prefix.LockPrefix == InUsePrefix)
      ) {
      GV.ERROR_OPCODE = UD_;
    }
}

/* ====================================================================
 *
 * ==================================================================== */
int __bea_callspec__ Security(int len, PDISASM pMyDisasm)
{
  if ((GV.EndOfBlock != 0) && (GV.EIP_+(UInt64)len >= GV.EndOfBlock)) {
    GV.OutOfBlock = 1;
    return 0;
  }
  return 1;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ FillFlags(PDISASM pMyDisasm, int index)
{
  (*pMyDisasm).Instruction.Flags = EFLAGS_TABLE[index];
}
/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ CalculateRelativeAddress(UInt64 * pMyAddress, Int64 MyNumber, PDISASM pMyDisasm)
{
  GV.RelativeAddress = 1;
  if (GV.EIP_VA != 0) {
      *pMyAddress = (UInt64) (GV.EIP_VA+(UInt64) MyNumber);
  }
  else {
      *pMyAddress = (UInt64) (GV.EIP_REAL+(UInt64) MyNumber);
  }
}

/* ====================================================================
 *
 * ==================================================================== */
#ifndef BEA_LIGHT_DISASSEMBLY
size_t __bea_callspec__ CopyFormattedNumber(PDISASM pMyDisasm, char* pBuffer, const char* pFormat, Int64 MyNumber)
{
  size_t i = 0;
  if (!strcmp(pFormat,"%.2X")) MyNumber = MyNumber & 0xFF;
  if (!strcmp(pFormat,"%.4X")) MyNumber = MyNumber & 0xFFFF;
  if (!strcmp(pFormat,"%.8X")) MyNumber = MyNumber & 0xFFFFFFFF;
  if (GV.FORMATNUMBER == PrefixedNumeral) {
      (void) strcpy(pBuffer, "0x");
      (void) sprintf (pBuffer+2, pFormat, MyNumber);
      i += strlen(pBuffer);
  }
  else {
      (void) sprintf (pBuffer+i, pFormat, MyNumber);
      i += strlen(pBuffer);
      (void) strcpy(pBuffer+i, "h");
      i++;
  }
  return i;
}
#endif

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ FillSegmentsRegisters(PDISASM pMyDisasm)
{
  if (
      ((*pMyDisasm).Prefix.LockPrefix == InUsePrefix) &&
      !((*pMyDisasm).Argument1.ArgType & (MEMORY_TYPE | REGISTER_TYPE))
    ) {
      (*pMyDisasm).Prefix.LockPrefix = InvalidPrefix;
  }
  if ((*pMyDisasm).Instruction.Category == GENERAL_PURPOSE_INSTRUCTION+STRING_INSTRUCTION) {
    (*pMyDisasm).Argument1.SegmentReg = ESReg;
    (*pMyDisasm).Argument2.SegmentReg = DSReg;
    /* =============== override affects Arg2 */
    if ((*pMyDisasm).Argument2.ArgType & MEMORY_TYPE) {
      if ((*pMyDisasm).Prefix.FSPrefix == InUsePrefix) {
        (*pMyDisasm).Argument2.SegmentReg = FSReg;
      }
      else if ((*pMyDisasm).Prefix.GSPrefix == InUsePrefix) {
        (*pMyDisasm).Argument2.SegmentReg = GSReg;
      }
      else if ((*pMyDisasm).Prefix.CSPrefix == InUsePrefix) {
        (*pMyDisasm).Argument2.SegmentReg = CSReg;
      }
      else if ((*pMyDisasm).Prefix.ESPrefix == InUsePrefix) {
        (*pMyDisasm).Argument2.SegmentReg = ESReg;
      }
      else if ((*pMyDisasm).Prefix.SSPrefix == InUsePrefix) {
        (*pMyDisasm).Argument2.SegmentReg = SSReg;
      }
      else {
        (*pMyDisasm).Argument2.SegmentReg = DSReg;
      }
    }
  }
  else {
    if ((*pMyDisasm).Argument1.ArgType & MEMORY_TYPE) {
      if (
          ((*pMyDisasm).Argument1.Memory.BaseRegister == REG4) ||
          ((*pMyDisasm).Argument1.Memory.BaseRegister == REG5)
        ) {
        (*pMyDisasm).Argument1.SegmentReg = SSReg;
        /* ========== override is invalid here */
        if ((*pMyDisasm).Argument2.ArgType != MEMORY_TYPE) {
          if ((*pMyDisasm).Prefix.FSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = FSReg;
            (*pMyDisasm).Prefix.FSPrefix = InvalidPrefix;
          }
          else if ((*pMyDisasm).Prefix.GSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = GSReg;
            (*pMyDisasm).Prefix.GSPrefix = InvalidPrefix;
          }
          else if ((*pMyDisasm).Prefix.CSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = CSReg;
            (*pMyDisasm).Prefix.CSPrefix = InvalidPrefix;
          }
          else if ((*pMyDisasm).Prefix.DSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = DSReg;
            (*pMyDisasm).Prefix.DSPrefix = InvalidPrefix;
          }
          else if ((*pMyDisasm).Prefix.ESPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = ESReg;
            (*pMyDisasm).Prefix.ESPrefix = InvalidPrefix;
          }
          else if ((*pMyDisasm).Prefix.SSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = SSReg;
            (*pMyDisasm).Prefix.SSPrefix = InvalidPrefix;
          }
        }
      }
      else {
        (*pMyDisasm).Argument1.SegmentReg = DSReg;
        /* ============= test if there is override */
        if ((*pMyDisasm).Prefix.FSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = FSReg;
        }
        else if ((*pMyDisasm).Prefix.GSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = GSReg;
        }
        else if ((*pMyDisasm).Prefix.CSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = CSReg;
        }
        else if ((*pMyDisasm).Prefix.ESPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = ESReg;
        }
        else if ((*pMyDisasm).Prefix.SSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument1.SegmentReg = SSReg;
        }
      }
    }

    if ((*pMyDisasm).Argument2.ArgType & MEMORY_TYPE) {
      if (
        ((*pMyDisasm).Argument2.Memory.BaseRegister == REG4) ||
         ((*pMyDisasm).Argument2.Memory.BaseRegister == REG5)
       ) {
        (*pMyDisasm).Argument2.SegmentReg = SSReg;
        /* ========== override is invalid here */
        if ((*pMyDisasm).Prefix.FSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = FSReg;
            (*pMyDisasm).Prefix.FSPrefix = InvalidPrefix;
        }
        else if ((*pMyDisasm).Prefix.GSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = GSReg;
            (*pMyDisasm).Prefix.GSPrefix = InvalidPrefix;
        }
        else if ((*pMyDisasm).Prefix.CSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = CSReg;
            (*pMyDisasm).Prefix.CSPrefix = InvalidPrefix;
        }
        else if ((*pMyDisasm).Prefix.DSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = DSReg;
            (*pMyDisasm).Prefix.DSPrefix = InvalidPrefix;
        }
        else if ((*pMyDisasm).Prefix.ESPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = ESReg;
            (*pMyDisasm).Prefix.ESPrefix = InvalidPrefix;
        }
        else if ((*pMyDisasm).Prefix.SSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = SSReg;
            (*pMyDisasm).Prefix.SSPrefix = InvalidPrefix;
        }
      }
      else {
        (*pMyDisasm).Argument2.SegmentReg = DSReg;
        /* ============= test if there is override */
        if ((*pMyDisasm).Prefix.FSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = FSReg;
        }
        else if ((*pMyDisasm).Prefix.GSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = GSReg;
        }
        else if ((*pMyDisasm).Prefix.CSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = CSReg;
        }
        else if ((*pMyDisasm).Prefix.ESPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = ESReg;
        }
        else if ((*pMyDisasm).Prefix.SSPrefix == InUsePrefix) {
            (*pMyDisasm).Argument2.SegmentReg = SSReg;
        }
      }
    }
  }
}

#ifndef BEA_LIGHT_DISASSEMBLY
/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printPrefixes(PDISASM pMyDisasm, size_t i)
{
  if ((*pMyDisasm).Prefix.RepnePrefix == InUsePrefix) {
    (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "repne ");
    i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  }
  if ((*pMyDisasm).Prefix.RepPrefix == InUsePrefix) {
    (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "rep ");
    i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  }
  if (
    ((*pMyDisasm).Prefix.LockPrefix == InUsePrefix) ||
    ((*pMyDisasm).Prefix.LockPrefix == InvalidPrefix)
    ) {
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "lock ");
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  }
  return i;
}
/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printMnemonic(PDISASM pMyDisasm, size_t i)
{
  (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, (char*) &(*pMyDisasm).Instruction.Mnemonic);
  i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  return i;
}
/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printTabulation(PDISASM pMyDisasm, size_t i)
{
  (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, space_tab[i>10 ? 0 : 10-i]);
  i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  return i;
}
/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printArg(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i)
{
  (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, (char*) &(*pMyArgument).ArgMnemonic);
  i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  return i;
}
/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printDecoratedArg(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i)
{
  if (GV.SYNTAX_ == NasmSyntax) {
    (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, NasmPrefixes[GV.MemDecoration-1]);
    i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    if ((GV.SEGMENTREGS != 0) || (GV.SEGMENTFS != 0)){
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "[");
      i++;
      if (GV.SEGMENTREGS != 0) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[(*pMyArgument).SegmentReg]);
      }
      else {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[3]);
      }
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }
    else {
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "[");
      i++;
    }
  }
  else {
    if (GV.SYNTAX_ == MasmSyntax) {
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, MasmPrefixes[GV.MemDecoration-1]);
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }
    else if (GV.SYNTAX_ == IntrinsicMemSyntax) {
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, IntrinsicPrefixes[GV.MemDecoration-1]);
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }
    else {
        (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, GoAsmPrefixes[GV.MemDecoration-1]);
        i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }
    if ((GV.SEGMENTREGS != 0) || (GV.SEGMENTFS != 0)){
      if (GV.SEGMENTREGS != 0) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[(*pMyArgument).SegmentReg]);
      }
      else {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[3]);
      }
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "[");
      i++;
    }
    else {
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "[");
      i++;
    }
  }
  (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, (char*) &(*pMyArgument).ArgMnemonic);
  i = strlen((char*) &(*pMyDisasm).CompleteInstr);
  (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "]");
  i++;
  return i;
}

/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printArg1(PDISASM pMyDisasm, size_t i)
{
  if ((GV.MemDecoration >0) && (GV.MemDecoration < 99)) {
    i = printDecoratedArg(&(*pMyDisasm).Argument1, pMyDisasm, i);
  }
  else {
    i = printArg(&(*pMyDisasm).Argument1, pMyDisasm, i);
  }
  return i;
}

/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printArg2(PDISASM pMyDisasm, size_t i)
{
  if ((GV.MemDecoration >100) && (GV.MemDecoration < 199)) {
      GV.MemDecoration -= 100;
      i = printDecoratedArg(&(*pMyDisasm).Argument2, pMyDisasm, i);
  }
  else {
    i = printArg(&(*pMyDisasm).Argument2, pMyDisasm, i);
  }
  return i;
}

/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printArg3(PDISASM pMyDisasm, size_t i)
{
  if ((GV.MemDecoration >200) && (GV.MemDecoration < 299)) {
    GV.MemDecoration -= 200;
    i = printDecoratedArg(&(*pMyDisasm).Argument3, pMyDisasm, i);
  }
  else {
    i = printArg(&(*pMyDisasm).Argument3, pMyDisasm, i);
  }
  return i;
}

/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printArg4(PDISASM pMyDisasm, size_t i)
{
  if ((GV.MemDecoration >300) && (GV.MemDecoration < 399)) {
    GV.MemDecoration -= 300;
    i = printDecoratedArg(&(*pMyDisasm).Argument4, pMyDisasm, i);
  }
  else {
    i = printArg(&(*pMyDisasm).Argument4, pMyDisasm, i);
  }
  return i;
}

/* ====================================================================
 *
 * ==================================================================== */
size_t __bea_callspec__ printArgsSeparator(ARGTYPE* pMyArgument1, ARGTYPE* pMyArgument2, PDISASM pMyDisasm, size_t i)
{
  if (
      ((UInt8)*((UInt8*) &(*pMyArgument1).ArgMnemonic) != 0) &&
       ((UInt8)*((UInt8*) &(*pMyArgument2).ArgMnemonic) != 0)
     ) {
    (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, ", ");
    i += 2;
  }
  return i;
}

/* ====================================================================
 *
 * ==================================================================== */
void __bea_callspec__ BuildCompleteInstruction(PDISASM pMyDisasm)
{
  size_t i = 0;

  i = printPrefixes(pMyDisasm, i);
  i = printMnemonic(pMyDisasm, i);
  if (GV.TAB_ == 1) {
    i = printTabulation(pMyDisasm, i);
  }
  i = printArg1(pMyDisasm, i);
  i = printArgsSeparator(&(*pMyDisasm).Argument1, &(*pMyDisasm).Argument2, pMyDisasm, i);
  i = printArg2(pMyDisasm, i);
  i = printArgsSeparator(&(*pMyDisasm).Argument2, &(*pMyDisasm).Argument3, pMyDisasm, i);
  i = printArg3(pMyDisasm, i);
  i = printArgsSeparator(&(*pMyDisasm).Argument3, &(*pMyDisasm).Argument4, pMyDisasm, i);
  i = printArg4(pMyDisasm, i);
}

/* ====================================================================
 *  @TODO : must be entirely recoded - for now, it is disabled
 * ==================================================================== */
void __bea_callspec__ BuildCompleteInstructionATSyntax(PDISASM pMyDisasm)
{
    size_t i = 0;
    i = printMnemonic(pMyDisasm, i);

    /* =============== suffix the mnemonic */
    if (GV.MemDecoration != 0) {
      if (GV.MemDecoration > 99) GV.MemDecoration -= 100;
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i-1, ATSuffixes[GV.MemDecoration-1]);
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }
    else {
      if ((*pMyDisasm).Argument1.ArgType != NO_ARGUMENT) {
        if ((*pMyDisasm).Argument1.ArgSize == 8) {
            (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i-1, ATSuffixes[0]);
        }
        else if ((*pMyDisasm).Argument1.ArgSize == 16) {
            (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i-1, ATSuffixes[1]);
        }
        else if ((*pMyDisasm).Argument1.ArgSize == 32) {
            (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i-1, ATSuffixes[2]);
        }
        else if ((*pMyDisasm).Argument1.ArgSize == 64) {
            (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i-1, ATSuffixes[3]);
        }
        i = strlen((char*) &(*pMyDisasm).CompleteInstr);
      }
    }
    if (GV.TAB_ == 1) {
      i = printTabulation(pMyDisasm, i);
    }

    /* =============== if Arg3.Exists, display it */
    if ((*pMyDisasm).Argument3.ArgMnemonic != 0) {
      if ((*pMyDisasm).Argument3.ArgType & REGISTER_TYPE) {
        (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "%");
        i++;
      }
      else if ((*pMyDisasm).Argument3.ArgType & CONSTANT_TYPE) {
        (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "\x24");
        i++;
      }
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, (char*) &(*pMyDisasm).Argument3.ArgMnemonic);
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }

    i = printArgsSeparator(&(*pMyDisasm).Argument2, &(*pMyDisasm).Argument3, pMyDisasm, i);

    /* =============== if Arg2 exists, display it */
    if (*((UInt8*) &(*pMyDisasm).Argument2.ArgMnemonic) != 0) {
      if ((*pMyDisasm).Argument2.ArgType & CONSTANT_TYPE) {
        (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "\x24");
        i++;
      }
      else {
        if ((*pMyDisasm).Instruction.BranchType != 0) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "*");
          i++;
        }
        if ((*pMyDisasm).Argument2.ArgType & REGISTER_TYPE) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "%");
          i++;
        }
        else if ((*pMyDisasm).Argument2.ArgType & CONSTANT_TYPE) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "\x24");
          i++;
        }
        else {
          if ((GV.SEGMENTREGS != 0) || (GV.SEGMENTFS != 0)){
            (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "%");
            i++;
            if (GV.SEGMENTREGS != 0) {
              (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[(*pMyDisasm).Argument2.SegmentReg]);
            }
            else {
              (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[3]);
            }
            i = strlen((char*) &(*pMyDisasm).CompleteInstr);
          }
        }
      }
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, (char*) &(*pMyDisasm).Argument2.ArgMnemonic);
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }

    i = printArgsSeparator(&(*pMyDisasm).Argument1, &(*pMyDisasm).Argument2, pMyDisasm, i);

    /* =============== if Arg1 exists, display it */
    if (*((UInt8*) &(*pMyDisasm).Argument1.ArgMnemonic) != 0) {
      if ((*pMyDisasm).Argument1.ArgType & CONSTANT_TYPE) {
        (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "\x24");
        i++;
      }
      else {
        if ((*pMyDisasm).Instruction.BranchType != 0) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "*");
          i++;
        }
        if ((*pMyDisasm).Argument1.ArgType & REGISTER_TYPE) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "%");
          i++;
        }
        else if ((*pMyDisasm).Argument1.ArgType & CONSTANT_TYPE) {
          (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "\x24");
          i++;
        }
        else {
          if ((GV.SEGMENTREGS != 0) || (GV.SEGMENTFS != 0)){
            (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, "%");
            i++;
            if (GV.SEGMENTREGS != 0) {
                (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[(*pMyDisasm).Argument1.SegmentReg]);
            }
            else {
                (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, SegmentRegs[3]);
            }
            i = strlen((char*) &(*pMyDisasm).CompleteInstr);
          }
        }
      }
      (void) strcpy ((char*) &(*pMyDisasm).CompleteInstr+i, (char*) &(*pMyDisasm).Argument1.ArgMnemonic);
      i = strlen((char*) &(*pMyDisasm).CompleteInstr);
    }
}
#endif
