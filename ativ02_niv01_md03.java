import { exit } from "process";
const readlinkSync = require('readline-sync');  //Biblioteca para dados de entrada

abstract class Veiculo {
    constructor(modelo, marca, cor, numeroRodas) {
        this.modelo = modelo;
        this.marca = marca;
        this.cor = cor;
        this.numeroRodas = numeroRodas;
    }
    clone() {}
    represent() {}
}
class Combustao extends Veiculo {
    type: string
    cambio: string
    constructor(modelo, marca, cor, numeroRodas, tipo, cambio) {
        super(modelo, marca, cor, numeroRodas)
        this.tipo = tipo;
        this.cambio = cambio;
    }
}
class Eletrico extends Veiculo {
    constructor(modelo, marca, cor, numeroRodas, tipo, autonomia) {
        super(modelo, marca, cor, numeroRodas)
        this.tipo = tipo;
        this.autonomia = autonomia;
    }
}

class Montadora extends Veiculo {
    especificaCarro() {
        let i: number = 0
        for (i = 1; i <= 6; i++) {
            let tipoVeiculo = readlinkSync.question('Escolha um tipo de carro para cadastrar? [1] A combustão / [2] Elétrico / [0] Sair\n')
            if (tipoVeiculo == '1') {
                console.log(`Iniciando montagem do Carro ${i} - a combustão`)
                let modeloVeiculo: string = readlinkSync.question('Informe o modelo: \n')
                let marcaVeiculo: string = readlinkSync.question('Informe o fabricante: \n')
                let corVeiculo: string = readlinkSync.question('Qual a cor? \n')
                let cambioCombustao = readlinkSync.question('Câmbio: Manual, ou Automático \n')
                let novoCarro = new Combustao(modeloVeiculo, marcaVeiculo, corVeiculo, '4', 'a combustão', cambioCombustao)
                console.log(`Montagem do carro ${i} / ${6 - i} efetuada com sucesso\n\n`)
                estoque.push(novoCarro)

            } else if (tipoVeiculo == '2') {
                console.log(`Montando o Carro ${i} - elétrico`)
                let modeloVeiculo: string = readlinkSync.question('Informe o modelo: \n')
                let marcaVeiculo: string = readlinkSync.question('Informe o fabricante: \n')
                let corVeiculo: string = readlinkSync.question('Qual a cor? \n')
                let autonomiaEletrico = readlinkSync.question('Qual a autonomia da bateria: \n')
                let novoCarro = new Pickup(modeloVeiculo, marcaVeiculo, corVeiculo, '4', 'Elétrico', autonomiaEletrico)
                console.log(`Montagem do carro ${i} / ${6 - i} efetuada com sucesso\n\n`)
                estoque.push(novoCarro)

            } else if (tipoVeiculo === '0') {
                console.log('Você escolheu sair...fechando...');
                process.exit()

            } else {
                console.log('Erro - opção inexistente - fechando...');
                process.exit()
            }
        }
        return estoque
    }

    clone() {
        let publicEstoque: object[] = Object.assign({}, estoque)
        return publicEstoque
    }
    represent() {
        console.log(`O estoque possui ${estoque.length} carros`)
        return console.log(this.clone())
    }

}

//CLIENT
const estoque: object[] = []
console.log(`Montadora de Carros\n`)
Montadora.prototype.especificaCarro()
Montadora.prototype.clone()
Montadora.prototype.represent()
