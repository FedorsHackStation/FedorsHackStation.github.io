#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
os.system("pip install pyshorteners")
import pyshorteners
import platform

opsys = platform.platform()
cls = "clear"
if ("Linux" in opsys) or ("linux" in opsys) or ("Mac" in opsys) or ("mac" in opsys):
    cls = "clear"
elif ("Windows" in opsys) or ("windows" in opsys):
    cls = "cls"
os.system(cls)

while True:
	try:
		print("Press enter to quit!")
		link = input("Enter link: ")
		os.system(cls)
		if len(link) == 0:
			break
		shortener = pyshorteners.Shortener()
		x = shortener.tinyurl.short(link)
		print(f"your link: {x}")
	except:
		pass
