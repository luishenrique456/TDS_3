// Dado o array numeros, crie um novo array chamado numerosUnicos, contendo
// os mesmos elementos do array original, mas sem valores repetidos e exibir no
// console.
// const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

const numeros = [3, 7, 3, 2, 7, 10, 2, 15, 10, 20];

const novo_numeros = [];

for(let i=0;i< numeros.length;i++){
    if(verficarRepertido(numeros[i])){
        console.log("número " + numeros[i] + " repertido")
    }
    else{
        novo_numeros.push(numeros[i]);
    }
}

function verficarRepertido(numero){
    for(let i = 0 ; i< novo_numeros.length;i++){
        if(numero === novo_numeros[i]){
            return true
        }
    }
    return false
}

console.log(novo_numeros)