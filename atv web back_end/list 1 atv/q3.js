// Crie um programa que peça ao usuário um número inteiro positivo n e exiba a
// tabuada desse número de 1 a 10 utilizando um loop for.

let num = 10;


function tabuada(){
    let resultado = []
    for (let i=0;i<11;i++){
        resp = num * i
        resultado.push(num + 'x' + i +'=' + resp); //push metodo add último elemento da lista
    }

    return resultado;
    
}

console.log(tabuada().join('\n')); //join fazer formatação de Arry

