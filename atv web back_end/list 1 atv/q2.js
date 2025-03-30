// Faça um script que leia três números inteiros, em seguida mostre o maior e o
// menor deles.
let n1 = 30;
let n2 = 50;
let n3 = 10;

var maior

var menor

function verficar_maior_menor(){
    if(n1>n2 && n1 >n3){
        maior = n1;
    }
    else if(n2>n1 && n2>n3){
        maior = n2;
    }
    else{
        maior = n3;
    }

    if(n1<n2 && n1<n3){
        menor = n1 ;
    }
    else if(n2<n1 && n2 < n3 ){
        menor = n2 ;
    }
    else{
        menor = n3 ;
    }
    return `maior :  ${maior}  menor : ${menor}`

}

console.log(verficar_maior_menor())