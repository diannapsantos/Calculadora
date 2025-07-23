import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')

def calcular(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    elif operacao == '**':
        return num1 ** num2
    else:
        return "Operação inválida"

def main():
    while True:
        try:
            num1 = float(input("Insere o primeiro número: "))
            num2 = float(input("Insere o segundo número: "))
            operacao = input("Escolhe a operação (+, -, *, /, **): ")

            resultado = calcular(num1, num2, operacao)
            print(f"Resultado: {resultado}")

            continuar = input("Desejas continuar? (s/n): ").lower()
            if continuar != 's':
                print("Calculadora encerrada.")
                break
        except ValueError:
            print("Por favor, insere um número válido.")

if __name__ == "__main__":
    main()
