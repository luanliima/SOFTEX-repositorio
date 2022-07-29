from distutils.util import execute


def calcular(op1, op2, operacao):
    if operacao == 1:
        return op1 + op2
    if operacao == 2:
        return op1 - op2
    if operacao == 3:
        return op1 * op2
    if operacao == 4:
        return op1 / op2

execute = True
while execute:
    print("Opções Válidas")
    print("1: soma") 
    print("2: subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    oper = int(input("Informe a operação: "))
    if oper >= 1 and oper <= 4:
        op1 = int(input("Informe o primeiro operador: "))
        op2 = int(input("Informe o segundo operador: "))

        resultado = calcular(op1, op2, oper)
        print(resultado)
    elif oper == 0:
        print("Obrigado até a próxima.")
        execute = False
    else:
        print("Esta opção não é valida. Informe outro valor. ")  
