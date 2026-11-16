# Chapter 1 foundations authoring

This component replaces teaching for topics 1.1–1.3 only. It uses React 19.3, TypeScript 7, Vite 8, native SVG/Web Animations and the existing CircuitStore IndexedDB adapter. Built output is ordinary static files. Studying the website requires only the existing static server, not Node or Python speech packages.

## Rebuild

Use Node 26 (the version used for verification) and npm:

```sh
npm ci
npm test
npm run build
python3 integrate.py
```

In the portable repository, integration defaults to `../../dist` relative to this authoring directory. An explicit existing website directory can also be passed: `python3 integrate.py /absolute/path/to/dist`.

`src/lessons.json` is the editable lesson content and narration index. Zod validates its shape at startup. `Visual.tsx` contains SVG figures. `model.ts` calculates the current, terminal voltage, power accounts and unit conversions used by the figures. `state.ts` validates and restores lesson state. `index.tsx` manages the reader and media lifetime.

Progress is stored under `guided[topic].foundationV1`. Existing `rulesAndCases` state, exercise drafts and old media positions remain alongside it. A route change unmounts the reader; opening practice only stops media. Page hiding and navigation flush the current position through CircuitStore. Reflection checks are self-reports, not scores.

## Audio

Twenty MP3 recordings are included in `audio/` and the built website's `foundation/audio/`. There are no speech-service requests during study, no microphone and no API key. The player starts manually and restores its position paused.

`author-lessons.py` is an optional content-seeding script; it overwrites the JSON, so edit the JSON directly for routine revisions. To regenerate changed narration, install `gTTS==2.5.4` in a Python environment and run `python3 generate-audio.py`, then rebuild. This authoring step uses an external speech service; unchanged recordings are reused by content hash. The website itself uses the bundled recordings.

## Verification boundaries

Eleven unit tests cover model physics and normalized saved lesson state. `verify-integration.cjs DIST BASELINE_JSON` checks that all 14 original question objects and the original practice renderer/grading function remain unchanged, selected existing course/storage files retain their baseline hashes, and all narration/offline manifest assets exist.

Desktop light/dark layouts, a 375px embedded viewport, section/phase/reference persistence, exercise input/grade persistence, audio resume and the 1.4 node-label correction were checked through the browser. This is not a learning-outcome study or an exhaustive cross-browser/offline acceptance test. Exact slide-by-slide verification of the source ledger remains pending; original complete references stay accessible.

Lesson design uses explicit learning goals, physical explanation before formulas, worked examples and consistent diagram labels. References: [MIT worked/faded examples](https://openlearning.mit.edu/mit-faculty/research-based-learning-findings/worked-and-faded-examples), [CMU learning objectives](https://www.cmu.edu/teaching/designteach/syllabus/newcourse/learningobjectives.html), [OpenStax EMF and terminal voltage](https://openstax.org/books/university-physics-volume-2/pages/10-1-electromotive-force), [W3C interaction animation](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions).

## Downloaded lesson videos

`src/video-catalog.json` assigns fifteen downloaded 720p H.264/AAC videos to the ten Chapter 1 lessons, each video in exactly one place. There is no section-based filtering. Each full player is followed by its own definitions, rules with conditions, symbol glossary, teacher examples and common mistakes from `src/cheatsheets.json`. Local files, thumbnails, checksums and original creator/source attribution live in `dist/videos/chapter1/` in the website package. They are included, not fetched from YouTube or Khan Academy at study time.

`Videos.tsx` renders the primary full-video and cheat-sheet lesson view, with pause, speed, seeking and full screen. `chapter-one-page.txt` and `chapter-one-mount.txt` are the canonical lesson-shell fragments used by integration. Older guided explanations/diagrams and complete references remain in optional sections. Exercises use the existing separate practice route; their questions, grading and stored records are unchanged. Manual lesson-finished buttons reuse the existing reviewed-topic records and display finished marks on the chapter cards. Video watching does not set those marks. Playback positions are stored under `guided.videoLibraryV1[videoId]`, shared when the same video appears in different lessons. Refresh restores a paused position when the video is loaded. Starting another player pauses other media; closing help, changing section or leaving the page pauses playback and saves its place.

Use the portable `serve.py` to run the complete folder. It supports HTTP byte ranges, including suffix ranges and invalid-range responses, for reliable seeking. The app service worker deliberately bypasses large video requests, avoiding partial-response caching and a forced 375 MiB app-shell download. Local playback does not need internet while the local server is running; hosted-video playback still needs access to the server.

The integration check verifies all fifteen MP4 checksums and their posters in addition to the original question baseline. Actual browser playback, seeking, paused refresh/resume, player exclusivity and closing behavior were checked. No third-party content license is granted by the application code; creator/source records are retained in the media manifest.

## Chapters 2 and 3 update

All 21 lessons now use the full-video / cheat-sheet / separate-exercise structure. `src/CourseLessons.ts` and `src/course-lessons.json` add the Chapter 2/3 shells, learning goals and per-video coverage/convention guidance. The catalog includes 27 unique local videos in all. Chapters 2/3 add 12 MP4s and 12 sheets; complete retained course references and original guided figures remain optional.

After editing source: run `npm ci` if dependencies are missing, `npm run build`, then `python3 integrate-course.py /absolute/path/to/dist`. This installer updates the shared bundle, offline asset list, new course routes and optional guided mount, without rebuilding Chapter 1 or changing exercises. Use it for ongoing updates instead of the earlier `integrate.py` seeding script. Media files must already be in `dist/videos/chapter2` and `chapter3`.

`Chapters-2-3-Audit.md` records source coverage, video limitations and verification. Test results do not constitute a learning-outcome study.
