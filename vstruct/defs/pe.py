
from __future__ import absolute_import
import vstruct
from vstruct.primitives import *
from six.moves import range

class IMAGE_BASE_RELOCATION(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.VirtualAddress = v_uint32()
        self.SizeOfBlock    = v_uint32()

class IMAGE_DATA_DIRECTORY(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.VirtualAddress = v_uint32()
        self.Size           = v_uint32()

class IMAGE_DOS_HEADER(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.e_magic    = v_uint16()
        self.e_cblp     = v_uint16()
        self.e_cp       = v_uint16()
        self.e_crlc     = v_uint16()
        self.e_cparhdr  = v_uint16()
        self.e_minalloc = v_uint16()
        self.e_maxalloc = v_uint16()
        self.e_ss       = v_uint16()
        self.e_sp       = v_uint16()
        self.e_csum     = v_uint16()
        self.e_ip       = v_uint16()
        self.e_cs       = v_uint16()
        self.e_lfarlc   = v_uint16()
        self.e_ovno     = v_uint16()
        self.e_res      = vstruct.VArray([v_uint16() for i in range(4)])
        self.e_oemid    = v_uint16()
        self.e_oeminfo  = v_uint16()
        self.e_res2     = vstruct.VArray([v_uint16() for i in range(10)])
        self.e_lfanew   = v_uint32()

class IMAGE_EXPORT_DIRECTORY(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Characteristics    = v_uint32()
        self.TimeDateStamp      = v_uint32()
        self.MajorVersion       = v_uint16()
        self.MinorVersion       = v_uint16()
        self.Name               = v_uint32()
        self.Base               = v_uint32()
        self.NumberOfFunctions  = v_uint32()
        self.NumberOfNames      = v_uint32()
        self.AddressOfFunctions = v_uint32()
        self.AddressOfNames     = v_uint32()
        self.AddressOfOrdinals  = v_uint32()

class IMAGE_FILE_HEADER(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Machine              = v_uint16()
        self.NumberOfSections     = v_uint16()
        self.TimeDateStamp        = v_uint32()
        self.PointerToSymbolTable = v_uint32()
        self.NumberOfSymbols      = v_uint32()
        self.SizeOfOptionalHeader = v_uint16()
        self.Ccharacteristics     = v_uint16()

class IMAGE_IMPORT_DIRECTORY(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.OriginalFirstThunk = v_uint32()
        self.TimeDateStamp      = v_uint32()
        self.ForwarderChain     = v_uint32()
        self.Name               = v_uint32()
        self.FirstThunk         = v_uint32()

class IMAGE_LOAD_CONFIG_DIRECTORY(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Size                          = v_uint32()
        self.TimeDateStamp                 = v_uint32()
        self.MajorVersion                  = v_uint16()
        self.MinorVersion                  = v_uint16()
        self.GlobalFlagsClear              = v_uint32()
        self.GlobalFlagsSet                = v_uint32()
        self.CriticalSectionDefaultTimeout = v_uint32()
        self.DeCommitFreeBlockThreshold    = v_uint32()
        self.DeCommitTotalFreeThreshold    = v_uint32()
        self.LockPrefixTable               = v_uint32()
        self.MaximumAllocationSize         = v_uint32()
        self.VirtualMemoryThreshold        = v_uint32()
        self.ProcessHeapFlags              = v_uint32()
        self.ProcessAffinityMask           = v_uint32()
        self.CSDVersion                    = v_uint16()
        self.Reserved1                     = v_uint16()
        self.EditList                      = v_uint32()
        self.SecurityCookie                = v_uint32()
        self.SEHandlerTable                = v_uint32()
        self.SEHandlerCount                = v_uint32()

class IMAGE_NT_HEADERS(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Signature      = v_bytes(4)
        self.FileHeader     = IMAGE_FILE_HEADER()
        self.OptionalHeader = IMAGE_OPTIONAL_HEADER()

class IMAGE_NT_HEADERS64(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Signature      = v_bytes(4)
        self.FileHeader     = IMAGE_FILE_HEADER()
        self.OptionalHeader = IMAGE_OPTIONAL_HEADER64()

class IMAGE_OPTIONAL_HEADER(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Magic                       = v_bytes(2)
        self.MajorLinkerVersion          = v_uint8()
        self.MinorLinkerVersion          = v_uint8()
        self.SizeOfCode                  = v_uint32()
        self.SizeOfInitializedData       = v_uint32()
        self.SizeOfUninitializedData     = v_uint32()
        self.AddressOfEntryPoint         = v_uint32()
        self.BaseOfCode                  = v_uint32()
        self.BaseOfData                  = v_uint32()
        self.ImageBase                   = v_uint32()
        self.SectionAlignment            = v_uint32()
        self.FileAlignment               = v_uint32()
        self.MajorOperatingSystemVersion = v_uint16()
        self.MinorOperatingSystemVersion = v_uint16()
        self.MajorImageVersion           = v_uint16()
        self.MinorImageVersion           = v_uint16()
        self.MajorSubsystemVersion       = v_uint16()
        self.MinorSubsystemVersion       = v_uint16()
        self.Win32VersionValue           = v_uint32()
        self.SizeOfImage                 = v_uint32()
        self.SizeOfHeaders               = v_uint32()
        self.CheckSum                    = v_uint32()
        self.Subsystem                   = v_uint16()
        self.DllCharacteristics          = v_uint16()
        self.SizeOfStackReserve          = v_uint32()
        self.SizeOfStackCommit           = v_uint32()
        self.SizeOfHeapReserve           = v_uint32()
        self.SizeOfHeapCommit            = v_uint32()
        self.LoaderFlags                 = v_uint32()
        self.NumberOfRvaAndSizes         = v_uint32()
        self.DataDirectory               = vstruct.VArray([IMAGE_DATA_DIRECTORY() for i in range(16)])

class IMAGE_OPTIONAL_HEADER64(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Magic                       = v_bytes(2)
        self.MajorLinkerVersion          = v_uint8()
        self.MinorLinkerVersion          = v_uint8()
        self.SizeOfCode                  = v_uint32()
        self.SizeOfInitializedData       = v_uint32()
        self.SizeOfUninitializedData     = v_uint32()
        self.AddressOfEntryPoint         = v_uint32()
        self.BaseOfCode                  = v_uint32()
        self.ImageBase                   = v_uint64()
        self.SectionAlignment            = v_uint32()
        self.FileAlignment               = v_uint32()
        self.MajorOperatingSystemVersion = v_uint16()
        self.MinorOperatingSystemVersion = v_uint16()
        self.MajorImageVersion           = v_uint16()
        self.MinorImageVersion           = v_uint16()
        self.MajorSubsystemVersion       = v_uint16()
        self.MinorSubsystemVersion       = v_uint16()
        self.Win32VersionValue           = v_uint32()
        self.SizeOfImage                 = v_uint32()
        self.SizeOfHeaders               = v_uint32()
        self.CheckSum                    = v_uint32()
        self.Subsystem                   = v_uint16()
        self.DllCharacteristics          = v_uint16()
        self.SizeOfStackReserve          = v_uint64()
        self.SizeOfStackCommit           = v_uint64()
        self.SizeOfHeapReserve           = v_uint64()
        self.SizeOfHeapCommit            = v_uint64()
        self.LoaderFlags                 = v_uint32()
        self.NumberOfRvaAndSizes         = v_uint32()
        self.DataDirectory               = vstruct.VArray([IMAGE_DATA_DIRECTORY() for i in range(16)])

class IMAGE_RESOURCE_DIRECTORY(vstruct.VStruct):
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Characteristics      = v_uint32()
        self.TimeDateStamp        = v_uint32()
        self.MajorVersion         = v_uint16()
        self.MinorVersion         = v_uint16()
        self.NumberOfNamedEntries = v_uint16()
        self.NumberOfIdEntries    = v_uint16()

class IMAGE_SECTION_HEADER(vstruct.VStruct):

    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.Name                 = v_str(8)
        self.VirtualSize          = v_uint32()
        self.VirtualAddress       = v_uint32()
        self.SizeOfRawData        = v_uint32()
        self.PointerToRawData     = v_uint32()
        self.PointerToRelocations = v_uint32()
        self.PointerToLineNumbers = v_uint32()
        self.NumberOfRelocations  = v_uint16()
        self.NumberOfLineNumbers  = v_uint16()
        self.Characteristics      = v_uint32()


class IMAGE_RUNTIME_FUNCTION_ENTRY(vstruct.VStruct):
    """
    Used in the .pdata section of a PE32+ for all non
    leaf functions.
    """
    def __init__(self):
        vstruct.VStruct.__init__(self)
        self.BeginAddress = v_uint32()
        self.EndAddress = v_uint32()
        self.UnwindInfoAddress = v_uint32()

