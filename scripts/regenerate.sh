#!/usr/bin/env bash
# Regenerate the QTSurfer Python API client from the upstream OpenAPI spec.
#
# - Fetches the canonical openapi.yaml from QTSurfer/qtsurfer-api.
# - Wipes and regenerates src/qtsurfer/api/client/_generated/.
# - Pins pyproject.toml's `version` to the spec's `info.version`.
# - Re-runs ruff fix + format on generated sources.
#
# Idempotent: running twice on the same upstream spec yields a clean git tree.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

SPEC_URL="${SPEC_URL:-https://raw.githubusercontent.com/QTSurfer/qtsurfer-api/main/openapi.yaml}"
GEN_OUT="${TMPDIR:-/tmp}/qtsurfer-client-gen"
TARGET_DIR="src/qtsurfer/api/client/_generated"
GENERATED_PKG="qtsurfer_api_client"

echo "==> Fetching spec from $SPEC_URL"
curl -fsSL "$SPEC_URL" -o openapi.yaml

echo "==> Wiping previous _generated/"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"

echo "==> Running openapi-python-client"
rm -rf "$GEN_OUT"
uv run openapi-python-client generate \
    --path openapi.yaml \
    --config codegen.config.yaml \
    --output-path "$GEN_OUT" \
    --overwrite

# Generator lays out:
#   $GEN_OUT/$GENERATED_PKG/...   (source tree)
#   $GEN_OUT/pyproject.toml       (generator's own scaffolding, discarded)
#   $GEN_OUT/README.md            (generator's own scaffolding, discarded)
if [[ ! -d "$GEN_OUT/$GENERATED_PKG" ]]; then
    echo "ERROR: expected $GEN_OUT/$GENERATED_PKG to exist after generation." >&2
    echo "Contents of $GEN_OUT:" >&2
    ls -la "$GEN_OUT" >&2 || true
    exit 1
fi

echo "==> Moving $GENERATED_PKG/* -> $TARGET_DIR/"
mv "$GEN_OUT/$GENERATED_PKG"/* "$TARGET_DIR/"

echo "==> Syncing pyproject.toml version to openapi.yaml info.version"
VERSION=$(uv run python -c "import yaml; print(yaml.safe_load(open('openapi.yaml'))['info']['version'])")
echo "    version = $VERSION"
# Update only the first `version = "..."` line in [project] table.
uv run python - <<PY
import re
from pathlib import Path
p = Path("pyproject.toml")
text = p.read_text()
new = re.sub(r'^version = "[^"]+"', f'version = "$VERSION"', text, count=1, flags=re.MULTILINE)
p.write_text(new)
PY

echo "==> Formatting generated sources"
uv run ruff check --fix --exit-zero src/qtsurfer/api/client/_generated/ >/dev/null
uv run ruff format src/qtsurfer/api/client/_generated/ >/dev/null

# Drop scratch dir.
rm -rf "$GEN_OUT"

echo "==> Done. Run \`uv run pytest\` to verify."
