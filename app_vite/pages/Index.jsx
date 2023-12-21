import {useContext} from "solid-js";
import {mainContext} from "../context_provider/MainContext";


export default function Index() {

    const ctx = useContext(mainContext);

    return (
        <>
            <div class={"large-test-div"}></div>
        </>
    );
};
