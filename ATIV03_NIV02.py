def calcular_media(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    print ("O aluno tirou", media)
    verificar_aprovacao(media)

def verificar_aprovacao(media):
    print ("Aluno aprovado :) ") if media >=7 else print ("aluno reprovado :( ")
calcular_media([10, 9, 8, 5])
