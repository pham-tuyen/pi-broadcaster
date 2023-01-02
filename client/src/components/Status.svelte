<script lang="ts">
    import { onMount } from "svelte";
    let time:any;
    function updateTime() {
        time = new Date();
        setTimeout(updateTime, 1000);
    }
    onMount(updateTime);
</script>

<style lang="scss">
.wrapper {
    display: flex;
    flex-direction: row;
    height: 48px;
}
.status {
    display: flex;
    align-items: center;
    line-height: 48px;
    margin: 0 12px 0 auto;
}
.clock {
    display: flex;
    align-items: center;
    margin: 0 12px 0 0;
}
</style>

<div class="wrapper">
    <div class="status">
        <span class="material-symbols-rounded">signal_cellular_off</span>
    </div>
    <div class="clock"><span class="time">{time}</span></div>
</div>
