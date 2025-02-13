### UseEffect
    Função do react que é necessário para trabalhar com API.

    useEffect(() => {
        
    }, [])



    useEffect(() => {
        // Criou o código
        async function fetchAPI() {
            const url = "";

            // Você está pedindo/solicitando os dados
            const requisicao = await fetch(url);

            // é o RETORNO/RESULTADO dos dados
            const resposta = await requisicao.json();

            // SALVANDO OS DADOS
            setNome(resposta.results)
        }

        // executou o código
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



### Função de component

    function Home() {
    return (
        <>

        
        </>
    )

    }
    export default home



    export default function Home() {
    return (
        <>

        
        </>
    )

    }