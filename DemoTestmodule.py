# DemoTestmodule.py

import testmodule as t1
import testmodule as t2
import socket
from _thread import *

print(dir())
t2.printDefaultValue()
t1.defaultvalue =100
t2.printDefaultValue()

_opener = None
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None):
    print("urlopen define")

