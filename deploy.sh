#!/usr/bin/env bash
#
# Despliega apuntes.eduardofilo.es con mkdocs a GitHub Pages.
# Funciona igual en el ThinkPad (usuario edu) y en el VPS (usuario ubuntu):
# todas las rutas se resuelven con $HOME, no con un home hardcodeado.
#
# Requisitos (una sola vez por máquina):
#   1) Repo fuente  clonado en  ~/git/eduardofilo.mkdocs
#   2) Repo destino clonado en  ~/git/eduardofilo.github.io
#      git clone git@github.com:eduardofilo/eduardofilo.github.io.git ~/git/eduardofilo.github.io
#   3) Virtualenv con mkdocs y dependencias en  ~/.virtualenvs/mkdocs
#      python3 -m venv ~/.virtualenvs/mkdocs
#      ~/.virtualenvs/mkdocs/bin/pip install -r ~/git/eduardofilo.mkdocs/requirements.txt
#   4) Clave SSH autorizada en GitHub como eduardofilo (para el push).

set -euo pipefail

# --- Rutas (portables) ---
SRC_DIR="$HOME/git/eduardofilo.mkdocs"
DST_DIR="$HOME/git/eduardofilo.github.io"
VENV="$HOME/.virtualenvs/mkdocs/bin/activate"

# --- Comprobaciones previas ---
if [ ! -f "$VENV" ]; then
    echo "✗ No encuentro el virtualenv: $VENV" >&2
    echo "  Créalo con:  python3 -m venv \"$HOME/.virtualenvs/mkdocs\"" >&2
    echo "  e instala:   \"$HOME/.virtualenvs/mkdocs/bin/pip\" install -r \"$SRC_DIR/requirements.txt\"" >&2
    exit 1
fi

if [ ! -d "$DST_DIR/.git" ]; then
    echo "✗ No encuentro el repo destino: $DST_DIR" >&2
    echo "  Clónalo con:  git clone git@github.com:eduardofilo/eduardofilo.github.io.git \"$DST_DIR\"" >&2
    exit 1
fi

# --- Activar virtualenv ---
source "$VENV"

# --- Dejar el repo destino limpio y actualizado ---
cd "$DST_DIR"
git pull origin
git reset HEAD .
git checkout -- .

# --- Construir y publicar ---
# gh-deploy se ejecuta desde el repo destino (ahí es donde hace el push);
# el sitio se construye a partir del repo fuente, indicado por --config-file.
mkdocs gh-deploy \
    --config-file "$SRC_DIR/mkdocs.yml" \
    --remote-branch master

cd "$SRC_DIR"
echo "✓ Despliegue completado."
