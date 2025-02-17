### UseEffect
    Função do react que é necessário para trabalhar com API.

    1:
    useEffect(() => {}, [])

    2:
    useEffect(() => {
        
    }, [])

    3: 
    useEffect(() => {
        async function fetchAPI() {}

        fetchAPI()
    }, [])

    4:
    useEffect(() => {
        async function fetchAPI() {
            const url = ""
            const req = await fetch(url)
            const res = await req.json()

            ...
        }   

        fetchAPI()
    }, [])


    Final:
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

    1:
    nomeDoEstado.map((element) => (

    ))

    2:
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



### OnClick
    Para criar uma funcionalidade para um botão
    
    1.
    function nomeDaFuncao() {

        alert()
    }

    return 

    <button onClick={nomeDaFuncao}>Nome do botão</button>


    2.

    function nomeDaFuncao(element) {

        alert(element.name)
    }

    return 

    <button onClick={() => aoClicar(element)}>Nome do botão</button>
    