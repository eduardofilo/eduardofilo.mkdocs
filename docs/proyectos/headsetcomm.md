---
layout: default
permalink: /proyectos/headsetcomm.html
---

# Headset Commander

## Enlaces

*  [How to detect Bluetooth headset key press](http://groups.google.com/group/android-developers/browse_thread/thread/bffee54fea341118?pli=1)
*  [headset button](http://groups.google.com/group/android-developers/browse_thread/thread/81e7fadd7f0b64fb/54d82fcdb0c01540)
*  [Using Android Headset Buttons (Earphone Buttons)](http://www.gauntface.co.uk/blog/2010/04/14/using-android-headset-buttons-earphone-buttons/)

## Logcat play/pause

```
#### Google Music
01-25 18:54:23.960  1226  1226 I AwesomePlayer: play_l
01-25 18:54:24.007 19228 19232 I dalvikvm: Jit: resizing JitTable from 4096 to 8192
01-25 18:54:25.038 19653 19663 D MediaPlaybackService: Event logging MUSIC_PAUSE_PLAYBACK_REQUESTED: [299, DEFAULT]/c10a328e-25f5-36a5-bb2b-8642bc8a8f76
01-25 18:54:25.053  1226  1779 I AwesomePlayer: pause_l 0
01-25 18:54:25.061  1373  1388 D NotificationService: turn off LED due to Dock full charging
01-25 18:54:25.085  1373  1384 D BluetoothA2dpService: received playstatechanged Action
01-25 18:54:25.085  1373  1384 D BluetoothA2dpService: Received Meta Data Details Track = Fool (If You Think It's Over) Artist = Chris Rea Album = The Best Of Chris Rea Trackno = null no.of track = null TrackDuration = null TrackPosition = null
01-25 18:54:25.085  1373  1384 D BluetoothA2dpService: received playstatechanged Action
01-25 18:54:25.249  1226  1367 D AudioHardwareMot: AudioStreamOutMot::setParameters() fm_attenuate=0;fm_mute=0

#### Pocket Cast
01-17 19:41:48.420 12280 12298 I AwesomePlayer: play_l
01-17 19:41:49.561 12280 12298 I AwesomePlayer: pause_l 0

#### Música
01-25 19:03:54.350  1226  1369 I AwesomePlayer: play_l
01-25 19:03:54.382 19958 19958 D DEBUGDEBUG: ALBUM ART WAS NOT FOUND: <unknown>:WhatsApp Audio
01-25 19:03:54.421 19958 19958 E TuneWiki: Sending AVRCP command with action: com.android.music.metachanged
01-25 19:03:54.428  1373  1384 D BluetoothA2dpService: received metachanged Action New Build
01-25 19:03:54.428  1373  1384 D BluetoothA2dpService: Received Meta Data Details Track = AUD-20110917-WA0004 Artist = Artista desconocido Album = WhatsApp Audio Trackno = 1 no.of track = 144 TrackDuration = 17040 TrackPosition = 9540
01-25 19:03:54.428 19958 19958 V TuneWiki: MPD - Status Changed: 0
01-25 19:03:54.483 19958 19958 D DEBUGDEBUG: ALBUM ART WAS NOT FOUND: <unknown>:WhatsApp Audio
01-25 19:03:54.522 19958 19958 D FMControllerService: Starting FMSControllerService, action: tunewiki.intent.action.SWITCH_MPD
01-25 19:03:55.249 19958 19958 E TuneWiki: Starting TunWikiMPD, action: tunewiki.intent.action.HEADSET_SINGLE_CLICK
01-25 19:03:55.249 19958 19958 V TuneWiki: MPD - pause() called
01-25 19:03:55.249 19958 19958 V TuneWiki: MPD - currently playing, so pausing
01-25 19:03:55.257  1226 15028 I AwesomePlayer: pause_l 0
01-25 19:03:55.272  1373  1388 D NotificationService: turn off LED due to Dock full charging
01-25 19:03:55.296 19958 19958 D DEBUGDEBUG: ALBUM ART WAS NOT FOUND: <unknown>:WhatsApp Audio
01-25 19:03:55.311 19958 19958 E TuneWiki: Sending AVRCP command with action: com.android.music.playerpaused
01-25 19:03:55.311  1373  1384 D BluetoothA2dpService: received paused Action
01-25 19:03:55.311 19958 19958 V TuneWiki: MPD - Status Changed: 1
01-25 19:03:55.327 19958 19958 D DEBUGDEBUG: ALBUM ART WAS NOT FOUND: <unknown>:WhatsApp Audio
01-25 19:03:55.455  1226  1367 D AudioHardwareMot: AudioStreamOutMot::setParameters() fm_attenuate=0;fm_mute=0
```
