const { data } = require("./data");

function getAll(){
    /*
        retornar todos, porem apenas nome e preço
    */

    const novoArray = 
        data.map((element) => ({
            nome: element.nome,
            preco: element.preco
        }))

    console.log(novoArray)
    return novoArray;
};

function getById(id){
    const findById = 
        data.find(e => e.id === id);

    console.log(findById);
    return findById;
};

getById("20")

function getByName(name){

};

