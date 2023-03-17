# Built-in libraries
import os


def main():
	print("Enter one of the following choices:")
	print("E: Encrypt file")
	print("D: Decrypt file")

	process = input("Choice: ")
	while process not in ('e', 'E', 'd', 'D'):
		process = input("Try again: ")

	file = input("File to process: ")

	print(process, file)


if __name__ == '__main__':
	main()
