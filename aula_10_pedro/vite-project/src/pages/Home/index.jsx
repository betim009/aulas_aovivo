import { useEffect, useState } from "react"
import Header from "../../components/header";

function Home() {
    const [computadores, setComputadores] = useState([])
    const [usuario, setUsuario] = useState("pedro@email.com")

    useEffect(() => {
        async function fetchAPI() {
            const url = "https://api.mercadolibre.com/sites/MLB/search?q=computador";
            const requisicao = await fetch(url);
            const resposta = await requisicao.json();

            setComputadores(resposta.results)
        }

        fetchAPI()
    }, [])

    function aoClicar(element) {
        alert(element.price)
    }

    return (
        <>
            <Header />
            <h2>{usuario}</h2>

            {computadores.map((element) => (
                <div>
                    <img src={element.thumbnail} alt="" />
                    <p>{element.title}</p>
                    <p>{element.price}</p>
                    <button onClick={() => aoClicar(element)}>Adicionar ao Carrinho</button>
                </div>
            ))}
        </>
    )
}

export default Home