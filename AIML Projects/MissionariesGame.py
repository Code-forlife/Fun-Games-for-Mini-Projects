print('''

███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗███████╗███████╗     █████╗ ███╗   ██╗██████╗      ██████╗ █████╗ ███╗   ██╗███╗   ██╗██╗██████╗  █████╗ ██╗          ██████╗  █████╗ ███╗   ███╗███████╗
████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗██║██╔════╝██╔════╝    ██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██╔══██╗████╗  ██║████╗  ██║██║██╔══██╗██╔══██╗██║         ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║███████║██████╔╝██║█████╗  ███████╗    ███████║██╔██╗ ██║██║  ██║    ██║     ███████║██╔██╗ ██║██╔██╗ ██║██║██████╔╝███████║██║         ██║  ███╗███████║██╔████╔██║█████╗  
██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗██║██╔══╝  ╚════██║    ██╔══██║██║╚██╗██║██║  ██║    ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██║██╔══██╗██╔══██║██║         ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║██║███████╗███████║    ██║  ██║██║ ╚████║██████╔╝    ╚██████╗██║  ██║██║ ╚████║██║ ╚████║██║██████╔╝██║  ██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                                                                                                                                
                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
''')
print("Game mein aapaka svaagat hai")
print("niyam is prakaar hain")
print("1.naav adhikatam do logon ko le ja sakatee hai \n2.yadi narabhakshiyon kee sankhya mishanariyon se adhik hai to narabhakshee mishanariyon ko kha jaayenge\n3.bina kisee vyakti ke naav akele nadee paar nahin kar sakatee")

Lm = 3
Lc = 3
Rm = 0
Rc = 0
Um = 0
Uc = 0
k = 0  # attempts
try:
    while (True):
        while (True):
            print("baen se daayaan")
            Um = int(input("mishanariyon kee yaatra kee sankhya darj karen => "))
            Uc = int(input("narabhakshiyon kee yaatra kee sankhya darj karen => "))
            if Um == 0 and Uc == 0:
                print("Wrong")
            elif (Um + Uc <= 2) and (Lm - Um >= 0) and (Lc - Uc >= 0):
                break
            else:
                print("What is this sir you have to enter again: ")
        Lm -= Um
        Lc -= Uc
        Rm += Um
        Rc += Uc

        print("\n")
        for i in range(0, Lm):
            print("M ", end="")
        for i in range(0, Lc):
            print("C ", end="")
        print("| --> | ", end="")
        for i in range(0, Rm):
            print("M ", end="")
        for i in range(0, Rc):
            print("C ", end="")
        print("\n")

        k += 1

        if (((Lc == 3) and (Lm == 1)) or ((Lc == 3) and (Lm == 2)) or ((Lc == 2) and (Lm == 1)) or ((Rc == 3) and (Rm == 1)) or ((Rc == 3) and (Rm == 2)) or ((Rc == 2) and (Rm == 1))):
            print("What is this sir you lost!")
            break

        if (Rm == 3) and Rc == 3:
            print("vaah, aapane gem jeet liya")
            break

        while (True):
            print("daen se baen")
            Um = int(input("mishanariyon kee yaatra kee sankhya darj karen => "))
            Uc = int(input("narabhakshiyon kee yaatra kee sankhya darj karen => "))
            if Um == 0 and Uc == 0:
                print("What is this sir you have to enter again: ")
            elif (Um + Uc <= 2) and (Rm - Um >= 0) and (Rc - Uc >= 0):
                break
            else:
                print("What is this sir you have to enter again: ")
        Lm += Um
        Lc += Uc
        Rm -= Um
        Rc -= Uc
        k += 1
        print("\n")
        for i in range(0, Lm):
            print("M ", end="")
        for i in range(0, Lc):
            print("C ", end="")
        print("| <-- | ", end="")
        for i in range(0, Rm):
            print("M ", end="")
        for i in range(0, Rc):
            print("C ", end="")
        print("\n")

        if (((Lc == 3) and (Lm == 1)) or ((Lc == 3) and (Lm == 2)) or ((Lc == 2) and (Lm == 1)) or ((Rc == 3) and (Rm == 1)) or ((Rc == 3) and (Rm == 2)) or ((Rc == 2) and (Rm == 1))):
            print("What is this sir you lost!")
            break
except EOFError as e:
    print("\nInvalid input please retry !!")




