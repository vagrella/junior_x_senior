# -*- coding: utf-8 -*-
"""
Vornei
PyGetWindow: https://pypi.org/project/PyGetWindow/
File "/home/dev/python/junior_x_senior/.venv/lib/python3.11/site-packages/pygetwindow/__init__.py", line 347, in <module>
    raise NotImplementedError(
NotImplementedError: PyGetWindow currently does not support Linux. If you have Xlib knowledge, please contribute! https://github.com/asweigart/pygetwindow
Perceba que quando acessamos o github do projeto, no README está escrito: "Currently only the Windows platform is implemented."

Environment : MacOS X, Win32 (MS Windows), X11 Applications
"""
import pygetwindow
title = 'Abrindo Google Chrome'
window = pygetwindow.getWindowsWithTitle(title)[0]
window.activate()
window.resizeTo(1280,720)