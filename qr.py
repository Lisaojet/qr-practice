# importing the qrcode library
import os
import pyqrcode

name = 'Project'
k = pyqrcode.create(name)
k.png('test.png', scale=10)

os.system('test.png')
