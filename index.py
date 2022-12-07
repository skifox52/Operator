# Opérateur
def operateur():
    try:
        a = int(input("Donner le premier nombre\n"))
        b = int(input("Donner le premier nombre\n"))
        choix = input('a => +\nb => -\nc => *\nd => /\n')
        if(choix == "a"):
            print("The result of addition is ",a+b)
        elif(choix == "b"):
            print("The result of soustraction is ",a-b)
        elif(choix == "c"):
            print("The result of multiplication is ",a*b)
        elif(choix == "d"):
            if(b == 0):
                 return print('Cannot devide by 0')
            print("The result of division is ",a/b)
        else:
            print("Choix invalide")
    except ValueError:
        print('Veullez saisir un chiffre')