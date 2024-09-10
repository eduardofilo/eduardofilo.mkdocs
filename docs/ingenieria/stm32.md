---
layout: default
permalink: /ingenieria/stm32.html
---

# STM 32

## Placa de pruebas STM32 VL Discovery

### Enlaces

* [STM32VLDISCOVERY](http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/stm32vldiscovery.html): Discovery kit with STM32F100RB MCU.
* [Atollic TrueSTUDIO](http://timor.atollic.com/truestudio/): Free to download and free to use. No code size limits! A commercial-quality tool developed and maintained by Atollic, a professional tools company with years of experience in tools for embedded development. Linux and Mac OS X support is scheduled for later 2016.
* [STM32-Template](https://github.com/geoffreymbrown/STM32-Template)
* [Open source version of the STMicroelectronics Stlink Tools](https://github.com/texane/stlink)
* [STM32VLDISCOVERY programming tutorial](http://en.radzio.dxp.pl/stm32vldiscovery/)
* [Programming STM32VLDISCOVERY with Codesourcery and Eclipse](http://en.radzio.dxp.pl/stm32vldiscovery/programming,with,opensource,toolchain,codesourcery,eclipse.html)

### Preparación entorno desarrollo

Desarrollado en este [post](../2016-08-02-stm32-vl-discovery.md).

### Utilización como programador ST-Link v1

Tal y como describe la página 10 del [manual](../files/pages/STM32VLDiscovery.pdf), retirando los dos jumpers del conector CN3, se puede utilizar el programador ST-Link v1 que hay en la parte superior de la placa, para programar cualquier STM32 externo, utilizando el conector CN2 con el siguiente patillaje:

|Pin|CN2|Designación|
|:--|:--|:----------|
|1|VDD_TARGET|VDD|
|2|SWCLK|SWD Clock|
|3|GND|GND|
|4|SWDIO|SWD data input/output|