def calcular(op1, op2, operacao):
    if operacao <= 4 and operacao >= 1:
        if operacao == 1:
            return op1 + op2
        elif operacao == 2:
            return op1 - op2
        elif operacao == 3:
            return op1 * op2
        elif operacao == 4:
            return op1 / op2
        else: 
            return "resultado = 0"
op1 = input("informe o primeiro operador: ")
op2 = input("informe o segundo operador: ")
operacao = int(input("informe a operacao: "))

resultado = calcular(op1, op2, operacao)
print(resultado)
