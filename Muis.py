import ctypes
from time import sleep

SetCursorPos = ctypes.windll.user32.SetCursorPos
mouse_event = ctypes.windll.user32.mouse_event

def left_click(x, y, clicks=1):
    SetCursorPos(x, y)
    for i in range(clicks):
        mouse_event(2, 0, 0, 0, 0)
        mouse_event(4, 0, 0, 0, 0)
        sleep(0.01)


left_click(190, 400, 10000) #lft clicks at 200, 200 on your screen. Was able to send 10k clicks instantly.