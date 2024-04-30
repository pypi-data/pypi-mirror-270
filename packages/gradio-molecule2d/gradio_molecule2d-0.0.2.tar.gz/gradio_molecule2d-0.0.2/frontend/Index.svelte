<svelte:options accessors={true} />

<script lang="ts">
  import type { Gradio } from "@gradio/utils";
  import { BlockTitle } from "@gradio/atoms";
  import { Block } from "@gradio/atoms";
  import { StatusTracker } from "@gradio/statustracker";
  import type { LoadingStatus } from "@gradio/statustracker";

  import { tick } from "svelte";
  import Viewer from "./Viewer.svelte";
  import Editor from "./Editor.svelte";

  import { BaseButton } from "@gradio/button";

  import { Sketch } from "@gradio/icons";

  import "./style.css";

  export let gradio: Gradio<{
    change: never;
    submit: never;
    input: never;
    clear_status: LoadingStatus;
  }>;
  export let label = "Textbox";
  export let elem_id = "";
  export let elem_classes: string[] = [];
  export let visible = true;
  export let value = "";
  export let placeholder = "";
  export let show_label: boolean;
  export let scale: number | null = null;
  export let min_width: number | undefined = undefined;
  export let loading_status: LoadingStatus | undefined = undefined;
  export let value_is_output = false;
  export let interactive: boolean;
  export let rtl = false;

  let el: HTMLTextAreaElement | HTMLInputElement;
  const container = true;

  function handle_change(): void {
    gradio.dispatch("change");
    if (!value_is_output) {
      gradio.dispatch("input");
    }
  }

  async function handle_keypress(e: KeyboardEvent): Promise<void> {
    await tick();
    if (e.key === "Enter") {
      e.preventDefault();
      gradio.dispatch("submit");
    }
  }

  $: if (value === null) value = "";

  // When the value changes, dispatch the change event via handle_change()
  // See the docs for an explanation: https://svelte.dev/docs/svelte-components#script-3-$-marks-a-statement-as-reactive
  $: value, handle_change();

  let showeditor = false;

  function handleMolecule(event) {
    value = event.detail.smiles;
    showeditor = false;
  }

  function showEditor() {
    showeditor = true;
  }
</script>

<Block
  {visible}
  {elem_id}
  {elem_classes}
  {scale}
  {min_width}
  allow_overflow={false}
  padding={true}
>
  <div style="min-height: 70vh;">
    {#if loading_status}
      <StatusTracker
        autoscroll={gradio.autoscroll}
        i18n={gradio.i18n}
        {...loading_status}
        on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
      />
    {/if}

    <label class:container>
      <BlockTitle {show_label} info={undefined}>{label}</BlockTitle>

      <input
        data-testid="textbox"
        type="text"
        class="scroll-hide"
        bind:value
        bind:this={el}
        {placeholder}
        disabled={!interactive}
        dir={rtl ? "rtl" : "ltr"}
        on:keypress={handle_keypress}
      />
    </label>

    <Viewer smiles={value} />

    {#if interactive}
      <div class="w-full flex justify-center">
        <button on:click={showEditor} class="flex items-center">
          <div class="w-4 h-4 mr-2"><Sketch /></div>
          <span>Draw molecule</span>
        </button>
      </div>
    {/if}

    {#if showeditor}
      <div class="absolute top-0 left-0 w-full z-10" style="height: 100%">
        <Editor on:moleculesketched={handleMolecule} />
      </div>
    {/if}
  </div>
</Block>

<style>
  label {
    display: block;
    width: 100%;
  }

  input {
    display: block;
    position: relative;
    outline: none !important;
    box-shadow: var(--input-shadow);
    background: var(--input-background-fill);
    padding: var(--input-padding);
    width: 100%;
    color: var(--body-text-color);
    font-weight: var(--input-text-weight);
    font-size: var(--input-text-size);
    line-height: var(--line-sm);
    border: none;
  }
  .container > input {
    border: var(--input-border-width) solid var(--input-border-color);
    border-radius: var(--input-radius);
  }
  input:disabled {
    -webkit-text-fill-color: var(--body-text-color);
    -webkit-opacity: 1;
    opacity: 1;
  }

  input:focus {
    box-shadow: var(--input-shadow-focus);
    border-color: var(--input-border-color-focus);
  }

  input::placeholder {
    color: var(--input-placeholder-color);
  }
  button {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    transition: var(--button-transition);
    box-shadow: var(--button-shadow);
    padding: 10px 15px;
    text-align: center;
    border-radius: 10px;
    border: #eee solid 1px;
  }

  button:hover,
  button[disabled],
  a:hover,
  a.disabled {
    box-shadow: var(--button-shadow-hover);
  }

  button:active,
  a:active {
    box-shadow: var(--button-shadow-active);
  }

  button[disabled],
  a.disabled {
    opacity: 0.5;
    filter: grayscale(30%);
    cursor: not-allowed;
  }

  .hidden {
    display: none;
  }

  .primary {
    border: var(--button-border-width) solid var(--button-primary-border-color);
    background: var(--button-primary-background-fill);
    color: var(--button-primary-text-color);
  }
  .primary:hover,
  .primary[disabled] {
    border-color: var(--button-primary-border-color-hover);
    background: var(--button-primary-background-fill-hover);
    color: var(--button-primary-text-color-hover);
  }

  .secondary {
    border: var(--button-border-width) solid
      var(--button-secondary-border-color);
    background: var(--button-secondary-background-fill);
    color: var(--button-secondary-text-color);
  }

  .secondary:hover,
  .secondary[disabled] {
    border-color: var(--button-secondary-border-color-hover);
    background: var(--button-secondary-background-fill-hover);
    color: var(--button-secondary-text-color-hover);
  }

  .stop {
    border: var(--button-border-width) solid var(--button-cancel-border-color);
    background: var(--button-cancel-background-fill);
    color: var(--button-cancel-text-color);
  }

  .stop:hover,
  .stop[disabled] {
    border-color: var(--button-cancel-border-color-hover);
    background: var(--button-cancel-background-fill-hover);
    color: var(--button-cancel-text-color-hover);
  }

  .sm {
    border-radius: var(--button-small-radius);
    padding: var(--button-small-padding);
    font-weight: var(--button-small-text-weight);
    font-size: var(--button-small-text-size);
  }

  .lg {
    border-radius: var(--button-large-radius);
    padding: var(--button-large-padding);
    font-weight: var(--button-large-text-weight);
    font-size: var(--button-large-text-size);
  }

  .button-icon {
    width: var(--text-xl);
    height: var(--text-xl);
    margin-right: var(--spacing-xl);
  }
</style>
