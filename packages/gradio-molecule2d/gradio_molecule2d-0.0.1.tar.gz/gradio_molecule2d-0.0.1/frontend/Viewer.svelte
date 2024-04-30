<!--file:Molecule.svlete-->
<!--Tested against v2.1.7 of smiles-drawer-->
<script>
  import { afterUpdate } from "svelte";
  import SmilesDrawer from "smiles-drawer";

  export let smiles = "";

  const SETTINGS = {
    width: 300,
    height: 200,
  };
  let drawer = new SmilesDrawer.SvgDrawer(SETTINGS);
  let svgElement;

  afterUpdate(() => {
    SmilesDrawer.parse(smiles, function (tree) {
      drawer.draw(tree, svgElement, "light");
    });
  });
</script>

{#if smiles.length > 0}
  <div>
    <svg bind:this={svgElement} data-smiles={smiles} />
  </div>
{:else}
  <div class="text-center my-10 py-10 text-gray-600">
    No molecule to display
  </div>
{/if}

<style>
  svg {
    width: 100%;
    height: 400px;
  }

  @import "tailwindcss";
</style>
