<script lang="ts">
    import FnTitle from "../components/FnTitle.svelte";
    import Form from "../components/Form.svelte";
    let n = 1;
</script>   

<style lang="scss">
.fnRow {
    margin: 8px 0 8px 0;
}
.programTable {
    border-style: solid;
    border-width: 2px;
    .funcTitle {
        display: flex;
        flex-direction: row;
        h3 {
            text-align: center; 
            width: 50%;
            margin: 4px auto 4px auto;
        }
    }
    form {
        display: flex;
        flex-direction: column;
        align-content: space-around;
        justify-content: space-around;
        button {
            margin: 4px 4px 4px 4px;
        }
        input {
            width: 50%;
            margin: 4px 4px 4px 4px;
        }
    }
}
</style>

<div class="wrapper">
    <FnTitle name="Điều khiển phát sóng"/>
    <div class="fnRow">
        <button on:click={() => {n = n + 1}}>Thêm</button>
        <button>Chạy</button>
    </div>
    <div class="programTable">
        <div class="funcTitle">
            <h3>Chương trình</h3>
            <h3>Thời gian phát sóng</h3>
        </div>
        <form action="">
            {#each Array(n) as _, i} 
            <div style="display: flex; flex-direction: row"> 
                <Form />
            </div>
            {/each}
        </form>
    </div>
</div>