#!/usr/bin/env python
#_*_coding:utf-8-*-


from ctypes import *
from _winapi import CREATE_NEW_CONSOLE

#Ϊctype������������������������������
WORD    = c_ushort
DWORD   = c_ulong
LPBYTE  = POINTER(c_ubyte)
LPTSTR  = POINTER(c_char)
HANDLE  = c_void_p

#���峣��
DEBUG_PROCESS = 0x01
CREATE_NEW_CONSOLE = 0x10

#���庯��CreateProcessA()����Ľṹ��
class STARTUPINFO(Structure):
    _fields_=[ 
              ("cb", DWORD),
              ("lpReserved", LPTSTR),
              ("lpDesktop", LPTSTR),
              ("lpTitle", LPTSTR),
              ("dwX", DWORD),
              ("dwY", DWORD),
              ("dwXSize", DWORD),
              ("dwYSize", DWORD),
              ("dwXCountChars", DWORD),
              ("dwYCountChars", DWORD),
              ("dwFillAttribute", DWORD),
              ("dwFlags", DWORD),
              ("wShowWindow", WORD),
              ("cbReserved2", WORD),
              ("lpReversed2",LPBYTE),
              ("hStdInput", HANDLE),
              ("hStdOutput", HANDLE),
              ("hStdError", HANDLE),
              ]
    
class PROCESS_INFOMATION(Structure):
    _fields_ = [
                ("hProcess", HANDLE),
                ("hThread", HANDLE),
                ("dwProcessId", DWORD),
                ("dwThreadId", DWORD),
                ]

    
    
    
    
    
