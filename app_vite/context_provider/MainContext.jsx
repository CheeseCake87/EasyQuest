import {createContext, createEffect, onMount} from "solid-js";
import {Outlet} from "@solidjs/router";
import {createStore} from "solid-js/store";
import TopMenu from "../components/TopMenu";


export const URL = 'http://127.0.0.1:5000';
export const API_URL = URL + "/api";

export const mainContext = createContext();

const [appCtx, setAppCtx] = createStore({

    socket_client: null,
    theme: 'dark',

    menu_dd_button: false,
    menu_dd: false,

});

export function MainContextProvider(props) {

    let html

    onMount(() => {
        html = document.querySelector('html')
    })

    createEffect(() => {
        html.setAttribute('data-theme', appCtx.theme)
    })

    // appCtx.socket_client = io(URL, {
    //     reconnection: true,
    //     reconnectionAttempts: Infinity,
    //     reconnectionDelay: 1000,
    //     reconnectionDelayMax: 5000,
    //     randomizationFactor: 0.5,
    //     transports: ['websocket']
    // });

    return (
        <mainContext.Provider value={{appCtx, setAppCtx}}>
            <TopMenu/>
            <Outlet/>
        </mainContext.Provider>
    );
}
