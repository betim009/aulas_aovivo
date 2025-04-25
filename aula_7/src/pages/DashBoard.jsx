import { useContext } from "react"
import Context from "../context/Context";
import { Link } from "react-router";

export default function DashBoard() {
    const {user, setUser} = useContext(Context);


    return (
        <>
            <h2>Dash</h2>
            <p>Bem vindo, {user}</p>

            <Link to="/">Home</Link>

            <input type="text" onChange={(event) => setUser(event.target.value)}/>
        </>
    )
}