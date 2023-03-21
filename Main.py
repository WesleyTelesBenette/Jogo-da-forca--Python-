
# Jogo da forca

import os
import random

def sortear_palavra():
    f = 0.
    palavra = ""
    dica = ""
    palavras = {}
    with open("C:\WF\Estudo\Python\PythonBrasil\meu01.txt", "r", encoding="utf-8") as arq:
        while (True):
            dados = arq.readline()
            if (dados != ""):
                for c in range(0, len(dados)):
                    if (dados[c] != " "):
                        palavra += dados[c]
                    else:
                        dica = dados[(c+1):]
                        if (dica[len(dica)-1] == "\n"):
                            d = list(dica)
                            d[len(dica)-1] = ""
                            dica = "".join(d)
                        break
                palavras[f] = [palavra, dica]
                f += 1
                palavra = ""
                dica = ""
            else:
                break
    index = random.randint(0, len(palavras)-1)

    return palavras[index][0], palavras[index][1]

def jogo():
    os.system("cls") or None

    #variáveis
    palavra, dica = sortear_palavra()
    palavra_final = str("_"*len(palavra))
    letras_ja = [""]
    repetido = 0

    alguma_letra = 0
    erros = 0

    while (True):
        os.system("CLS") or None
        print("\n Letras chutadas: ", end="")
        for c in letras_ja:
            if (c != ""):
                print(c + ", ", end="")
        print("\n Erros: ", erros);

        print("\n _______")
        print(" |     | Dica: " + dica)
        print(" |     ", end="")
        if (erros > 0):
            print("o", end="")
        print("")
        print(" |    ", end="")
        if (erros > 1): print("/", end="")
        if (erros > 2): print("|", end="")
        if (erros > 3): print("\\", end="")
        print("")
        print(" |    ", end="")
        if (erros > 4): print("/", end="")
        if (erros > 5): print(" \\", end="")
        print("")
        print(" |")
        print(" |")
        print(" |", end="")
        for c in range(0,len(palavra_final)):
            print(" " + palavra_final[c], end="")
        print()
        digit = input_teclado()
        dig = digit.upper()

        for c in letras_ja:
            if (dig == c):
                repetido = 1
                break
        if (repetido == 1):
            repetido = 0
            continue

        for c in range(0, len(palavra)):
            if (dig == palavra[c].upper()):
                f = list(palavra_final)
                f[c] = dig
                palavra_final = "".join(f)
                alguma_letra = 1
        if ((alguma_letra == 0) and (len(dig) == 1)):
            letras_ja.append(dig)
            erros += 1
        alguma_letra = 0
        repetido = 0
        digit = ""
        dig = ""


def como_jogar():
    os.system("cls") or None
    print("\n Será sorteado uma palavra, e você tera que adivinhar que palavra é.")
    print(" Ao todo, você pode errar até 5 vezes, mais que isso você perde :)")
    input("")

def menu():
    os.system("cls") or None
    print("\n Bem-vindo(a) ao JOGO DA FORCA!")
    print("\n 1 - Iniciar o jogo")
    print(" 2 - Como jogar?")
    print(" 3 - Sair")

def input_teclado():
    c = input("\n <<: ")
    return c

def forca_main():
    while (True):
        menu()
        digit = input_teclado()
        if (digit == "1"):
            jogo()
        elif (digit == "2"):
            como_jogar()
        elif (digit == "3"):
            exit()
        else:
            print("\n COMANDO INVÁLIDO...")
            input("")

if __name__ == "__main__":
    forca_main()
