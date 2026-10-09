import os
from pathlib import Path
import subprocess
import tempfile
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ManifestContractTests(unittest.TestCase):
    def test_delegated_sidebar_action_contract(self):
        manifest = tomllib.loads((ROOT / "herdr-plugin.toml").read_text())

        self.assertEqual(manifest["id"], "dev.ariel.herdr-sidebar-menu")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(
            manifest["actions"],
            [
                {
                    "id": "sidebar",
                    "title": "Toggle file sidebar",
                    "contexts": ["pane", "workspace"],
                    "command": [
                        "sh",
                        "-c",
                        'exec "${HERDR_BIN_PATH:-herdr}" plugin action invoke '
                        "herdr-sidebar.open-sidebar",
                    ],
                }
            ],
        )

    def test_action_uses_configured_herdr_binary(self):
        command = tomllib.loads((ROOT / "herdr-plugin.toml").read_text())["actions"][0]["command"]
        with tempfile.TemporaryDirectory(prefix="sidebar action ") as temporary:
            executable = Path(temporary) / "custom herdr"
            capture = Path(temporary) / "arguments"
            executable.write_text('#!/bin/sh\nprintf "%s\\n" "$@" > "$CAPTURE"\n')
            executable.chmod(0o755)
            result = subprocess.run(
                command,
                cwd=ROOT,
                env={**os.environ, "HERDR_BIN_PATH": str(executable), "CAPTURE": str(capture)},
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                capture.read_text().splitlines(),
                ["plugin", "action", "invoke", "herdr-sidebar.open-sidebar"],
            )


if __name__ == "__main__":
    unittest.main()
