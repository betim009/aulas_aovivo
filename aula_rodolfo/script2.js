// NOVO TESTAMENTO DO JAVASCRIPT


/*
ES6 - ECMA SCRIPT

arrow function
() => {

}

*/


const vendas = [
    {
        id: 1,
        data: "22/04",
        valor: 350,
        id_compra: 2,
        id_venda: 3
    },
    {
        id: 2,
        data: "22/04",
        valor: 150,
        id_compra: 53,
        id_venda: 12
    },
    {
        id: 3,
        data: "22/04",
        valor: 3320,
        id_compra: 12,
        id_venda: 21
    },
];

// Vai passar por cada elemento do array
// vendas.forEach(e => console.log(e))

// Estrutura completa 
vendas.forEach((e, i) => {
    e.id === 3 ? console.log(e) : null
})

// Estrutura simplificada
vendas.forEach(e => e.id === 3 ? console.log(e) : null)


/*

Explicação do TERNARIO

CONDIÇÃO ? RETORNO VERDADEIRO : RETORNO FALSO

4 > 2  ----> condição
console.log("MAIOR") ----> RETORNO VERDADEIRO
console.log("MENOR") ----> RETORNO FALSO


4 > 2 ? console.log("maior") : console.log("menor")
*/

4 > 20 ? console.log("maior") : console.log("menor")