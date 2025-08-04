# Build CSS with Tailwind
build-css:
    uv run tailwindcss -i {{INPUT_CSS_PATH}}/input.css -o {{OUTPUT_CSS_PATH}}/output.css

# Watch CSS changes
watch-css:
    uv run tailwindcss -i {{INPUT_CSS_PATH}}/input.css -o {{OUTPUT_CSS_PATH}}/output.css --watch

# Build CSS for production
build-css-prod:
    uv run tailwindcss -i {{INPUT_CSS_PATH}}/input.css -o {{OUTPUT_CSS_PATH}}/output-min.css --minify