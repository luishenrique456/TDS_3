function testeEscopo(){
    var a = 10 ;
    let b = 20 ;
    const c = 30 ;

    if(true){
        var a = 40 ;
        let b = 50 ;
        const c = 60 ;
        console.log(a,b,c) ;
    }

    console.log(a,b,c) ;
}

testeEscopo()