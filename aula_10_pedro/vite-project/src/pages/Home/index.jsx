import { useEffect, useState } from "react"

function Home() {

    const [computadores, setComputadores] = useState([])

    useEffect(() => {
        async function fetchAPI() {
            const url = "https://api.mercadolibre.com/sites/MLB/search?q=computador";
            const requisicao = await fetch(url);
            const resposta = await requisicao.json();

            setComputadores(resposta.results)
        }

        fetchAPI()
    }, [])



    return (
        <>
            <h2>Home</h2>

            {computadores.map((element) => (
                <div>
                    <img src={element.thumbnail} alt="" />
                    <p>{element.title}</p>
                    <p>{element.price}</p>
                </div>
            ))}
        </>
    )
}

export default Home