#!/usr/bin/env bash
# Build the browsable API docs (pdoc) into docs/.
#
# docs/ is gitignored: this runs in CI on tag pushes and publishes to GitHub Pages,
# not something to commit locally.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

uv run pdoc -o docs qtsurfer.api.client
