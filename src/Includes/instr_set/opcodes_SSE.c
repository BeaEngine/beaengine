/*
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
 *
 * @author : beaengine@gmail.com

 * ====================================================================
 *      0x 0f 58
 * ==================================================================== */
void __bea_callspec__ addps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaddsd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3qword;
            GV.SSE_ = 0;

            /* FillFlags(pMyDisasm,125); */

        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "addsd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaddss ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }

            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3dword;
            GV.SSE_ = 0;


            /* FillFlags(pMyDisasm,125); */

        }
        else {
            (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "addss ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaddpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

            /* FillFlags(pMyDisasm,125); */

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "addpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaddps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

            /* FillFlags(pMyDisasm,125); */

        }
        else {

            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "addps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}

/* ====================================================================
 *      0x 0f d0
 * ==================================================================== */
void __bea_callspec__ addsubpd_(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+SIMD_FP_PACKED;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaddsubps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            if (GV.VEX.L == 0) {
                GV.SSE_ = 1;
                GyEy(pMyDisasm);
                fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
                GV.MemDecoration = Arg3_m128_xmm;
                GV.SSE_ = 0;
            }
            else {
                GV.AVX_ = 1;
                GyEy(pMyDisasm);
                fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
                GV.MemDecoration = Arg3_m256_ymm;
                GV.AVX_ = 0;

            }
            /* FillFlags(pMyDisasm,125); */

        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SIMD_FP_PACKED;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "addsubps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
            (*pMyDisasm).Argument2.ArgSize = 128;
        }
    }

    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+SIMD_FP_PACKED;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vaddsubpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            if (GV.VEX.L == 0) {
                GV.SSE_ = 1;
                GyEy(pMyDisasm);
                fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
                GV.MemDecoration = Arg3_m128d_xmm;
                GV.SSE_ = 0;
            }
            else {
                GV.AVX_ = 1;
                GyEy(pMyDisasm);
                fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
                GV.MemDecoration = Arg3_m256d_ymm;
                GV.AVX_ = 0;

            }

            /* FillFlags(pMyDisasm,125); */

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SIMD_FP_PACKED;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "addsubpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
            (*pMyDisasm).Argument2.ArgSize = 128;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 55
 * ==================================================================== */
void __bea_callspec__ andnps_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vandnpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "andnpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vandnps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "andnps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}


/* ====================================================================
 *      0x 0f 54
 * ==================================================================== */
void __bea_callspec__ andps_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

      if (GV.VEX.state == InUsePrefix) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vandpd ");
        #endif

        if (GV.VEX.opcode == 0xc4) {
          /* using VEX3Bytes */
          if (GV.REX.W_ == 0x1) {
              GV.OperandSize = 64;
          }
        }
        ArgsVEX(pMyDisasm);
      }
      else {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128d_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "andpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
    }
    else {
        if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vandps ");
          #endif

          if (GV.VEX.opcode == 0xc4) {
            /* using VEX3Bytes */
            if (GV.REX.W_ == 0x1) {
                GV.OperandSize = 64;
            }
          }
          ArgsVEX(pMyDisasm);
        }
        else {
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "andps ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
}


/* ====================================================================
 *      0x 0f 3a 0d
 * ==================================================================== */
void __bea_callspec__ blendpd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {


        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + PACKED_BLENDING_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vblendpd ");
            #endif

            if (GV.VEX.L == 0) {
                GV.SSE_ = 1;
                GxEx(pMyDisasm);
                GV.MemDecoration = Arg2_m128_xmm;
                GV.SSE_ = 0;
            }
            else {
                GV.AVX_ = 1;
                GxEx(pMyDisasm);
                GV.MemDecoration = Arg2_m256_ymm;
                GV.AVX_ = 0;

            }

            GV.ImmediatSize = 8;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
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
            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+PACKED_BLENDING_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "blendpd ");
            #endif
            GV.ImmediatSize = 8;
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
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


/* ====================================================================
 *      0x 0f 3a 0c
 * ==================================================================== */
void __bea_callspec__ blendps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + PACKED_BLENDING_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vblendps ");
            #endif

            if (GV.VEX.L == 0) {
                GV.SSE_ = 1;
                GxEx(pMyDisasm);
                GV.MemDecoration = Arg2_m128_xmm;
                GV.SSE_ = 0;
            }
            else {
                GV.AVX_ = 1;
                GxEx(pMyDisasm);
                GV.MemDecoration = Arg2_m256_ymm;
                GV.AVX_ = 0;

            }

            GV.ImmediatSize = 8;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
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
            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+PACKED_BLENDING_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "blendps ");
            #endif
            GV.ImmediatSize = 8;
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
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


/* ====================================================================
 *      0x 0f 38 15 / 0x 0f 3a 4b
 * ==================================================================== */
void __bea_callspec__ blendvpd_(PDISASM pMyDisasm)
{
  UInt8 Imm8;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
      if (GV.VEX.state == InUsePrefix) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vblendvpd ");
        #endif

        if (GV.VEX.opcode == 0xc4) {
          /* using VEX3Bytes */
          if (GV.REX.W_ == 0x1) {
            GV.ERROR_OPCODE = UD_;
          }
        }
        if (GV.VEX.L == 0) {
          GV.SSE_ = 1;
          GV.MemDecoration = Arg3_m128_xmm;
          GyEy(pMyDisasm);
          fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
          GV.EIP_++;
          if (!Security(0, pMyDisasm)) return;
          Imm8 = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
          fillRegister((Imm8 >> 4) & 0xF, &(*pMyDisasm).Argument4, pMyDisasm);
          GV.SSE_ = 0;
        }
        else {
          GV.AVX_ = 1;
          GV.MemDecoration = Arg3_m256_ymm;
          GyEy(pMyDisasm);
          fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
          GV.EIP_++;
          if (!Security(0, pMyDisasm)) return;
          Imm8 = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
          fillRegister((Imm8 >> 4) & 0xF, &(*pMyDisasm).Argument4, pMyDisasm);
          GV.AVX_ = 0;
        }
      }
      else {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128d_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+PACKED_BLENDING_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
          (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "blendvpd ");
        #endif
        GV.SSE_ = 1;
        (*pMyDisasm).Argument3.AccessMode = READ;
        (*pMyDisasm).Argument3.ArgType = REGISTER_TYPE+SSE_REG+REG0;
        (*pMyDisasm).Argument3.ArgSize = 128;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((char*) (*pMyDisasm).Argument3.ArgMnemonic, RegistersSSE[0]);
        #endif
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 38 14
 * ==================================================================== */
void __bea_callspec__ blendvps_(PDISASM pMyDisasm)
{
    UInt8 Imm8;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
      if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vblendvps ");
          #endif
          if (GV.VEX.opcode == 0xc4) {
            /* using VEX3Bytes */
            if (GV.REX.W_ == 0x1) {
              GV.ERROR_OPCODE = UD_;
            }
          }
          if (GV.VEX.L == 0) {
            GV.SSE_ = 1;
            GV.MemDecoration = Arg3_m128_xmm;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            Imm8 = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            fillRegister((Imm8 >> 4) & 0xF, &(*pMyDisasm).Argument4, pMyDisasm);
            GV.SSE_ = 0;
          }
          else {
            GV.AVX_ = 1;
            GV.MemDecoration = Arg3_m256_ymm;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            Imm8 = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            fillRegister((Imm8 >> 4) & 0xF, &(*pMyDisasm).Argument4, pMyDisasm);
            GV.AVX_ = 0;
          }
        }
        else {
          GV.OperandSize = GV.OriginalOperandSize;
          (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+PACKED_BLENDING_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
            (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "blendvps ");
          #endif
          GV.SSE_ = 1;
          (*pMyDisasm).Argument3.AccessMode = READ;
          (*pMyDisasm).Argument3.ArgType = REGISTER_TYPE+SSE_REG+REG0;
          (*pMyDisasm).Argument3.ArgSize = 128;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((char*) (*pMyDisasm).Argument3.ArgMnemonic, RegistersSSE[0]);
          #endif
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
      FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f c2
 * ==================================================================== */
void __bea_callspec__ cmpps_VW(PDISASM pMyDisasm)
{
    UInt8 Imm8;
    char pseudoOpcodes_sd[0x20][16] = {
        "vcmpeqsd ",
        "vcmpltsd ",
        "vcmplesd ",
        "vcmpunordsd ",
        "vcmpneqsd ",
        "vcmpnltsd ",
        "vcmpnlesd ",
        "vcmpordsd ",
        "vcmpeq_uqsd ",
        "vcmpngesd ",
        "vcmpngtsd ",
        "vcmpfalsesd ",
        "vcmpneq_oqsd ",
        "vcmpgesd ",
        "vcmpgtsd ",
        "vcmptruesd ",
        "vcmpeq_ossd ",
        "vcmplt_oqsd ",
        "vcmple_oqsd ",
        "vcmpunord_ssd ",
        "vcmpneq_ussd ",
        "vcmpnlt_uqsd ",
        "vcmpnle_uqsd ",
        "vcmpord_ssd ",
        "vcmpeq_ussd ",
        "vcmpnge_uqsd ",
        "vcmpngt_uqsd ",
        "vcmpfalse_ossd ",
        "vcmpneq_ossd ",
        "vcmpge_oqsd ",
        "vcmpgt_oqsd ",
        "vcmptrue_ussd "
    };

    char pseudoOpcodes_ss[0x20][16] = {
        "vcmpeqss ",
        "vcmpltss ",
        "vcmpless ",
        "vcmpunordss ",
        "vcmpneqss ",
        "vcmpnltss ",
        "vcmpnless ",
        "vcmpordss ",
        "vcmpeq_uqss ",
        "vcmpngess ",
        "vcmpngtss ",
        "vcmpfalsess ",
        "vcmpneq_oqss ",
        "vcmpgess ",
        "vcmpgtss ",
        "vcmptruess ",
        "vcmpeq_osss ",
        "vcmplt_oqss ",
        "vcmple_oqss ",
        "vcmpunord_sss ",
        "vcmpneq_usss ",
        "vcmpnlt_uqss ",
        "vcmpnle_uqss ",
        "vcmpord_sss ",
        "vcmpeq_usss ",
        "vcmpnge_uqss ",
        "vcmpngt_uqss ",
        "vcmpfalse_osss ",
        "vcmpneq_osss ",
        "vcmpge_oqss",
        "vcmpgt_oqss ",
        "vcmptrue_usss "
    };

    char pseudoOpcodes_pd[0x20][16] = {
        "vcmpeqpd ",
        "vcmpltpd ",
        "vcmplepd ",
        "vcmpunordpd ",
        "vcmpneqpd ",
        "vcmpnltpd ",
        "vcmpnlepd ",
        "vcmpordpd ",
        "vcmpeq_uqpd ",
        "vcmpngepd ",
        "vcmpngtpd ",
        "vcmpfalsepd ",
        "vcmpneq_oqpd ",
        "vcmpgepd ",
        "vcmpgtpd ",
        "vcmptruepd ",
        "vcmpeq_ospd ",
        "vcmplt_oqpd ",
        "vcmple_oqpd ",
        "vcmpunord_spd ",
        "vcmpneq_uspd ",
        "vcmpnlt_uqpd ",
        "vcmpnle_uqpd ",
        "vcmpord_spd ",
        "vcmpeq_uspd ",
        "vcmpnge_uqpd ",
        "vcmpngt_uqpd ",
        "vcmpfalse_ospd ",
        "vcmpneq_ospd ",
        "vcmpge_oqpd ",
        "vcmpgt_oqpd ",
        "vcmptrue_uspd "
    };

    char pseudoOpcodes_ps[0x20][16] = {
        "vcmpeqps ",
        "vcmpltps ",
        "vcmpleps ",
        "vcmpunordps ",
        "vcmpneqps ",
        "vcmpnltps ",
        "vcmpnleps ",
        "vcmpordps ",
        "vcmpeq_uqps ",
        "vcmpngeps ",
        "vcmpngtps ",
        "vcmpfalseps ",
        "vcmpneq_oqps ",
        "vcmpgeps ",
        "vcmpgtps ",
        "vcmptrueps ",
        "vcmpeq_osps ",
        "vcmplt_oqps ",
        "vcmple_oqps ",
        "vcmpunord_sps ",
        "vcmpneq_usps ",
        "vcmpnlt_uqps ",
        "vcmpnle_uqps ",
        "vcmpord_sps ",
        "vcmpeq_usps ",
        "vcmpnge_uqps ",
        "vcmpngt_uqps ",
        "vcmpfalse_osps ",
        "vcmpneq_osps ",
        "vcmpge_oqps ",
        "vcmpgt_oqps ",
        "vcmptrue_usps "
    };


    /* ========= 0xf2 */
    GV.ImmediatSize = 8;
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + COMPARISON_INSTRUCTION;
            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vcmpsd ");
            #endif*/

            ArgsVEX(pMyDisasm);

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument4.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument4.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x1F;

            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, pseudoOpcodes_sd[Imm8]);
            #endif

            /* FillFlags(pMyDisasm,125); */

        }
        else {

            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+COMPARISON_INSTRUCTION;

            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpsd ");
            #endif*/

            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument3.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x7;

            if (Imm8 == 0x0) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpeqsd ");
                #endif
            }
            else if (Imm8 == 0x1) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpltsd ");
                #endif
            }
            else if (Imm8 == 0x2) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmplesd ");
                #endif
            }
            else if (Imm8 == 0x3) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpunordsd ");
                #endif
            }
            else if (Imm8 == 0x4) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpneqsd ");
                #endif
            }
            else if (Imm8 == 0x5) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnltsd ");
                #endif
            }
            else if (Imm8 == 0x6) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnlesd ");
                #endif
            }
            else if (Imm8 == 0x7) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpordsd ");
                #endif
            }
        }


    }
    /* ========== 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + COMPARISON_INSTRUCTION;
            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vcmpss ");
            #endif*/

            ArgsVEX(pMyDisasm);

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument4.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument4.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x1F;

            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, pseudoOpcodes_ss[Imm8]);
            #endif

            /* FillFlags(pMyDisasm,125); */

        }
        else {

            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+COMPARISON_INSTRUCTION;

            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpsd ");
            #endif*/


            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument3.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x7;

            if (Imm8 == 0x0) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpeqss ");
                #endif
            }
            else if (Imm8 == 0x1) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpltss ");
                #endif
            }
            else if (Imm8 == 0x2) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpless ");
                #endif
            }
            else if (Imm8 == 0x3) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpunordss ");
                #endif
            }
            else if (Imm8 == 0x4) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpneqss ");
                #endif
            }
            else if (Imm8 == 0x5) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnltss ");
                #endif
            }
            else if (Imm8 == 0x6) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnless ");
                #endif
            }
            else if (Imm8 == 0x7) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpordsd ");
                #endif
            }
        }

    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {


        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + COMPARISON_INSTRUCTION;
            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vcmppd ");
            #endif*/

            ArgsVEX(pMyDisasm);

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument4.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument4.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x1F;

            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, pseudoOpcodes_pd[Imm8]);
            #endif

            /* FillFlags(pMyDisasm,125); */

        }
        else {

            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+COMPARISON_INSTRUCTION;

            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmppd ");
            #endif*/


            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument3.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x7;

            if (Imm8 == 0x0) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpeqpd ");
                #endif
            }
            else if (Imm8 == 0x1) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpltpd ");
                #endif
            }
            else if (Imm8 == 0x2) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmplepd ");
                #endif
            }
            else if (Imm8 == 0x3) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpunordpd ");
                #endif
            }
            else if (Imm8 == 0x4) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpneqpd ");
                #endif
            }
            else if (Imm8 == 0x5) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnltpd ");
                #endif
            }
            else if (Imm8 == 0x6) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnlepd ");
                #endif
            }
            else if (Imm8 == 0x7) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpordpd ");
                #endif
            }
        }
    }
    else {


        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION + COMPARISON_INSTRUCTION;
            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vcmpps ");
            #endif*/

            if (GV.VEX.L == 0) {
                GV.SSE_ = 1;
                GyEy(pMyDisasm);
                fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
                GV.MemDecoration = Arg3_m128_xmm;
                GV.SSE_ = 0;
            }
            else {
                GV.AVX_ = 1;
                GyEy(pMyDisasm);
                fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
                GV.MemDecoration = Arg3_m256_ymm;
                GV.AVX_ = 0;

            }

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument4.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument4.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x1F;

            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, pseudoOpcodes_ps[Imm8]);
            #endif

            /* FillFlags(pMyDisasm,125); */

        }
        else {

            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+COMPARISON_INSTRUCTION;

            /* use pseudo-opcode instead */
            /*#ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmppd ");
            #endif*/


            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;

            (*pMyDisasm).Argument1.AccessMode = READ;
            GV.EIP_++;
            if (!Security(0, pMyDisasm)) return;
            GV.third_arg = 1;
            (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
            (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
            (*pMyDisasm).Argument3.ArgSize = 8;

            Imm8 = (*pMyDisasm).Instruction.Immediat & 0x7;

            if (Imm8 == 0x0) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpeqps ");
                #endif
            }
            else if (Imm8 == 0x1) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpltps ");
                #endif
            }
            else if (Imm8 == 0x2) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpleps ");
                #endif
            }
            else if (Imm8 == 0x3) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpunordps ");
                #endif
            }
            else if (Imm8 == 0x4) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpneqps ");
                #endif
            }
            else if (Imm8 == 0x5) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnltps ");
                #endif
            }
            else if (Imm8 == 0x6) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpnleps ");
                #endif
            }
            else if (Imm8 == 0x7) {
                #ifndef BEA_LIGHT_DISASSEMBLY
                   (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cmpordps ");
                #endif
            }
        }
    }


}


/* ====================================================================
 *      0x 0f 38 f0
 * ==================================================================== */
void __bea_callspec__ crc32_GvEb(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+ACCELERATOR_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "crc32 ");
        #endif
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
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        }

        if (GV.OperandSize == 16) {
            GV.OperandSize = 32;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.OperandSize = 16;
        }
        else {
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        }
        GV.EIP_ += GV.DECALAGE_EIP+2;
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 f1
 * ==================================================================== */
void __bea_callspec__ crc32_GvEv(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+ACCELERATOR_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "crc32 ");
        #endif

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

        if (GV.OperandSize == 16) {
            GV.OperandSize = 32;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.OperandSize = 16;
        }
        else {
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        }
        GV.EIP_ += GV.DECALAGE_EIP+2;
    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 2f
 * ==================================================================== */
void __bea_callspec__ comiss_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "comisd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "comiss ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 5a
 * ==================================================================== */
void __bea_callspec__ cvtps2pd_(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtsd2ss ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========== 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtss2sd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtpd2ps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtps2pd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 5b
 * ==================================================================== */
void __bea_callspec__ cvtdq2ps_(PDISASM pMyDisasm)
{
    /* ========== 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvttps2dq ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtps2dq ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtdq2ps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 2a
 * ==================================================================== */
void __bea_callspec__ cvtpi2ps_(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtsi2sd ");
        #endif
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2qword;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 1;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.SSE_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2dword;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 1;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.SSE_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    /* ========== 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtsi2ss ");
        #endif
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2qword;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 1;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.SSE_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2dword;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 1;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.SSE_ = 0;
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtpi2pd ");
        #endif
        GV.MemDecoration = Arg2qword;
        GV.MMX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.MMX_ = 0;
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    else {
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtpi2ps ");
        #endif
        GV.MemDecoration = Arg2qword;
        GV.MMX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.MMX_ = 0;
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
}


/* ====================================================================
 *      0x 0f 2d
 * ==================================================================== */
void __bea_callspec__ cvtps2pi_(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtsd2si ");
        #endif
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2qword;
            GV.SSE_ = 1;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 0;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2qword;
            GV.SSE_ = 1;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 0;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    /* ========== 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtss2si ");
        #endif
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2dword;
            GV.SSE_ = 1;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 0;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2dword;
            GV.SSE_ = 1;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 0;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtpd2pi ");
        #endif
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.MMX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    else {
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtps2pi ");
        #endif
        GV.MemDecoration = Arg2qword;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.MMX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
}


/* ====================================================================
 *      0x 0f 2c
 * ==================================================================== */
void __bea_callspec__ cvttps2pi_(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvttsd2si ");
        #endif
        if (GV.REX.W_ == 1) {
            GV.MemDecoration = Arg2qword;
            GV.SSE_ = 1;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 0;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
        else {
            GV.MemDecoration = Arg2qword;
            GV.SSE_ = 1;
            MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.SSE_ = 0;
            Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.EIP_+= GV.DECALAGE_EIP+2;
        }
    }
    /* ========== 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvttss2si ");
        #endif
        GV.MemDecoration = Arg2dword;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvttpd2pi ");
        #endif
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.MMX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    else {
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvttps2pi ");
        #endif
        GV.MemDecoration = Arg2qword;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.MMX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
}


/* ====================================================================
 *      0x 0f e6
 * ==================================================================== */
void __bea_callspec__ cvtpd2dq_(PDISASM pMyDisasm)
{
    /* ========== 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtpd2dq ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========== 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvtdq2pd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CONVERSION_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "cvttpd2dq ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 3a 41
 * ==================================================================== */
void __bea_callspec__ dppd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+DOT_PRODUCT;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "dppd ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}

/* ====================================================================
 *      0x 0f 3a 40
 * ==================================================================== */
void __bea_callspec__ dpps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+DOT_PRODUCT;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "dpps ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}

/* ====================================================================
 *      0x 0f 3a 17
 * ==================================================================== */
void __bea_callspec__ extractps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1dword;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "extractps ");
        #endif
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 7c
 * ==================================================================== */
void __bea_callspec__ haddpd_VW(PDISASM pMyDisasm)
{

  if (GV.VEX.state == InUsePrefix) {
    if (GV.EVEX.state == InUsePrefix) {
      FailDecode(pMyDisasm);
    }
    else {
      if (GV.VEX.pp == 0x1) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vhaddpd ");
        #endif
        ArgsVEX(pMyDisasm);
      }
      else if (GV.VEX.pp == 0x3){
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vhaddps ");
        #endif
        ArgsVEX(pMyDisasm);
      }
      else {
        FailDecode(pMyDisasm);
      }
    }

  }
  else {
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SIMD_FP_HORIZONTAL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "haddpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SIMD_FP_HORIZONTAL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "haddps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
  }

}


/* ====================================================================
 *      0x 0f 7d
 * ==================================================================== */
void __bea_callspec__ hsubpd_VW(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.EVEX.state == InUsePrefix) {
      FailDecode(pMyDisasm);
    }
    else {
      if (GV.VEX.pp == 0x1) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vhsubpd ");
        #endif
        ArgsVEX(pMyDisasm);
      }
      else if (GV.VEX.pp == 0x3){
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vhsubps ");
        #endif
        ArgsVEX(pMyDisasm);
      }
      else {
        FailDecode(pMyDisasm);
      }
    }

  }
  else {
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
      GV.OperandSize = GV.OriginalOperandSize;
      (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
      GV.MemDecoration = Arg2_m128_xmm;
      (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SIMD_FP_HORIZONTAL;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "hsubpd ");
      #endif
      GV.SSE_ = 1;
      GxEx(pMyDisasm);
      GV.SSE_ = 0;
    }
    else {
      GV.MemDecoration = Arg2_m128_xmm;
      (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SIMD_FP_HORIZONTAL;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "hsubps ");
      #endif
      GV.SSE_ = 1;
      GxEx(pMyDisasm);
      GV.SSE_ = 0;
    }
  }
}


/* ====================================================================
 *      0x 0f 3a 21
 * ==================================================================== */
void __bea_callspec__ insertps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "insertps ");
        #endif
        GV.SSE_ = 1;
        GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
        if (GV.MOD_== 0x3) {
            GV.MemDecoration = Arg2qword;
        }
        else {
            GV.MemDecoration = Arg2dword;
        }

        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);


        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}



/* ====================================================================
 *      0x 0f f0
 * ==================================================================== */
void __bea_callspec__ lddqu_(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dqword;
        (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+SPECIALIZED_128bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "lddqu ");
        #endif
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_+= GV.DECALAGE_EIP+2;
    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f f7
 * ==================================================================== */
void __bea_callspec__ maskmovq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CACHEABILITY_CONTROL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "maskmovdqu ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+CACHEABILITY_CONTROL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "maskmovq ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 28
 * ==================================================================== */
void __bea_callspec__ movaps_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movapd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movaps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 29
 * ==================================================================== */
void __bea_callspec__ movaps_WV(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movapd ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movaps ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 16
 * ==================================================================== */
void __bea_callspec__ movhps_VM(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
      if (GV.MOD_ == 0x3) {
        FailDecode(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        ArgsVEX(pMyDisasm);
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovhpd ");
        #endif
        GV.MemDecoration = Arg3qword;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovshdup ");
      #endif
      ArgsVEX_GxEx(pMyDisasm);
    }
    else if (GV.VEX.pp == 0x0) {
      (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
      ArgsVEX(pMyDisasm);
      if (GV.MOD_ == 0x3) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovlhps ");
        #endif
      }
      else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovhps ");
        #endif
        GV.MemDecoration = Arg3qword;
      }
    }
  }
  else {
    /* ========= 0xf3 */
    if (GV.PrefRepe == 1) {
      (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
      GV.MemDecoration = Arg2_m128_xmm;
      (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+DATA_TRANSFER;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movshdup ");
      #endif
      GV.SSE_ = 1;
      GxEx(pMyDisasm);
      GV.SSE_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
      GV.OperandSize = GV.OriginalOperandSize;
      (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
      GV.MemDecoration = Arg2qword;
      (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movhpd ");
      #endif
      GV.SSE_ = 1;
      GxEx(pMyDisasm);
      GV.SSE_ = 0;
    }
    else {
      GV.MemDecoration = Arg2qword;
      (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+DATA_TRANSFER;
      GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
      if (GV.MOD_== 0x3) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movlhps ");
        #endif
      }
      else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movhps ");
        #endif
      }
      GV.SSE_ = 1;
      GxEx(pMyDisasm);
      GV.SSE_ = 0;
    }
  }
}


/* ====================================================================
 *      0x 0f 17
 * ==================================================================== */
void __bea_callspec__ movhps_MV(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
      if (GV.MOD_== 0x3) {
          FailDecode(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovhpd ");
        #endif
        GV.MemDecoration = Arg1qword;
      }
    }
    else {
      GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
      if (GV.MOD_== 0x3) {
          FailDecode(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;

        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovhps ");
        #endif
        GV.MemDecoration = Arg1qword;
      }
    }
  } else {
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movhpd ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg1qword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movhps ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
  }
}


/* ====================================================================
 *      0x 0f 12
 * ==================================================================== */
void __bea_callspec__ movlps_VM(PDISASM pMyDisasm)
{
    if (GV.VEX.state == InUsePrefix) {
      if (GV.VEX.pp == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        ArgsVEX(pMyDisasm);
        if (GV.MOD_ == 0x3) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovhlpd ");
          #endif
        }
        else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovlpd ");
          #endif
          GV.MemDecoration = Arg3qword;
        }
      }
      else if (GV.VEX.pp == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovsldup ");
        #endif
        ArgsVEX_GxEx(pMyDisasm);
      }
      else if (GV.VEX.pp == 0x3) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovddup ");
        #endif
        ArgsVEX_GxEx(pMyDisasm);
        if (GV.VEX.L == 0) {
          GV.MemDecoration = Arg2qword;
        }

      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        ArgsVEX(pMyDisasm);
        if (GV.MOD_ == 0x3) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovhlps ");
          #endif
        }
        else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovlps ");
          #endif
          GV.MemDecoration = Arg3qword;
        }
      }

    } else {
      /* ========= 0xf2 */
      if (GV.PrefRepne == 1) {
          (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
          GV.MemDecoration = Arg2qword;
          (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+DATA_TRANSFER;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movddup ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      /* ========= 0xf3 */
      else if (GV.PrefRepe == 1) {
          (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE3_INSTRUCTION+DATA_TRANSFER;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movsldup ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      /* ========== 0x66 */
      else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
          GV.OperandSize = GV.OriginalOperandSize;
          (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
          GV.MemDecoration = Arg2qword;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movlpd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      else {
          GV.MemDecoration = Arg2qword;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+DATA_TRANSFER;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
          if (GV.MOD_== 0x3) {
              #ifndef BEA_LIGHT_DISASSEMBLY
                 (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movhlps ");
              #endif
          }
          else {
              #ifndef BEA_LIGHT_DISASSEMBLY
                 (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movlps ");
              #endif
          }
      }
    }
}


/* ====================================================================
 *      0x 0f 13
 * ==================================================================== */
void __bea_callspec__ movlps_MV(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
      if (GV.MOD_== 0x3) {
          FailDecode(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovlpd ");
        #endif
        GV.MemDecoration = Arg1qword;
      }
    }
    else {
      GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
      if (GV.MOD_== 0x3) {
          FailDecode(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;

        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovlps ");
        #endif
        GV.MemDecoration = Arg1qword;
      }
    }
  } else {
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movlpd ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg1qword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movlps ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
  }
}


/* ====================================================================
 *      0x 0f 50
 * ==================================================================== */
void __bea_callspec__ movmskps_(PDISASM pMyDisasm)
{
    GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
    if (GV.MOD_!= 0x3) {
        FailDecode(pMyDisasm);
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movmskpd ");
        #endif
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;

    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+DATA_TRANSFER;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movmskps ");
        #endif
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;

    }
}


/* ====================================================================
 *      0x 0f 38 2a
 * ==================================================================== */
void __bea_callspec__ movntdqa_(PDISASM pMyDisasm)
{

    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+STREAMING_LOAD;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movntdqa ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f c3
 * ==================================================================== */
void __bea_callspec__ movnti_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CACHEABILITY_CONTROL;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movnti ");
    #endif
    EvGv(pMyDisasm);

}


/* ====================================================================
 *      0x 0f 2b
 * ==================================================================== */
void __bea_callspec__ movntps_(PDISASM pMyDisasm)
{
    GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
    if (GV.MOD_== 0x3) {
        FailDecode(pMyDisasm);
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CACHEABILITY_CONTROL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movntpd ");
        #endif
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;

    }
    else {
        GV.MemDecoration = Arg1_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CACHEABILITY_CONTROL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movntps ");
        #endif
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;

    }
}


/* ====================================================================
 *      0x 0f e7
 * ==================================================================== */
void __bea_callspec__ movntq_(PDISASM pMyDisasm)
{
    GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
    if (GV.MOD_== 0x3) {
        FailDecode(pMyDisasm);
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg1_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+CACHEABILITY_CONTROL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movntdq ");
        #endif
        GV.SSE_ = 1;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg1qword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+CACHEABILITY_CONTROL;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movntq ");
        #endif
        GV.MMX_ = 1;
        ExGx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 10
 * ==================================================================== */
void __bea_callspec__ movups_VW(PDISASM pMyDisasm)
{
    if (GV.VEX.state == InUsePrefix) {
      if (GV.VEX.pp == 0x3) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        if (GV.VEX.vvvv == 0xF) {
          /* VEX.LIG.F2.0F.WIG 10 /r */
          /* VMOVSD xmm1, m64 */
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovsd ");
          #endif

          GV.MemDecoration = Arg2qword;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovsd ");
          #endif

          /* VEX.NDS.LIG.F2.0F.WIG 10 /r */
          /* VMOVSD xmm1, xmm2, xmm3 */
          ArgsVEX(pMyDisasm);
        }
      }
      else if (GV.VEX.pp == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        if (GV.VEX.vvvv == 0xF) {
          /* VEX.LIG.F3.0F.WIG 10 /r */
          /* VMOVSS xmm1, m64 */
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovss ");
          #endif

          GV.MemDecoration = Arg2dword;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovss ");
          #endif

          /* VEX.NDS.LIG.F3.0F.WIG 10 /r */
          /* VMOVSS xmm1, xmm2, xmm3 */
          ArgsVEX(pMyDisasm);
        }
      }
      else if (GV.VEX.pp == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovupd ");
        #endif
        ArgsVEX_GxEx(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovups ");
        #endif
        ArgsVEX_GxEx(pMyDisasm);
      }
    } else {
      /* ========= 0xf2 */
      if (GV.PrefRepne == 1) {
          (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
          GV.MemDecoration = Arg2qword;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movsd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      /* ========= 0xf3 */
      else if (GV.PrefRepe == 1) {
          (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
          GV.MemDecoration = Arg2dword;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movss ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      /* ========== 0x66 */
      else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
          GV.OperandSize = GV.OriginalOperandSize;
          (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movupd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      else {
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movups ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
    }
}

/* ====================================================================
 *      0x 0f 11
 * ==================================================================== */
void __bea_callspec__ movups_WV(PDISASM pMyDisasm)
{
    if (GV.VEX.state == InUsePrefix) {
      if (GV.VEX.pp == 0x3) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        if (GV.VEX.vvvv == 0xF) {
          /* VEX.LIG.F2.0F.WIG 10 /r */
          /* VMOVSD xmm1, m64 */
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovsd ");
          #endif

          GV.MemDecoration = Arg1qword;
          GV.SSE_ = 1;
          ExGx(pMyDisasm);
          GV.SSE_ = 0;
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovsd ");
          #endif

          /* VEX.NDS.LIG.F2.0F.WIG 10 /r */
          /* VMOVSD xmm1, xmm2, xmm3 */
          ArgsVEX_EyGy(pMyDisasm);
        }
      }
      else if (GV.VEX.pp == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        if (GV.VEX.vvvv == 0xF) {
          /* VEX.LIG.F3.0F.WIG 10 /r */
          /* VMOVSS xmm1, m64 */
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovss ");
          #endif

          GV.MemDecoration = Arg1dword;
          GV.SSE_ = 1;
          ExGx(pMyDisasm);
          GV.SSE_ = 0;
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovss ");
          #endif

          /* VEX.NDS.LIG.F3.0F.WIG 10 /r */
          /* VMOVSS xmm1, xmm2, xmm3 */
          ArgsVEX_EyGy(pMyDisasm);
        }
      }
      else if (GV.VEX.pp == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovupd ");
        #endif
        ArgsVEX_ExGx(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmovups ");
        #endif
        ArgsVEX_ExGx(pMyDisasm);
      }
    } else {
      /* ========= 0xf2 */
      if (GV.PrefRepne == 1) {
          (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
          GV.MemDecoration = Arg1qword;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movsd ");
          #endif
          GV.SSE_ = 1;
          ExGx(pMyDisasm);
          GV.SSE_ = 0;
      }
      /* ========= 0xf3 */
      else if (GV.PrefRepe == 1) {
          (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
          GV.MemDecoration = Arg1dword;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movss ");
          #endif
          GV.SSE_ = 1;
          ExGx(pMyDisasm);
          GV.SSE_ = 0;
      }
      /* ========== 0x66 */
      else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
          GV.OperandSize = GV.OriginalOperandSize;
          (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
          GV.MemDecoration = Arg1_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movupd ");
          #endif
          GV.SSE_ = 1;
          ExGx(pMyDisasm);
          GV.SSE_ = 0;
      }
      else {
          GV.MemDecoration = Arg1_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "movups ");
          #endif
          GV.SSE_ = 1;
          ExGx(pMyDisasm);
          GV.SSE_ = 0;
      }
    }
}

/* ====================================================================
 *      0x 0f 3a 42
 * ==================================================================== */
void __bea_callspec__ mpsadbw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+SAD_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mpsadbw ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 56
 * ==================================================================== */
void __bea_callspec__ orps_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

      if (GV.VEX.state == InUsePrefix) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vorpd ");
        #endif

        if (GV.VEX.opcode == 0xc4) {
          /* using VEX3Bytes */
          if (GV.REX.W_ == 0x1) {
              GV.OperandSize = 64;
          }
        }
        ArgsVEX(pMyDisasm);
      }
      else {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128d_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "orpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
    }
    else {
        if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vorps ");
          #endif

          if (GV.VEX.opcode == 0xc4) {
            /* using VEX3Bytes */
            if (GV.REX.W_ == 0x1) {
                GV.OperandSize = 64;
            }
          }
          ArgsVEX(pMyDisasm);
        }
        else {
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "orps ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
}
/* ====================================================================
 *      0x 0f 3a 0f
 * ==================================================================== */
void __bea_callspec__ palignr_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "palignr ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    else {
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "palignr ");
        #endif
        GV.ImmediatSize = 8;
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
}


/* ====================================================================
 *      0x 0f 38 10 / 0x 0f 3a 4c
 * ==================================================================== */
void __bea_callspec__ pblendvb_(PDISASM pMyDisasm)
{
  UInt8 Imm8;
  /* ========= 0xf3 */
  if ((GV.PrefRepe == 1) && (GV.EVEX.state == InUsePrefix)) {
      (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
      if (GV.EVEX.W == 0) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovuswb ");
        #endif

        if (GV.VEX.L == 0) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
            GV.SSE_ = 1;
            GV.MemDecoration = Arg1qword;
            ExGx(pMyDisasm);
            GV.SSE_ = 0;
        }
        else if (GV.VEX.L == 0x1) {
            (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
            GV.SSE_ = 1;
            GV.MemDecoration = Arg1_m128_xmm;
            MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.SSE_ = 0;
            GV.AVX_ = 1;
            Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.AVX_ = 0;
            GV.EIP_ += GV.DECALAGE_EIP+2;
        }
        else if (GV.EVEX.LL == 0x2) {
            (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
            GV.AVX_ = 1;
            GV.MemDecoration = Arg1_m128_xmm;
            MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
            GV.AVX_ = 2;
            Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
            GV.AVX_ = 0;
            GV.EIP_ += GV.DECALAGE_EIP+2;
        }
      } else {
        FailDecode(pMyDisasm);
      }
  }
  /* ========== 0x66 */
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    if (GV.EVEX.state == InUsePrefix) {
      if (GV.EVEX.W == 1) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsrlvw ");
        #endif
        ArgsVEX(pMyDisasm);
      } else {
        FailDecode(pMyDisasm);
      }
    } else if (GV.VEX.state == InUsePrefix) {
      (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+PACKED_BLENDING_INSTRUCTION;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpblendvb ");
      #endif
      if (GV.VEX.opcode == 0xc4) {
        /* using VEX3Bytes */
        if (GV.REX.W_ == 0x1) {
          GV.ERROR_OPCODE = UD_;
        }
      }
      if (GV.VEX.L == 0) {
        GV.SSE_ = 1;
        GV.MemDecoration = Arg3_m128_xmm;
        GyEy(pMyDisasm);
        fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);

        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        Imm8 = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        fillRegister((Imm8 >> 4) & 0xF, &(*pMyDisasm).Argument4, pMyDisasm);
        GV.SSE_ = 0;
      }
      else {
        GV.AVX_ = 1;
        GV.MemDecoration = Arg3_m256_ymm;
        GyEy(pMyDisasm);
        fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        Imm8 = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        fillRegister((Imm8 >> 4) & 0xF, &(*pMyDisasm).Argument4, pMyDisasm);
        GV.AVX_ = 0;
      }
    }
    else {
      (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+PACKED_BLENDING_INSTRUCTION;
      GV.MemDecoration = Arg2_m128_xmm;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pblendvb ");
      #endif
      (*pMyDisasm).Argument3.AccessMode = READ;
      (*pMyDisasm).Argument3.ArgType = REGISTER_TYPE+SSE_REG+REG0;
      (*pMyDisasm).Argument3.ArgSize = 128;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((char*) (*pMyDisasm).Argument3.ArgMnemonic, RegistersSSE[0]);
      #endif
      GV.SSE_ = 1;
      GxEx(pMyDisasm);
      GV.SSE_ = 0;

    }
  }
  else {
    FailDecode(pMyDisasm);
  }
}


/* ====================================================================
 *      0x 0f 3a 0e
 * ==================================================================== */
void __bea_callspec__ pblendw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+SAD_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pblendw ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}

/* ====================================================================
 *      0x 0f 3a 61
 * ==================================================================== */
void __bea_callspec__ pcmpestri_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pcmpestri ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 3a 60
 * ==================================================================== */
void __bea_callspec__ pcmpestrm_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pcmpestrm ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 3a 63
 * ==================================================================== */
void __bea_callspec__ pcmpistri_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pcmpistri ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 3a 62
 * ==================================================================== */
void __bea_callspec__ pcmpistrm_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pcmpestrm ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}

/* ====================================================================
 *      0x 0f 3a 14
 * ==================================================================== */
void __bea_callspec__ pextrb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pextrb ");
        #endif
        GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
        if (GV.MOD_== 0x3) {
            GV.MemDecoration = Arg1dword;
        }
        else {
            GV.MemDecoration = Arg1byte;
        }
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 3a 16
 * ==================================================================== */
void __bea_callspec__ pextrd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        if (GV.REX.W_ == 0x1) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pextrq ");
            #endif
            GV.MemDecoration = Arg1qword;
            GV.OperandSize = 64;
        }
        else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pextrd ");
            #endif
            GV.MemDecoration = Arg1dword;
        }
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}

/* ====================================================================
 *      0x 0f c5
 * ==================================================================== */
void __bea_callspec__ pextrw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pextrw ");
        #endif
        GV.MemDecoration = Arg2_m128_xmm;
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pextrw ");
        #endif
        GV.MemDecoration = Arg2dqword;
        GV.ImmediatSize = 8;
        GV.MMX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.MMX_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }

}

/* ====================================================================
 *      0x 0f 3a 15
 * ==================================================================== */
void __bea_callspec__ pextrw2_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pextrw ");
        #endif
        GV.MOD_= ((*((UInt8*)(UIntPtr) (GV.EIP_+1))) >> 6) & 0x3;
        if (GV.MOD_== 0x3) {
            GV.MemDecoration = Arg1dword;
        }
        else {
            GV.MemDecoration = Arg1word;
        }
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 38 02
 * ==================================================================== */
void __bea_callspec__ phaddd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;


        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vphaddd ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phaddd ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phaddd ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 38 03
 * ==================================================================== */
void __bea_callspec__ phaddsw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vphaddsw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phaddsw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phaddsw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 38 01
 * ==================================================================== */
void __bea_callspec__ phaddw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vphaddw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phaddw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }

    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phaddw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 38 41
 * ==================================================================== */
void __bea_callspec__ phminposuw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+HORIZONTAL_SEARCH;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phminposuw ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 38 05
 * ==================================================================== */
void __bea_callspec__ phsubw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vphsubw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phsubw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phsubw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 38 06
 * ==================================================================== */
void __bea_callspec__ phsubd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vphsubd ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phsubd ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phsubd ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 38 0e
 * ==================================================================== */
void __bea_callspec__ vtestps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          if ((GV.REX.W_ == 1) || (GV.VEX.vvvv != 0x15)) {
            GV.ERROR_OPCODE = UD_;
          }
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vtestps ");
          #endif
          if (GV.VEX.L == 0) {
              GV.SSE_ = 1;
              GV.MemDecoration = Arg2_m128_xmm;
              GxEx(pMyDisasm);
              GV.SSE_ = 0;
          }
          else if (GV.VEX.L == 0x1) {
              GV.AVX_ = 1;
              GV.MemDecoration = Arg2_m256_ymm;
              GxEx(pMyDisasm);
              GV.AVX_ = 0;
          }
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 0f
 * ==================================================================== */
void __bea_callspec__ vtestpd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          if ((GV.REX.W_ == 1) || (GV.VEX.vvvv != 0x15)) {
            GV.ERROR_OPCODE = UD_;
          }
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vtestpd ");
          #endif
          if (GV.VEX.L == 0) {
              GV.SSE_ = 1;
              GV.MemDecoration = Arg2_m128_xmm;
              GxEx(pMyDisasm);
              GV.SSE_ = 0;
          }
          else if (GV.VEX.L == 0x1) {
              GV.AVX_ = 1;
              GV.MemDecoration = Arg2_m256_ymm;
              GxEx(pMyDisasm);
              GV.AVX_ = 0;
          }
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}
/* ====================================================================
 *      0x 0f 38 07
 * ==================================================================== */
void __bea_callspec__ phsubsw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vphsubsw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phsubsw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "phsubsw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 3a 20
 * ==================================================================== */
void __bea_callspec__ pinsrb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2byte;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pinsrb ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f 3a 22
 * ==================================================================== */
void __bea_callspec__ pinsrd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+INSERTION_EXTRACTION;
        if (GV.REX.W_ == 0x1) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pinsrq ");
            #endif
            GV.MemDecoration = Arg1qword;
        }
        else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pinsrd ");
            #endif
            GV.MemDecoration = Arg1dword;
        }
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        FailDecode(pMyDisasm);
    }

}


/* ====================================================================
 *      0x 0f c4
 * ==================================================================== */
void __bea_callspec__ pinsrw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pinsrw ");
        #endif
        GV.MemDecoration = Arg2word;
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;


    }
    else {
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pinsrw ");
        #endif
        GV.MemDecoration = Arg2word;
        GV.ImmediatSize = 8;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.MMX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+3;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }

}

/* ====================================================================
 *      0x 0f 38 04
 * ==================================================================== */
void __bea_callspec__ pmaddubsw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmaddubsw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmaddubsw ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }

    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmaddubsw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f d7
 * ==================================================================== */
void __bea_callspec__ pmovmskb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovmskb ");
        #endif
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;
    }
    else {
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SIMD64bits;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovmskb ");
        #endif
        GV.MemDecoration = Arg2qword;
        GV.MMX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.MMX_ = 0;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.EIP_ += GV.DECALAGE_EIP+2;
    }

}

/* ====================================================================
 *      0x 0f 38 0b
 * ==================================================================== */
void __bea_callspec__ pmulhrsw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+SHUFFLE_UNPACK;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmulhrsw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+SHUFFLE_UNPACK;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmulhrsw ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmulhrsw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 38 0c
 * ==================================================================== */
void __bea_callspec__ vpermilps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        if (GV.VEX.state == InUsePrefix) {
          if (GV.REX.W_ == 1) {
            GV.ERROR_OPCODE = UD_;
          }
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpermilps ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* ====================================================================
 *      0x 0f 38 0d
 * ==================================================================== */
void __bea_callspec__ vpermilpd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        if (GV.VEX.state == InUsePrefix) {
          if (GV.REX.W_ == 1) {
            GV.ERROR_OPCODE = UD_;
          }
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpermilpd ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}

/* =======================================
 *      0x 0f b8
 * ======================================= */
void __bea_callspec__ popcnt_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = SSE42_INSTRUCTION+DATA_TRANSFER;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "popcnt ");
    #endif
    GvEv(pMyDisasm);
    FillFlags(pMyDisasm,114);
}

/* ====================================================================
 *      0x 0f 38 00
 * ==================================================================== */
void __bea_callspec__ pshufb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;

        if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+SHUFFLE_UNPACK;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpshufb ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+SHUFFLE_UNPACK;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pshufb ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+SHUFFLE_UNPACK;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pshufb ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 70
 * ==================================================================== */
void __bea_callspec__ pshufw_(PDISASM pMyDisasm)
{
    (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+SIMD128bits;
    /* ========= 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pshufhw ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    /* ========= 0xf2 */
    else if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pshuflw ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }

    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pshufd ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    else {
        GV.MemDecoration = Arg2qword;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pshufw ");
        #endif
        GV.ImmediatSize = 8;
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
}

/* ====================================================================
 *      0x 0f 38 08
 * ==================================================================== */
void __bea_callspec__ psignb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+PACKED_SIGN;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsignb ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psignb ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+PACKED_SIGN;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psignb ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 38 0a
 * ==================================================================== */
void __bea_callspec__ psignd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+PACKED_SIGN;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsignd ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psignd ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+PACKED_SIGN;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psignd ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 38 09
 * ==================================================================== */
void __bea_callspec__ psignw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;

        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+PACKED_SIGN;
        if (GV.EVEX.state == InUsePrefix) {
          FailDecode(pMyDisasm);
        } else if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsignw ");
          #endif
          ArgsVEX(pMyDisasm);

        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psignw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION+PACKED_SIGN;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psignw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 38 17
 * ==================================================================== */
void __bea_callspec__ ptest_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+PACKED_TEST;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "ptest ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        FailDecode(pMyDisasm);
    }

}

/* ====================================================================
 *      0x 0f 53
 * ==================================================================== */
void __bea_callspec__ rcpps_(PDISASM pMyDisasm)
{
    /* ========== 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "rcpss ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "rcpps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 3a 09
 * ==================================================================== */
void __bea_callspec__ roundpd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+ROUND_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "roundpd ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 3a 08
 * ==================================================================== */
void __bea_callspec__ roundps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+ROUND_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "roundps ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 3a 0b
 * ==================================================================== */
void __bea_callspec__ roundsd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+ROUND_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "roundsd ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 3a 0a
 * ==================================================================== */
void __bea_callspec__ roundss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2dword;
        (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+ROUND_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "roundss ");
        #endif
        GV.ImmediatSize = 8;
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
        GV.EIP_++;
        if (!Security(0, pMyDisasm)) return;
        GV.third_arg = 1;
        (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
        #endif
        (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
        (*pMyDisasm).Argument3.ArgSize = 8;

    }
    else {
        FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f 52
 * ==================================================================== */
void __bea_callspec__ rsqrtps_(PDISASM pMyDisasm)
{
    /* ========== 0xf3 */
    if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "rsqrtss ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "rsqrtps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f c6
 * ==================================================================== */
void __bea_callspec__ shufps_(PDISASM pMyDisasm)
{

    /* ========== 0x66 */
    GV.ImmediatSize = 8;
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+SHUFFLE_UNPACK;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "shufpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+SHUFFLE_UNPACK;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "shufps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    (*pMyDisasm).Argument1.AccessMode = READ;
    GV.EIP_++;
    if (!Security(0, pMyDisasm)) return;
    GV.third_arg = 1;
    (*pMyDisasm).Instruction.Immediat = *((UInt8*)(UIntPtr) (GV.EIP_- 1));
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) CopyFormattedNumber(pMyDisasm, (char*) (*pMyDisasm).Argument3.ArgMnemonic, "%.2X",(Int64) *((UInt8*)(UIntPtr) (GV.EIP_- 1)));
    #endif
    (*pMyDisasm).Argument3.ArgType = CONSTANT_TYPE+ABSOLUTE_;
    (*pMyDisasm).Argument3.ArgSize = 8;

}


/* ====================================================================
 *      0x 0f 51
 * ==================================================================== */
void __bea_callspec__ sqrtps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "sqrtsd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
        GV.MemDecoration = Arg2dword;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "sqrtss ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "sqrtpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "sqrtps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 2e
 * ==================================================================== */
void __bea_callspec__ ucomiss_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2dword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "ucomisd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+COMPARISON_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "ucomiss ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
}


/* ====================================================================
 *      0x 0f 15
 * ==================================================================== */
void __bea_callspec__ unpckhps_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vunpckhpd ");
      #endif
      ArgsVEX(pMyDisasm);
    }
    else {
      (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION;
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vunpckhps ");
      #endif
      ArgsVEX(pMyDisasm);
    }
  }
  else {
    /* ========== 0x66 */
    if (GV.OperandSize == 16) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+SHUFFLE_UNPACK;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "unpckhpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
    else {
        GV.MemDecoration = Arg2_m128_xmm;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+SHUFFLE_UNPACK;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "unpckhps ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
    }
  }
}

/* ====================================================================
 *      0x 0f 14
 * ==================================================================== */
void __bea_callspec__ unpcklps_(PDISASM pMyDisasm)
{
    if (GV.VEX.state == InUsePrefix) {
      (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
      if (GV.VEX.pp == 0x1) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vunpcklpd ");
        #endif
        ArgsVEX(pMyDisasm);
      }
      else {
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vunpcklps ");
        #endif
        ArgsVEX(pMyDisasm);
      }
    }
    else {
      /* ========== 0x66 */
      if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
          GV.OperandSize = GV.OriginalOperandSize;
          (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+SHUFFLE_UNPACK;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "unpcklpd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
      else {
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+SHUFFLE_UNPACK;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "unpcklps ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
      }
    }
}


/* ====================================================================
 *      0x 0f 57
 * ==================================================================== */
void __bea_callspec__ xorps_VW(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {

      if (GV.VEX.state == InUsePrefix) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vxorpd ");
        #endif

        if (GV.VEX.opcode == 0xc4) {
          /* using VEX3Bytes */
          if (GV.REX.W_ == 0x1) {
              GV.OperandSize = 64;
          }
        }
        ArgsVEX(pMyDisasm);
      }
      else {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        GV.MemDecoration = Arg2_m128d_xmm;
        (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "xorpd ");
        #endif
        GV.SSE_ = 1;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
    }
    else {
        if (GV.VEX.state == InUsePrefix) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vxorps ");
          #endif

          if (GV.VEX.opcode == 0xc4) {
            /* using VEX3Bytes */
            if (GV.REX.W_ == 0x1) {
                GV.OperandSize = 64;
            }
          }
          ArgsVEX(pMyDisasm);
        }
        else {
          GV.MemDecoration = Arg2_m128_xmm;
          (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+LOGICAL_INSTRUCTION;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "xorps ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
}






/* ====================================================================
 *      0x 0f 38 29
 * ==================================================================== */

void __bea_callspec__ pcmpeqq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpcmpeqq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pcmpeqq ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 3e
 * ==================================================================== */

void __bea_callspec__ pmaxuw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmaxuw ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmaxuw ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 45
 * ==================================================================== */

void __bea_callspec__ psrlvd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 1)) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsrlvq ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsrlvd ");
            #endif
          }
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psrlvd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 38
 * ==================================================================== */

void __bea_callspec__ pminsb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpminsb ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pminsb ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 3a
 * ==================================================================== */

void __bea_callspec__ pminuw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpminuw ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pminuw ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 3f
 * ==================================================================== */

void __bea_callspec__ pmaxud_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmaxud ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmaxud ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 39
 * ==================================================================== */

void __bea_callspec__ pminsd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpminsd ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pminsd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 46
 * ==================================================================== */

void __bea_callspec__ psravd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 1)) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsravq ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsravd ");
            #endif
          }
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psravd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 37
 * ==================================================================== */

void __bea_callspec__ pcmpgtq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpcmpgtq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pcmpgtq ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 3c
 * ==================================================================== */

void __bea_callspec__ pmaxsb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmaxsb ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmaxsb ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 2b
 * ==================================================================== */

void __bea_callspec__ packusdw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpackusdw ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packusdw ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 3d
 * ==================================================================== */

void __bea_callspec__ pmaxsd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmaxsd ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmaxsd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 3b
 * ==================================================================== */

void __bea_callspec__ pminud_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpminud ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pminud ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 28
 * ==================================================================== */

void __bea_callspec__ pmuldq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmuldq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmuldq ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 40
 * ==================================================================== */

void __bea_callspec__ pmulld_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 1)) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmullq ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmulld ");
            #endif
          }
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmulld ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 47
 * ==================================================================== */

void __bea_callspec__ psllvd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 1)) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsllvq ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpsllvd ");
            #endif
          }
          ArgsVEX(pMyDisasm);
        } else {
          (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION;
          GV.MemDecoration = Arg2_m128_xmm;
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "psllvd ");
          #endif
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 ac
 * ==================================================================== */

void __bea_callspec__ vfnmadd213ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd213ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd213pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 ad
 * ==================================================================== */

void __bea_callspec__ vfnmadd213ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd213ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd213sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 bb
 * ==================================================================== */

void __bea_callspec__ vfmsub231ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub231ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub231sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 92
 * ==================================================================== */

void __bea_callspec__ vgatherps_(PDISASM pMyDisasm)
{
  /* ========== 0x66 */
  if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    if (GV.VEX.state == InUsePrefix) {
      if (
          ((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) ||
          ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))
        ) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherdps ");
        #endif

        if (GV.VEX.L == 0) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          GV.VSIB_ = SSE_REG;
          GV.SSE_ = 1;
          if (GV.EVEX.state != InUsePrefix) {
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
          }
          else {
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
          }
          GV.SSE_ = 0;
        }
        else if (GV.VEX.L == 0x1) {
          (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
          GV.VSIB_ = AVX_REG;

          if (GV.EVEX.state != InUsePrefix) {
            GV.SSE_ = 1;
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
            GV.SSE_ = 0;
          }
          else {
            GV.SSE_ = 1;
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
          }
        }
        else if (GV.EVEX.LL == 0x2) {
          (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
          GV.VSIB_ = AVX512_REG;
          GV.AVX_ = 1;
          GV.MemDecoration = Arg2dword;
          GxEx(pMyDisasm);
          GV.AVX_ = 0;
        }

      } else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherdpd ");
        #endif
        GV.MemDecoration = Arg2dword;
        if (GV.VEX.L == 0) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          GV.VSIB_ = SSE_REG;
          GV.SSE_ = 1;
          if (GV.EVEX.state != InUsePrefix) {
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
          }
          else {
            GxEx(pMyDisasm);
          }
          GV.SSE_ = 0;
        }
        else if (GV.VEX.L == 0x1) {
          (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
          GV.VSIB_ = AVX_REG;
          GV.AVX_ = 1;
          if (GV.EVEX.state != InUsePrefix) {
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
          }
          else {
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
          }
          GV.AVX_ = 0;
        }
        else if (GV.EVEX.LL == 0x2) {
          (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
          GV.VSIB_ = AVX512_REG;
          GV.AVX_ = 2;
          GV.MemDecoration = Arg2dword;
          GxEx(pMyDisasm);
          GV.AVX_ = 0;
        }
      }
    } else {
      FailDecode(pMyDisasm);
    }
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 ae
 * ==================================================================== */

void __bea_callspec__ vfnmsub213ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub213ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub213pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 a7
 * ==================================================================== */

void __bea_callspec__ vfmsubadd213ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsubadd213ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsubadd213pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 b6
 * ==================================================================== */

void __bea_callspec__ vfmaddsub231ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmaddsub231ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmaddsub231pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 97
 * ==================================================================== */

void __bea_callspec__ vfmsubadd132ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsubadd132ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsubadd132pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 9c
 * ==================================================================== */

void __bea_callspec__ vfnmadd132ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd132ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd132pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 9d
 * ==================================================================== */

void __bea_callspec__ vfnmadd132ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd132ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd132sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 98
 * ==================================================================== */

void __bea_callspec__ vfmadd132ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd132ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd132pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 9f
 * ==================================================================== */

void __bea_callspec__ vfnmsub132ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub132ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub132sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 9e
 * ==================================================================== */

void __bea_callspec__ vfnmsub132ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub132ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub132pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 91
 * ==================================================================== */

void __bea_callspec__ vgatherqd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherqd ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherqq ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 99
 * ==================================================================== */

void __bea_callspec__ vfmadd132ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd132ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd132sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 bc
 * ==================================================================== */

void __bea_callspec__ vfnmadd231ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd231ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd231pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 9a
 * ==================================================================== */

void __bea_callspec__ vfmsub132ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub132ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub132pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 90
 * ==================================================================== */

void __bea_callspec__ vgatherdd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if ((GV.REX.W_ == 0x1) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 1))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherdq ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherdd ");
            #endif
          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 b7
 * ==================================================================== */

void __bea_callspec__ vfmsubadd231ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsubadd231ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsubadd231pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 a6
 * ==================================================================== */

void __bea_callspec__ vfmaddsub213ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmaddsub213ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmaddsub213pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 9b
 * ==================================================================== */

void __bea_callspec__ vfmsub132ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub132ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub132sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 aa
 * ==================================================================== */

void __bea_callspec__ vfmsub213ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub213ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub213pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 bd
 * ==================================================================== */

void __bea_callspec__ vfnmadd231ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd231ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmadd231sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 b9
 * ==================================================================== */

void __bea_callspec__ vfmadd231ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd231ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd231sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 ab
 * ==================================================================== */

void __bea_callspec__ vfmsub213ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub213ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub213sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 be
 * ==================================================================== */

void __bea_callspec__ vfnmsub231ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub231ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub231pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 bf
 * ==================================================================== */

void __bea_callspec__ vfnmsub231ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub231ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub231sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 b8
 * ==================================================================== */

void __bea_callspec__ vfmadd231ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd231ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd231pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 a9
 * ==================================================================== */

void __bea_callspec__ vfmadd213ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd213ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd213sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 af
 * ==================================================================== */

void __bea_callspec__ vfnmsub213ss_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub213ss ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfnmsub213sd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 93
 *      VGATHERQPS xmm1 {k1}, vm64x
 * ==================================================================== */

void __bea_callspec__ vgatherqps_(PDISASM pMyDisasm)
{
  /* ========== 0x66 */
  if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    if (GV.VEX.state == InUsePrefix) {
      if (
          ((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) ||
          ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))
        ) {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherqps ");
        #endif

        if (GV.VEX.L == 0) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          GV.VSIB_ = SSE_REG;
          GV.SSE_ = 1;
          if (GV.EVEX.state != InUsePrefix) {
            GV.MemDecoration = Arg2qword;
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
          }
          else {
            GV.MemDecoration = Arg2qword;
            GxEx(pMyDisasm);
          }
          GV.SSE_ = 0;
        }
        else if (GV.VEX.L == 0x1) {
          (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
          GV.VSIB_ = AVX_REG;

          if (GV.EVEX.state != InUsePrefix) {
            GV.SSE_ = 1;
            GV.MemDecoration = Arg2qword;
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
            GV.SSE_ = 0;
          }
          else {
            GV.SSE_ = 1;
            GV.MemDecoration = Arg2qword;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
          }
        }
        else if (GV.EVEX.LL == 0x2) {
          (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
          GV.VSIB_ = AVX512_REG;
          GV.AVX_ = 1;
          GV.MemDecoration = Arg2qword;
          GxEx(pMyDisasm);
          GV.AVX_ = 0;
        }

      } else {
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vgatherqpd ");
        #endif
        GV.MemDecoration = Arg2qword;
        if (GV.VEX.L == 0) {
          (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
          GV.VSIB_ = SSE_REG;
          GV.SSE_ = 1;
          if (GV.EVEX.state != InUsePrefix) {
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
          }
          else {
            GxEx(pMyDisasm);
          }
          GV.SSE_ = 0;
        }
        else if (GV.VEX.L == 0x1) {
          (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
          GV.VSIB_ = AVX_REG;
          GV.AVX_ = 1;
          if (GV.EVEX.state != InUsePrefix) {
            GV.MemDecoration = Arg2dword;
            GxEx(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument3, pMyDisasm);
          }
          else {
            GV.MemDecoration = Arg2qword;
            GxEx(pMyDisasm);
          }
          GV.AVX_ = 0;
        }
        else if (GV.EVEX.LL == 0x2) {
          (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
          GV.VSIB_ = AVX512_REG;
          GV.AVX_ = 2;
          GV.MemDecoration = Arg2qword;
          GxEx(pMyDisasm);
          GV.AVX_ = 0;
        }
      }
    } else {
      FailDecode(pMyDisasm);
    }
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 96
 * ==================================================================== */

void __bea_callspec__ vfmaddsub132ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmaddsub132ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmaddsub132pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 a8
 * ==================================================================== */

void __bea_callspec__ vfmadd213ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd213ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmadd213pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f 38 ba
 * ==================================================================== */

void __bea_callspec__ vfmsub231ps_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        if (GV.VEX.state == InUsePrefix) {
          if (((GV.REX.W_ == 0x0) && (GV.EVEX.state != InUsePrefix)) || ((GV.EVEX.state == InUsePrefix) && (GV.EVEX.W == 0))) {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub231ps ");
            #endif
          } else {
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vfmsub231pd ");
            #endif

          }
          ArgsVEX(pMyDisasm);
        } else {
          FailDecode(pMyDisasm);
        }
    }
    else {
        FailDecode(pMyDisasm);
    }
}



/* ====================================================================
 *      0x 0f d3
 * ==================================================================== */

void __bea_callspec__ psrlq_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsrlq ", "psrlq ");
}

/* ====================================================================
 *      0x 0f d1
 * ==================================================================== */

void __bea_callspec__ psrlw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsrlw ", "psrlw ");
}

/* ====================================================================
 *      0x 0f 75
 * ==================================================================== */

void __bea_callspec__ pcmpeqw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpcmpeqw ", "pcmpeqw ");
}

/* ====================================================================
 *      0x 0f d8
 * ==================================================================== */

void __bea_callspec__ psubusb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubusb ", "psubusb ");
}

/* ====================================================================
 *      0x 0f eb
 * ==================================================================== */

void __bea_callspec__ por_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpor ", "por ");
}

/* ====================================================================
 *      0x 0f d9
 * ==================================================================== */

void __bea_callspec__ psubusw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubusw ", "psubusw ");
}

/* ====================================================================
 *      0x 0f 74
 * ==================================================================== */

void __bea_callspec__ pcmpeqb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpcmpeqb ", "pcmpeqb ");
}

/* ====================================================================
 *      0x 0f 76
 * ==================================================================== */

void __bea_callspec__ pcmpeqd_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpcmpeqd ", "pcmpeqd ");
}

/* ====================================================================
 *      0x 0f d2
 * ==================================================================== */

void __bea_callspec__ psrld_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsrld ", "psrld ");
}

/* ====================================================================
 *      0x 0f db
 * ==================================================================== */

void __bea_callspec__ pand_block(PDISASM pMyDisasm, const char* mnemonic1, const char* mnemonic2)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, mnemonic1);
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, mnemonic2);
          #endif
          if (GV.VEX.L == 0) {
              (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
              GV.SSE_ = 1;
              GV.MemDecoration = Arg2_m128_xmm;
              GxEx(pMyDisasm);
              GV.SSE_ = 0;
          }
          else if (GV.VEX.L == 0x1) {
              (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
              GV.AVX_ = 1;
              GV.MemDecoration = Arg2_m256_ymm;
              GxEx(pMyDisasm);
              GV.AVX_ = 0;
          }
          else if (GV.EVEX.LL == 0x2) {
              (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
              GV.AVX_ = 2;
              GV.MemDecoration = Arg2_m512_zmm;
              GxEx(pMyDisasm);
              GV.AVX_ = 0;
          }
        }
    }
    else if (GV.VEX.state != InUsePrefix) {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, mnemonic2);
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
    else {
      FailDecode(pMyDisasm);
    }
}


/* ====================================================================
 *      0x 0f db
 * ==================================================================== */

void __bea_callspec__ pand_(PDISASM pMyDisasm)
{
    pand_block(pMyDisasm, "vpand ", "pand ");
}

/* ====================================================================
 *      0x 0f fa
 * ==================================================================== */

void __bea_callspec__ psubd_(PDISASM pMyDisasm)
{
    pand_block(pMyDisasm, "vpsubd ", "psubd ");
}


/* ====================================================================
 *      0x 0f ee
 * ==================================================================== */

void __bea_callspec__ pmaxsw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmaxsw ", "pmaxsw ");

}

/* ====================================================================
 *      0x 0f 69
 * ==================================================================== */

void __bea_callspec__ punpckhwd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpckhwd ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhwd ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhwd ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f 6c
 * ==================================================================== */

void __bea_callspec__ punpcklqdq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpcklqdq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpcklqdq ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpcklqdq ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}





/* ====================================================================
 *      0x 0f 6a
 * ==================================================================== */

void __bea_callspec__ punpckhdq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpckhdq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhdq ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhdq ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}





/* ====================================================================
 *      0x 0f e4
 * ==================================================================== */

void __bea_callspec__ pmulhuw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmulhuw ", "pmulhuw ");

}


/* ====================================================================
 *      0x 0f 62
 * ==================================================================== */

void __bea_callspec__ punpckldq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpckldq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckldq ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckldq ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f ed
 * ==================================================================== */

void __bea_callspec__ paddsw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddsw ", "paddsw ");
}


/* ====================================================================
 *      0x 0f e1
 * ==================================================================== */

void __bea_callspec__ psraw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsraw ", "psraw ");
}

/* ====================================================================
 *      0x 0f df
 * ==================================================================== */

void __bea_callspec__ pandn_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpandn ", "pandn ");
}

/* ====================================================================
 *      0x 0f e2
 * ==================================================================== */

void __bea_callspec__ psrad_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsrad ", "psrad ");
}


/* ====================================================================
 *      0x 0f e5
 * ==================================================================== */

void __bea_callspec__ pmulhw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmulhw ", "pmulhw ");
}


/* ====================================================================
 *      0x 0f 67
 * ==================================================================== */

void __bea_callspec__ packuswb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpackuswb ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packuswb ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packuswb ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}





/* ====================================================================
 *      0x 0f f4
 * ==================================================================== */

void __bea_callspec__ pmuludq_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmuludq ", "pmuludq ");
}


/* ====================================================================
 *      0x 0f e9
 * ==================================================================== */

void __bea_callspec__ psubsw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubsw ", "psubsw ");
}


/* ====================================================================
 *      0x 0f 6d
 * ==================================================================== */

void __bea_callspec__ punpckhqdq_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpckhqdq ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhqdq ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhqdq ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f f8
 * ==================================================================== */

void __bea_callspec__ psubb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubb ", "psubb ");
}


/* ====================================================================
 *      0x 0f d5
 * ==================================================================== */

void __bea_callspec__ pmullw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmullw ", "pmullw ");
}


/* ====================================================================
 *      0x 0f f2
 * ==================================================================== */

void __bea_callspec__ pslld_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpslld ", "pslld ");
}


/* ====================================================================
 *      0x 0f 6b
 * ==================================================================== */

void __bea_callspec__ packssdw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpackssdw ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packssdw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packssdw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f f9
 * ==================================================================== */

void __bea_callspec__ psubw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubw ", "psubw ");
}

/* ====================================================================
 *      0x 0f 63
 * ==================================================================== */

void __bea_callspec__ packsswb_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpacksswb ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packsswb ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "packsswb ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f fb
 * ==================================================================== */

void __bea_callspec__ psubq_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubq ", "psubq ");
}


/* ====================================================================
 *      0x 0f e8
 * ==================================================================== */

void __bea_callspec__ psubsb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsubsb ", "psubsb ");
}


/* ====================================================================
 *      0x 0f f1
 * ==================================================================== */

void __bea_callspec__ psllw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsllw ", "psllw ");
}


/* ====================================================================
 *      0x 0f f3
 * ==================================================================== */

void __bea_callspec__ psllq_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsllq ", "psllq ");
}


/* ====================================================================
 *      0x 0f da
 * ==================================================================== */

void __bea_callspec__ pminub_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpminub ", "pminub ");
}


/* ====================================================================
 *      0x 0f fe
 * ==================================================================== */

void __bea_callspec__ paddd_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddd ", "paddd ");
}


/* ====================================================================
 *      0x 0f fc
 * ==================================================================== */

void __bea_callspec__ paddb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddb ", "paddb ");
}


/* ====================================================================
 *      0x 0f 65
 * ==================================================================== */

void __bea_callspec__ pcmpgtw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpcmpgtw ", "pcmpgtw ");
}


/* ====================================================================
 *      0x 0f e3
 * ==================================================================== */

void __bea_callspec__ pavgw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpavgw ", "pavgw ");
}


/* ====================================================================
 *      0x 0f fd
 * ==================================================================== */

void __bea_callspec__ paddw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddw ", "paddw ");
}

/* ====================================================================
 *      0x 0f 64
 * ==================================================================== */

void __bea_callspec__ pcmpgtb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpcmpgtb ", "pcmpgtb ");
}


/* ====================================================================
 *      0x 0f ef
 * ==================================================================== */

void __bea_callspec__ pxor_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpxor ", "pxor ");
}

/* ====================================================================
 *      0x 0f 66
 * ==================================================================== */

void __bea_callspec__ pcmpgtd_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpcmpgtd ", "pcmpgtd ");
}


/* ====================================================================
 *      0x 0f de
 * ==================================================================== */

void __bea_callspec__ pmaxub_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmaxub ", "pmaxub ");
}


/* ====================================================================
 *      0x 0f d4
 * ==================================================================== */

void __bea_callspec__ paddq_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddq ", "paddq ");
}


/* ====================================================================
 *      0x 0f ec
 * ==================================================================== */

void __bea_callspec__ paddsb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddsb ", "paddsb ");
}

/* ====================================================================
 *      0x 0f 68
 * ==================================================================== */

void __bea_callspec__ punpckhbw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpckhbw ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhbw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpckhbw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f f5
 * ==================================================================== */

void __bea_callspec__ pmaddwd_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpmaddwd ", "pmaddwd ");
}


/* ====================================================================
 *      0x 0f e0
 * ==================================================================== */

void __bea_callspec__ pavgb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpavgb ", "pavgb ");
}


/* ====================================================================
 *      0x 0f dd
 * ==================================================================== */

void __bea_callspec__ paddusw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddusw ", "paddusw ");
}

/* ====================================================================
 *      0x 0f dc
 * ==================================================================== */

void __bea_callspec__ paddusb_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpaddusb ", "paddusb ");
}

/* ====================================================================
 *      0x 0f 60
 * ==================================================================== */

void __bea_callspec__ punpcklbw_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpcklbw ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpcklbw ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpcklbw ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f f6
 * ==================================================================== */

void __bea_callspec__ psadbw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpsadbw ", "psadbw ");
}

/* ====================================================================
 *      0x 0f 61
 * ==================================================================== */

void __bea_callspec__ punpcklwd_(PDISASM pMyDisasm)
{
    /* ========== 0x66 */
    if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        GV.OperandSize = GV.OriginalOperandSize;
        (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
        (*pMyDisasm).Instruction.Category = SSSE3_INSTRUCTION;
        if (GV.VEX.state == InUsePrefix) {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpunpcklwd ");
          #endif
          ArgsVEX(pMyDisasm);
        } else {
          #ifndef BEA_LIGHT_DISASSEMBLY
             (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpcklwd ");
          #endif
          GV.MemDecoration = Arg2_m128_xmm;
          GV.SSE_ = 1;
          GxEx(pMyDisasm);
          GV.SSE_ = 0;
        }
    }
    else {
        GV.MemDecoration = Arg2qword;
        (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION;
        #ifndef BEA_LIGHT_DISASSEMBLY
           (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "punpcklwd ");
        #endif
        GV.MMX_ = 1;
        GxEx(pMyDisasm);
        GV.MMX_ = 0;
    }
}

/* ====================================================================
 *      0x 0f ea
 * ==================================================================== */

void __bea_callspec__ pminsw_(PDISASM pMyDisasm)
{
  pand_block(pMyDisasm, "vpminsw ", "pminsw ");
}


 /* ====================================================================
 *      0x 0f 5c
 * ==================================================================== */
void __bea_callspec__ subps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vsubsd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3qword;
            GV.SSE_ = 0;
        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "subsd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vsubss ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }

            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3dword;
            GV.SSE_ = 0;

        }
        else {
            (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "subss ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vsubpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "subpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vsubps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);
        }
        else {

            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "subps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}


 /* ====================================================================
 *      0x 0f 5f
 * ==================================================================== */
void __bea_callspec__ maxps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmaxsd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3qword;
            GV.SSE_ = 0;
        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "maxsd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmaxss ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }

            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3dword;
            GV.SSE_ = 0;

        }
        else {
            (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "maxss ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmaxpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "maxpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmaxps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);
        }
        else {

            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "maxps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}


 /* ====================================================================
 *      0x 0f 5d
 * ==================================================================== */
void __bea_callspec__ minps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vminsd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3qword;
            GV.SSE_ = 0;
        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "minsd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vminss ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }

            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3dword;
            GV.SSE_ = 0;

        }
        else {
            (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "minss ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vminpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "minpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vminps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);
        }
        else {

            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "minps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}


 /* ====================================================================
 *      0x 0f 59
 * ==================================================================== */
void __bea_callspec__ mulps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmulsd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3qword;
            GV.SSE_ = 0;
        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mulsd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmulss ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }

            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3dword;
            GV.SSE_ = 0;

        }
        else {
            (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mulss ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmulpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mulpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vmulps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);
        }
        else {

            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "mulps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}


 /* ====================================================================
 *      0x 0f 5e
 * ==================================================================== */
void __bea_callspec__ divps_VW(PDISASM pMyDisasm)
{
    /* ========= 0xf2 */
    if (GV.PrefRepne == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vdivsd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3qword;
            GV.SSE_ = 0;
        }
        else {
            (*pMyDisasm).Prefix.RepnePrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2qword;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "divsd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========= 0xf3 */
    else if (GV.PrefRepe == 1) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vdivss ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }

            GV.SSE_ = 1;
            GyEy(pMyDisasm);
            fillRegister(~GV.VEX.vvvv & 0xF, &(*pMyDisasm).Argument2, pMyDisasm);
            GV.MemDecoration = Arg3dword;
            GV.SSE_ = 0;

        }
        else {
            (*pMyDisasm).Prefix.RepPrefix = MandatoryPrefix;
            GV.MemDecoration = Arg2dword;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "divss ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    /* ========== 0x66 */
    else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vdivpd ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);

        }
        else {
            GV.OperandSize = GV.OriginalOperandSize;
            (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
            GV.MemDecoration = Arg2_m128d_xmm;
            (*pMyDisasm).Instruction.Category = SSE2_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "divpd ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
    else {

        if (GV.VEX.state == InUsePrefix) {
            (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vdivps ");
            #endif

            if (GV.VEX.opcode == 0xc4) {
                /* using VEX3Bytes */
                if (GV.REX.W_ == 0x1) {
                    GV.OperandSize = 64;
                }
            }
            ArgsVEX(pMyDisasm);
        }
        else {

            GV.MemDecoration = Arg2_m128_xmm;
            (*pMyDisasm).Instruction.Category = SSE_INSTRUCTION+ARITHMETIC_INSTRUCTION;
            #ifndef BEA_LIGHT_DISASSEMBLY
               (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "divps ");
            #endif
            GV.SSE_ = 1;
            GxEx(pMyDisasm);
            GV.SSE_ = 0;
        }
    }
}



/* ====================================================================
 *      0x 0f 38 20
 * ==================================================================== */
void __bea_callspec__ pmovsxbw_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsxbw ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovswb ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovsxbw ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 21
 * ==================================================================== */
void __bea_callspec__ pmovsxbd_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsxbd ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsdb ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovsxbd ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 22
 * ==================================================================== */
void __bea_callspec__ pmovsxbq_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsxbq ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsqb ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovsxbq ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 23
 * ==================================================================== */
void __bea_callspec__ pmovsxwd_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsxwd ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsdw ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovsxwd ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 24
 * ==================================================================== */
void __bea_callspec__ pmovsxwq_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsxwq ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsqw ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovsxwq ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 25
 * ==================================================================== */
void __bea_callspec__ pmovsxdq_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsxdq ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovsqd ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovsxdq ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 30
 * ==================================================================== */
void __bea_callspec__ pmovzxbw_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovzxbw ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovwb ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovzxbw ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 31
 * ==================================================================== */
void __bea_callspec__ pmovzxbd_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovzxbd ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovdb ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovzxbd ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 32
 * ==================================================================== */
void __bea_callspec__ pmovzxbq_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovzxbq ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovqb ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovzxbq ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 33
 * ==================================================================== */
void __bea_callspec__ pmovzxwd_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovzxwd ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovdw ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovzxwd ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 34
 * ==================================================================== */
void __bea_callspec__ pmovzxwq_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovzxwq ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovqw ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovzxwq ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}



/* ====================================================================
 *      0x 0f 38 35
 * ==================================================================== */
void __bea_callspec__ pmovzxdq_(PDISASM pMyDisasm)
{
  if (GV.VEX.state == InUsePrefix) {
    if (GV.VEX.pp == 0x1) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovzxdq ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg2qword;
        GxEx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg2_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg2_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else if (GV.VEX.pp == 0x2) {
      #ifndef BEA_LIGHT_DISASSEMBLY
         (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "vpmovqd ");
      #endif
      if (GV.VEX.L == 0) {
        (*pMyDisasm).Instruction.Category = AVX_INSTRUCTION;
        GV.SSE_ = 1;
        GV.MemDecoration = Arg1qword;
        ExGx(pMyDisasm);
        GV.SSE_ = 0;
      }
      else if (GV.VEX.L == 0x1) {
        (*pMyDisasm).Instruction.Category = AVX2_INSTRUCTION;
        GV.MemDecoration = Arg1_m128_xmm;
        GV.SSE_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.SSE_ = 0;
        GV.AVX_ = 1;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
      else if (GV.EVEX.LL == 0x2) {
        (*pMyDisasm).Instruction.Category = AVX512_INSTRUCTION;
        GV.MemDecoration = Arg1_m256_ymm;
        GV.AVX_ = 1;
        MOD_RM(&(*pMyDisasm).Argument1, pMyDisasm);
        GV.AVX_ = 0;
        GV.AVX_ = 2;
        Reg_Opcode(&(*pMyDisasm).Argument2, pMyDisasm);
        GV.AVX_ = 0;
        GV.EIP_ += GV.DECALAGE_EIP+2;
      }
    }
    else {
      FailDecode(pMyDisasm);
    }

  }
  else if ((*pMyDisasm).Prefix.OperandSize == InUsePrefix) {
    GV.OperandSize = GV.OriginalOperandSize;
    (*pMyDisasm).Prefix.OperandSize = MandatoryPrefix;
    GV.MemDecoration = Arg2qword;
    (*pMyDisasm).Instruction.Category = SSE41_INSTRUCTION+CONVERSION_INSTRUCTION;
    #ifndef BEA_LIGHT_DISASSEMBLY
       (void) strcpy ((*pMyDisasm).Instruction.Mnemonic, "pmovzxdq ");
    #endif
    GV.SSE_ = 1;
    GxEx(pMyDisasm);
    GV.SSE_ = 0;
  }
  else {
    FailDecode(pMyDisasm);
  }
}
