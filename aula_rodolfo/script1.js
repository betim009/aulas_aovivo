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


/* ESTRUTURA DE REPETIÇÕES
    É percorrer um array, ir do primeiro ao ultimo.

    Array possui ELEMENT, INDEX    
*/

// Estrutura de repetição que só possui element
for (const element of vendas) {
    // console.log(element)
}



// Como acessar um array?
vendas[0]


// Estrutura de repetiçãpo de INDEX - Traz posições
for (const index in vendas) {
    // console.log(vendas[index]) // POREM consigo resgatar o element
}


// E se tiver que usar o FOR of e ter posição? 

// contador !!!

let contador = 0;
for (const element of vendas) {
    // console.log(contador)
    contador+=1
}


// NESSE CASO entra o MOTHER FUCKER for


for (let index = 0; index < 3; index+=2) {
    const element = vendas[index]; 
    console.log(element)
}


/* 
Resumo:
for of -> percore sempre do primeiro ao ultimo, e só tem element
for in -> percore sempre do primeiro ao ultimo, e só tem index
for -> percore a lista, voce decide o inicio, o fim, e de quanto em quanto.

observação: 
com for of você é capaz de criar um contador
com for in você é capaz de usar o array[index]

porém só cria logo a porra do for se precisar dos 2






Você tem uma base de dados pequena, e você não se importa com index: for of
Você tem base de dados pequena, você se importa com index: for in

Qualquer outra situação: for

SEMPRE em dúvida de qual usar: for

*/