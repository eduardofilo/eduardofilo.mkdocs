---
layout: default
permalink: /ingenieria/radio.html
---

# Radio

## Acrónimos/Términos

* Frecuencia:
    * **ELF**: Frecuencia Extremadamente Baja (Extremely Low Frequency): 3 Hz - 30 Hz; 100000 km - 10000 km
    * **SLF**: Frecuencia Super Baja (Super Low Frequency): 30 Hz - 300 Hz; 10000 km - 1000 km
    * **ULF**: Frecuencia Ultra Baja (Ultra Low Frequency): 300 Hz - 3 kHz; 1000 km - 100 km
    * **VLF**: Frecuencia Muy Baja (Very Low Frequency): 3 kHz - 30 kHz; 100 km - 10 km
    * **LF**: Frecuencia Baja (Low Frequency): 30 kHz - 300 kHz; 10 km - 1 km
    * **MF**: Frecuencia Media (Medium Frequency): 300 kHz - 3 MHz; 1 km - 100 m
    * **HF**: Frecuencia Alta (High Frequency): 3 MHz - 30 MHz; 100 m - 10 m
    * **VHF**: Frecuencia Muy Alta (Very High Frequency): 30 MHz - 300 MHz; 10 m - 1 m
    * **UHF**: Frecuencia Ultra Alta (Ultra High Frequency): 300 MHz - 3 GHz; 1 m - 10 cm
    * **SHF**: Frecuencia Super Alta (Super High Frequency): 3 GHz - 30 GHz; 10 cm - 1 cm
    * **EHF**: Frecuencia Extremadamente Alta (Extremely High Frequency): 30 GHz - 300 GHz; 1 cm - 1 mm
    * **THF**: Frecuencia Terahertz (Terahertz Frequency): 300 GHz - 3 THz; 1 mm - 0.1 mm
* Modulación:
    * **CW**: Onda Continua (Continuous Wave) (200 Hz default bandwidth). En radioafición se utiliza para transmitir código Morse.
    * Analógica:
        * **AM**: Amplitud Modulada (Amplitude Modulation) (8323 Hz default bandwidth)
        * **FM**: Frecuencia Modulada (Frequency Modulation)
            * **NFM**: Frecuencia Modulada Normal (Normal FM) (12500 Hz default bandwidth)
            * **WFM**: Frecuencia Modulada Ancha (Wideband FM) (150000 Hz default bandwidth)
        * **PM**: Modulación de Fase (Phase Modulation)
        * **QAM**: Modulación de Amplitud en Cuadratura (Quadrature Amplitude Modulation)
        * **DSB**: Banda Lateral Doble (Dual Side Band) (4200 Hz default bandwith)
        * **SSB**: Banda Lateral Única (Single Side Band)
            * **LSB**: Banda Lateral Inferior (Lower Side Band) (2800 Hz default bandwith). En Radioafición se utiliza para frecuencias por debajo de 10,7 MHz.
            * **USB**: Banda Lateral Superior (Upper Side Band) (2800 Hz default bandwith). En Radioafición se utiliza para frecuencias por encima de 10,7 MHz.
    * Digital:
        * **PSK**: Modulación por Desplazamiento de Fase (Phase Shift Keying)
            * **BPSK**: Modulación por Desplazamiento de Fase Binaria (Binary Phase Shift Keying)
            * **QPSK**: Modulación por Desplazamiento de Fase Cuaternaria (Quadrature Phase Shift Keying)
            * **8PSK**: Modulación por Desplazamiento de Fase de 8 Estados (8 Phase Shift Keying)
            * **16PSK**: Modulación por Desplazamiento de Fase de 16 Estados (16 Phase Shift Keying)
* **SMA**: Conector de Rosca de 1.13 mm
* **AGC**: Control Automático de Ganancia (Automatic Gain Control)
* **LNA**: Amplificador de Bajo Ruido (Low Noise Amplifier)
* **SDR**: Radio Definida por Software (Software Defined Radio)
* **Bias-T**: Alimentación a través del cable coaxial (Bias Tee)
* **VOLMET**: Servicio de información meteorológica para aeronaves en vuelo. Se transmite en HF y VHF.
* **WWV**: Servicio de tiempo y frecuencia de la Administración Nacional Oceánica y Atmosférica (NOAA) de EE. UU. Se transmite en LF y VHF.
* **VFO**: Oscilador Variable de Frecuencia (Variable Frequency Oscillator).
* **IF**: Frecuencia Intermedia (Intermediate Frequency).

## Enlaces

#### Conceptos

* [La modulación y sus modos](https://www.cb27.com/primerospasos/la-modulacion-y-sus-modos)
* [Comprendiendo la banda lateral única (SSB)](https://crecj.org/comprender-la-banda-lateral-unica-ssb/)

#### Frecuencias

* [Listado de frecuencias EIBI/AOKI/HFCC](https://docs.google.com/spreadsheets/d/1StTd2lRB1UTUitbo7YTDxhw2ZInUk_LaIVmO6orQ64w/edit)
* [Tabla de frecuencias de la banda de 11 metros (27 MHz - CB)](https://www.cb27.com/dx/tabla-frecuencias)
* [Balizas de navegación aérea](https://aip.enaire.es/AIP/contenido_AIP/ENR/LE_ENR_4_1_en.html). [NDBs](https://es.wikipedia.org/wiki/Baliza_no_direccional) encontradas:
    * Desde Zaragoza:
        * 335 kHz: TON - Torralba de Aragón
        * 389 kHz: ZRZ - Zaragoza
        * 404 kHz: LRD - Lérida

#### SDR

* Tutoriales:
    * [Quick Start Guide - RTL-SDR.COM](https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/)
    * [El gran libro de SDRsharp](https://airspy.com/downloads/SDRSharp_Guia_v5.5_ESP.pdf)
    * [Tutorials - GNU Radio](https://wiki.gnuradio.org/index.php/Tutorials)
* Páginas de referencia:
    * [RTL-SDR.COM](https://www.rtl-sdr.com/)
    * [Airspy](https://airspy.com/)
    * [HackRF](https://greatscottgadgets.com/hackrf/)
    * [SDRplay](https://www.sdrplay.com/)
    * [LimeSDR](https://www.limemicro.com/)
    * [GNU Radio](https://www.gnuradio.org/)
* Software:
    * [The BIG List of RTL-SDR Supported Software](https://www.rtl-sdr.com/big-list-rtl-sdr-supported-software/)
    * [SDR++](https://www.sdrpp.org/)
    * [SDR#](https://airspy.com/downloads/)
    * CubicSDR: [Repositorio](https://github.com/cjcliffe/CubicSDR), [Página](https://cubicsdr.com/).
    * Gqrx: [Repositorio](https://github.com/gqrx-sdr/gqrx/), [Página](https://gqrx.dk/)
    * [OpenWebRX](https://openwebrx.de/)
    * SigDigger: [Repositorio](https://github.com/BatchDrake/SigDigger/), [Página](https://batchdrake.github.io/SigDigger/)
    * [Dump1090](https://github.com/antirez/dump1090): Dump1090 es un decodificador de modo S para dispositivos RTLSDR. Puede usarse para decodificar mensajes ADS-B de los transpondedores de aeronaves.
    * RTL_433: [Documentación](https://triq.org/rtl_433/), [Repositorio](https://github.com/merbanan/rtl_433). RTL_433 es un software para decodificar señales de dispositivos de 433 MHz.
* [WebSDR](http://websdr.org/)

## Ajustes SDR

#### PMR446

* Tuner AGC: ON
* Modulación: NFM
* De-emphasis: 50us
* IF Noise Reduction: Voice
* Low Pass: ON