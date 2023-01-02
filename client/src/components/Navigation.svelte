<script lang="ts">
    import { onMount } from "svelte";
    let lang:string = "vi";
    let ifPlaying:boolean = false; // use this variable to set play mode in rpi 
    let ifDark:boolean = false;
    onMount(() => {
        localStorage.setItem('lang', lang);
        document.documentElement.setAttribute('lang', 'vi');
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            localStorage.setItem('theme', 'dark');
            document.documentElement.setAttribute('theme', 'dark');
            ifDark = true;
        } else {
            localStorage.setItem('theme', 'light');
            document.documentElement.setAttribute('theme', 'light');
            ifDark = false;
        }
    })
    function languageCtl() {
        if (lang == "vi") {lang = "en";} else {lang = "vi";}
        document.documentElement.setAttribute('lang', lang);
        console.log(lang);
    }
    function guiControl() {
        ifDark = !ifDark;
        ifDark ? document.documentElement.setAttribute('theme', 'dark') : document.documentElement.setAttribute('theme', 'light');
    }
    function audioControl() {
        ifPlaying = !ifPlaying;
    }
</script>

<style lang="scss">
button {
    border: none;
    background-color: rgba(51, 51, 51, 0);
}
.navBar {
    width: 48px;
    // border-bottom: 1px solid;
    border-color: var(--cmp);
    color: var(--cmp);
    div {
        height: inherit;
    }
    .items {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        .end {
            margin-top: auto;
            display: flex;
            flex-direction: column;
        }
        button {
            height: 48px;
            width: 48px;
            float: left;
            padding: 0 0 0 0;
            transition: all 0.1s ease-out;
        }
        span {
            margin: auto 0 auto 0;
            padding: 12px 12px 12px 12px;
            color: var(--cmp);
        }
        button:hover {
            background-color: var(--cmp);
            span:hover {
                color: var(--bg);
            }
        }
    }
}
.material-symbols-rounded {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' -25,
  'opsz' 48
}

</style>

<div class="navBar">
    <div class="items">
        <a href="/"><button><span class="material-symbols-rounded">queue_music</span></button></a>
        <a href="/console"><button><span class="material-symbols-rounded">terminal</span></button></a>
        <div class="end">
            <button on:click={languageCtl}><span class="material-symbols-rounded">language</span></button>
        {#if !ifDark}    
            <button on:click={guiControl}><span class="material-symbols-rounded">dark_mode</span></button>
        {:else}
            <button on:click={guiControl}><span class="material-symbols-rounded">light_mode</span></button>
        {/if}
        <button><span class="material-symbols-rounded">settings</span></button>
        </div>
    </div>
</div>