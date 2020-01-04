---
layout: default
permalink: /electronica/componentes.html
---

# Componentes

## Tiendas

* [LCSC](https://lcsc.com/)
* [Viinko Electronics HK Ltd](https://viinko.es.aliexpress.com/store/1361740): Acepta pedidos BOM.

## Componentes interesantes

|Componente|Enlace compra|Footprint KiCad|
|:---------|:------------|:--------|
|Resistencia 1/4W P=10,16mm| |`Resistors_ThroughHole:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`|
|Condensador cerámico 100nF P=2,54mm| |`Capacitors_ThroughHole:C_Disc_D3.0mm_W1.6mm_P2.50mm`|
|LED D=5mm| |`LED_THT:LED_D5.0mm`|
|USB micro-B|[LCSC](https://lcsc.com/product-detail/USB-Connectors_Amphenol-ICC-10118194-0001LF_C132563.html)|`Connect:USB_Micro-B`|
|Lector microSD|[LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_HRS-Hirose_DM3AT-SF-PEJM5_HRS-Hirose-HRS-DM3AT-SF-PEJM5_C114218.html)|`Connector_Card:microSD_HC_Hirose_DM3AT-SD-PEJMS`|
|Lector microSD|[LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_Korean-Hroparts-Elec-TF-04A_C145799.html)|`Connector_Card:microSD_HC_Wuerth_693072010801`|
|Lector microSD|[LCSC](https://lcsc.com/product-detail/Card-Sockets-Connectors_XUNPU-TF-104_C266612.html)| |
|Transistor TO-92| |`TO_SOT_Packages_THT:TO-92_Inline_Wide`|
|Switch horizontal|[LCSC](https://lcsc.com/product-detail/Toggle-Switches_SHOU-HAN-SK12D07VG4_C393937.html)|`Buttons_Switches_ThroughHole:SW_CuK_OS102011MA1QN1_SPDT_Angled`|
|Tactile button horizontal|[LCSC](https://lcsc.com/product-detail/Others_C-K-PTS645VM832LFS_C285530.html)|`Button_Switch_THT/SW_Tactile_SPST_Angled_PTS645Vx83-2LFS`|
|Tactile button 6mm| |`Buttons_Switches_ThroughHole:SW_PUSH_6mm`|
|Zócalo 8 pin (ATtiny85)| |`Housings_DIP:DIP-8_W7.62mm`|
|Conector alimentación jack barril 5.5mm|[LCSC](https://lcsc.com/product-detail/Power-Connectors_XKB-Enterprise-DC-005-5A-2-0_C381116.html)|`Connector_BarrelJack:BarrelJack_Wuerth_6941xx301002`|

## Símbolos y footprints propios KiCad

En [este repositorio](https://github.com/eduardofilo/kicad_footprints).

|Componente|Symbol|Footprint|Compra|
|:---------|:-----|:--------|:-----|
|Switch horizontal|eduardofilo_symbols.lib/SK12D07VG4|`Buttons_Switches_ThroughHole:SW_CuK_OS102011MA1QN1_SPDT_Angled`|[LCSC](https://lcsc.com/product-detail/Toggle-Switches_SHOU-HAN-SK12D07VG4_C393937.html)|
|AY-8760|eduardofilo_symbols.lib/AY-3-8760|`Package_DIP:DIP-28_W15.24mm_Socket_LongPads`| |
|SNES Connector|eduardofilo_symbols.lib/SNES_Connector|eduardofilo_footprints.pretty/SNES.kicad_mod|[Aliexpress](https://es.aliexpress.com/item/32828768824.html)|
|EURO conector|`Connector:SCART-F`|eduardofilo_footprints.pretty/SCART.kicad_mod|[Aliexpress](https://es.aliexpress.com/item/32997772379.html)|
|Portapilas 2xAA|eduardofilo_symbols.lib/Battery_Holder|eduardofilo_footprints.pretty/BatteryHolder.kicad_mod|[LCSC](https://lcsc.com/product-detail/Battery-Holders-Clips-Contacts_Keystone-1013_C238059.html)|
|Logo Niubit| |eduardofilo_footprints.pretty/NiubitLogo.kicad_mod| |
