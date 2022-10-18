function area(metros) {
    area = metros * metros;
    return area;
}
var num = prompt("Digite um valor em metros: ");
document.write(" A area de" + num + "é" + area(num));

function minhaFuncao(objeto){
    objeto.carro = "Toyota";
}

var meucarro = {carro: "Honda", modelo: "civic", ano: 1997};
var x, y;

x = meucarro.carro;

minhaFuncao(meucarro);
y = meucarro.carro;
