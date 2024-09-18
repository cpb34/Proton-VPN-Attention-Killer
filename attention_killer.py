import win32gui
import win32process
import win32con
import psutil
import time

def callback(hwnd, handle):
    if win32gui.IsWindowVisible(hwnd):
        window_name = win32gui.GetWindowText(hwnd)
        if window_name == "Attention":
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            if psutil.Process(pid).name() == "ProtonVPN.exe":
                handle.append(hwnd)
    return True

start_time = time.time()
timeout = 60

while time.time() - start_time < timeout:
    handle = []
    win32gui.EnumWindows(callback, handle)
    
    if handle:
        win32gui.PostMessage(handle[0], win32con.WM_CLOSE, 0, 0)
        break
    else:
        time.sleep(0.1)