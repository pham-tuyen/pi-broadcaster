<script lang="ts">
	import Queue from "../components/Queue.svelte";
	import Status from "../components/Status.svelte";
</script>

<style lang="scss">
.layout {
	display: flex;
	flex-direction: column;
}
.placeholder {
	height: calc(100vh - 96px);
}
</style>

<div class="layout">
<Queue />

<span class="placeholder"></span>

<Status />
</div>
