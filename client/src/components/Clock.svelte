<script lang="ts">
    import { onMount } from 'svelte';
    let currentTime:any;
    onMount(function clock() {
        currentTime = new Date();
        setInterval(function() { clock(); }, 1000);
    }) 
</script>

<style lang="scss">
    #clock {
        font-size: small;
    }
</style>

<div class="clockWrapper">
    <span id="clock">{currentTime}</span>
</div>