import random
import os

def dibujo(i):
    print("******HANGMAN GAME******\n\n")
    if i==0:
        
        print("""
         VAMOS BIEN, NO DEJES QUE ME AHORQUEN, GANA
            +---+
                !
                !
                !
                !
                !
                !
        ---------
        ---------""")
    elif i==1:
        print(""" 
        OH! OH! CUIDADO
            +---+
           /    !
                !
                !
                !
                !
                !
        ---------
        ---------
        
        """)
    elif i==2:
        print(""" 
        CONCENTRATE!!
            +---+
           /    !
          O     !
                !
                !
                !
                !                
        ---------
        ---------
        
        """)
    elif i==3:
        print("""
        NO TE EQUIVOQUES MAS POR FAVOR
            +---+
           /    !
          O     !
          |     !
                !
                !
                !
        ---------
        ---------
        
        """)
    elif i==4:
        print("""
        TENGO MIEDO
            +---+
           /    !
          O     !
         /|\    !
                !
                !
                !
        ---------
        ---------
        
        """)
    elif i==5:
        print("""
        NO ME QUIERO IR
            +---+
           /    !
          O     !
         /|\    !
         /      !
                !
                !
        ---------
        ---------
        
        """)
    elif i==6:
        print("""
        HASTA LA VISTA BABY
            +---+
           /    !
          o     !
         /|\    !
         / \    !
                !
                !
        ---------
        ---------
        
        """)
    elif i==7:
        print("""
        ESTOY VIVO

            \O/
             |
            / \ 
                
        """)
    elif i==8:
        print("""
        ADIOS
            +---+
           /    !
          o     !
         /|\    !
         / \    !
                !
                !
        ---------
        ---------
        
        """)


def ahorcado(word):
    quant = len(word)
    error = 0
    lines = '-' * quant
    letra = "a"
    right = 0
    #print(' '.join(lines))
    l = list(lines)

   
    while error != 6 and letra != "exit" and letra != word and right != quant:

        try:
            dibujo(error)
            print(' '.join(l).upper())
            letra = input("Adivina una Letra: ")
            if not(len(letra)==1 and letra.isalpha()):
                raise ValueError("Debese ingresar solo una letra")        
            if letra in word:
                for i in range(0,quant):
                    if word[i] == letra:
                        l[i] = letra
                        right += 1
            else:
                error += 1            
        except ValueError as ve:
            print(ve)
        
        os.system("cls")


    return error

def getWord(words):
    word = words[random.randint(0,len(words)-1)]
    return word


def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line.replace("\n","") for line in f ]  
    return words


def run():
    words = read()
    word = getWord(words)
    print("*****BIENVENIDO A HANGMAN GAME******\n\n")
   
    error = ahorcado(word)
    if error != 6:
        dibujo(7)
    else:
        dibujo(8)



if __name__ == ('__main__'):
    run()