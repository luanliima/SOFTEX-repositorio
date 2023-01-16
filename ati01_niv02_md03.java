interface Sanduiche{
    getInfo()
    getValor()
}

class SandFrangoassado implements Sanduiche{
    private info = 'Sanduíche de Frango Assado'
 valor privado = 4,50 
    
    getInfo() {
 this.info de retorno
    }
    
    getValor() {
 retornar this.valor
    }
}

class AdicionalDecorator implements Sanduiche{
 construtor(protected lanche: Sanduiche){}
        
    getInfo() {
 retornar this.lanche.getInfo()
    }
    getValor() {
 retornar this.lanche.getValor()
    }
}    


class Pepperoni extends AdicionalDecorator{
    
    getInfo(){
        return this.lanche.getInfo() + ', Pepperoni'
    }

    getValor():number{
 retornar this.lanche.getValor() + 0.99
    }
}

class MussarelaRalada extends AdicionalDecorator{
    
    getInfo() {
        return this.lanche.getInfo() + ', Queijo mussarela ralado'
    }

 getValor(): número {
 retornar this.lanche.getValor() + 2,00
    }
}

const pedido1 = novo SandFrangoassado()
const pedido2 = new Pepperoni(pedido1)
const pedido3 = new MussarelaRalada(pedido2)
 console.log('Total do pedido: ${pedido3.getInfo()}, Custa: $${pedido3.getValor()}');
