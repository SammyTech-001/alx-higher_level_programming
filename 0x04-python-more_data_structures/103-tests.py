import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_Python_list.argtypes = [ctypes.py_object]
lib.print_Python_bytes.argtypes = [stypes.py_object]
s = b"hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_Python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_Python_bytes(b);
l = [b'Hello', b'World']
lib.print_Python_list(l)
del l[1]
lib.print_Python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_Python_list(l)
l = []
lib.print_Python_list(l)
l.append(0)
lib.print_Python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_Python_list(l)
l = ["Holberton"]
lib.print_Python_list(l)
lib.print_Python_bytes(l);
