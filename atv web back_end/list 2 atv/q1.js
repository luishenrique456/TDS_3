// Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio
// e métodos para calcular a área e o perímetro do círculo.
class Circulo{
    constructor(raio){
        this.raio = raio
    }

    calArea(){
        return `Área é ${3.14 * this.raio ** 2}`
    }

    calPerimetro(){
        return `Perímetro é ${ 2 * 3.14 * this.raio}`
    }

}

const c1 = new Circulo(2)

console.log(c1); //mostra objeto

console.log(c1.calArea()); //mostra método calArea() area = 3.14 * raio ** 2

console.log(c1.calPerimetro()); //mostra método CalPerimetro perimetro = 2 * 3.14 * raio

