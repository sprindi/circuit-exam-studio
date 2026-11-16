# Circuit Exam Studio

A self-contained study website with reading material, practice exercises, and a remembered light/dark theme. Progress stays in your browser.

## Run locally

Requires Python 3. From this folder, run:

```sh
python3 serve.py --port 8765
```

Then open http://127.0.0.1:8765/ . On Windows, use `py` instead of `python3`.

## Files and deployment

`dist/` contains the complete website: editable HTML, CSS, JavaScript, and study content. No dependency installation or build is required. Serve `dist/` with any static website host.

For Vercel, import this repository, choose Other as the framework, leave the build command empty, and set the output directory to `dist`.

## Content

The study material is based on course documents or a supplied textbook. Original third-party material retains its respective ownership; this repository does not grant a license to that material.

## Chapter 1 teaching

The main lesson flow is **full video → its cheat sheet → separate exercises**. Fifteen downloaded videos are assigned to the ten teacher topics, each video appearing in exactly one lesson. The sheet directly below each player contains definitions, rules and conditions, symbol meanings, teacher examples and common mistakes. There is no filtering by the explanation section currently being read.

Mark **Lesson finished** manually. That mark is saved and appears on the chapter cards; it is separate from playback position and practice scores. Previous reviewed-topic marks are retained. Exercises open through clear topic-specific links and have a return link to the lesson. The original 14 Chapter 1 questions, grading and stored records are unchanged.

All original reviewed lesson text remains in expandable references. Optional guided explanations and diagrams are also retained: the redesigned foundations in 1.1–1.3 and the existing cases in later lessons. This layout change is not a claim of a new page-by-page verification of every original slide.

For rebuilding, see `authoring/foundations/README.md`. The built `dist/` and supplied Python server run immediately without JavaScript build tools.

## Saved work

IndexedDB stores review marks, practice scores, unfinished question order and inputs, checked feedback, lab values for both models, lesson positions, narration steps and positions, prediction answers, display preferences, and the exam checklist. An immediate local browser backup supports recovery when IndexedDB is unavailable. The save indicator reports actual completed database writes. Existing browser review records are migrated when available.

Use **Export backup** and **Import backup** to transfer progress between browsers, computers, or website addresses. Progress belongs to one browser and site address; it is not a shared account database. Browser-data deletion and private browsing can remove local storage. **Protect saved work** requests persistent storage, subject to the browser's decision.

Guided examples pair verbal descriptions with diagrams and worked examples, informed by the [IES study guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1). They are prepared study aids, not automatically generated tutoring or a claim of validated learning outcomes.

## Downloaded video help

All 21 lessons now have dedicated local videos with their cheat sheets underneath and exercises in a separate section. Chapter 1 is preserved; Chapters 2 and 3 add 12 videos, preparation/goals, rules with conditions, full symbol meanings and worked course examples. Original detailed references and guided explanations remain available in optional sections.

All 27 videos, posters, creator/source records and checksums are included in `dist/videos/chapter1`, `chapter2` and `chapter3` (about 620 MiB of video). Use `python3 serve.py --port 8765` and open http://127.0.0.1:8765/. No JavaScript build tools or extra Python packages are needed to study. The server supports byte ranges for seeking. Playback positions and manual lesson-finished marks stay saved in this browser/site address. Exercises and grading are unchanged.

To edit and rebuild, see `authoring/foundations/README.md`. The content/video review and verification boundaries are recorded in `authoring/foundations/Chapters-2-3-Audit.md`.
