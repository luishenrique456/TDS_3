// Implemente uma classe chamada “ContaBancaria” que possua atributos para
// armazenar o número da conta, nome do titular e saldo. Adicione métodos para
// realizar depósitos e saques que recebem como parâmetro o valor.
class ContaBancaria{
    constructor(numeroCont,nomeTitular,saldoAtual){
        this.numeroCont = numeroCont
        this.nomeTitular = nomeTitular
        this.saldoAtual = saldoAtual

    }

    deposito(valoDeposito){
        //verificar não tem número negativos
        if(valoDeposito > 0){
            let saldoDeposito = this.saldoAtual + valoDeposito
            return `Valor seu Deposito é : ${saldoDeposito}`
        }
        else{
            return `Valor deposito invalidor ${valoDeposito}`
        }
        
    }


    saque(valorSaque){




    }


}


const c1 = new ContaBancaria(123,'Carlos',500)

console.log(c1);

console.log(c1.deposito(200));

console.log(c1.saldoAtual);



