const btn = document.getElementById('btn');




window.addEventListener('DOMContentLoaded', () => {

});

btn.addEventListener('click', () => {
    const txt = document.getElementById('text');
    
    if (txt.textContent === "Hi") {
        txt.textContent = "Bye"
    } else {
        txt.textContent = "Hi"
    }
})