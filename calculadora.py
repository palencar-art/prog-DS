a = int(input("digite um numero: "))
b = int(input("digite outro numero: "))

controle = True

while controle == True:
    print ("digite uma opçao: 0 - sair \n 1 - soma: \n 2 - subtraçao: \n 3 - multiplicaçao: \n 4 - divisao: ")
    opcao = input ("")
    if opcao == ("0"):
        controle = False
    if opcao == ("1"):
        print ("resultado: ", a + b)
    if opcao == ("2"):
        print ("resultado", a - b)
    if opcao == ("3"):
        print ("resultado", a * b)
    if opcao == ("4"):
        if b != 0:
            print ("resultado", a / b)
        else:
            print ("nao da pra dividir por 0 :") 
    else: 
        print ("opçao invalida -_-") 