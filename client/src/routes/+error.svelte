<script lang="ts">
    import { page } from '$app/stores';
    let eCode = $page.status;
    let eMsg = $page.error!.message;
</script>

<style lang="scss">

</style>

<div class="wrapper">
    <pre>{eCode}: {eMsg}</pre>
</div>