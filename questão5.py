def inverter_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

def main():
    string = input("Informe uma string para ser invertida: ")
    
    string_invertida = inverter_string(string)
    print(f"A string invertida é: {string_invertida}")

if __name__ == "__main__":
    main()