/*
    2 tipos de seletores
    - getElementByID
    - querySelectorAll
*/

const btns = document.querySelectorAll('.btn'); // VAI resgatar todos pela class btn
const btnEnviar = document.getElementById('enviar'); // Só do id enviar

const display = document.getElementById('display')

btnEnviar.addEventListener('click', () => {
    display.innerHTML = `
        <h2> Coba </h2>
    `
});

btns.forEach(e => {
    e.addEventListener('click', () => {
        alert();
    })
})