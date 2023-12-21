const {createThemes} = require("tw-colors");

module.exports = {
    content: [
        "./app_vite/**/*.{js,jsx,ts,tsx}",
    ],
    plugins: [
        createThemes({
            dark_theme: {
                'body': {
                    'background-color': 'black',
                },
                'primary': 'orange',
                'secondary': 'yellow',
            },
            light_theme: {
                'body': {
                    'background-color': 'black',
                },
                'primary': 'pink',
                'secondary': 'red',
            },
        })
    ],
}
