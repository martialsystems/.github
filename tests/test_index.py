# Copyright (c) 2026 Martial Systems LLC. MIT.
"""Fail closed if the git file becomes a second full index."""

from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

PAGES_INDEX = "martialsystems.github.io/indiana_wx_pages"
PAGES_URL = "https://martialsystems.github.io/indiana_wx_pages/"
CONSOLE_BADGE = (
    "[![Open the research console]"
    "(https://img.shields.io/badge/Open_the_research_console-2e7d32"
    "?style=for-the-badge)]"
    f"({PAGES_URL})"
)
INDEX_GIST = "66b896b0"
LANE_GISTS = (
    "16584e78d079666f7e8994b4cc6158be",
    "1104e5e47b8a04006ec694d289d43639",
    "b5f900aad37487bb8c0206a321c1ed5c",
    "e5de316dbb5f672573906572730e3735",
)


class IndexTest(unittest.TestCase):
    def _research(self) -> str:
        return (ROOT / "RESEARCH.md").read_text(encoding="utf-8")

    def test_copies_match_research(self) -> None:
        body = self._research()
        for name in ("README.md", "profile/README.md"):
            other = (ROOT / name).read_text(encoding="utf-8")
            self.assertEqual(other, body, msg=name + " drifted from RESEARCH.md")

    def test_stub_points_at_live_console(self) -> None:
        text = self._research()
        self.assertIn(PAGES_INDEX, text)
        self.assertIn(PAGES_URL, text)
        self.assertIn("Open the research console", text)
        self.assertIn("img.shields.io", text)
        self.assertIn(CONSOLE_BADGE, text)
        self.assertIn("2e7d32", text)
        self.assertNotIn("labelColor", text)
        self.assertNotIn("6e1f1c", text)
        self.assertNotIn("e6d5b8", text)
        self.assertIn("pointer", text.lower())
        self.assertIn(INDEX_GIST, text)
        self.assertNotIn("```mermaid", text)
        self.assertNotIn("indiana_djf_snow_tercile", text)
        for g in LANE_GISTS:
            self.assertIn(g, text)
        for i, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            self.assertFalse(
                stripped.startswith("https://gist.github.com"),
                msg=f"line {i} is a bare gist URL",
            )
            self.assertFalse(
                stripped.startswith("- https://"),
                msg=f"line {i} is a pasted URL bullet",
            )

    def test_pages_url_is_not_an_autolink_line(self) -> None:
        """Href inside the badge is allowed. A line that is only the URL is not."""
        text = self._research()
        bare = PAGES_URL.rstrip("/")
        forbidden = {
            PAGES_URL,
            bare,
            f"<{PAGES_URL}>",
            f"<{bare}>",
        }
        for i, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            self.assertNotIn(
                stripped,
                forbidden,
                msg=f"line {i} is a Pages autolink",
            )

    def test_prose_defaults(self) -> None:
        for name in ("RESEARCH.md", "README.md", "profile/README.md", "AGENTS.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotIn("\u2014", text, msg=name)
            self.assertNotIn("What it is not", text, msg=name)


if __name__ == "__main__":
    unittest.main()
