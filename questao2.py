def fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def main():
    try:
        num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        if num < 0:
            print("Por favor, informe um número positivo.")
        elif fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Entrada inválida. Por favor, informe um número inteiro.")

if __name__ == "__main__":
    main()