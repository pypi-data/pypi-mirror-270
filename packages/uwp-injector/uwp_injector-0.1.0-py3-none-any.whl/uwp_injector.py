import logging
import os
import sys

import ntsecuritycon
import psutil
import pywintypes
import win32api
import win32con
import win32event
import win32process
import win32security


def inject(executable_name, dll_path):
    logging.basicConfig(
        filename="injector-log.txt",
        level=logging.DEBUG,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
    )

    dll_path = os.path.abspath(dll_path)
    logging.info(f"inject {repr(dll_path)}")

    # edit dll access permissions, required for UWP injection
    sid = win32security.ConvertStringSidToSid("S-1-15-2-1")  # ALL APPLICATION PACKAGES

    sec = win32security.GetFileSecurity(
        dll_path, win32security.DACL_SECURITY_INFORMATION
    )
    acl = sec.GetSecurityDescriptorDacl()
    acl.AddAccessAllowedAce(
        win32security.ACL_REVISION,
        ntsecuritycon.FILE_GENERIC_READ | ntsecuritycon.FILE_GENERIC_EXECUTE,
        sid,
    )
    sec.SetSecurityDescriptorDacl(1, acl, 0)
    win32security.SetFileSecurity(
        dll_path, win32security.DACL_SECURITY_INFORMATION, sec
    )

    # get pid
    pid = None
    for p in psutil.process_iter():
        if p.name() == executable_name:
            pid = p.pid
            break

    # inject dll
    logging.debug(f"pid {pid}")
    if pid is not None:
        handle = win32api.OpenProcess(win32con.MAXIMUM_ALLOWED, pywintypes.FALSE, pid)
        logging.debug(f"handle {int(handle)}")
        p1 = win32process.VirtualAllocEx(
            handle,
            0,
            len(dll_path) + 1,
            win32con.MEM_COMMIT | win32con.MEM_RESERVE,
            win32con.PAGE_EXECUTE_READWRITE,
        )
        win32con.PAGE_NOACCESS
        logging.debug(f"p1 {p1}")
        written = win32process.WriteProcessMemory(handle, p1, dll_path)
        logging.debug(f"written {written}")
        procAddress = win32api.GetProcAddress(
            win32api.GetModuleHandle("kernel32.dll"), "LoadLibraryA"
        )
        logging.debug(f"procAddress {procAddress}")
        p3 = win32process.CreateRemoteThread(handle, None, 0, procAddress, p1, 0)
        logging.debug(f"p3 {int(p3[0]),p3[1]}")
        n = win32event.WaitForSingleObject(p3[0], 5000)
        logging.debug(f"n {n}")
        win32process.VirtualFreeEx(handle, p1, 0, win32con.MEM_RELEASE)
        win32api.CloseHandle(p3[0])
        win32api.CloseHandle(handle)

    else:
        err = "Process not running"
        logging.error(err)
        raise ProcessLookupError(err)


if __name__ == "__main__":
    inject(*sys.argv[1:])
