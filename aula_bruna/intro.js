/*

    A estrutura de dados que eu vou trabalhar:
    - Existe mais de um dado? 
        sim? array.
            caso sim
            - Esse dados possuem mais de 1 caracteristica? 
                sim? array de objetos
                não? array de strings, booleans, numbers 


        não? não é array. 

    - Ele possui mais de 1 caracteristica? 
        sim? objeto
        não? string, boolean, number







    Vou falar sobre a CIDADE RIO DE JANEIRO.
    - habitantes da cidade, e sobre os - bairros. 
    vai ter infomação sobre o nome de cada bairro e total de habitantes.


    const RJ = {
        habitantes_cidade: 4500,
        bairros: [
            { 
                nome: "Copa Cabana", 
                habitantes: 200, 
                praias: [
                    {
                        "quiosk": [
                            {
                                funcionarios: [
                                    {
                                        
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            { nome: "Leblon", habitantes: 120 }
        ]
    }


*/

const arr1 = ["the strokes", "rage against machine", "rchp"]
const arr2 = [2000, 1994, 1990]

const arr3 = [
    { nome: "the strokes", totalMusicas: 45 },
    { nome: "rhcp", totalMusicas: 100 }
];

const theStrokes = {
    vocalista: "Casa Blanca",
    totalMusicas: 45,
    musicas: ["repetila", "you live once", "the adults are talking", "why sundays..."],
    ativa: true,
    grammy: false
}

const bruna = {
    nomeCompleto: "Bruna Nerd",
    idade: 25,
    pet: ["gato1", "...", "..."]
}
