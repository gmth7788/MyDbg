#!/usr/bin/env python
#_*_coding:utf-8-*-

from ctypes import *
from my_debugger_defines import *
from test.test_timeout import CreationTestCase

kernel32 = windll.kernel32

class debugger():
    def __init__(selfs):
        pass
    
    def load(self, path_to_exe):
        '''
        创建一个可供调试的全新进程
        '''
        
        #参数dwCreationFlags中的标志位控制着进程的创建方式。
        #若希望创建的进程独占一个新的控制台窗口，而不是与父
        #进程公用同一个控制台，可以加上标志位CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROCESS|CREATE_NEW_CONSOLE
        
        #实例化之前定义的结构体
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFOMATION()
        
        #新建进程将在一个单独的窗体中显示
        startupinfo.dwFlags = 0x01
        startupinfo.wShowWindow = 0x0
        
        #设置结构体STARTUPINFO中的成员变量
        
        #cb的值表示结构体本身的大小
        startupinfo.cb = sizeof(startupinfo)
        
        if (kernel32.CreateProcessA(path_to_exe, 
                                    None,
                                    creation_flags,
                                    None,
                                    None,
                                    startupinfo,
                                    process_information)):
            print("[*] 已经成功启动任务，pid=%d",
                  process_information.dwProcessId)
        else:
            print("[*] 启动任务失败，Error=0x%08x", 
                  kernel32.GetLastError())

        print("okkkkkkk")






        