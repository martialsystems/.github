# Copyright (c) 2026 Martial Systems LLC. MIT.
"""Fail closed if FLY.md becomes a second full fly index."""

from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

FLY_INDEX_GIST = "12835f747d6360781f3cc7f91f243178"
FLY_GIST_URL = "https://gist.github.com/martialsystems/12835f747d6360781f3cc7f91f243178"
TREES = ("fly_pong", "fly_chess", "fly_climax", "fly_vial", "vial_sanguis", "vial_sanguis2", "gf_cheat", "fly_icarus", "fly_p1_sign")


class FlyIndexTest(unittest.TestCase):
    def _fly(self) -> str:
        return (ROOT / "FLY.md").read_text(encoding="utf-8")

    def test_stub_points_at_fly_gist(self) -> None:
        text = self._fly()
        self.assertIn("readable index is the gist", text)
        self.assertIn(FLY_GIST_URL, text)
        self.assertIn(FLY_INDEX_GIST, text)
        self.assertNotIn("66b896b0", text)
        self.assertNotIn("weather", text.lower())
        self.assertNotIn("different gist", text.lower())
        self.assertIn("pointer", text.lower())
        self.assertNotIn("```mermaid", text)
        self.assertNotIn("img.shields.io", text)
        for name in TREES:
            self.assertIn(name, text)

    def test_research_stub_omits_fly_trees(self) -> None:
        research = (ROOT / "RESEARCH.md").read_text(encoding="utf-8")
        self.assertEqual(research, (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertEqual(research, (ROOT / "profile/README.md").read_text(encoding="utf-8"))
        self.assertNotIn("fly_pong", research)
        self.assertNotIn("fly_climax", research)
        self.assertNotIn(FLY_INDEX_GIST, research)

    def test_prose_defaults(self) -> None:
        for name in ("FLY.md", "AGENTS.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotIn("\u2014", text, msg=name)
            self.assertNotIn("What it is not", text, msg=name)

    def test_agents_names_fly_gist(self) -> None:
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(FLY_INDEX_GIST, text)
        self.assertIn("FLY.md", text)
        self.assertIn("fly-research.md", text)
        self.assertIn("vial_sanguis", text)
        self.assertIn("vial_sanguis2", text)
        self.assertIn("fly_vial", text)
        self.assertNotIn("use a separate gist", text)
        self.assertNotIn("Do not add fly trees to gist", text)


if __name__ == "__main__":
    unittest.main()
