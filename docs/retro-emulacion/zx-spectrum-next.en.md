---
layout: default
permalink: /en/retro-emulacion/zx-spectrum-next.html
---

# ZX Spectrum Next / N-GO

## Links

* [ZX Spectrum Next](https://www.specnext.com/)
* [N-GO basic](https://manuferhi.com/c/n-go)

## Cheatsheet

#### Keyboard shortcuts

|Shortcut|Used for|Notes|
|:------------|:-------|:------|
|F1 / Reset (long press)|Hard Reset|Resets CPU and Peripherals, reloads the FW and loads the hardware settings anew but doesn't clear the RAM|
|F2|Scandoubler|Doubles the output resolution. Must be off for older monitors and SCART cables|
|F3|50Hz/60Hz Vertical Frequency|Changes the display's vertical frequency from 50 to 60Hz and vice-versa|
|F4 / Reset (short press)|Soft Reset|Resets CPU and Peripherals and reloads the Operating System. Used with Caps Shift it forces a rescan of drives and a reload of the boot screen under esxDOS|
|F5|Not Used| |
|F6|Not Used| |
|F7|Scanlines|Cyclically toggles scan line emulation in 4 steps/intensities: 0%, 25%, 50%, 75%. This emulates the older CRT monitors|
|F8|Turbo modes|Cyclically toggles CPU speed (3.5MHz, 7MHz, 14MHz, 28Mhz)|
|F9|NMI (Multiface)|Simulates pressing the NMI button|
|F10|divMMC NMI (Drive)|Simulates pressing the Drive button (divMMC NMI – used with esxDOS). Used with Caps Shift it forces a rescan of drives and a reload of the boot screen under esxDOS|
|NMI + <numeric keys>|Simulates PS/2 keyboard function keys| |

#### Key files

|File|Description|
|:-------|:------------|
|`machines/next/CONFIG.INI`|Next main core settings (scanlines, scandoubler, screen refresh rate, ULAPlus modes, etc.). Select the default mode from those defined in `machines/next/menu.def`.|