title: ZX Mechtrum
summary: Fabricación de un ZX Mechtrum Harlequin, es decir un ZX Spectrum con la placa Harlequin 128 y con teclado mecánico.
date: 2024-09-09 12:00:00

![Mechtrum](/images/posts/2024-09-09_zx_mechtrum/mechtrum_logo.png)

Hace tiempo que me apetecía montar un kit de [ZX Spectrum Harlequin 128](https://www.bytedelight.com/?product=harlequin-128k-rev-2d-black-large-diy-kit). Es el Spectrum perfecto (128KB, soporte de todos los modelos/ROMs de las distintas versiones producidas por Sinclair y Amstrad, y con componentes que se pueden adquirir a día de hoy, incluida la ULA que está reemplazada por lógica discreta). Pero para la caja, la opción de adquirir una de las carcasas réplica del 48K original (gomas), no me entusiasmaba.

Hace unos meses conocí el proyecto [ZX Mechtrum](https://leesmithsworkshop.co.uk/products/the-mechtrum-mechanical-keyboard-zx-spectrum-case) de Lee Smith, una caja para placas de formato 48KB con un teclado mecánico, y me pareció el complemento perfecto para el Harlequin. De hecho, en el [vídeo del canal More Fun Making It](https://www.youtube.com/watch?v=Gr8KhQHaJr4) gracias al que supe de su existencia, su creador comenta que tiene el proyecto inmediato de instalar un Harlequin 128 en una de estas cajas.

Como ya existen varios vídeos y guías tanto del kit Harlequin como de la caja ZX Mechtrum, no voy a detallar el proceso de montaje, pero sí describirlo en general y comentar algunas particularidades y problemas que he encontrado.

#### Mechtrum

Como el kit Harlequin 128 es distribuido por Byte Delight, por lo que su disponibilidad es bastante estable, el punto más crítico del plan era adquirir el [Mechtrum de Lee Smith](https://leesmithsworkshop.co.uk/products/the-mechtrum-mechanical-keyboard-zx-spectrum-case), ya que la venta de productos no es su principal actividad. De hecho pude conseguir la última unidad de una tirada que hizo a finales de 2023. En el momento de escribir esto (septiembre 2024) vuelve a estar a la venta, pero no es de esperar que se mantenga siempre así. El caso es que pude adquirir una unidad que llegó ya montada. Mi unidad venía con 3 faceplates, una para el 48K, otra para el [Sifzif 512](https://github.com/UzixLS/zx-sizif-512/) y otra para el Harlequin 128.

![Mechtrum](/images/posts/2024-09-09_zx_mechtrum/mechtrum.jpg)

#### Harlequin 128

El Harlequin 128, es un diseño de Don Superfo y puede adquirirse la PCB a través de los enlaces que hay en el [repositorio base del proyecto](https://github.com/DonSuperfo/Superfo-Harlequin-128). En el repositorio se encuentra también la BOM (Bill Of Materials) para las distintas versiones con todos los componentes necesarios. Pero con diferencia la opción más sencilla es adquirir uno de los kits que distribuye Ben Versteeg, de [Byte Delight](https://www.bytedelight.com/). El kit viene con una PCB de la versión issue 2D y todos los componentes necesarios para montarlo, convenientemente clasificados en bolsitas junto a un manual con el que es casi imposible perderse. También hay épocas en las que no está disponible en su tienda, pero es cuestión de estar atento o suscribirse a las notificaciones de disponibilidad. En mi caso tuve que esperar un par de meses a que volviera a estar disponible.

![Harlequin 128](/images/posts/2024-09-09_zx_mechtrum/harlequin_128.jpg)

El único problema que tuve durante su montaje fue que según el manual el array de resistencias R61 es opcional si no se va a instalar la interfaz de joystick. Pero esas resistencias, además de dar servicio al puerto de joystick, hacen de pullup para los microinterruptores de selección del banco de ROM, por lo que sin instalarlas, la selección de bancos de ROM superiores al 0 no era estable. Tras instalar el array R61, todo funcionó correctamente.

![Harlequin 128 ROM selector pullups](/images/posts/2024-09-09_zx_mechtrum/harlequin_128_pullups.png)

#### Resultado

El resultado es un sueño hecho realidad, un Spectrum 128K con teclado mecánico y componentes fiables. Además de una belleza. 🤩

![Mechtrum](/images/posts/2024-09-09_zx_mechtrum/resultado.jpg)