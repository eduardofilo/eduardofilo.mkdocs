#!/usr/bin/env bash
# Extrae APK(s) + OBB de los juegos instalados en un Meta Quest y los deja con el
# layout que FramePort escanea:
#   <JUEGOS>/<package>/<base.apk y splits>        (uno o varios APK por juego)
#   <JUEGOS>/<package>/<package>/<*.obb>          (carpeta de datos = package name)
#
# Uso:  ./extract-quest-games.sh [DESTINO] [PREFIJO_PAQUETE]
#       ./extract-quest-games.sh ~/QuestGames com.
#
# ADB se puede sobreescribir (ADB=./mockadb) para probarlo sin visor.
set -euo pipefail

OUT="${1:-$PWD/QuestGames}"
FILTER="${2:-}"
ADB="${ADB:-adb}"

command -v "$ADB" >/dev/null || { echo "adb no está en el PATH" >&2; exit 1; }
[ "$("$ADB" get-state 2>/dev/null)" = device ] \
  || { echo "Quest no autorizado: ejecuta 'adb devices' y acepta en el visor" >&2; exit 1; }
mkdir -p "$OUT"

mapfile -t PKGS < <("$ADB" shell pm list packages -3 | tr -d '\r' | sed 's/^package://' | grep -v '^$' |
  { if [ -n "$FILTER" ]; then grep "^$FILTER" || true; else cat; fi; } | sort)
[ "${#PKGS[@]}" -gt 0 ] || { echo "sin apps que coincidan con '$FILTER'" >&2; exit 1; }

for pkg in "${PKGS[@]}"; do
  dest="$OUT/$pkg"; mkdir -p "$dest"; n=0
  while IFS= read -r apk; do                       # base.apk + split_config.*.apk -> dest/
    apk="${apk#package:}"; [ -n "$apk" ] || continue
    "$ADB" pull -a "$apk" "$dest/" >/dev/null 2>&1 && n=$((n + 1))
  done < <("$ADB" shell pm path "$pkg" | tr -d '\r')

  [ "$n" -gt 0 ] || { echo "[skip] $pkg (sin APK accesible)"; rmdir "$dest" 2>/dev/null || true; continue; }

  src="/sdcard/Android/obb/$pkg"
  if [ -n "$("$ADB" shell "ls -A $src 2>/dev/null" | tr -d '\r')" ]; then
    "$ADB" pull "$src" "$dest/" >/dev/null 2>&1      # crea dest/<package>/
    echo "[ok] $pkg — $n APK + OBB"
  else
    echo "[ok] $pkg — $n APK (sin OBB)"
  fi
done

echo
echo "Importa en FramePort:  Add games → Scan a folder… → $OUT"
