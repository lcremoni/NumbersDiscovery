#!/usr/bin/env python

import sys

def compose(number):
	i = 2
	compose = False
	while i <= number // 2:
		if number % i == 0:
			number_set = [i,number // i]
			compose = True
			#print(number_set)
		i += 1
	return compose

def composite(last_number):
	i = 2
	number_set = []
	while i <= last_number:
		if compose(i): number_set.append(i)
		i += 1
	return number_set

def prime(last_number):
	i = 2
	number_set = []
	while i <= last_number:
		if not compose(i): number_set.append(i)
		i += 1
	return number_set

def multiple(number,last_number):
	number_set = [number]
	i = 2
	while i*number <= last_number:
		number_set.append(i*number)
		i += 1
	return number_set

def natural(last_number):
    number_set = [i+1 for i in range(last_number)]
    return number_set

def line(number_set):
	print(number_set)
    
def main():
	if len(sys.argv) < 2:
		print ("Inserisci almeno un parametro. (Es. natural.py 50)")
		return
	command = sys.argv[1]
	if command == 'natural':
		last_number = int(sys.argv[2])
		number_set = natural(last_number)
		line(number_set)
	if command == 'multiple':
		last_number = int(sys.argv[2])
		number = int(sys.argv[3])
		number_set = multiple(number,last_number)
		line(number_set)
	if command == 'compose':
		number = int(sys.argv[2])
		print(compose(number))
	if command == 'composite':
		last_number = int(sys.argv[2])
		number_set = composite(last_number)
		line(number_set)
	if command == 'prime':
		last_number = int(sys.argv[2])
		number_set = prime(last_number)
		line(number_set)

if __name__ == "__main__":
	main()
	

