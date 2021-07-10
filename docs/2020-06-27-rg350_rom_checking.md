title: Corrección de ROMs MAME
summary: Comprobación y corrección de ROM para MAME.
date: 2020-06-27 13:30:00

## ROM `Soccer Superstars` - `soccerss.zip`

Ese juego necesita una pequeña BIOS de Konami. En el DAT pone esto:

```
<game name="soccerss" romof="konamigx">
	<description>Soccer Superstars (ver JAA)</description>
	<year>1994</year>
	<manufacturer>Konami</manufacturer>
	<rom name="300a01.34k" merge="300a01.34k" size="131072" crc="d5fa95f5" sha1="c483aa98ff8ef40cdac359c19ad23fea5ecc1906"/>
	<rom name="427a04.28r" size="524288" crc="c7d3e1a2" sha1="5e1e4f4c97def36902ad853248014a7af62e0c5e"/>
	<rom name="427a05.30r" size="524288" crc="5372f0a5" sha1="36e8d0a73918cbd018c1865d1a05445daba8997c"/>
	<rom name="427a06.9m" size="131072" crc="979df65d" sha1="7499e9a27aa562692bd3a296789696492a6254bc"/>
	<rom name="427a07.6m" size="131072" crc="8dbaf4c7" sha1="cb69bf94090a4871b35e7ba1f58e3225077b82cd"/>
	<rom name="427a08.140" size="2097152" crc="221250af" sha1="fd24e7f0e3024df5aa08506523953c5e35d2267b"/>
	<rom name="427a09.137" size="2097152" crc="56bdd480" sha1="01d164aedc77f71f6310cfd739c00b33289a2e7e"/>
	<rom name="427a10.25r" size="2097152" crc="6b3ccb41" sha1="b246ef350a430e60f0afd1b80ff48139c325e926"/>
	<rom name="427a11.23r" size="2097152" crc="c1ca74c1" sha1="b7286df8e59f8f1939ebf17aaf9345a857b0b100"/>
	<rom name="427a12.21r" size="2097152" crc="97d6fd38" sha1="8d2895850cafdea95db08c84e7eeea90a1921515"/>
	<rom name="427a13.18r" size="2097152" crc="815a9b87" sha1="7d9d5932fff7dd7aa4cbccf0c8d3784dc8042e70"/>
	<rom name="427a14.143" size="524288" crc="7575a0ed" sha1="92fda2747ac090f93e60cff8478af6721b949dc2"/>
	<rom name="427a15.11r" size="1048576" crc="33ce2b8e" sha1="b0936386cdc7c41f33b1d7b4f5ce25fe618d1286"/>
	<rom name="427a16.9r" size="2097152" crc="39547265" sha1="c0efd68c0c1ea59141045150842f36d43e1f01d8"/>
	<rom name="427a17.24c" size="524288" crc="fb6eb01f" sha1="28cdb30ff70ee5fc7624e18fe048dd85dfa49ace"/>
	<rom name="427a18.145" size="1048576" crc="bb6e6ec6" sha1="aa1365a4318866d9e7e74461a6e6c113f83b6771"/>
	<rom name="427jaa02.28m" size="524288" crc="210f9ba7" sha1="766fc821d1c7aaf9e306c6e2379d85e7aa50738c"/>
	<rom name="427jaa03.30m" size="524288" crc="f76add04" sha1="755dff41ce3b0488ed8f9f5feebfe95a22b70d16"/>
</game>
```

Si abrimos el .zip vemos que contiene todas las ROMs menos la primera. El `romof="konamigx"` del principio indica que la ROM necesita la BIOS `konamigx`. La definición de este fichero en el mismo DAT del romset es:

```
<game name="konamigx" isbios="yes">
    <description>System GX</description>
    <year>1994</year>
    <manufacturer>Konami</manufacturer>
    <rom name="300a01.34k" size="131072" crc="d5fa95f5" sha1="c483aa98ff8ef40cdac359c19ad23fea5ecc1906"/>
</game>
```

Ahí vemos claramente que se trata de una BIOS (`isbios="yes"`).

Para que funcione el juego pues hay que localizar el fichero `konamigx.zip` que contenga la ROM `300a01.34k`.

## ROM `The Simpsons (2 Players World, set 2)` - `simps2pa.zip`

Este juego es un clon de `The Simpsons (4 Players World, set 1)` tal y como vemos en el dat:

```
<game name="simps2pa" cloneof="simpsons" romof="simpsons">
	<description>The Simpsons (2 Players alt)</description>
	<year>1991</year>
	<manufacturer>Konami</manufacturer>
	<rom name="simp1.17c" size="131072" crc="07ceeaea" sha1="c18255ae1d578c2d53de80d6323cdf41cbe47b57"/>
	<rom name="simp2.16c" merge="g02.16c" size="131072" crc="580ce1d6" sha1="5b07fb8e8041e1663980aa35d853fdc13b22dac5"/>
	<rom name="simp3.15c" size="131072" crc="96636225" sha1="5de95606e5c9337f18bc42f4df791cacafa20399"/>
	<rom name="simp4.13c" size="131072" crc="54e6df66" sha1="1b83ae56cf1deb51b04880fa421f06568c938a99"/>
	<rom name="simp5.6g" size="131072" crc="76c1850c" sha1="9047c6b26c4e33c74eb7400a807d3d9f206f7bbe"/>
	<rom name="simp_12n.rom" merge="simp_12n.rom" size="1048576" crc="577dbd53" sha1="e603e03e3dcba766074561faa92afafa5761953d"/>
	<rom name="simp_16h.rom" merge="simp_16h.rom" size="524288" crc="cf2bbcab" sha1="47afea47f9bc8cb5eb1c7b7fbafe954b3e749aeb"/>
	<rom name="simp_16l.rom" merge="simp_16l.rom" size="1048576" crc="55fab05d" sha1="54db8559d71ed257de9a29c8808654eaea0df9e2"/>
	<rom name="simp_18h.rom" merge="simp_18h.rom" size="524288" crc="ba1ec910" sha1="0805ccb641271dea43185dc0365732260db1763d"/>
	<rom name="simp_1d.rom" merge="simp_1d.rom" size="262144" crc="78778013" sha1="edbd6d83b0d1a20df39bb160b92395586fa3c32d"/>
	<rom name="simp_1f.rom" merge="simp_1f.rom" size="1048576" crc="1397a73b" sha1="369422c84cca5472967af54b8351e29fcd69f621"/>
	<rom name="simp_3n.rom" merge="simp_3n.rom" size="1048576" crc="7de500ad" sha1="61b76b8f402e3bde1509679aaaa28ef08cafb0ab"/>
	<rom name="simp_8n.rom" merge="simp_8n.rom" size="1048576" crc="aa085093" sha1="925239d79bf607021d371263352618876f59c1f8"/>
</game>
```

Necesita por tanto que el juego base esté instalado:

```
<game name="simpsons">
	<description>The Simpsons (4 Players)</description>
	<year>1991</year>
	<manufacturer>Konami</manufacturer>
	<rom name="e03.6g" size="131072" crc="866b7a35" sha1="98905764eb4c7d968ccc17618a1f24ee12e33c0e"/>
	<rom name="g01.17c" size="131072" crc="9f843def" sha1="858432b59101b0577c5cec6ac0c7c20ab0780c9a"/>
	<rom name="g02.16c" size="131072" crc="580ce1d6" sha1="5b07fb8e8041e1663980aa35d853fdc13b22dac5"/>
	<rom name="j12.15c" size="131072" crc="479e12f2" sha1="15a6cb12e68b4773a29ab463640a43f8e814de59"/>
	<rom name="j13.13c" size="131072" crc="aade2abd" sha1="10f178d5ed399b4866266e075d91ca3db26798f8"/>
	<rom name="simp_12n.rom" size="1048576" crc="577dbd53" sha1="e603e03e3dcba766074561faa92afafa5761953d"/>
	<rom name="simp_16h.rom" size="524288" crc="cf2bbcab" sha1="47afea47f9bc8cb5eb1c7b7fbafe954b3e749aeb"/>
	<rom name="simp_16l.rom" size="1048576" crc="55fab05d" sha1="54db8559d71ed257de9a29c8808654eaea0df9e2"/>
	<rom name="simp_18h.rom" size="524288" crc="ba1ec910" sha1="0805ccb641271dea43185dc0365732260db1763d"/>
	<rom name="simp_1d.rom" size="262144" crc="78778013" sha1="edbd6d83b0d1a20df39bb160b92395586fa3c32d"/>
	<rom name="simp_1f.rom" size="1048576" crc="1397a73b" sha1="369422c84cca5472967af54b8351e29fcd69f621"/>
	<rom name="simp_3n.rom" size="1048576" crc="7de500ad" sha1="61b76b8f402e3bde1509679aaaa28ef08cafb0ab"/>
	<rom name="simp_8n.rom" size="1048576" crc="aa085093" sha1="925239d79bf607021d371263352618876f59c1f8"/>
</game>
```

Empaquetar al final las ROMs con:

```
zip -0 rom.zip *
```
