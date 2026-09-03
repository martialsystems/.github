# Copyright (c) 2026 Martial Systems LLC. MIT.
"""Fail closed if the git file becomes a second full index."""

from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

PAGES_URL = "https://martialsystems.github.io/indiana_wx_pages/"
INDEX_GIST = "66b896b0"
GIST_URL = "https://gist.github.com/martialsystems/66b896b0a4a0b8cba2b478aef64312f3"
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

    def test_stub_points_at_gist(self) -> None:
        text = self._research()
        self.assertIn("readable index is the gist", text)
        self.assertIn(GIST_URL, text)
        self.assertIn(INDEX_GIST, text)
        self.assertNotIn("Open the research console", text)
        self.assertNotIn("img.shields.io", text)
        self.assertNotIn("```mermaid", text)
        self.assertNotIn("indiana_djf_snow_tercile", text)
        for g in LANE_GISTS:
            self.assertIn(g, text)
        self.assertIn("pointer", text.lower())

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

    def test_public_files_omit_research_console(self) -> None:
        for name in ("RESEARCH.md", "README.md", "profile/README.md", "AGENTS.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotIn("indiana_research_console", text, msg=name)
            self.assertNotIn("Open_the_research_console", text, msg=name)


if __name__ == "__main__":
    unittest.main()
