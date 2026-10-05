# Echo Peel

Echo Peel takes the sound out of screen recordings and other videos and saves it as an MP3, or as the video's own sound, untouched. It all happens on your iPhone or computer: nothing is uploaded, and it works offline.

## What it does

- **Speech MP3**: mono, 96 kbps, about 0.7 MB a minute. Small files with clear voices: the right choice for listening practice.
- **Music MP3**: stereo, 192 kbps, about 1.4 MB a minute. Keeps left and right.
- **Original**: copies the video's own sound exactly as it is, without re-encoding it. Instant and lossless. iPhone recordings give an `.m4a` file.
- **Trim**: cut off the start and end, like the moment you open Control Center. Drag the edges of the frame over the waveform, nudge them 0.1 s at a time with − and +, or play to a moment and tap **Set at playhead**. Tap a start or end time to hear that edge. MP3 trims are exact to the sample.
- **Several at once**: add as many recordings as you like, rename each file before extracting, and extract them in one go. **Cancel** stops at any moment.
- **Two sound tracks**: a recording that carries the app's sound and your microphone as separate tracks is mixed by default. The card lets you take just one track.
- **Your files stay**: finished audio files are kept in Echo Peel until you clear them. Play them, rename them, then save them: **Save or share › Save to Files** on the iPhone, **Download** on a computer.

## Put it online (GitHub Pages)

1. On GitHub, on the same account as your Echo Loop apps, create a new public repository, for example `echo-peel`. Upload every file in this folder and keep the file names as they are. **`mediabunny.min.mjs` and `mediabunny-mp3-encoder.min.mjs` must sit next to `index.html`**: they are the engine.
2. In the repository, open **Settings → Pages** and choose **Deploy from a branch → main → / (root)**. Save.
3. After a minute, open `https://<your-username>.github.io/echo-peel/` in **Safari** on the iPhone.
4. Tap **Share → Add to Home Screen**, keep **Open as Web App** switched on, then tap **Add**. It appears as **Echo Peel**.
5. Open it from the Home Screen **once while online**. When the dot at the top turns green (**Offline ready**), it works in airplane mode.

On a computer, open the same address in Chrome or Edge. Click the install icon in the address bar if you want it in its own window.

## Use it on the iPhone

1. **Put the recording in Files** (the fastest way): in Photos, open the screen recording, tap **Share → Save to Files** and pick a folder.
2. In Echo Peel, tap **+** and pick the recording from Files. Choosing from the Photo Library works too, but the iPhone converts the video before Echo Peel gets it, which takes a while for long recordings.
3. Choose **Speech**, **Music** or **Original**. Tap **Trim** if you want to cut the ends. Tap **Extract**.
4. Tap the share button on the finished file, then **Save to Files**. In Echo Loop Touch, tap **+** and import it from there.

## Good to know

- **MP3s need iOS 26.** Safari can decode sound for web apps only from iOS 26. On an older iPhone, Echo Peel shows a note and offers **Original** only.
- **Keep it open while it works.** The screen stays on during extraction. If you switch to another app, the iPhone pauses Echo Peel, and it carries on when you come back. In testing on a computer, a one-minute recording took about two seconds and a 30-minute lecture 23 seconds; a recent iPhone should be in the same range.
- **A file marked *silent*** came from a recording with no sound in it: the app you recorded was muted (Silent mode mutes some apps), or it blocks sound in screen recordings.
- **Trimmed Original files** start a fraction of a second early (under 0.1 s), because compressed sound needs a few packets before a cut to decode cleanly. Nothing inside your selection is lost. MP3 trims are exact.
- **Where the files live.** Finished files are stored inside Echo Peel on this device. Deleting the Home Screen app or clearing Safari's website data removes them, so save the ones you want to keep to Files. Each Home Screen app has its own storage, so Echo Loop Touch can't see Echo Peel's files directly: go through Files.
- **The picture in Trim.** The iPhone shows its own screen recordings. A computer may show only a note instead of the picture for some iPhone videos (HEVC); the sound and the waveform still work.
- **Opened from a folder.** Double-clicking `index.html` doesn't work. Browsers only run Echo Peel from a web address.
- **Updating later.** If you change any file, also change `epeel-v1` to `epeel-v2` (and so on) at the top of `sw.js`. The app picks up the new version the next time it's opened online. Your finished files stay.

## What has been tested

Echo Peel was tested in a Chromium browser that decodes AAC, at iPhone and desktop sizes, with iPhone-style recordings: MP4 and MOV containers, H.264 and HEVC video, AAC sound at 44.1 and 48 kHz, a recording with two sound tracks at different rates, one with no sound track, one with a silent sound track, a 30-minute lecture, Opus sound in WebM and 96 kHz sound. Timed beeps in the test files showed that MP3 trims land on the exact sample and that nothing drifts over 30 minutes. It has not yet run on a real iPhone, so tell me if anything behaves differently there; the **Details** button under any error gives the technical facts to send.

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app, with plain-English comments throughout |
| `mediabunny.min.mjs` | Mediabunny: reads video files and writes audio files |
| `mediabunny-mp3-encoder.min.mjs` | Mediabunny's MP3 encoder: LAME, compiled to run in the browser |
| `sw.js` | Saves the app for offline use |
| `manifest.webmanifest` | Home Screen name, icon and colours |
| `icon-180.png`, `icon-192.png`, `icon-512.png` | App icons |
| `make_icons.py` | Script that draws the icons (only needed if you want to change them) |

Your recordings never leave the device. Echo Peel reads them where they are and keeps only the finished audio files.

## Credits

- **Mediabunny** 1.61.1 by Vanilagy and contributors, Mozilla Public License 2.0. The two `.mjs` files are unchanged copies from the npm packages `mediabunny` and `@mediabunny/mp3-encoder`; their source code is at [github.com/Vanilagy/mediabunny](https://github.com/Vanilagy/mediabunny).
- **LAME MP3 encoder** 3.100, GNU LGPL: [lame.sourceforge.io](https://lame.sourceforge.io).
