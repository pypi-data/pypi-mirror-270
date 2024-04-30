#  Python wrapper module header file for PIRC API
#
#  Copyright (C) 1988 - 2024, Pickering Interfaces ltd.
#
#  Support: support@pickeringswitch.com
#  Supported OS: Mac OS 10.9.2, Windows XP/7/8/10/11, Linux
#
# Licence:
# This agreement is made between Pickering Interfaces Ltd ("Pickering") and you,
# the person who makes use of Pickering software products ("You"). You must agree
# all terms in this agreement in order to use Pickering software legally. If you
# don't agree all terms in the agreement, please don't use Pickering software, and
# delete all related files from your computer.
#
# 1. OWNERSHIP: Pickering software is fully owned by Pickering, this license
# agreement doesn't change the ownership.
#
# 2. LICENSE: Pickering grants You the license to use Pickering software, free of
# charge, if you accept all the conditions listed in this agreement. "Use" means
# loading the product to CPU, memory, and/or other storage on your computer.
#
# 3. CONDITIONS: To be licensed to use Pickering software, You must:
#    a) Not modify any part of Pickering software;
#    b) Agree to release Pickering from all liabilities caused directly or
#       indirectly by using Pickering software;
#    c) Agree not to attempt to reverse engineer, de-compile or use any other
#       tools to extract source code from Pickering Software.
#
# 4. CONSEQUENTIAL LICENSES: Some functions of Pickering software requires
# additional licenses to fully operate. Pickering accepts no responsibility for
# the provision of said licenses.
#
# 5. REDISTRIBUTION:. You may freely re-distribute Pickering software in any way
# unless explicitly stated to the contrary for a particular product.

import ctypes
import platform
import sys
from enum import IntEnum

__version__ = "1.0"
"""Pil relay counting python wrapper version"""

#region Enums

class ErrorCodes(IntEnum):
    RC_NO_ERR					= 0,    # No error
    RC_ER_NO_CARD				= 1,    # No card present with specified number
    RC_ER_NO_INFO				= 2,    # Card information unobtainable - (file problem)
    RC_ER_BAD_SUB				= 3,    # Card has no sub-unit with specified number
    RC_ER_BAD_BIT				= 4,    # Sub-unit has no bit with specified number
    RC_ER_INVALID_ARG_POINTER	= 5,    # Invalid user-argument function pointer
    RC_ER_INVALID_POINTER		= 6,    # Internal error pointer inside library
    RC_ER_FILESYSTEM			= 7,    # Filesystem error
    RC_ER_INTERNAL_PTR_FREE		= 8,    # Internal Free pointer error
    RC_ER_UNKNOWN_LIMIT_TYPE	= 9,    # Unknown limit type
    RC_ER_NUM = 10,					    # Number of error codes

class SubUnitTypes(IntEnum):
    TYPE_PHYSICAL	= 0,	            # Physical card structure
    TYPE_SW			= 1,	            # Uncommitted switches
    TYPE_MUX		= 2,	            # Relay multiplexer (single-channel only)
    TYPE_MUXM		= 3,	            # Relay multiplexer (multi-channel capable)
    TYPE_MAT		= 4,	            # Standard matrix
    TYPE_MATR		= 5,	            # RF matrix
    TYPE_DIG		= 6,	            # Digital outputs
    TYPE_RES		= 7,	            # Programmable Resistor
    TYPE_ATTEN		= 8,	            # Programmable Attenuator
    TYPE_PSUDC		= 9,	            # Power supply - DC
    TYPE_BATT		= 10,	            # Battery simulator
    TYPE_VSOURCE	= 11,	            # Programmable voltage source
    TYPE_MATP		= 12,	            # Matrix with restricted operating modes
    TYPE_MUXMS		= 13,	            # Relay multiplexer (MUXM hardware emulated as MUX)
    TYPE_FI			= 14,	            # Sub-unit with restricted operation based on other Sub-unit operation 
    TYPE_DM			= 15,	            # Displacement Module simulator
    TYPE_PSOURCE	= 16,	            # Power Source module
    TYPE_DIO		= 17	            # DIO Subunit

class CountLimits(IntEnum):
    COUNT_WARNING	= 0,
    COUNT_CRITICAL	= 1,
    COUNT_LIMIT_NUM = 2,

#endregion

class _CardInfo:
    def __init_(self, cardIdStr):
        cardIdData = str.split(cardIdStr, ',')
        self.typecode = cardIdData[0]
        self.serialNumber = cardIdData[1]
        self.revision = cardIdData[2]
        
class Error(Exception):
    """Base error class provides error message and optional error code from library."""
    
    def __init__(self, message, errorCode=None):
        self.message = message
        self.errorCode = errorCode
        
    def __str__(self):
        return self.message

class PIRC_Base:
    def __init__(self):
        if platform.system() == "Windows":
            self.handle = ctypes.windll.LoadLibrary("Pirc")
        elif platform.system() == "Linux":
            arch = platform.architecture()
            if "64bit" in arch:
                self.handle = ctypes.cdll.LoadLibrary("libpirc64.so")
            else:
                self.handle = ctypes.cdll.LoadLibrary("libpirc32.so")
        
        self.pythonMajorVersion = sys.version_info[0]
        
        # Holds data for clearing later
        self._CardListFnStr = 0
        self._ListLen = 0
        
        #region Dict enums
        
        # Error Code Enum
        self.ERRORCODE = {
            "RC_NO_ERR" : 0,	            # No error
            "RC_ER_NO_CARD" : 1,            # No card present with specified number
            "RC_ER_NO_INFO" : 2,            # Card information unobtainable - (file problem)
            "RC_ER_BAD_SUB" : 3,            # Card has no sub-unit with specified number
            "RC_ER_BAD_BIT" : 4,            # Sub-unit has no bit with specified number
            "RC_ER_INVALID_ARG_POINTER" : 5,# Invalid user-argument function pointer
            "RC_ER_INVALID_POINTER" : 6,    # Internal error pointer inside library
            "RC_ER_FILESYSTEM" : 7,         # Filesystem error
            "RC_ER_INTERNAL_PTR_FREE" : 8,  # Internal Free pointer error
            "RC_ER_UNKNOWN_LIMIT_TYPE" : 9, # Unknown limit type
            "RC_ER_NUM" : 10                # Number of error codes
        }
        
        self.SUBUNITTYPE = {
            "TYPE_PHYSICAL" : 0,	        # Physical card structure
            "TYPE_SW" : 1,	                # Uncommitted switches
            "TYPE_MUX" : 2,	                # Relay multiplexer (single-channel only)
            "TYPE_MUXM" : 3,	            # Relay multiplexer (multi-channel capable)
            "TYPE_MAT" : 4,	                # Standard matrix
            "TYPE_MATR" : 5,	            # RF matrix
            "TYPE_DIG" : 6,	                # Digital outputs
            "TYPE_RES" : 7,	                # Programmable Resistor
            "TYPE_ATTEN" : 8,	            # Programmable Attenuator
            "TYPE_PSUDC" : 9,	            # Power supply - DC
            "TYPE_BATT" : 10,	            # Battery simulator
            "TYPE_VSOURCE" : 11,	        # Programmable voltage source
            "TYPE_MATP" : 12,	            # Matrix with restricted operating modes
            "TYPE_MUXMS" : 13,	            # Relay multiplexer (MUXM hardware emulated as MUX)
            "TYPE_FI" : 14,	                # Sub-unit with restricted operation based on other Sub-unit operation 
            "TYPE_DM" : 15,	                # Displacement Module simulator
            "TYPE_PSOURCE" : 16,	        # Power Source module
            "TYPE_DIO" : 17	                # DIO Subunit
        }
        
        self.COUNTLIMITS = {
            "COUNT_WARNING" : 0,
            "COUNT_CRITICAL" : 1,
            "COUNT_LIMIT_NUM" : 2
        }
        #endregion
        
    #region Internal methods
        
    def _handleError(self, error):
        if error:
            errorString = self.GetErrorMessage(error)
            raise Error(errorString, errorCode=error)
            
    def _calc_dwords(self,bits):
        dwords = floor(bits/32)
        if ((bits) % 32 > 0):
            dwords += 1
        return int(dwords)    
            
    def _pythonString(self, inputString):
        if self.pythonMajorVersion < 3:
            return inputString
        else:
            return inputString.decode()
                
    #endregion
    
    def Version(self):
        ver = self.handle.PIRC_Version()
        return ver
    
    def CardDataAvailable(self):
        StrLen = ctypes.pointer(ctypes.c_uint32())
        ListLen = ctypes.pointer(ctypes.c_uint32())

        c_char_pp = ctypes.POINTER(ctypes.c_char_p)()

        c_cardlistfnstr_p = ctypes.pointer(c_char_pp)

        err = self.handle.PIRC_CardDataAvailable(c_cardlistfnstr_p, StrLen, ListLen)
        self._handleError(err)

        self._CardListFnStr = c_cardlistfnstr_p
        CardDataList = []
        for i in range(ListLen.contents.value):
            c_str = c_cardlistfnstr_p.contents[i]
            if c_str is not None:
                CardDataList.append(c_str.decode('utf-8'))

        return CardDataList, StrLen.contents.value, ListLen.contents.value
    
    def CardDataFree(self):
        err = self.handle.PIRC_CardDataFree(self._CardListFnStr, self._ListLen)
        self._handleError(err)

        return err
        
    def OpenSpecifiedCardData(self, CardFnStr:str):
        CardFnStr = ctypes.c_char_p(bytes(CardFnStr.encode()))
        CardNum = ctypes.c_uint32()

        err = self.handle.PIRC_OpenSpecifiedCardData(CardFnStr, ctypes.byref(CardNum))
        self._handleError(err)

        return CardNum.value
    
    def CloseSpecifiedCardData(self):
        err = self.handle.PIRC_CloseSpecifiedCardData()
        self._handleError(err)

        return err
        
    def OpenSpecifiedLocationCardData(self, FilePathFn):
        FilePathFn = ctypes.c_char_p(FilePathFn)
        CardNum = ctypes.c_uint32()
        err = self.handle.PIRC_OpenSpecifiedLocationCardData(FilePathFn, ctypes.byref(CardNum))
        self._handleError(err)
        return CardNum.value
    
    def EnumerateSub(self,CardNum):
        CardNum = ctypes.c_uint32(CardNum)
        SubNum = ctypes.c_uint32()

        err = self.handle.PIRC_EnumerateSub(CardNum, ctypes.byref(SubNum))
        self._handleError(err)

        return SubNum.value
    
    def CardDataId(self, CardNum):
        CardNum = ctypes.c_uint32(CardNum)
        Str = ctypes.create_string_buffer(255)

        err = self.handle.PIRC_CardDataId(CardNum, Str)
        self._handleError(err)

        return Str.value
    
    def CardDataRevision(self, CardNum):
        CardNum = ctypes.c_uint32(CardNum)
        Count = ctypes.c_uint32()

        err = self.handle = PIRC_CardDataRevision(CardNum, ctypes.byref(Count))
        self._handleError(err)

        return Count.value
    
    def SubInfo(self, CardNum, SubNum):
        CardNum = ctypes.c_uint32(CardNum)
        SubNum = ctypes.c_uint32(SubNum)
        TypeNum = ctypes.c_uint32()
        Rows = ctypes.c_uint32()
        Cols = ctypes.c_uint32()

        err = self.handle.PIRC_SubInfo(CardNum, SubNum, ctypes.byref(TypeNum), ctypes.byref(Rows), ctypes.byref(Cols))
        self._handleError(err)

        return TypeNum.value, Rows.value, Cols.value
    
    def SubType(self, CardNum, SubNum):
        CardNum = ctypes.c_uint32(CardNum)
        SubNum = ctypes.c_uint32(SubNum)
        Str = ctypes.pointer(ctypes.c_char_p)

        err = self.handle.PIRC_SubType(CardNum, SubNum, Str)
        self._handleError(err)

        return Str.contents
    
    def GetCrosspointOps(self, CardNum, OutSub, Row, Column):
        CardNum = ctypes.c_uint32(CardNum)
        OutSub = ctypes.c_uint32(OutSub)
        Row = ctypes.c_uint32(Row)
        Column = ctypes.c_uint32(Column)
        Count = ctypes.c_uint32()

        err = self.handle.PIRC_GetCrosspointOps(CardNum, OutSub, Row, Column, ctypes.byref(Count))
        self._handleError(err)

        return Count.value
    
    def GetSwitchOps(self, CardNum, OutSub, BitNum):
        CardNum = ctypes.c_uint32(CardNum)
        OutSub = ctypes.c_uint32(OutSub)
        BitNum = ctypes.c_uint32(BitNum)
        Count = ctypes.c_uint32()

        err = self.handle.PIRC_GetSwitchOps(CardNum, OutSub, BitNum, ctypes.byref(Count))
        self._handleError(err)

        return Count.value


    def GetLastHighestSwitchOps(self, CardNum, SubNum, CountsNum):
        CardNum = ctypes.c_uint32(CardNum)
        SubNum = ctypes.c_uint32(SubNum)
        Counts = ctypes.c_uint32()
        CountsNum = ctypes.c_uint32(CountsNum)

        err = self.handle.PIRC_GetLastHighestSwitchOps(CardNum, SubNum, ctypes.byref(Counts), CountsNum)
        self._handleError(err)

        return Counts.value
    
    def GetMaxOps(self, CardNum, OutSub, Counts):
        CardNum = ctypes.c_uint32(CardNum)
        OutSub = ctypes.c_uint32(OutSub)
        Count = ctypes.c_uint32()

        err = self.handle.PIRC_GetMaxOps(CardNum, OutSub, ctypes.byref(Counts))
        self._handleError(err)

        return Count.value
    
    def GetMeanOps(self, CardNum, OutSub):
        CardNum = ctypes.c_uint32(CardNum)
        OutSub = ctypes.c_uint32(OutSub)
        Count = ctypes.c_double()
        
        err = self.handle.PIRC_GetMeanOps(self, CardNum, OutSub, ctypes.byref(Count))
        self._handleError(err)

        return Count.value

    def SetSwitchLimit(self, LimitType, Value):
        LimitType = ctypes.c_uint32(LimitType)
        Value = ctypes.c_uint32(Value)

        err = self.handle.SetSwitchLimit(LimitType, Value)
        self._handleError(err)
        return err
    
    def GetSwitchLimit(self, LimitType):
        LimitType = ctypes.c_uint32(LimitType)
        Value = ctypes.c_uint32()

        err = self.handle.PIRC_SetSwitchLimit(LimitType, ctypes.byref(Value))
        self._handleError(err)

        return Value.value
    
    def GetErrorMessage(self, errorCode):
        errorCode = ctypes.c_uint32(errorCode)
        
        message: ctypes.c_char_p
        message = self.handle.PIRC_GetErrorMessage(errorCode)

        return message.value
