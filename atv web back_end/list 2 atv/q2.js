// Implemente uma classe chamada “Aluno” que possua atributos para armazenar o
// nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média
// das notas e verificar a situação do aluno (aprovado ou reprovado) de acordo com
// as regras de onde você estuda ou estudou.
class Aluno{
    constructor(nome,matricula,n1,n2){
        this.nome = nome;
        this.matricula = matricula;
        this.n1 = n1 //nota 1
        this.n2 = n2 // nota 2

    }

    mediaNota(){
        let soma = this.n1 + this.n2

        let media = soma / 2

        if(media>=7){
            return `Sua media é ${media}\nVocê estar aprovado!`
        }
        else{
            return `Sua media é ${media}\nVocê estar reprovado`
        }
        
    }

}


const a1 = new Aluno('Luis','mtds12',0,8);

console.log(a1);

console.log(a1.mediaNota());

