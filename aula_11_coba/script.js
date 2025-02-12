const eminemMusicas = document.getElementById('eminem-musicas')

let eminem = null;

async function fetchApi() {
    const url = "https://api.deezer.com/artist/13/top?limit=5";
    const req = await fetch(url);
    const res = await req.json();

    return res;
}

window.addEventListener('DOMContentLoaded', async () => {
    eminem = await fetchApi();

    console.log(eminem)

    eminem.data.map((element) => eminemMusicas.innerHTML += `
        <div class="card" style="width: 24rem;">
            <img class="card-img-top" src="${element.contributors[0].picture}" >
            <div class="card-body">
                <h2>${element.title}</h2>
                <p>${element.duration / 60}</p>

                <audio controls>
                    <source src="${element.preview}" type="audio/mpeg">    
                </audio>
            </div>
        </div>
    `)
});