<script lang="ts">
    import Navigation from '../components/Navigation.svelte';
</script>

<style lang="scss">
.allWrapper {
    display: flex;
    flex-direction: row;
}
</style>

<div class="allWrapper">
    <Navigation />

    <slot />
</div>