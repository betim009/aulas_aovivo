import { useContext } from "react"
import Context from "../context/Context";

export default function Home() {
    const {valorGlobal, setValorGlobal} = useContext(Context);

    return (
        <>
            <h2>Home</h2>
            <p>Valor do estado: {valorGlobal}</p>
        </>
    )
}