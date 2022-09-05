def calcular(op1, op2, operacao):
    if operacao == "+":
        return op1 + op2
    elif operacao == "-":
        return op1 - op2
    elif operacao == "*":
        return op1 * op2
    elif operacao == '/':
        return(op1 // op2, op1 % op2)
    else: 
        return "Operação invalida"
op1 = input("informe o primeiro operador: ")
op2 = input("informe o segundo operador: ")
operacao = input("informe a operacao: ")
v1 = int(op1)
v2 = int(op2)
resultado = calcular(v1, v2, operacao)
print(resultado)
