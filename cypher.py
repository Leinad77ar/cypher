def reemplazar_letra(s, rep):
    string = ""
    for letra in s:
        if letra in "aeiouAEIOU" or letra in "12345":
            string += str(rep[letra.lower()])
        else:
            string += letra
    return string

def encode(s):
    return reemplazar_letra(s, rep={'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5 })

def decode(s):
    return reemplazar_letra(s, rep={'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'})

def main():
    while True:
        print("1. Codificar")
        print("2. Decodificar")
        print("3. Salir")
        option = int(input("Ingrese la opcion: "))
        if option == 1:
            s = input("Ingrese el texto: ")
            print('>>> ' + encode(s) + '\n')
        elif option == 2:
            s = input("Ingrese el texto a decodificar: ")
            print('>>> ' + decode(s) + '\n')
        elif option == 3:
            break
        else:
            print("!>>> Opcion invalida \n")

if __name__ == "__main__":
    main()
