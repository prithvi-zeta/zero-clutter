# Platforms

Zero Clutter runs on anything with a user interface: native apps, Flutter,
web apps and websites, from code, a running build, a URL, a screenshot or a
Figma frame. The principles don't change; how you collect evidence, and a
few checks, do. The project's `.zero-clutter/adapter.md` overrides anything
here.

## Find the platform

| You see | Platform |
| --- | --- |
| `pubspec.yaml` with `flutter:` | Flutter |
| `*.xcodeproj`, `Package.swift`, SwiftUI or UIKit files | iOS native |
| `build.gradle(.kts)` with `com.android.application`, Compose or XML layouts | Android native |
| `package.json` with React, Next, Vue, Svelte, Angular; an app behind sign-in | Web app |
| Marketing or content pages: Next/Astro/Gatsby sites, WordPress, Webflow, plain HTML, or a public URL | Website |
| Only a screenshot, mock or Figma frame | Judge the picture; take the platform from the frame size or what the person says |

A repo can hold several (an app plus a web funnel); judge each change on its
own platform.

## Evidence by platform

| | Flutter | iOS native | Android native | Web app / website |
| --- | --- | --- | --- | --- |
| Screenshot (SHOT) | widget-test capture or simulator/emulator | Simulator (`xcrun simctl io <id> screenshot`) | Emulator (`adb exec-out screencap -p`) | Browser at 390×844 and 1440×900 (Playwright or the browser tool) |
| Smallest size (COMPACT) | 375×667 | iPhone SE (375×667) | 360×640 | 320px wide, and 200% zoom |
| Large text | text scaler 1.3+ | Dynamic Type XXL and an accessibility size | font scale 1.3+ | browser zoom 200%, text-only zoom |
| Motion (FRAMES) | widget-test frames or a recording | Simulator recording | `adb shell screenrecord` | browser recording or a trace |
| Contrast, accessibility | measure from the SHOT | Accessibility Inspector | Accessibility Scanner | axe or Lighthouse accessibility |
| Speed (FB, under 100ms) | widget test or a profile build | Instruments | Profiler | Lighthouse / Web Vitals (INP under 200ms, LCP under 2.5s) |
| Haptics and sound | device | device | device | n/a for websites; vibration only if the web app uses it |

When you can't run anything (only a picture), mark the capture-based checks
`pending` and name the capture needed.

## Checks that change by platform

- **Native and Flutter (phone):** safe areas and the home indicator; Dynamic
  Type / font scale; the platform's back gesture and system sheets keep their
  meaning (MENT-02); haptics on taps and completions (FB-01, SENSE-02); tap
  targets at least 44pt (iOS) or 48dp (Android).
- **Web apps:** every control works by keyboard with a visible focus ring;
  hover is never the only way to find something; layouts hold from 320px to
  wide screens; form fields use the right `type` and `autocomplete` (DEF-05);
  no surprise reloads that lose input (PROG-07); haptics items are usually n/a.
- **Websites:** one primary action per page or section (ZCL-02); the
  headline says the one thing (HIER-01, CLUT-01); no carousels or popups that
  block the content; pages load fast (FB items via Web Vitals); copy checked
  as hard as in the app (WORD items). Senses items apply to motion and
  completion moments only (sign-up done, form sent).
- **Everything:** contrast against the worst real background, in light and
  dark themes (HIER-05); one value per fact everywhere (CONS-07); copy word
  for word from the source (HR-04).

When an item doesn't apply to the platform, it's `n/a` with the reason
("website: no haptics").
