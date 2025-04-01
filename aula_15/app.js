import { movies } from "./data.js";

const div = document.getElementById('filmes');

for (const element of movies) {
    div.innerHTML += `
        <p>${element.title}</p>
        <img src="${element.poster}"/>
    `
}