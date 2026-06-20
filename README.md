# B2B SaaS Growth & Research Portfolio

This repository contains my portfolio assignments for the 100Hires selection process, demonstrating automated research pipelines, high-signal data synthesis, and proficiency with AI-assisted development tools (Cursor, Claude Code, Codex).

---

## 🚀 Part 2: Cold Outreach Pipeline for B2B SaaS (Research Project)

### 🎯 Chosen Topic
I selected **Cold Outreach Pipeline for B2B SaaS**. In modern B2B growth, outbound acquisition is no longer a game of spamming high volume; it requires highly sophisticated data engineering, deliverability isolation, and rigorous copywriting frameworks to extract market signals.

### 🧠 Why I Chose These Experts (Selection Rationale)
Instead of relying on top Google search results or generic marketing influencers, I strictly curated practical experts based on two core criteria: **Software Authorship** and **Active Client Execution**.
* **Guillaume Moubeche:** As the founder of Lemlist, his insights come from processing millions of outbound emails daily. His focus on "signal over polish" provides the foundational execution framework for early-stage B2B SaaS validation.
* **Eric Nowoslawski:** As the founder of GrowthX, he is at the absolute bleeding edge of programmatic outbound. His technical breakdown of using Clay for data enrichment and his innovative 4-batch inbox diversification strategy represent the modern playbook for zero-spam delivery.
* **Nick Abraham:** Founder of Inbound Leadership (OutboundPhD), he bridges the gap between complex technical setups (SPF/DKIM/DMARC) and deep customer resonance.

### 📁 What Was Collected & Repository Structure
The extracted knowledge base is organized anatomically to ensure modularity and ease of reference:
* **`/research/sources.md`**: The annotated master bibliography containing verified links, collection dates, and core focus areas for all 10 curated practitioners.
* **`/research/linkedin-posts/`**: Deep-dives into raw, high-signal tactical posts, separated by author:
  * `guillaume_moubeche_1.md` & `_2.md`: Documentation on outbound fundamentals, early validation, and utilizing public content streams as execution mentors.
  * `eric_nowoslawski_1.md` & `_2.md`: Granular analysis of hybrid Google/Outlook 4-batch deliverability setups and the 4 tactical tiers of AI-generated emails.
  * `nick_abraham.md`: Case study on aligning data enrichment with 80% customer resonance.
* **`/research/youtube-transcripts/`**: Technical video breakdowns and script automation targets.

### 🛠️ Data Collection Methodology
* **LinkedIn Data (Manual Curation):** To satisfy the manual collection guidelines, I hand-picked organic, non-fluff posts. This approach avoids the immediate risk of IP/Account suspensions associated with aggressive LinkedIn anti-scraping firewalls within a short 48-hour window.
* **YouTube Data (API Integration):** Programmatic retrieval utilizing the `youtube-transcript-api` to pull raw video text without relying on heavy third-party scraper overhead.

---

## 🛠️ Part 1: Initial Environment & Tools Setup

### Tools Configured
* **Cursor IDE:** Deployed as the core workspace environment.
* **Claude Code & Codex Add-ons:** Configured within the extensions layer to handle rapid contextual scripting.

### Issues Resolved During Setup
* **Terminal Cross-Compatibility:** Resolved native PowerShell command binding errors (e.g., `touch` or `mkdir -p` restrictions on Windows systems) by utilizing explicit `New-Item` Directory and File cmdlets to safely construct the repository's architecture.