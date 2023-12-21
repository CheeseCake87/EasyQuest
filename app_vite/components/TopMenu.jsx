import {mainContext} from "../context_provider/MainContext";
import {useContext} from "solid-js";
import {useNavigate} from "@solidjs/router";

export default function TopMenu() {

    const ctx = useContext(mainContext);
    const navigate = useNavigate();

    return (
        <nav class="top-nav">
            <div className={"top-nav-item"}>
                <img
                    src="../assets/easyquest-logo.gif"
                    alt="EasyQuest Logo"
                    width={180}
                    onClick={() => navigate("/", {replace: true})}
                />
            </div>
            <div className={"top-nav-item"}>
                <img
                    src="../assets/nav-dice.gif"
                    alt="EasyQuest Logo"
                    onClick={() => navigate("/", {replace: true})}
                />
                <img
                    src={
                        ctx.appCtx.menu_dd_button ?
                            "../assets/nav-icon-open-alt.gif" :
                            "../assets/nav-icon-closed.gif"
                    }
                    alt="nav-closed"
                    onClick={() => {
                        ctx.setAppCtx('menu_dd', !ctx.appCtx.menu_dd)
                        ctx.setAppCtx('menu_dd_button', true)
                    }}
                    onMouseOver={() => ctx.setAppCtx('menu_dd_button', true)}
                    onMouseOut={() => {
                        if (ctx.appCtx.menu_dd) {
                            ctx.setAppCtx('menu_dd_button', true)
                        } else {
                            ctx.setAppCtx('menu_dd_button', false)
                        }
                    }}
                />
            </div>
        </nav>
    );
}
