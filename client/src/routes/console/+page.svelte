<script lang="ts">
    import { info } from '../../stores.js';
    import { onMount } from 'svelte';
    let user = window.navigator;
    let date = new Date();
</script>
<style lang="scss">
    .terminalWrapper {
        margin: 12px;
    }
</style>
<div class="terminalWrapper">
    <div class="info">
        DashPi version {info.version} ({info.codename})<br>
        Author: {info.author} <br>
        Running on {user.platform} at {date} <br> <br> 
        $ froze <br>
        The terminal is frozen. This might happen because the terminal component of this program is currently in development.
    </div>
    <div class="renderer"></div>
</div>