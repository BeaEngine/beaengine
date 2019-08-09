# =====================================
#
#	BeaEngine 5.x header for Python
#	using ctypes
#
# =====================================

from ctypes import *
import re

INSTRUCT_LENGTH = 64

class REX_Struct(Structure):
   _pack_= 1
   _fields_= [("W_",c_uint8),
              ("R_",c_uint8),
              ("X_",c_uint8),
              ("B_",c_uint8),
              ("state",c_uint8)]

class PREFIXINFO(Structure):
   _pack_= 1
   _fields_= [("Number",c_int),
              ("NbUndefined",c_int),
              ("LockPrefix",c_uint8),
              ("OperandSize",c_uint8),
              ("AddressSize",c_uint8),
              ("RepnePrefix",c_uint8),
              ("RepPrefix",c_uint8),
              ("FSPrefix",c_uint8),
              ("SSPrefix",c_uint8),
              ("GSPrefix",c_uint8),
              ("ESPrefix",c_uint8),
              ("CSPrefix",c_uint8),
              ("DSPrefix",c_uint8),
              ("BranchTaken",c_uint8),
              ("BranchNotTaken",c_uint8),
              ("REX",REX_Struct),
			  ("alignment1",c_uint8),
			  ("alignment2",c_uint8)]

class EFLStruct(Structure):
   _pack_= 1
   _fields_= [("OF_",c_uint8),
              ("SF_",c_uint8),
              ("ZF_",c_uint8),
              ("AF_",c_uint8),
              ("PF_",c_uint8),
              ("CF_",c_uint8),
              ("TF_",c_uint8),
              ("IF_",c_uint8),
              ("DF_",c_uint8),
              ("NT_",c_uint8),
              ("RF_",c_uint8),
              ("alignment",c_uint8)]

class REGISTERTYPE(Structure):
   _pack_= 4
   _fields_= [("type", c_int64),
              ("gpr",c_int64),
              ("mmx",c_int64),
              ("xmm",c_int64),
              ("ymm",c_int64),
              ("zmm",c_int64),
              ("special",c_int64),
              ("cr",c_int64),
              ("dr",c_int64),
              ("mem_management",c_int64),
              ("mpx",c_int64),
              ("opmask",c_int64),
              ("segment",c_int64),
              ("fpu",c_int64)]

class MEMORYTYPE(Structure):
   _pack_= 4
   _fields_= [("BaseRegister", c_int64),
              ("IndexRegister",c_int64),
              ("Scale",c_int32),
              ("Displacement",c_int64)]


class INSTRTYPE(Structure):
   _pack_= 1
   _fields_= [("Category", c_int32),
              ("Opcode", c_int32),
              ("Mnemonic", c_char * 24),
              ("BranchType", c_int32),
              ("Flags", EFLStruct),
              ("AddrValue", c_uint64),
              ("Immediat", c_int64),
              ("ImplicitModifiedRegs", REGISTERTYPE)]

class OPTYPE(Structure):
   _pack_= 1
   _fields_= [("OpMnemonic", c_char * 24),
              ("OpType", c_int64),
              ("OpSize", c_int32),
              ("OpPosition", c_int32),
              ("AccessMode", c_uint32),
              ("Memory", MEMORYTYPE),
              ("Registers", REGISTERTYPE),
              ("SegmentReg", c_uint32)]

class VEX_Struct(Structure):
   _pack_= 1
   _fields_= [("L",c_uint8),
              ("vvvv",c_uint8),
              ("mmmmm",c_uint8),
              ("pp",c_uint8),
              ("state",c_uint8),
              ("opcode",c_uint8)]

class EVEX_Struct(Structure):
   _pack_= 1
   _fields_= [("P0",c_uint8),
              ("P1",c_uint8),
              ("P2",c_uint8),
              ("mm",c_uint8),
              ("pp",c_uint8),
              ("R",c_uint8),
              ("X",c_uint8),
              ("B",c_uint8),
              ("R1",c_uint8),
              ("vvvv",c_uint8),
              ("V",c_uint8),
              ("aaa",c_uint8),
              ("W",c_uint8),
              ("z",c_uint8),
              ("b",c_uint8),
              ("LL",c_uint8),
              ("state",c_uint8),
              ("masking",c_uint8),
              ("tupletype",c_uint8)]

class InternalDatas(Structure):
    _pack_ = 1
    _fields_ = [("EIP_", c_void_p),
                ('EIP_VA', c_uint64),
                ('EIP_REAL', c_void_p),
                ('OriginalOperandSize', c_uint32),
                ('OperandSize', c_uint32),
                ('MemDecoration', c_uint32),
                ('AddressSize', c_uint32),
                ('MOD_', c_uint32),
                ('RM_', c_uint32),
                ('INDEX_', c_uint32),
                ('SCALE_', c_uint32),
                ('BASE_', c_uint32),
                ('REGOPCODE', c_uint32),
                ('DECALAGE_EIP', c_uint32),
                ('FORMATNUMBER', c_uint32),
                ('SYNTAX_', c_uint32),
                ('EndOfBlock', c_uint64),
                ('RelativeAddress', c_uint32),
                ('Architecture', c_uint32),
                ('ImmediatSize', c_uint32),
                ('NB_PREFIX', c_uint32),
                ('PrefRepe', c_uint32),
                ('PrefRepne', c_uint32),
                ('SEGMENTREGS', c_uint32),
                ('SEGMENTFS', c_uint32),
                ('third_arg', c_uint32),
                ('OPTIONS', c_uint64),
                ('ERROR_OPCODE', c_uint32),
                ('REX', REX_Struct),
                ('OutOfBlock', c_uint32),
                ('VEX', VEX_Struct),
                ('EVEX', EVEX_Struct),
                ('VSIB_', c_uint32),
                ('Register_', c_uint32),
                ]

class INSTRUCTION(Structure):
    _pack_= 1
    _fields_= [("offset", c_void_p),                # EIP
               ("VirtualAddr", c_uint64),
               ("SecurityBlock", c_uint32),
               ("repr", c_char * INSTRUCT_LENGTH),  # CompleteInstr
               ("Archi", c_uint32),
               ("Options", c_uint64),
               ("Instruction", INSTRTYPE),
               ("Operand1", OPTYPE),
               ("Operand2", OPTYPE),
               ("Operand3", OPTYPE),
               ("Operand4", OPTYPE),
               ("Prefix", PREFIXINFO),
               ("Error", c_int32),
               ("Reserved_", InternalDatas)]

# ======================= PREFIXES

NotUsedPrefix = 0
InUsePrefix = 1
SuperfluousPrefix = 2
InvalidPrefix = 4
MandatoryPrefix = 8

UNKNOWN_OPCODE = -1
OUT_OF_BLOCK = -2

# ======================= OPTIONS
NoTabulation = 0
Tabulation = 1
MasmSyntax = 0
GoAsmSyntax = 0x100
NasmSyntax = 0x200
ATSyntax = 0x400
IntrinsicMemSyntax= 0x800
PrefixedNumeral = 0x10000
SuffixedNumeral = 0x20000
ShowSegmentRegs = 0x01000000
ShowEVEXMasking = 0x02000000

LowPosition = 0
HighPosition = 1

# EVEX tupletypes

FULL = 1
HALF = 2
FULL_MEM =         3
TUPLE1_SCALAR__8 = 4
TUPLE1_SCALAR__16 =5
TUPLE1_SCALAR =    6
TUPLE1_FIXED__32 = 7
TUPLE1_FIXED__64 = 8
TUPLE2 =           9
TUPLE4 =           10
TUPLE8 =           11
HALF_MEM =         12
QUARTER_MEM =      13
EIGHTH_MEM =       14
MEM128   =         15
MOVDDUP =          16

# ======================= EFLAGS states

TE_ = 1
MO_ = 2
RE_ = 4
SE_ = 8
UN_ = 0x10
PR_ = 0x20


GENERAL_PURPOSE_INSTRUCTION   =     0x10000
FPU_INSTRUCTION               =     0x20000
MMX_INSTRUCTION               =     0x30000
SSE_INSTRUCTION               =     0x40000
SSE2_INSTRUCTION              =     0x50000
SSE3_INSTRUCTION              =     0x60000
SSSE3_INSTRUCTION             =     0x70000
SSE41_INSTRUCTION             =     0x80000
SSE42_INSTRUCTION             =     0x90000
SYSTEM_INSTRUCTION            =     0xa0000
VM_INSTRUCTION                =     0xb0000
UNDOCUMENTED_INSTRUCTION      =     0xc0000
AMD_INSTRUCTION               =     0xd0000
ILLEGAL_INSTRUCTION           =     0xe0000
AES_INSTRUCTION               =     0xf0000
CLMUL_INSTRUCTION             =    0x100000
AVX_INSTRUCTION               =    0x110000
AVX2_INSTRUCTION              =    0x120000
MPX_INSTRUCTION               =    0x130000
AVX512_INSTRUCTION            =    0x140000
SHA_INSTRUCTION               =    0x150000
BMI2_INSTRUCTION              =    0x160000
CET_INSTRUCTION               =    0x170000
BMI1_INSTRUCTION              =    0x180000
XSAVEOPT_INSTRUCTION          =    0x190000
FSGSBASE_INSTRUCTION          =    0x1a0000
CLWB_INSTRUCTION              =    0x1b0000
CLFLUSHOPT_INSTRUCTION        =    0x1c0000
FXSR_INSTRUCTION              =    0x1d0000
XSAVE_INSTRUCTION             =    0x1e0000
SGX_INSTRUCTION               =    0x1f0000
PCONFIG_INSTRUCTION           =    0x200000

DATA_TRANSFER = 0x1
ARITHMETIC_INSTRUCTION = 2
LOGICAL_INSTRUCTION = 3
SHIFT_ROTATE = 4
BIT_BYTE = 5
CONTROL_TRANSFER = 6
STRING_INSTRUCTION = 7
InOutINSTRUCTION = 8
ENTER_LEAVE_INSTRUCTION = 9
FLAG_CONTROL_INSTRUCTION = 10
SEGMENT_REGISTER = 11
MISCELLANEOUS_INSTRUCTION = 12
COMPARISON_INSTRUCTION = 13
LOGARITHMIC_INSTRUCTION = 14
TRIGONOMETRIC_INSTRUCTION = 15
UNSUPPORTED_INSTRUCTION = 16
LOAD_CONSTANTS = 17
FPUCONTROL = 18
STATE_MANAGEMENT = 19
CONVERSION_INSTRUCTION = 20
SHUFFLE_UNPACK = 21
PACKED_SINGLE_PRECISION = 22
SIMD128bits = 23
SIMD64bits = 24
CACHEABILITY_CONTROL = 25
FP_INTEGER_CONVERSION = 26
SPECIALIZED_128bits = 27
SIMD_FP_PACKED = 28
SIMD_FP_HORIZONTAL = 29
AGENT_SYNCHRONISATION = 30
PACKED_ALIGN_RIGHT = 31
PACKED_SIGN = 32
PACKED_BLENDING_INSTRUCTION = 33
PACKED_TEST = 34
PACKED_MINMAX = 35
HORIZONTAL_SEARCH = 36
PACKED_EQUALITY = 37
STREAMING_LOAD = 38
INSERTION_EXTRACTION = 39
DOT_PRODUCT = 40
SAD_INSTRUCTION = 41
ACCELERATOR_INSTRUCTION = 42
ROUND_INSTRUCTION = 43

JO = 1
JC = 2
JE = 3
JA = 4
JS = 5
JP = 6
JL = 7
JG = 8
JB = 2
JECXZ = 10
JmpType = 11
CallType = 12
RetType = 13
JNO = -1
JNC = -2
JNE = -3
JNA = -4
JNS = -5
JNP = -6
JNL = -7
JNG = -8
JNB = -2

NO_ARGUMENT = 0x10000
REGISTER_TYPE = 0x20000
MEMORY_TYPE = 0x30000
CONSTANT_TYPE = 0x40000

GENERAL_REG = 0x1
MMX_REG = 0x2
SSE_REG = 0x4
AVX_REG = 0x8
AVX512_REG = 0x10
SPECIAL_REG = 0x20
CR_REG = 0x40
DR_REG = 0x80
MEMORY_MANAGEMENT_REG = 0x100
MPX_REG = 0x200
OPMASK_REG = 0x400
SEGMENT_REG = 0x800
FPU_REG = 0x1000


RELATIVE_ = 0x4000000
ABSOLUTE_ = 0x8000000

READ = 0x1
WRITE = 0x2

REG0 = 0x1
REG1 = 0x2
REG2 = 0x4
REG3 = 0x8
REG4 = 0x10
REG5 = 0x20
REG6 = 0x40
REG7 = 0x80
REG8 = 0x100
REG9 = 0x200
REG10 = 0x400
REG11 = 0x800
REG12 = 0x1000
REG13 = 0x2000
REG14 = 0x4000
REG15 = 0x8000
REG16 = 0x10000
REG17 = 0x20000
REG18 = 0x40000
REG19 = 0x80000
REG20 = 0x100000
REG21 = 0x200000
REG22 = 0x400000
REG23 = 0x800000
REG24 = 0x1000000
REG25 = 0x2000000
REG26 = 0x4000000
REG27 = 0x8000000
REG28 = 0x10000000
REG29 = 0x20000000
REG30 = 0x40000000
REG31 = 0x80000000

# Exceptions codes
UD_ = 2

NoTabulation      = 0x00000000
Tabulation        = 0x00000001

MasmSyntax        = 0x00000000
GoAsmSyntax       = 0x00000100
NasmSyntax        = 0x00000200
ATSyntax          = 0x00000400

PrefixedNumeral   = 0x00010000
SuffixedNumeral   = 0x00000000

ShowSegmentRegs   = 0x01000000


# ====================================== Import Disasm function
import os

if os.name == 'nt':
  __module = WinDLL('BeaEngine')
elif os.name == 'posix':
  linuxso = os.path.abspath(os.path.join(os.path.dirname(__file__), 'libBeaEngine.so'))
  __module = CDLL(linuxso)

BeaEngineVersion = __module.BeaEngineVersion
BeaEngineRevision = __module.BeaEngineRevision
BeaEngineVersion.restype = c_char_p
BeaEngineRevision.restype = c_char_p
BeaDisasm = __module.Disasm

#
# BeaEngine helpers
#

class EVEX:
    def __init__(self, params = ""):
        self.reset()

        if re.match("(.*)\.(NDS|NDD|DDS)\.(.*)", params):
            self.vvvv = 0b0

        if re.match("(.*)\.512\.(.*)", params):
            self.LL = 0b10
        elif re.match("(.*)\.256\.(.*)", params):
            self.LL = 0b1

        if re.match("(.*)\.66\.(.*)", params):
            self.pp = 0b1
        elif re.match("(.*)\.F3\.(.*)", params):
            self.pp = 0b10
        elif re.match("(.*)\.F2\.(.*)", params):
            self.pp = 0b11

        if re.match("(.*)\.0F\.(.*)", params):
            self.mm = 0b1
        elif re.match("(.*)\.0F38\.(.*)", params):
            self.mm = 0b10
        elif re.match("(.*)\.0F3A\.(.*)", params):
            self.mm = 0b11

        if re.match("(.*)\.W1(.*)", params):
            self.W = 0b1

    def reset(self):
        self.mm = 0
        self.pp = 0
        self.R = 0
        self.B = 0
        self.R1 = 0
        self.X = 0
        self.vvvv = 0b1111
        self.V = 0
        self.aaa = 0
        self.W = 0
        self.z = 0
        self.b = 0
        self.LL = 0

    def prefix(self):
        return '62{:02x}{:02x}{:02x}'.format(self.p0(),self.p1(),self.p2())

    def p0(self):
        return self.mm + (self.R1 << 4) + (self.B << 5) + (self.X << 6)+ (self.R << 7)

    def p1(self):
        return self.pp + 0b100 + (self.vvvv << 3) + (self.W << 7)

    def p2(self):
        return self.aaa + (self.V << 3) + (self.b << 4) + (self.LL << 5) + (self.z << 7)

class VEX:
    def __init__(self, params = ""):
        self.reset()

        if re.match("(.*)\.(NDS|NDD|DDS)\.(.*)", params):
            self.vvvv = 0b0

        if re.match("(.*)\.256\.(.*)", params):
            self.L = 0b1

        if re.match("(.*)\.66\.(.*)", params):
            self.pp = 0b1
        elif re.match("(.*)\.F3\.(.*)", params):
            self.pp = 0b10
        elif re.match("(.*)\.F2\.(.*)", params):
            self.pp = 0b11

        if re.match("(.*)\.0F38\.(.*)", params):
            self.mmmm = 0b10
        elif re.match("(.*)\.0F3A\.(.*)", params):
            self.mmmm = 0b11
        elif re.match("(.*)\.(0F\.(.*)|0F)", params):
            self.mmmm = 0b1

        if re.match("(.*)\.W1(.*)", params):
            self.W = 0b1

        if re.match("(.*)\.L1(.*)", params):
            self.L = 0b1

    def reset(self):
        self.L = 0
        self.pp = 0
        self.mmmm = 0
        self.W = 0
        self.vvvv = 0b1111
        self.R = 0
        self.X = 0
        self.B = 0

    def c4(self):
        return 'c4{:02x}{:02x}'.format(self.byte1(), self.byte2())

    def c5(self):
        return 'c5{:02x}'.format(self.byte3())

    def byte1(self):
        return self.mmmm + (self.B << 5) + (self.X << 6) + (self.R << 7)

    def byte2(self):
        return self.pp + (self.L << 2) + (self.vvvv << 3) + (self.W << 7)

    def byte3(self):
        return self.pp + (self.L << 2) + (self.vvvv << 3) + (self.R << 7)

class REX:
    def __init__(self):
        self.reset()

    def reset(self):
        self.W = 0
        self.R = 0
        self.X = 0
        self.B = 0

    def byte(self):
        return self.B + (self.X << 1) + (self.R << 2) + (self.W << 3) + 0b01000000


#
# BeaEngine Wrapper
# to hide ctypes complexity
#
class Disasm():
    def __init__(self, buffer, offset=0, virtualAddr=0):
        """
        Init Disasm object
        Example :
            # instantiate BeaEngine on buffer
            buffer = b'\x90\x90\x6a\x00\xe8\xa5\xc7\x02\x00'
            disasm = Disasm(buffer)
        """
        self.buffer = buffer
        self.target = create_string_buffer(buffer,len(buffer))
        self.infos = INSTRUCTION()
        #self.infos.Options = PrefixedNumeral
        self.infos.offset = addressof(self.target) + offset
        self.infos.VirtualAddr = virtualAddr
        self.infos.Archi = 64
        self.length = 0
        self.bytes = bytearray()

    def seek(self, offset = -1):
        """
        getter/setter for offset
        Example :
            disasm.seek(0x400)  # define offset where disasm engine must work
            print("%08x" % disasm.seek())   # get offset position
        """
        if offset == -1:
            return self.infos.offset - addressof(self.target)
        else:
            self.infos.offset = addressof(self.target) + offset
            return offset

    def getBytes(self):
        """
        getter to get bytes sequence of disassembled instruction
        Example:
            print(" ".join("{:02x}".format(b if type(b) == int else ord(b)) for b in self.bytes))
        """
        offset = self.infos.offset - addressof(self.target)
        if self.length == -1:
            self.bytes = self.buffer[offset : offset + 1]
        else:
            self.bytes = self.buffer[offset : offset + self.length]

    def getNextOffset(self):
        """
        setter to define next instruction offset
        """
        if self.infos.Error < 0:
            self.infos.offset += 1
            self.infos.VirtualAddr += 1
        else:
            self.infos.offset = self.infos.offset + self.length
            self.infos.VirtualAddr= self.infos.VirtualAddr+ self.length
        self.length = 0

    def read(self):
        """
        Disassembler routine
        Example:
            buffer = b'\x90\x90\x6a\x00\xe8\xa5\xc7\x02\x00'
            disasm = Disasm(buffer2)
            for i in range(4):
                disasm.read()
        """
        self.getNextOffset()
        self.length = BeaDisasm(c_void_p(addressof(self.infos)))
        self.getBytes()

        return self.length

    def repr(self):
        """
        Complete instruction representation for quick analysis
        Example:
            buffer = b'\x90\x90\x6a\x00\xe8\xa5\xc7\x02\x00'
            disasm = Disasm(buffer2)
            for i in range(4):
                disasm.read()
                print(disasm.repr())
        """
        return "{}".format(self.infos.repr.decode("utf-8"))

        # return "{} {:<30} {}".format(
        #    "0x%08x" %(self.seek()),
        #    " ".join("{:02x}".format(b if type(b) == int else ord(b)) for b in self.bytes),
        #    self.infos.repr.decode("utf-8")
        # )
