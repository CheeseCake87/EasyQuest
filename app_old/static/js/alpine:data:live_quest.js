document.addEventListener('alpine:init', () => {
    Alpine.data('live_quest', () => ({
        health: 0,
        attack: 0,
        defence: 0,
        weapon: '',
        sleeping: false,
        confused: false,
        poisoned: false,
        buffed: false,

        poll_stats(url) {
            fetch(url, {method: 'GET',})
                .catch(error => {
                    console.log(error);
                })
                .then(response => response.json())
                .then(jsond => {
                    this.health = jsond['health'];
                    this.attack = jsond['attack'];
                    this.defence = jsond['defence'];
                    this.weapon = jsond['weapon'];
                    this.sleeping = jsond['sleeping'];
                    this.confused = jsond['confused'];
                    this.poisoned = jsond['poisoned'];
                    this.buffed = jsond['buffed'];
                });
        },
    }))
})
