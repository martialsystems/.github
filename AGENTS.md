# Agent notes: martialsystems/.github

This repo is the Indiana / White River **research index**, not the org root.

Canonical page: [RESEARCH.md](RESEARCH.md).
Gist copy: https://gist.github.com/martialsystems/66b896b0a4a0b8cba2b478aef64312f3

Home rule: `~/.grok/rules/weather-research.md`.

When a new weather git is created, the same finish that pushes it also:

1. Adds the tree to `RESEARCH.md` (ascii tree, mermaid, repo table)
2. Writes the same bytes to `README.md` and `profile/README.md` while they still duplicate `RESEARCH.md`
3. Pushes this repo
4. Copies `RESEARCH.md` onto gist `66b896b0a4a0b8cba2b478aef64312f3`
5. Updates the lane gist (Maps, White River Q, or Precip)

Do not leave a new git linked only at https://github.com/martialsystems.

Add the repo name to `tests/test_index.py` `TREES` in the same change.

```bash
python3 -m pytest tests -q
```
