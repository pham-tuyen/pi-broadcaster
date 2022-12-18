<script lang="ts">
    import Clock from './components/Clock.svelte';
    import Panel from './components/Panel.svelte';
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