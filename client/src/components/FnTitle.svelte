<svelte:head>
	<script src="http://localhost:5173/eel.js" on:load={eelLoaded}></script>
</svelte:head>

<script lang="ts">
    export var name:string;

    const eelLoaded = () => {
        console.log("eel loaded");
        const eel = window.eel
        eel.set_host( 'ws://localhost:8080' )
        
        eel.expose(say_hello_js);
        eel.say_hello_py("Javascript World!");

    }
    function say_hello_js(x: string) {
        console.log("Hello from " + x);
    }
            
    say_hello_js("Javascript World!");
</script>

<style lang="scss">
    .wrapper {
        padding: 4px 4px 4px 4px;
        background-color: black;
        color: white;
        p {
            margin: 0 0 0 0;
        }
    }
</style>

<div class="wrapper">
    <p>{name}</p>
</div>