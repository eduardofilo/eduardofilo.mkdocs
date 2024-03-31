---
layout: default
permalink: /retro-emulacion/zx-spectrum-next.html
---

# ZX Spectrum Next / N-GO

## Enlaces

* [ZX Spectrum Next](https://www.specnext.com/)
* [N-GO](https://manuferhi.com/c/n-go)

## Cheatsheet

#### Atajos teclado

|Combinación|Acción|Notas|
|:------------|:-------|:------|
|F1 / Reset (pulsación larga)|Hard Reset|Resets CPU and Peripherals, reloads the FW and loads the hardware settings anew but doesn't clear the RAM|
|F2|Scandoubler|Doubles the output resolution. Must be off for older monitors and SCART cables|
|F3|50Hz/60Hz Vertical Frequency|Changes the display's vertical frequency from 50 to 60Hz and vice-versa|
|F4 / Reset (pulsación corta)|Soft Reset|Resets CPU and Peripherals and reloads the Operating System. Used with Caps Shift it forces a rescan of drives and a reload of the boot screen under esxDOS|
|F5|Not Used| |
|F6|Not Used| |
|F7|Scanlines|Cyclically toggles scan line emulation in 4 steps/intensities: 0%, 25%, 50%, 75%. This emulates the older CRT monitors|
|F8|Turbo modes|Cyclically toggles CPU speed (3.5MHz, 7MHz, 14MHz, 28Mhz)|
|F9|NMI (Multiface)|Simulates pressing the NMI button|
|F10|divMMC NMI (Drive)|Simulates pressing the Drive button (divMMC NMI – used with esxDOS). Used with Caps Shift it forces a rescan of drives and a reload of the boot screen under esxDOS|
|NMI + <teclas numéricas>|Simula teclas de función teclado PS/2| |

#### Ficheros importantes

|Fichero|Descripción|
|:-------|:------------|
|`machines/next/CONFIG.INI`|Ajustes del core principal del Next (scanlines, scandoubler, frecuencia refresco pantalla, modos ULAPlus, etc.). Selecciona el modo predeterminado de los definidos en `machines/next/menu.def`|

#### Modos

|Modo|Selección|Descripción|
|:---|:--------|:----------|
|`ZX Spectrum Next (standard)`|Espacio durante hard boot/reset|NextZXOS normal|
|`ZX Spectrum Next (LG 48K ROM)`|Espacio durante hard boot/reset| |
|`ZX Spectrum 48K`|Espacio durante hard boot/reset y página `more...` de menú NextZXOS| |
|`ZX Spectrum 128k`|Espacio durante hard boot/reset y página `more...` de menú NextZXOS| |
|`ZX Spectrum +2`|Espacio durante hard boot/reset| |
|`ZX Spectrum +2A/+3`|Espacio durante hard boot/reset| |
|`ZX Spectrum +3e`|Espacio durante hard boot/reset| |
|`ZX80 Emulator (c) Paul Farrow`|Espacio durante hard boot/reset y página `more...` de menú NextZXOS| |
|`ZX81 Emulator (c) Paul Farrow`|Espacio durante hard boot/reset y página `more...` de menú NextZXOS| |
|`48K Gosh Wonderful ROM v3.3`|Espacio durante hard boot/reset| |
|`48K Looking Glass ROM v1.07`|Espacio durante hard boot/reset|Modo 48K con comandos tecla a tecla y corrección de bugs|
|`48K Looking Glass ROM v1.07-altfont-`|Espacio durante hard boot/reset|Modo 48K con comandos tecla a tecla y corrección de bugs. Tiene un tipo de letra más grueso|
|`Timex Sinclair TC2048`|Espacio durante hard boot/reset| |
|`Investronica Spectrum 128K`|Espacio durante hard boot/reset| |
|`Pentagon 128K`|Espacio durante hard boot/reset| |

#### Modos de cursor NextBASIC

|32 columnas (Color)|64/85 columnas (Forma)|Función|
|:---------------------|:---------------------------------|:--------|
|Blue|Barra horizontal en la mitad inferior del carácter|Introducción normal de texto|
|Cyan|Barra horizontal en la mitad superior del carácter|Bloq Mayús activado (conmutar con la tecla CAPS LOCK)|
|Magenta|Barra Vertical|Modo GRÁFICO (Conmutar con la tecla GRAPHICS)|
|Green|Rayas horizontales|Modo EXTEND (Conmutar con la tecla EXTEND)|
|Red|Contorno rectangular|Marcador de error: Hay un error en la línea que hay que corregir|

#### Conexiones cassette

![Conexiones cassette 1](/images/pages/zx-spectrum-next/Ear-mic-socket-1.png)

![Conexiones cassette 2](/images/pages/zx-spectrum-next/Spectrum-plus-3-tape-lead.jpg)
