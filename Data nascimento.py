from datetime import datetime

while True:
    try:
        nomecompleto = str(input("Nome completo: "))
        anonascimento = int(input("ano de nascimento: "))
        if 1922 <= anonascimento <= 2021:
            break
        else:
            print("Idade invalida! Tente novamente.")
    except ValueError:
        print("Idade invalida! Digite o ano no formato: 0000")
print(f"Nome completo: {nomecompleto}: {datetime.today().year - anonascimento} anos")
