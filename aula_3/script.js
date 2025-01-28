// Imports

// Seletores
const inputName = document.getElementById('input-name');
const inputCity = document.getElementById('input-city');
const btnSearch = document.getElementById('btn-search');
const divContainer = document.getElementById('container');

// Variaveis
let results = [];

// Funções
const fetchApi = async () => {
    const url = "https://jsonplaceholder.typicode.com/users";
    const req = await fetch(url);
    const res = await req.json();

    return res
};

// Eventos
window.addEventListener('load', async () => {
    results = await fetchApi();

    results.map((element) =>
        divContainer.innerHTML += `
            <h4>Nome: ${element.name}</h4>
            <p>Email: ${element.email}</p>
            <p>Cidade: ${element.address.city}</p>
        `
    );
});

btnSearch.addEventListener('click', () => {
    const userName = inputName.value;
    const userCity = inputCity.value;

    const filterByName = results.filter((element) => element.name === userName);

    divContainer.innerHTML = "";
    filterByName.map((element) =>
        divContainer.innerHTML += `
            <h4>Nome: ${element.name}</h4>
            <p>Email: ${element.email}</p>
            <p>Cidade: ${element.address.city}</p>
        `
    );
});