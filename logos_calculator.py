import sys
import os
import platform
from sympy import *

try:
	def menu(): # This section displays the different options available to the user
		clear()
		print(ctext("Welcome to Logos Calculator. Please select one of the options below:", "red", "bold", "white"))
		options = ["1) Limit calculator", "2) Derivative Calculator", "3) Integral Calculator"]
		for i in options:
			print(ctext(i, "cyan", "neutral", "white"))
		print(ctext("[type q to quit.]\n", "white", "neutral", "black"))
		while 1:
			cho = input(ctext("[choice]> ", "yellow", "neutral", "black"))
			back(cho)
			if cho == "1":
				limits()
			if cho == "2":
				derivative()
			if cho == "3":
				integral()
			else:
				print("Invalid input.")

	def limits():
		clear()
		print("Enter the function of x you want to find the limit of as x approaches c, then enter c:\n(type b to go back to the menu)")
		while 1:
			funct = input("f(x) = ")
			back(funct)
			c = input("c = ")
			back(c)
			x = symbols('x')
			init_printing(use_unicode=True)
			answer = limit(funct, x, c)
			print("lim(x→{0})({1}) = {2}".format(c, funct, answer))


	def derivative():
		clear()
		print("Enter the function of x you want to find the derivative of:\n(type b to go back to the menu)")
		while 1:
			funct = input("f(x) = ")
			back(funct)
			x, y, z = symbols('x y z')
			init_printing(use_unicode=True)
			answer = diff(funct, x)
			print("d/dx ⋅ {0} = {1}".format(funct, answer))

	def integral():
		clear()
		print("Enter the function of x you want to find the integral of:\n(type b to go back to the menu)")
		while 1:
			funct = input("f(x) = ")
			back(funct)
			x, y, z = symbols('x y z')
			init_printing(use_unicode=True)
			answer = integrate(funct, x)
			print("∫{0}dx = {1}".format(funct, answer))

	def back(char):
		if char == "b":
			menu()
		if char == "q":
			sys.exit()
		return 0

	def clear():
		if platform.system() == "Windows":
			os.system('cls')
		else:
			os.system('clear')
		return 0

	def ctext(text, textColor, textStyle, backgroundColor):
		tColor = {
			"black": "30",
			"red": "31",
			"green": "32",
			"yellow": "33",
			"blue": "34",
			"purple": "35",
			"cyan": "36",
			"white": "37",
		}

		tStyle = {
			"neutral": "0",
			"bold": "1",
			"underline": "2",
		}

		bColor = {
			"black": "40",
			"red": "41",
			"green": "42",
			"yellow": "43",
			"blue": "44",
			"purple": "45",
			"cyan": "46",
			"white": "47",
		}

		coloredText = "\033[{0};{1};{2}m{3}".format(tStyle[textStyle], tColor[textColor], bColor[backgroundColor], text)
		return coloredText + "\033[0m"

	menu()

except Exception as e:
	print(e)