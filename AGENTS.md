# Agent notes: martialsystems/.github

The readable index is the gist: https://gist.github.com/martialsystems/66b896b0a4a0b8cba2b478aef64312f3

[RESEARCH.md](RESEARCH.md), README.md, and profile/README.md are the same stub. Do not keep a full copy of the index in this git.

Home rule: `~/.grok/rules/weather-research.md`.

When a new weather git is created, the same finish that pushes it also:

1. Adds the tree to gist `66b896b0` (ascii tree, mermaid, repo table)
2. Keeps `RESEARCH.md`, `README.md`, and `profile/README.md` as the same stub
3. Updates the lane gist (Maps, White River Q, Precip, Temp, or Re-TRAC). Precip is one gist with sections, not a gist per sequel. Re-TRAC stays off Site / `indiana_wx_pages`.
4. New README footer, exact URL:

```text
Research index: https://gist.github.com/martialsystems/66b896b0a4a0b8cba2b478aef64312f3
```

Do not ship a shields.io badge as the README footer.

Do not leave a new git linked only at https://github.com/martialsystems.

```bash
python3 -m pytest tests -q
```
