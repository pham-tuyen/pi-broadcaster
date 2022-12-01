<svelte:head>
	<script src="http://localhost:5173/eel.js" on:load={eelLoaded}></script>
</svelte:head>

<script lang="ts">
    import Clock from '../components/Clock.svelte';
    import Panel from '../components/Panel.svelte';

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
.titleWrapper {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin: 8px 0 8px 0;
    .titleText {
        margin: 0 0 0 auto;
    }
    .titleLogo {
        aspect-ratio: 4 / 3;
        height: 64px;
    }
}
.timeWidget {
    color: white;
    background-color: black;
    padding: 2px 2px 2px 2px;
}
</style>

<div class="mainWrapper">
    <div class="timeWidget">
        <Clock />
    </div>
    <div class="titleWrapper">
        <img src="/pi.png" alt="logo" class="titleLogo">
        <h1 class="titleText">Bảng điều khiển</h1>
    </div>
    <div class="panelWrapper">
        <Panel />
    </div>
</div>