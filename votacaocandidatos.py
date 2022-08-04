from argparse import _VersionAction
from ast import While
import enum
from operator import truediv

class Candidato(enum.Enum):
    candidato_x = 889
    candidato_y = 847
    candidato_z = 515
    branco = 0

votar = True
votosx = 0
votosy = 0
votosz = 0
votosBrancos = 0
votosNulos = 0

while votar:
    votoInvalido = True
    voto = -1
    while votoInvalido:
        try:
            voto = int(input("Informe seu voto: "))
            votoInvalido = False
        except:
            print("Informe um valor valido. vote novamente.") 

    if Candidato.candidato_x.value == voto:
        votosx += 1
    elif  Candidato.candidato_y.value == voto:
        votosy += 1
    elif  Candidato.candidato_z.value == voto:
        votosz += 1
    elif  Candidato.branco.value == voto:
        votosBrancos += 1  
    else:
        votosNulos += 1

    opcao = int(input("Deseja continuar votando? (1-SIM, 2-NÃO): "))
    if opcao == 1:
        votar = True
    else:
        votar = False

print("Votos para o(a) candidato(a) {}: {}".format(Candidato.
candidato_x.name, votosx))
print("Votos para o(a) candidato(a) {}: {}".format(Candidato.
candidato_y.name, votosy))         
print("Votos para o(a) candidato(a) {}: {}".format(Candidato.
candidato_z.name, votosz)) 
print("Votos nulos: {}".format(votosNulos))
print("Votos Brancos: {}".format(votosBrancos)) 

if (votosx > votosy) and (votosy >= votosz):
    print ("O vencedor foi o candidato X.")
if (votosy > votosx) and (votosx >= votosz):
    print ("O vencedor foi o candidato Y.")
if (votosz > votosy) and (votosy >= votosx):
    print ("O vencedor foi o candidato Z.")
if (votosx == votosy) and (votosy == votosz):
    print ("A votação foi empate.") 
