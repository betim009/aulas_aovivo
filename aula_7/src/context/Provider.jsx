import Context from './Context';
import { useState } from "react";

function Provider({ children }) {
    const [valorGlobal, setValorGlobal] = useState("tipo de dado que você quiser");


    const contextValue = {
        valorGlobal,
    };

    return (
        <Context.Provider value={contextValue}>
            {children}
        </Context.Provider>
    )
}


export default Provider;