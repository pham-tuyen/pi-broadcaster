<svelte:head>
	<script src="http://localhost:8000/eel.js" on:load={eelLoad}></script>
</svelte:head>

<script lang="ts">
    import { fade } from 'svelte/transition';
    const eelLoad = () => {
        const eel = window.eel
    }
    
</script>

<style lang="scss">
.en {
    display: var(--en);
}
.vi {
    display: var(--vi);
}
button {
    border: none;
    background-color: rgba(51, 51, 51, 0);
    color: var(--cmp);
    height: 48px; width: 48px;
}
button:hover {
    transition: all 0.1s ease-out;
    background-color: var(--cmp);
    color: var(--bg);
}
.bar {
    display: flex;
    height: 48px;
    width: calc(100vw - 48px);
    .searchInput {
        padding: 0;
        height: 48px;
        line-height: 48px;
        font-size: 16px;
        background-color: inherit;
        border: none;
        font-family: "Roboto Mono", monospace;
        width: 100%;
        margin-inline-start: 12px;
        color: var(--cmp);
    }
    .searchInput:focus {
        outline: none;
    }
    .searchInput:focus::placeholder {
        color: #888888;
    }
    .searchInput::-webkit-search-cancel-button {
        display: none;
    }
}
</style>

<div class="queueControl">
    <div class="searchBarWrapper" >
        <form action="" class="bar"> <!--process search-->
                <input type="url" placeholder="Input YouTube video / playlist link..." class="searchInput en" name="s" autocomplete="off">  
                <input type="url" placeholder="Nhập liên kết video hoặc danh sách phát Youtube..." class="searchInput vi" name="s" autocomplete="off">
            <button type="submit"><span class="material-symbols-rounded">add</span></button>
        </form>
    </div>
</div>
