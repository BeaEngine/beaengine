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
 *    along with BeaEngine.  If not, see <http://www.gnu.org/licenses/>.
 * =======================================
 *
 * ======================================= */
void __bea_callspec__ MOD_RM(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    GV.DECALAGE_EIP = 0;
    if (!Security(1, pMyDisasm)) return;
    GV.MOD_ = ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
    GV.RM_  = (*((UInt8*)(UIntPtr) (GV.EIP_+1))) & 0x7;
    if (GV.MOD_ == 0) {
        ModRM_0[GV.RM_](pMyArgument, pMyDisasm);
    }
    else if (GV.MOD_ == 1) {
        GV.DECALAGE_EIP++;
        ModRM_1[GV.RM_](pMyArgument, pMyDisasm);
    }
    else if (GV.MOD_ == 2) {
        if (GV.AddressSize >= 32) {
            GV.DECALAGE_EIP += 4;
        }
        else {
            GV.DECALAGE_EIP += 2;
        }
        ModRM_2[GV.RM_](pMyArgument, pMyDisasm);
    }
    else {
        ModRM_3[GV.RM_](pMyArgument, pMyDisasm);
    }

}

/* =======================================
 *  used in Reg_Opcode
 * ======================================= */
void __bea_callspec__ fillRegister(int index, ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{

    size_t i = 0;

    if (GV.Register_ == OPMASK_REG) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersOpmask[index]);
      #endif
      (*pMyArgument).ArgType = REGISTER_TYPE + OPMASK_REG;
      (*pMyArgument).Registers = REGS[index];
      (*pMyArgument).ArgSize = 64;
    }
    else if (GV.Register_ == MPX_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersMPX[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE + MPX_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 128;
    }
    else if (GV.Register_ == AVX_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersAVX[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+AVX_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 256;
    }
    else if (GV.Register_ == AVX512_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersAVX512[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+AVX512_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 512;
    }
    else if (GV.Register_ == MMX_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersMMX[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+MMX_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 64;
    }
    else if (GV.Register_ == SEGMENT_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersSEG[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+SEGMENT_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 16;
    }
    else if (GV.Register_ == CR_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersCR[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+CR_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 32;
    }
    else if (GV.Register_ == DR_REG) {
        if (GV.SYNTAX_ == ATSyntax) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersDR_AT[index]);
            #endif
        }
        else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersDR[index]);
            #endif
        }
        (*pMyArgument).ArgType = REGISTER_TYPE+DR_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 32;
    }
    else if (GV.Register_ == SSE_REG) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersSSE[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+SSE_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 128;
    }
    else if (GV.OperandSize == 8) {
      OperandSize8Reg(pMyArgument, pMyDisasm, i, index);
    }
    else if (GV.OperandSize == 16) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers16Bits[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 16;
    }
    else if (GV.OperandSize == 32) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 32;
    }
    else if (GV.OperandSize == 64) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[index]);
        #endif
        (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
        (*pMyArgument).Registers = REGS[index];
        (*pMyArgument).ArgSize = 64;
    }
}

void __bea_callspec__ OperandSize8Reg(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i, int index)
{
  if (GV.REX.state == 0) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers8BitsLegacy[index]);
      #endif
      (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
      (*pMyArgument).Registers = REGS8BITS[index+0];
      (*pMyArgument).ArgSize = 8;
  }
  else {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers8Bits[index]);
      #endif
      (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
      (*pMyArgument).Registers = REGS[index+0];
      (*pMyArgument).ArgSize = 8;
  }
  return;
}


/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Reg_Opcode(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{

    if (!Security(1, pMyDisasm)) return;
    GV.REGOPCODE = ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 3) & 0x7;
    GV.REGOPCODE += 8 * GV.REX.R_ + 16 * GV.EVEX.R1;
    fillRegister(GV.REGOPCODE, pMyArgument, pMyDisasm);
}

void __bea_callspec__ fillModrm0Register(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i, UInt8 index)
{
  int index_final;
  (*pMyArgument).ArgType = MEMORY_TYPE;
  if (GV.AddressSize == 64) {
      index_final = (GV.REX.B_ == 1) ? index + 8 : index;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[index_final]);
      #endif
      (*pMyArgument).Memory.BaseRegister = REGS[index_final];
  }
  else if (GV.AddressSize == 32) {
    index_final = (GV.REX.B_ == 1) ? index + 8 : index;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[index_final]);
    #endif
    (*pMyArgument).Memory.BaseRegister = REGS[index_final];
  }
  else {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersSIB[index]);
    #endif
  }
}


/* =======================================
 *          ModRM_0
 * ======================================= */
void __bea_callspec__ Addr_EAX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    #ifndef BEA_LIGHT_DISASSEMBLY
	size_t i = 0;
    if (GV.SYNTAX_ == ATSyntax) {
	   (void) strcpy((char*) (*pMyArgument).ArgMnemonic, "(%");
	   i += 2;
    }
    #endif
    fillModrm0Register(pMyArgument, pMyDisasm, i, 0);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[3];
      (*pMyArgument).Memory.IndexRegister = REGS[6];
    }
    #ifndef BEA_LIGHT_DISASSEMBLY
       i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
       if (GV.SYNTAX_ == ATSyntax) {
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
           i += 1;
       }
    #endif

}
/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_ECX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    #ifndef BEA_LIGHT_DISASSEMBLY
    size_t i = 0;
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic, "(%");
        i += 2;
    }
	#endif
  fillModrm0Register(pMyArgument, pMyDisasm, i, 1);
  if (GV.AddressSize == 16) {
    (*pMyArgument).Memory.BaseRegister = REGS[3];
    (*pMyArgument).Memory.IndexRegister = REGS[7];
  }
	#ifndef BEA_LIGHT_DISASSEMBLY
		i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
		if (GV.SYNTAX_ == ATSyntax) {
			(void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
			i += 1;
		}
	#endif

}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_EDX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    #ifndef BEA_LIGHT_DISASSEMBLY
		size_t i = 0;
		if (GV.SYNTAX_ == ATSyntax) {
			(void) strcpy((char*) (*pMyArgument).ArgMnemonic, "(%");
			i += 2;
		}
	#endif
  fillModrm0Register(pMyArgument, pMyDisasm, i, 2);
  if (GV.AddressSize == 16) {
    (*pMyArgument).Memory.BaseRegister = REGS[5];
    (*pMyArgument).Memory.IndexRegister = REGS[6];
  }
	#ifndef BEA_LIGHT_DISASSEMBLY
		i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
		if (GV.SYNTAX_ == ATSyntax) {
			(void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
			i += 1;
		}
	#endif
}


/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_EBX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    #ifndef BEA_LIGHT_DISASSEMBLY
	size_t i = 0;
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic, "(%");
        i += 2;
    }
	#endif
  fillModrm0Register(pMyArgument, pMyDisasm, i, 3);
  if (GV.AddressSize == 16) {
    (*pMyArgument).Memory.BaseRegister = REGS[5];
    (*pMyArgument).Memory.IndexRegister = REGS[7];
  }
  #ifndef BEA_LIGHT_DISASSEMBLY
  i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
  if (GV.SYNTAX_ == ATSyntax) {
      (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
      i += 1;
  }
	#endif

}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_SIB(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    if (!Security(2, pMyDisasm)) return;
    (*pMyArgument).ArgType = MEMORY_TYPE;
    if (GV.AddressSize >= 32) {
        GV.DECALAGE_EIP++;
        GV.BASE_  = ((UInt8) *((UInt8*) (UIntPtr) (GV.EIP_+2))) & 0x7;
        GV.SCALE_  = (((UInt8) *((UInt8*) (UIntPtr)(GV.EIP_+2))) & 0xc0) >> 6;
        GV.INDEX_  = (((UInt8) *((UInt8*) (UIntPtr)(GV.EIP_+2))) & 0x38) >> 3;
        (void) SIB[GV.SCALE_ ](pMyArgument, 0, pMyDisasm);
    }
    else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic, Registers16Bits[6]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[6];
    }
}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    Int32 MyNumber;
    UInt64 MyAddress;
    size_t i = 0;
    (*pMyArgument).ArgType = MEMORY_TYPE;
    if (GV.AddressSize >= 32) {
        if (!Security(6, pMyDisasm)) return;
        GV.DECALAGE_EIP+=4;
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
        (*pMyArgument).Memory.Displacement = MyNumber;
        if (GV.Architecture == 64) {
            /* add len(opcode + modrm + imm32) */
            MyNumber += 6;
            /* add nb prefixes */
            MyNumber += GV.NB_PREFIX;
            /* add immediat if exists */
            if (GV.ImmediatSize == 32) {
                MyNumber += 4;
            }
            if (GV.ImmediatSize == 16) {
                MyNumber += 2;
            }
            if (GV.ImmediatSize == 8) {
                MyNumber += 1;
            }

            /* add len (62h + P0 + P1 + P2) - 1 */
            if (GV.EVEX.state == InUsePrefix) {
              MyNumber += 3;
            }

            else if (GV.VEX.state == InUsePrefix) {
              /* add len (c4h + byte1 + byte2) - 1 */
              if (GV.VEX.opcode == 0xc4) {
                MyNumber += 2;
              }
              /* add len (c5h + byte1) - 1 */
              else {
                MyNumber += 1;
              }
            }
            else if ((*pMyDisasm).Instruction.Opcode >= 0x0F3800) {      /* add two bytes if opcode is a 3-bytes */
                MyNumber +=2;
            }
            else if ((*pMyDisasm).Instruction.Opcode >= 0x0100) {   /* add one byte if opcode is a 2-bytes */
                MyNumber +=1;
            }
            CalculateRelativeAddress(&MyAddress, (Int64)MyNumber, pMyDisasm);
            (*pMyDisasm).Instruction.AddrValue = MyAddress;
            #ifndef BEA_LIGHT_DISASSEMBLY
               i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+i,"%.16llX", (Int64)MyAddress);
            #endif
            (*pMyArgument).ArgType |= RELATIVE_;
        }
        else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+i,"%.8X", (Int64)MyNumber);
            #endif
        }
    }
    else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic, Registers16Bits[7]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[7];
    }
}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_ESI(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    long MyNumber;
    #ifndef BEA_LIGHT_DISASSEMBLY
	size_t i = 0;
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic, "(%");
        i += 2;
    }
	#endif
    (*pMyArgument).ArgType = MEMORY_TYPE;
    if (GV.AddressSize == 64) {
        if (GV.REX.B_ == 1) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[14]);
            #endif
            (*pMyArgument).Memory.BaseRegister = REGS[6+8];
        }
        else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[6]);
            #endif
            (*pMyArgument).Memory.BaseRegister = REGS[6];
        }
    }
    else if (GV.AddressSize == 32) {

        if (GV.REX.B_ == 1) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[14]);
            #endif
            (*pMyArgument).Memory.BaseRegister = REGS[6+8];
        }
        else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[6]);
            #endif
            (*pMyArgument).Memory.BaseRegister = REGS[6];
        }
    }
    else {
        GV.DECALAGE_EIP+=2;
        MyNumber = *((UInt16*)(UIntPtr) (GV.EIP_+2));
        (*pMyArgument).Memory.Displacement = MyNumber;
        if (!Security(2, pMyDisasm)) return;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+i,"%.4X", (Int64)MyNumber);
        #endif
    }
    #ifndef BEA_LIGHT_DISASSEMBLY
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
    }
	#endif
}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_EDI(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    #ifndef BEA_LIGHT_DISASSEMBLY
	size_t i = 0;
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic, "(%");
        i += 2;
    }
	#endif

  fillModrm0Register(pMyArgument, pMyDisasm, i, 7);
  if (GV.AddressSize == 16) {
    (*pMyArgument).Memory.BaseRegister = REGS[3];
  }
  #ifndef BEA_LIGHT_DISASSEMBLY
  i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
  if (GV.SYNTAX_ == ATSyntax) {
      (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
      i += 1;
  }
	#endif
}

size_t __bea_callspec__ printDisp8(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm, long MyNumber)
{
  size_t j;

  if (MyNumber < 0) {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "-");
    #endif
    i++;
    j=i;
    #ifndef BEA_LIGHT_DISASSEMBLY
       i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+j,"%.2X",(Int64) ~MyNumber+1);
    #endif
  }
  else {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "+");
    #endif
    i ++;
    j=i;
    #ifndef BEA_LIGHT_DISASSEMBLY
       i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+j,"%.2X",(Int64) MyNumber);
    #endif
  }
  return i;
}


size_t __bea_callspec__ printDisp32(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm, long MyNumber)
{
  size_t j;

  if (MyNumber < 0) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "-");
      #endif
      i ++;
      j=i;
      #ifndef BEA_LIGHT_DISASSEMBLY
         i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+j,"%.8X",(Int64) ~MyNumber+1);
      #endif
  }
  else {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "+");
    #endif
    i ++;
      j = i;
      #ifndef BEA_LIGHT_DISASSEMBLY
         i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+j,"%.8X",(Int64) MyNumber);
      #endif
  }

  return i;
}


/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_EAX_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 0);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[3];
      (*pMyArgument).Memory.IndexRegister = REGS[6];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_ECX_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    MyNumber = (Int8) *((UInt8*) (UIntPtr)GV.EIP_+2);
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 1);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[3];
      (*pMyArgument).Memory.IndexRegister = REGS[7];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_EDX_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 2);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[5];
      (*pMyArgument).Memory.IndexRegister = REGS[6];
    }

    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }

}

/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_EBX_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }

    fillModrm0Register(pMyArgument, pMyDisasm, i, 3);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[5];
      (*pMyArgument).Memory.IndexRegister = REGS[7];
    }

    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
      (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
      i += 1;
      #endif
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }

}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_SIB_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0, j;
    long MyNumber;
    if (!Security(2, pMyDisasm)) return;
    if (GV.AddressSize >= 32) {
        MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+3));
    }
    else {
        MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }
    (*pMyArgument).ArgType = MEMORY_TYPE;
    if (GV.AddressSize >= 32) {
        GV.DECALAGE_EIP++;
        GV.BASE_  = (*((UInt8*)(UIntPtr) (GV.EIP_+2))) & 0x7;
        GV.SCALE_  = ((*((UInt8*)(UIntPtr) (GV.EIP_+2))) & 0xc0) >> 6;
        GV.INDEX_  = ((*((UInt8*)(UIntPtr) (GV.EIP_+2))) & 0x38) >> 3;
        j = i;
        i += SIB[GV.SCALE_ ](pMyArgument, j, pMyDisasm);
    }
    else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic, Registers16Bits[6]);
        #endif
        i += strlen (Registers16Bits[6]);
        (*pMyArgument).Memory.BaseRegister = REGS[6];

    }

    if (GV.SYNTAX_ == ATSyntax) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        #endif
        i++;
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }

}

/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_EBP_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }

    fillModrm0Register(pMyArgument, pMyDisasm, i, 5);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.IndexRegister = REGS[7];
    }

    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_ESI_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 6);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[5];
    }

    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    }

}

/* =======================================
 *          ModRM_1
 * ======================================= */
void __bea_callspec__ Addr_EDI_disp8(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  size_t i = 0;
  long MyNumber;
  MyNumber = *((Int8*)(UIntPtr) (GV.EIP_+2));
  (*pMyArgument).Memory.Displacement = MyNumber;
  if (GV.SYNTAX_ == ATSyntax) {
    i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
    #endif
    i+=2;
  }
  fillModrm0Register(pMyArgument, pMyDisasm, i, 7);
  if (GV.AddressSize == 16) {
    (*pMyArgument).Memory.BaseRegister = REGS[3];
  }

  i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
  if (GV.SYNTAX_ == ATSyntax) {
    #ifndef BEA_LIGHT_DISASSEMBLY
    (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
    i += 1;
    #endif
  }
  else {
    i = printDisp8(pMyArgument, i, pMyDisasm, MyNumber);
  }

}

/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_EAX_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
        i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);

        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
        #endif
        i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 0);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[3];
      (*pMyArgument).Memory.IndexRegister = REGS[6];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
}


/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_ECX_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
        i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
        #endif
        i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 1);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[3];
      (*pMyArgument).Memory.IndexRegister = REGS[7];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_EDX_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);

        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
        #endif
        i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 2);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[5];
      (*pMyArgument).Memory.IndexRegister = REGS[6];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_EBX_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);

      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 3);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[5];
      (*pMyArgument).Memory.IndexRegister = REGS[7];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *
 * ======================================= */
void __bea_callspec__ Addr_SIB_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0, j;
    long MyNumber;
    if (!Security(2, pMyDisasm)) return;
    if (GV.AddressSize >= 32) {
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+3));
    }
    else {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
    (*pMyArgument).ArgType = MEMORY_TYPE;
    if (GV.AddressSize >= 32) {
        GV.DECALAGE_EIP++;
        GV.BASE_  = ((UInt8) *((UInt8*) (UIntPtr)GV.EIP_+2)) & 0x7;
        GV.SCALE_  = (((UInt8) *((UInt8*) (UIntPtr)GV.EIP_+2)) & 0xc0) >> 6;
        GV.INDEX_  = (((UInt8) *((UInt8*) (UIntPtr)GV.EIP_+2)) & 0x38) >> 3;
        j = i;
        i += SIB[GV.SCALE_ ](pMyArgument, j, pMyDisasm);
    }
    else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyArgument).ArgMnemonic, Registers16Bits[6]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[6];
        i += strlen (Registers16Bits[6]);
    }

    if (GV.SYNTAX_ == ATSyntax) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        #endif
        i += 1;
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }

}

/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_EBP_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 5);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.IndexRegister = REGS[7];
    }
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
      #endif
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
}

/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_ESI_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 6);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[5];
    }
    #ifndef BEA_LIGHT_DISASSEMBLY
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
    #endif
}

/* =======================================
 *          ModRM_2
 * ======================================= */
void __bea_callspec__ Addr_EDI_disp32(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
    size_t i = 0;
    long MyNumber;
    if (GV.AddressSize == 16) {
        MyNumber = *((Int16*)(UIntPtr) (GV.EIP_+2));
    }
    else{
        MyNumber = *((Int32*)(UIntPtr) (GV.EIP_+2));
    }
    (*pMyArgument).Memory.Displacement = MyNumber;
    if (GV.SYNTAX_ == ATSyntax) {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i+=2;
    }
    fillModrm0Register(pMyArgument, pMyDisasm, i, 7);
    if (GV.AddressSize == 16) {
      (*pMyArgument).Memory.BaseRegister = REGS[3];
    }
    #ifndef BEA_LIGHT_DISASSEMBLY
    i = strlen ((char*) &(*pMyArgument).ArgMnemonic);
    if (GV.SYNTAX_ == ATSyntax) {
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
        i += 1;
    }
    else {
      i = printDisp32(pMyArgument, i, pMyDisasm, MyNumber);
    }
    #endif
}

void __bea_callspec__ fillModrm3Register(ARGTYPE* pMyArgument, PDISASM pMyDisasm, UInt8 index)
{
  size_t i = 0;
  int index_final;
  GV.MemDecoration = 0;

  if (GV.Register_ == OPMASK_REG) {
    #ifndef BEA_LIGHT_DISASSEMBLY
      (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersOpmask[index]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE+OPMASK_REG;
    (*pMyArgument).Registers = REGS[index];
    (*pMyArgument).ArgSize = 64;
    return;
  }

  if (GV.Register_ == AVX512_REG)
    {
    if (
        (GV.EVEX.state == InUsePrefix) &&
        (GV.EVEX.X == 1)
      ) {
      index_final = (GV.REX.B_ == 1) ? index + 8 + 16 : index + 0 + 16;
    }
    else {
      index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
    }
    #ifndef BEA_LIGHT_DISASSEMBLY
      (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersAVX512[index_final]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE + AVX512_REG + REGS[index_final];
    (*pMyArgument).ArgSize = 512;
    return;
  }
  if (GV.Register_ == AVX_REG) {
    if (
        (GV.EVEX.state == InUsePrefix) &&
        (GV.EVEX.X == 1)
      ) {
      index_final = (GV.REX.B_ == 1) ? index + 8 + 16 : index + 0 + 16;
    }
    else {
      index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
    }
    #ifndef BEA_LIGHT_DISASSEMBLY
      (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersAVX[index_final]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE + AVX_REG + REGS[index_final];
    (*pMyArgument).ArgSize = 256;
    return;
  }
  if (GV.Register_ == MPX_REG)
    {
    index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
    #ifndef BEA_LIGHT_DISASSEMBLY
      (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersMPX[index_final]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE+MPX_REG;
    (*pMyArgument).Registers = REGS[index_final];
    (*pMyArgument).ArgSize = 128;
    return;
  }
  if (GV.Register_ == MMX_REG)
    {

      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersMMX[index+0]);
      #endif
      (*pMyArgument).ArgType = REGISTER_TYPE+MMX_REG;
      (*pMyArgument).Registers = REGS[index+0];
      (*pMyArgument).ArgSize = 64;

      return;
  }

  if (GV.Register_ == SSE_REG)
    {
      if (
          (GV.EVEX.state == InUsePrefix) &&
          (GV.EVEX.X == 1)
        ) {
        index_final = (GV.REX.B_ == 1) ? index + 8 + 16 : index + 0 + 16;
      }
      else {
        index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
      }
      #ifndef BEA_LIGHT_DISASSEMBLY
        (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, RegistersSSE[index_final]);
      #endif
      (*pMyArgument).ArgType = REGISTER_TYPE+SSE_REG;
      (*pMyArgument).Registers = REGS[index_final];
      (*pMyArgument).ArgSize = 128;
      return;
  }
  if (GV.OperandSize == 64) {
    index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[index_final]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
    (*pMyArgument).Registers = REGS[index_final];
    (*pMyArgument).ArgSize = 64;
  }
  else if (GV.OperandSize == 32) {
    index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[index_final]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
    (*pMyArgument).Registers = REGS[index_final];
    (*pMyArgument).ArgSize = 32;
  }
  else if (GV.OperandSize == 16) {
    index_final = (GV.REX.B_ == 1) ? index + 8 : index + 0;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers16Bits[index_final]);
    #endif
    (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
    (*pMyArgument).Registers = REGS[index_final];
    (*pMyArgument).ArgSize = 16;
  }
  else if (GV.OperandSize == 8) {
    OperandSize8RM(pMyArgument, pMyDisasm, i, index);
  }
}

void __bea_callspec__ OperandSize8RM(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i, int index)
{
  if (GV.REX.B_ == 1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers8Bits[index+8]);
      #endif
      (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
      (*pMyArgument).Registers = REGS[index+8];
      (*pMyArgument).ArgSize = 8;
  }
  else {
      if (GV.REX.state == 0) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers8BitsLegacy[index+0]);
          #endif
          (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
          (*pMyArgument).Registers = REGS8BITS[index+0];
          (*pMyArgument).ArgSize = 8;
      }
      else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyArgument).ArgMnemonic+i, Registers8Bits[index+0]);
          #endif
          (*pMyArgument).ArgType = REGISTER_TYPE+GENERAL_REG;
          (*pMyArgument).Registers = REGS[index+0];
          (*pMyArgument).ArgSize = 8;
      }
  }

}

/* =======================================
 *          ModRM_3
 * ======================================= */
void __bea_callspec__ _rEAX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 0);
}

void __bea_callspec__ _rECX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 1);
}

void __bea_callspec__ _rEDX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 2);
}

void __bea_callspec__ _rEBX(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 3);
}

void __bea_callspec__ _rESP(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 4);
}

void __bea_callspec__ _rEBP(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 5);
}

void __bea_callspec__ _rESI(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 6);
}

void __bea_callspec__ _rEDI(ARGTYPE* pMyArgument, PDISASM pMyDisasm)
{
  fillModrm3Register(pMyArgument, pMyDisasm, 7);
}

/* =======================================
 *              SIB
 * ======================================= */

size_t __bea_callspec__ interpretBase(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm)
{
  size_t j;
  if ((GV.BASE_  == 5) && (GV.MOD_ == 0)) {
      GV.DECALAGE_EIP += 4;
      if (!Security(7, pMyDisasm)) return i;
      j = i;
      #ifndef BEA_LIGHT_DISASSEMBLY
         i+= CopyFormattedNumber(pMyDisasm, (char*) (*pMyArgument).ArgMnemonic+j,"%.8X",(Int64) *((UInt32*)(UIntPtr) (GV.EIP_+3)));
      #endif
      (*pMyArgument).Memory.Displacement = *((UInt32*)(UIntPtr) (GV.EIP_+3));

  }
  else {

    if (GV.SYNTAX_ == ATSyntax) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(%");
      #endif
      i += 2;
    }
    if (GV.AddressSize == 64) {
      if (GV.REX.B_ == 0) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[GV.BASE_ ]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[GV.BASE_ ];
        i += strlen(Registers64Bits[GV.BASE_ ]);
      }
      else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[GV.BASE_ +8]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[GV.BASE_ +8];
        i += strlen( Registers64Bits[GV.BASE_ +8]);
      }
    }
    else if (GV.AddressSize == 32) {
      if (GV.REX.B_ == 0) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[GV.BASE_ ]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[GV.BASE_ ];
        i += strlen( Registers32Bits[GV.BASE_ ]);
      }
      else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[GV.BASE_ +8]);
        #endif
        (*pMyArgument).Memory.BaseRegister = REGS[GV.BASE_ +8];
        i += strlen( Registers32Bits[GV.BASE_ +8]);
      }
    }
  }
  return i;
}

size_t __bea_callspec__ interpretIndex(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm, UInt8 scale)
{
  if (GV.INDEX_  != 4 || GV.REX.X_) {
      i = printSeparator(pMyArgument, i, pMyDisasm);

      if (GV.AddressSize == 64) {
          if (GV.REX.X_ == 0) {
              #ifndef BEA_LIGHT_DISASSEMBLY
                 (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[GV.INDEX_ ]);
              #endif
              (*pMyArgument).Memory.IndexRegister = REGS[GV.INDEX_ ];
              i += strlen( Registers64Bits[GV.INDEX_ ]);
          }
          else {
              #ifndef BEA_LIGHT_DISASSEMBLY
                 (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers64Bits[GV.INDEX_ +8]);
              #endif
              (*pMyArgument).Memory.IndexRegister = REGS[GV.INDEX_ +8];
              i += strlen( Registers64Bits[GV.INDEX_ +8]);
          }
      }
      else if (GV.AddressSize == 32) {
          if (GV.REX.X_ == 0) {
              #ifndef BEA_LIGHT_DISASSEMBLY
                 (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[GV.INDEX_ ]);
              #endif
              (*pMyArgument).Memory.IndexRegister = REGS[GV.INDEX_ ];
              i += strlen( Registers32Bits[GV.INDEX_ ]);
          }
          else {
              #ifndef BEA_LIGHT_DISASSEMBLY
                 (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, Registers32Bits[GV.INDEX_ +8]);
              #endif
              (*pMyArgument).Memory.IndexRegister = REGS[GV.INDEX_ +8];
              i += strlen( Registers32Bits[GV.INDEX_ +8]);
          }
      }
      (*pMyArgument).Memory.Scale = scale;
      if (scale != 1) {
        if (GV.SYNTAX_ == ATSyntax) {
          if ((GV.BASE_  != 5) || (GV.INDEX_  != 4 || GV.REX.X_)) {
            #ifndef BEA_LIGHT_DISASSEMBLY
              char str[2] = "";
              (void) sprintf(str, ",%d", scale);
              (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, str);
            #endif
            i+=2;
          }
        }
        else {
          #ifndef BEA_LIGHT_DISASSEMBLY
            char str[2] = "";
            (void) sprintf(str, "*%d", scale);
            (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, str);
          #endif
          i+=2;
        }
      }

  }
  if ((GV.SYNTAX_ == ATSyntax) && ((GV.BASE_  != 5) || (GV.INDEX_  != 4 || GV.REX.X_))) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
      #endif
      i++;
  }
  return i;

}



size_t __bea_callspec__ printVSIBRegisters(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i, Int32 index)
{

  if (GV.VSIB_ == SSE_REG) {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, RegistersSSE[index]);
    #endif
    i += strlen( RegistersSSE[index]);
  }
  else if (GV.VSIB_ == AVX_REG) {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, RegistersAVX[index]);
    #endif
    i += strlen( RegistersAVX[index]);
  }
  else if (GV.VSIB_ == AVX512_REG) {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, RegistersAVX512[index]);
    #endif
    i += strlen( RegistersAVX512[index]);
  }
  (*pMyArgument).Memory.IndexRegister = REGS[index];

  return i;

}

size_t __bea_callspec__ printSIBScale(ARGTYPE* pMyArgument, PDISASM pMyDisasm, size_t i, UInt8 scale)
{

  (*pMyArgument).Memory.Scale = scale;
  if (scale != 1) {
    if (GV.SYNTAX_ == ATSyntax) {
      if (GV.BASE_  != 5) {
        #ifndef BEA_LIGHT_DISASSEMBLY
          char str[2] = "";
          (void) sprintf(str, ",%d", scale);
          (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, str);
        #endif
        i+=2;
      }
    }
    else {
      #ifndef BEA_LIGHT_DISASSEMBLY
        char str[2] = "";
        (void) sprintf(str, "*%d", scale);
        (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, str);
      #endif
      i+=2;
    }
  }

  return i;

}

size_t __bea_callspec__ printSeparator(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm)
{
  if (GV.SYNTAX_ == ATSyntax) {
    if (GV.BASE_  == 5) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "(,%");
      #endif
      i+=3;
    }
    else {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ",%");
      #endif
      i+=2;
    }
  }
  else {
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, "+");
    #endif
    i+=1;
  }
  return i;
}


size_t __bea_callspec__ interpretVSIBIndex(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm, UInt8 scale)
{
  int index_final;
  i = printSeparator(pMyArgument, i, pMyDisasm);

  if (GV.AddressSize >= 32) {
    if (GV.EVEX.X == 0) {
      index_final = (GV.EVEX.V == 0) ? GV.INDEX_ : GV.INDEX_ + 16;
    }
    else {
      index_final = (GV.EVEX.V == 0) ? GV.INDEX_ + 8 : GV.INDEX_ + 8 + 16;
    }
    i = printVSIBRegisters(pMyArgument, pMyDisasm, i, index_final);
  }
  i = printSIBScale(pMyArgument, pMyDisasm, i, scale);

  if ((GV.SYNTAX_ == ATSyntax) && (GV.BASE_  != 5)) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy((char*) (*pMyArgument).ArgMnemonic+i, ")");
      #endif
      i++;
  }
  return i;
}

/* =======================================
 *
 * ======================================= */
size_t __bea_callspec__ SIB_0(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm)
{
  i = interpretBase(pMyArgument, i, pMyDisasm);
  if ((GV.VEX.state == InUsePrefix) && (GV.VSIB_ != 0)) {
    i = interpretVSIBIndex(pMyArgument, i, pMyDisasm, 1);
  }
  else {
    i = interpretIndex(pMyArgument, i, pMyDisasm, 1);
  }

  return i;
}

/* =======================================
 *
 * ======================================= */
size_t __bea_callspec__ SIB_1(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm)
{
  i = interpretBase(pMyArgument, i, pMyDisasm);
  if ((GV.VEX.state == InUsePrefix) && (GV.VSIB_ != 0)) {
    i = interpretVSIBIndex(pMyArgument, i, pMyDisasm, 2);
  }
  else {
    i = interpretIndex(pMyArgument, i, pMyDisasm, 2);
  }  return i;
}

/* =======================================
 *
 * ======================================= */
size_t __bea_callspec__ SIB_2(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm)
{
  i = interpretBase(pMyArgument, i, pMyDisasm);
  if ((GV.VEX.state == InUsePrefix) && (GV.VSIB_ != 0)) {
    i = interpretVSIBIndex(pMyArgument, i, pMyDisasm, 4);
  }
  else {
    i = interpretIndex(pMyArgument, i, pMyDisasm, 4);
  }
  return i;
}

/* =======================================
 *
 * ======================================= */
size_t __bea_callspec__ SIB_3(ARGTYPE* pMyArgument, size_t i, PDISASM pMyDisasm)
{
  i = interpretBase(pMyArgument, i, pMyDisasm);
  if ((GV.VEX.state == InUsePrefix) && (GV.VSIB_ != 0)) {
    i = interpretVSIBIndex(pMyArgument, i, pMyDisasm, 8);
  }
  else {
    i = interpretIndex(pMyArgument, i, pMyDisasm, 8);
  }
  return i;

}
