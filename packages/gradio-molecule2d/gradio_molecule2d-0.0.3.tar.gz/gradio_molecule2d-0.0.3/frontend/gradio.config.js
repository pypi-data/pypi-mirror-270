import tailwindcss from "@tailwindcss/vite";
import { mdsvex } from "mdsvex";

export default {
    plugins: [tailwindcss()],
    svelte: {
        preprocess: [
            mdsvex()
        ]
    }
};