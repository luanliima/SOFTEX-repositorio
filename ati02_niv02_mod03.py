import { Galinha } from "./Galinha";

import AdaptadorPatoDemo;



export class AdaptadorPato implements Galinha{
    pato = AdaptadorPato
    constructor (pato: AdaptadorPatoDemo){
    this.pato = pato;
    }
    fazerCocorico(): any {
        let fazerCocorico: string = `Cocoricó`;
        return `O pato faz ${this.pato.fazerQuaQua()} e ${fazerCocorico}`;
    }
    voar(): string {
        return 'Voou';
    }    
}
