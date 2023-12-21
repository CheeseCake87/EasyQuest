import {useContext} from "solid-js";
import {mainContext} from "../context_provider/MainContext";


export default function Index() {

    const ctx = useContext(mainContext);

    return (
        <>
            <p>Test - {ctx.appCtx.theme}</p>
        </>
    );
};
