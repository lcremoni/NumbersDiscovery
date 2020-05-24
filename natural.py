#!/usr/bin/env python

import sys

def natural(last_number):
    number_set = [i+1 for i in range(last_number)]
    return number_set

def line(number_set):
	print(number_set)
    
def main():
	if len(sys.argv) < 2:
		print ("Inserisci almeno un parametro. (Es. natural.py 50)")
		return
	last_number = int(sys.argv[1])
	number_set = natural(last_number)
	line(number_set)

if __name__ == "__main__":
	main()
	

