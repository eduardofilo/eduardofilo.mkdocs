#!/usr/bin/env python3
"""Pone nombre a los paquetes de los juegos de Quest ya extraídos con adb.

El nombre del juego no está en el AndroidManifest.xml como texto: el fichero es binario
(AXML) y el nombre suele ser una *referencia* (@string/app_name) que hay que resolver
contra resources.arsc. Por eso el editor hexadecimal no sirve. Lo hace androguard.

Genera, junto a la carpeta de juegos: icons/<package>.png, mapping.tsv e iconos.html.

Requiere androguard (una sola vez):
  python3 -m venv ~/.venvs/apkid && ~/.venvs/apkid/bin/pip install androguard

Uso:
  ~/.venvs/apkid/bin/python identify-quest-games.py ~/QuestGames
  ~/.venvs/apkid/bin/python identify-quest-games.py ~/QuestGames --rename
"""
import argparse
import html
import os
import re
import sys

try:                                    # androguard loguea por loguru; sin handlers, silencio
    from loguru import logger
    logger.remove()
except Exception:
    pass

from androguard.core.apk import APK


def find_base_apk(game_dir):
    """El APK del juego: base.apk si existe; si no, el primero que no sea un split."""
    lvl1 = [f for f in sorted(os.listdir(game_dir))
            if f.lower().endswith(".apk") and os.path.isfile(os.path.join(game_dir, f))]
    if not lvl1:                        # layouts anidados (backups de SideQuest, p. ej.)
        for root, _dirs, files in os.walk(game_dir):
            for f in sorted(files):
                if f.lower().endswith(".apk"):
                    lvl1.append(os.path.relpath(os.path.join(root, f), game_dir))
        lvl1.sort()
    if not lvl1:
        return None

    def rank(name):
        base = os.path.basename(name).lower()
        if base == "base.apk":
            return (0, name)
        if not base.startswith("split_config"):
            return (1, name)
        return (2, name)

    return os.path.join(game_dir, min(lvl1, key=rank))


def read_apk(path):
    """package, nombre, version, actividad principal, icono (bytes o None)."""
    a = APK(path)
    label = None
    try:
        label = a.get_app_name()
    except Exception:
        pass
    icon = None
    for dpi in (640, 480, 320, 160):    # el de más resolución que exista
        try:
            p = a.get_app_icon(max_dpi=dpi)
            if p:
                icon = a.get_file(p)
                if icon:
                    break
        except Exception:
            continue
    return {
        "package": a.get_package(),
        "label": (label or "").strip(),
        "version": a.get_androidversion_name() or "",
        "activity": a.get_main_activity() or "",
        "icon": icon,
    }


def safe_name(text):
    text = re.sub(r'[/\\:*?"<>|\x00-\x1f]', "-", text).strip().strip(".")
    return re.sub(r"\s+", " ", text)[:80]


def main():
    ap = argparse.ArgumentParser(description="Identifica los juegos de una carpeta de APK/OBB.")
    ap.add_argument("folder", nargs="?", default="QuestGames", help="carpeta de juegos (por defecto ./QuestGames)")
    ap.add_argument("--rename", action="store_true",
                    help='renombra cada carpeta a "Nombre [package]" (no hace nada si el destino existe)')
    args = ap.parse_args()

    root = os.path.abspath(os.path.expanduser(args.folder))
    if not os.path.isdir(root):
        sys.exit(f"no existe la carpeta: {root}")

    games = sorted(d for d in os.listdir(root)
                   if os.path.isdir(os.path.join(root, d))
                   and not d.startswith((".", "_")) and d != "icons")
    if not games:
        sys.exit(f"no hay subcarpetas de juegos en {root}")

    icons_dir = os.path.join(root, "icons")
    os.makedirs(icons_dir, exist_ok=True)

    rows, unknown = [], []
    for game in games:
        gdir = os.path.join(root, game)
        apk = find_base_apk(gdir)
        if not apk:
            print(f"[?] {game}: sin APK dentro")
            unknown.append((game, "", "sin APK"))
            continue
        try:
            info = read_apk(apk)
        except Exception as e:
            print(f"[?] {game}: no se pudo leer {os.path.basename(apk)} ({type(e).__name__})")
            unknown.append((game, "", f"APK ilegible ({type(e).__name__})"))
            continue

        name = info["label"] or info["package"]
        if info["icon"]:
            with open(os.path.join(icons_dir, f"{info['package']}.png"), "wb") as f:
                f.write(info["icon"])
        if not info["label"]:
            unknown.append((game, info["package"], "sin nombre en el manifiesto"))
        rows.append({**info, "game_dir": game, "apk": os.path.relpath(apk, root)})
        print(f"[ok] {info['package']:<42} {name}")

    # --- mapping.tsv ---
    tsv = os.path.join(root, "mapping.tsv")
    with open(tsv, "w", encoding="utf-8") as f:
        f.write("package\tnombre\tversion\tactividad\tcarpeta\tapk\n")
        for r in sorted(rows, key=lambda r: (r["label"] or r["package"]).lower()):
            f.write("\t".join([r["package"], r["label"], r["version"], r["activity"],
                               r["game_dir"], r["apk"]]) + "\n")

    # --- iconos.html: para identificar a ojo los que el nombre no aclare ---
    doc = os.path.join(root, "iconos.html")
    with open(doc, "w", encoding="utf-8") as f:
        f.write("<!doctype html><meta charset='utf-8'><title>Juegos por icono</title>\n"
                "<style>body{font:14px/1.4 system-ui,sans-serif;margin:24px}"
                "ul{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));"
                "gap:16px;list-style:none;padding:0}"
                "li{border:1px solid #ddd;border-radius:8px;padding:12px;text-align:center}"
                "img{width:96px;height:96px;object-fit:contain}"
                "code{display:block;font-size:11px;color:#666;word-break:break-all;margin-top:6px}"
                "</style>\n<ul>\n")
        for r in sorted(rows, key=lambda r: (r["label"] or r["package"]).lower()):
            icon = f"icons/{r['package']}.png" if r["icon"] else ""
            img = f"<img src='{html.escape(icon)}'>" if icon else "<div style='width:96px;height:96px'></div>"
            f.write(f"<li>{img}<b>{html.escape(r['label'] or '(sin nombre)')}</b>"
                    f"<code>{html.escape(r['package'])}</code>"
                    f"<code>{html.escape(r['game_dir'])}</code></li>\n")
        f.write("</ul>\n")

    # --- renombrado opcional de carpetas ---
    if args.rename:
        for r in rows:
            label = safe_name(r["label"])
            if not label:
                continue
            target = f"{label} [{r['package']}]"
            src, dst = os.path.join(root, r["game_dir"]), os.path.join(root, target)
            if os.path.abspath(src) == os.path.abspath(dst):
                continue
            if os.path.exists(dst):
                print(f"[rename] {r['game_dir']} -> ya existe {target}, se deja")
                continue
            os.rename(src, dst)
            print(f"[rename] {r['game_dir']} -> {target}")

    print(f"\n{len(rows)} juegos identificados, {len(unknown)} sin nombre claro.")
    for game, pkg, why in unknown:
        print(f"  - {game} ({pkg or 'sin package'}): {why}")
    print(f"\nmapping.tsv  -> {tsv}")
    print(f"iconos.html  -> {doc}   (ábrelo para poner cara a los paquetes dudosos)")


if __name__ == "__main__":
    main()
