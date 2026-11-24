# Adaire New Site: Broken Sections Audit

**Site audited:** [Adaire Digital staging site](https://adairedigitaldev.adaire.dev/adaire_new/)

**Audit scope:** All 19 published WordPress pages listed in the backend, checked on the rendered front end. This was a read-only audit; no WordPress content or settings were changed.

**Context:** The site was migrated from GutenBlocks to EditorsBlocks. Findings below distinguish visibly broken or missing content from content and navigation defects that may have been carried over or are unrelated to the block migration.

## Executive summary

- **10 case-study detail pages have effectively empty main content** in the rendered page.
- **Ambulanzpartner has substantial content from unrelated projects** mixed into its case study.
- The case-study index has **incorrect, missing, or placeholder destinations** and omits several case studies that exist as published pages.
- A **placeholder footer appears across the site**, with `#` links and “Your Company” copyright text.
- Several general pages contain stale template content, duplicated or malformed text, or likely placeholder content.

## Page-by-page findings

### 1. Home

**Link:** [Home](https://adairedigitaldev.adaire.dev/adaire_new/)

**Severity: Medium**

- The “Adaire X – Our AI Powered Products” heading and following text appear split across blocks at an awkward point. The next line begins “engineering ,” with an extra space before the comma.
- A product card still uses the label “GutenBlocks” after the migration.
- The client logo area exposes figure elements without accessible labels. Verify that the logos render and have appropriate alternative text.
- The shared placeholder footer is present (see site-wide issue below).

### 2. About

**Link:** [About](https://adairedigitaldev.adaire.dev/adaire_new/about/)

**Severity: Medium**

- Six team cards display the same biography, “15 years shaping brands people remember. Leads design across every client engagement,” despite listing different roles. This appears to be copied or incorrectly bound content.
- All “View Profile” links point to `#`, so they do not open a profile.
- A stray “Drag” label appears after the team carousel.
- The shared placeholder footer is present.

### 3. Services

**Link:** [Services](https://adairedigitaldev.adaire.dev/adaire_new/services/)

**Severity: Medium**

- The Programming section repeats AI/ML-focused copy in its introduction and accordion, so the content does not describe programming distinctly.
- Missing space in “platform.Every solution”.
- Typo: “years form now” (likely “years from now”).
- The shared placeholder footer is present.

### 4. Contact

**Link:** [Contact](https://adairedigitaldev.adaire.dev/adaire_new/contact/)

**Severity: Verify / possible missing section**

- The rendered page shows an email contact, a case-studies call to action, and location accordions for Namibia, Switzerland, Germany, and Ghana. No contact form was visible. Confirm whether a form is intended for this page.
- The shared placeholder footer is present.

### 5. Case-study index

**Link:** [Case studies](https://adairedigitaldev.adaire.dev/adaire_new/case-study/)

**Severity: High**

- Visible card destinations are incorrect or placeholders:
  - Ambulanzpartner points to its matching detail page.
  - Apleona points to the Nedbank page.
  - Nedbank points to `#`.
  - Toradex points to Scoutsync.
  - INSCYD and Startup Nights point to `#`.
- The index displays six cards, while the backend contains 11 published case-study detail pages. Berg Swiss Ice Tea, Future Tree, Innovation Atelier, Physio und Sport, and Scoutsync were not represented in the rendered index.
- Intro copy runs “way.That focus” without a space after the period.
- The shared placeholder footer is present.

### 6. Ambulanzpartner

**Link:** [Ambulanzpartner case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/ambulanzpartner/)

**Severity: Critical – incorrect content**

- The project summary is about APST Research / ALS and Ambulanzpartner, but solution sections describe unrelated Masterworks fine-art investment and mobile fintech products.
- The unrelated copy includes trading art shares, an art portfolio, AWS/Node/MariaDB, and claims about a million subscribers.
- A sentence is corrupted at a content transition: “we were tasked with eThe original mobile app suffered...”
- Solution content appears duplicated and mismatched to the project. The page needs its case-study sections restored or replaced with the correct Ambulanzpartner content.
- The shared placeholder footer is present.

### 7. Apleona

**Link:** [Apleona case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/apleona/)

**Severity: Critical – blank main content**

- The page title and site header load, but the main case-study area is empty before the footer.
- The shared placeholder footer is present.

### 8. Berg Swiss Ice Tea

**Link:** [Berg Swiss Ice Tea case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/berg-swiss-ice-tea/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 9. Future Tree

**Link:** [Future Tree case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/future-tree/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 10. Innovation Atelier

**Link:** [Innovation Atelier case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/innovation-atelier/)

**Severity: Critical – blank main content**

- The page title and header load, but the main area is a large empty section before the footer.
- The shared placeholder footer is present.

### 11. INSCYD

**Link:** [INSCYD case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/inscyd-3/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 12. Nedbank

**Link:** [Nedbank case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/nedbank/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 13. Physio und Sport

**Link:** [Physio und Sport case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/physio-und-sport-2/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 14. Scoutsync

**Link:** [Scoutsync case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/scoutsync-2/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 15. Startup Nights

**Link:** [Startup Nights case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/startup-nights/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 16. Toradex

**Link:** [Toradex case study](https://adairedigitaldev.adaire.dev/adaire_new/case-study/toradex/)

**Severity: Critical – blank main content**

- No case-study content is exposed in the rendered main area; the main wrapper is effectively empty.
- The shared placeholder footer is present.

### 17. Impressum

**Link:** [Impressum](https://adairedigitaldev.adaire.dev/adaire_new/impressum/)

**Severity: No obvious page-specific break found**

- Legal entity, registration, director, address, email, and website information are present in the rendered body.
- The shared placeholder footer is present.

### 18. Privacy Policy

**Link:** [Privacy Policy](https://adairedigitaldev.adaire.dev/adaire_new/privacy-policy/)

**Severity: Medium – stale content**

- The policy refers to the old site path `https://adairedigitaldev.adaire.dev/adairemain/` instead of `/adaire_new/`.
- It contains generic policy-generator and advertising-network language that may not reflect the current site. Verify against the live privacy requirements before publishing.
- The shared placeholder footer is present.

### 19. Sample Page

**Link:** [Sample Page](https://adairedigitaldev.adaire.dev/adaire_new/sample-page/)

**Severity: Medium – default placeholder page**

- The page still contains the standard WordPress “This is an example page” copy, including instructions to delete it and create new pages.
- The shared placeholder footer is present.

## Site-wide issue: placeholder footer

**Severity: High – site-wide navigation and brand defect**

The same footer appears across the inspected pages and contains:

- Quick Links for Home, About, Services, and Contact all pointing to `#`.
- Blog, Documentation, and Support links all pointing to `#`.
- Twitter, Facebook, and LinkedIn links all pointing to `#`.
- Privacy Policy, Terms of Service, and Cookie Policy links all pointing to `#`.
- Copyright text reading “© 2024 Your Company. All rights reserved.”

Fixing the footer once in the shared template should address it across all 19 pages. The footer’s legal and policy links should also be wired to the correct destinations.

## Suggested repair order

1. Restore the missing main content on the 10 blank case-study detail pages.
2. Correct Ambulanzpartner’s mixed-in case-study content.
3. Repair case-study index card destinations and add the missing case studies to the index if they are intended to be listed.
4. Replace the shared footer placeholders and `#` destinations.
5. Correct About team biographies and profile links, then clean up Home and Services copy.
6. Confirm whether Contact needs a form; update Privacy Policy references and remove or repurpose the Sample Page.

## Audit notes

This is a rendered-front-end audit, not a source-content comparison against the former site. Empty case-study findings reflect the pages checked in the browser; wording, missing form, and missing index-card concerns should be compared with the intended design/content before final repair. The URLs above use the `/adaire_new/` staging path.
