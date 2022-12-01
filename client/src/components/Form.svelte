<script lang="ts">
    export let ifLocal:boolean = false;
    export let ifExist:boolean = true;
</script>   

<style lang="scss">
    button {
        margin: 4px 4px 4px 4px;
    }
    input {
        width: 50%;
        margin: 4px 4px 4px 4px;
    }
</style>
{#if ifExist}
{#if !ifLocal}
<button on:click={async() => {ifLocal = !ifLocal;}}>Sử dụng file cục bộ</button>
<input type="url" placeholder="Nhập liên kết YouTube">
<input type="time" placeholder="Nhập giờ">   
<button on:click={async() => {ifExist = !ifExist;}}>Xoá</button>
{:else}
<button on:click={async() => {ifLocal = !ifLocal;}}>Sử dụng nội dung Internet</button>
<input type="file" placeholder="Tải lên file cục bộ" accept=".mp3" id="file">
<input type="time" placeholder="Nhập giờ"> 
<button on:click={async() => {ifExist = !ifExist;}}>Xoá</button> 
{/if}
{:else}
{/if}