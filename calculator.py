#!/bin/bash
python3 << EOF 

def get_number_input(prompt):
	while True:
		try:
			number = float(input(prompt))
			return number
		except ValueError:
			print("Por favor, insira um número válido.")

def perform_operation(num1, num2, operation):
	if operation == '1':
		return num1 + num2
	elif operation == '2':
		return num1 - num2
	elif operation == '3':
		return num1 * num2
	elif operation == '4':
		if num2 != 0:
			return num1 / num2
		else:
			return "Divisão por zero não é permitida"
	else:
		return "Operação Inválida."

def main():
	while True:
		print("\nEscolha uma operação:")
		print("1. Adição")
		print("2. Subtração")
		print("3. Multiplicação")
		print("4. Divisão")
		print("5. sair")

	operation = input("Digite o número da operação desejada.")

	if operation == '5':
		print("Saindo...")
		break

	num1 = get_number_input("Digite o primeiro número: ")
	num2 = get_number_input("Digite o segundo número: ")

	result = perform_operation(num1, num2, operation)

	print("O resultado da operação é: {result}")

if __name__ == "__main__":
	main()

EOF
