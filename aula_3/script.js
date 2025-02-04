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
    console.log(results);

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
    const filterByCity = results.filter((element) => element.address.city === userCity);

    console.log(filterByName.length);

    if (filterByName.length === 0 && userCity === "") {
        return divContainer.innerHTML = `
            <p>Não foi possível encontrar um usuário com esse nome.</p>
        `;
    };

    if (filterByCity.length === 0  && userName === "") {
        return divContainer.innerHTML = `
            <p>Não foi possível encontrar uma cidade com esse nome.</p>
        `;
    };

    if (filterByName.length === 0 && filterByCity.length === 0) {
        return divContainer.innerHTML = `
            <p>Não foi possível encontrar uma cidade ou usuário.</p>
        `;
    };


    divContainer.innerHTML = "";
    filterByName.map((element) =>
        divContainer.innerHTML += `
            <h4>Nome: ${element.name}</h4>
            <p>Email: ${element.email}</p>
            <p>Cidade: ${element.address.city}</p>
        `
    );

    filterByCity.map((element) =>
        divContainer.innerHTML += `
            <h4>Nome: ${element.name}</h4>
            <p>Email: ${element.email}</p>
            <p>Cidade: ${element.address.city}</p>
        `
    );
});