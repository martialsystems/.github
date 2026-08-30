# Copyright (c) 2026 Martial Systems LLC. MIT.
"""Fail closed if the research index drops a tree or drifts from its copies."""

from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

TREES = (
    "indiana_flood_completion",
    "white_river_stage_inundation",
    "white_river_fim_compare",
    "white_river_hwm_crest",
    "white_river_rain_stage",
    "white_river_nwm_error",
    "white_river_anderson_nora",
    "white_river_fall_creek_gap",
    "white_river_eagle_creek_gap",
    "white_river_eagle_persistence",
    "indiana_cocorahs_mrms",
    "indiana_radar_miss",
    "indiana_winter_lake_miss",
    "indiana_djf_snow_tercile",
)

GISTS = (
    "66b896b0a4a0b8cba2b478aef64312f3",
    "16584e78d079666f7e8994b4cc6158be",
    "1104e5e47b8a04006ec694d289d43639",
    "b5f900aad37487bb8c0206a321c1ed5c",
    "a1b032d2f353c56f3f91caeb09748978",
    "d68a0bd0c0b6cc12749db4c40330e538",
    "cd2eadaba9fc1c776ba4a8a22c45a516",
)

class IndexTest(unittest.TestCase):
    def _research(self) -> str:
        return (ROOT / "RESEARCH.md").read_text(encoding="utf-8")

    def test_copies_match_research(self) -> None:
        body = self._research()
        for name in ("README.md", "profile/README.md"):
            other = (ROOT / name).read_text(encoding="utf-8")
            self.assertEqual(other, body, msg=name + " drifted from RESEARCH.md")

    def test_trees_and_gists_listed(self) -> None:
        text = self._research()
        missing = [name for name in TREES if name not in text]
        self.assertEqual(missing, [])
        missing_gists = [g for g in GISTS if g not in text]
        self.assertEqual(missing_gists, [])
        self.assertIn("These trees are research.", text)
        self.assertIn("This page is the index.", text)
        self.assertIn("gist.github.com/martialsystems/" + GISTS[0], text)

    def test_prose_defaults(self) -> None:
        for name in ("RESEARCH.md", "README.md", "profile/README.md", "AGENTS.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotIn("\u2014", text, msg=name)
            self.assertNotIn("What it is not", text, msg=name)


if __name__ == "__main__":
    unittest.main()
