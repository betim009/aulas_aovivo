### UseEffect
    Função do react que é necessário para trabalhar com API.

    useEffect(() => {
        
    }, [])



    useEffect(() => {
        async function fetchAPI() {
            const url = "";
            const requisicao = await fetch(url);
            const resposta = await requisicao.json();

            setNome(resposta.results)
        }

        fetchAPI()
    }, [])



### UseState
    Função do react que vai salvar uma informação(dados) para ser criado na tela.

    1 passo:
    const [] = useState()
    
    2 passo:
    const [nome, setNome] = useState()


    3 passo:
    const [nome, setNome] = useState([]) # INICIA COM UM ARRAY



### MAP
    é uma função que CRIA elementos de uma lista(array).

    nomeDoEstado.map((element) => (

    ))


    {computadores.map((element) => (
            <div>
                <img src={element.thumbnail} alt="" />
                <p>{element.title}</p>
            </div>
    ))}