a = int(input ("digite um número"))
b = int(input ("digite outro número"))
banana = True
while banana == True:
    print ("digite uma opção: \n 1-Soma \n 2-Divisão \n 3-Subtração \n 0-Sair")
    op = input ()
    if op == "0":
        banana = False
    if op == "1":
        print (resultado)
        resultado =  a + b
    if op == "2":
        resultado = a / b
        print (resultado)
    if op == "3":
        resultado = a - b 
        print (resultado)
    