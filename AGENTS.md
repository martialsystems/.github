# Agent notes: martialsystems/.github

The readable index is the live console: https://martialsystems.github.io/indiana_wx_pages/

Gist `66b896b0` is a pointer to that page so old README footers still land. [RESEARCH.md](RESEARCH.md) is the same pointer. Do not keep a full copy of the index in this git.

Home rule: `~/.grok/rules/weather-research.md`.

When a new weather git is created, the same finish that pushes it also:

1. Adds a `pins.d/<id>.toml` row to `indiana_research_console`, ingest, rebuild pages, and push the Pages snapshot (`indiana_wx_pages`)
2. Keeps `RESEARCH.md`, `README.md`, and `profile/README.md` as the same stub (pointer to Pages). Leave gist `66b896b0` as a pointer
3. Updates the lane gist (Maps, White River Q, Precip, or Temp). Precip is one gist with sections, not a gist per sequel
4. New README footer: a solid-green shields badge (`Open_the_research_console-2e7d32`, no `labelColor` split) whose href is https://martialsystems.github.io/indiana_wx_pages/. Do not paste a visible index URL.

Do not leave a new git linked only at https://github.com/martialsystems.

```bash
python3 -m pytest tests -q
```
