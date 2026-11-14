<div align="center">
  <img src="./assets/header.svg" width="100%" alt="Mao Seavik — AI Engineer & Backend Software Developer" />
  <br />
  <br />
  <p>
    <a href="https://seavik-gamma.vercel.app/">
      <img src="https://img.shields.io/badge/Portfolio-seavik--gamma.vercel.app-18181B?style=for-the-badge&logo=vercel&logoColor=FAFAFA&labelColor=09090B" alt="Portfolio" />
    </a>
    <a href="https://huggingface.co/Maoseavik">
      <img src="https://img.shields.io/badge/Hugging_Face-@Maoseavik-18181B?style=for-the-badge&logo=huggingface&logoColor=FACC15&labelColor=09090B" alt="Hugging Face" />
    </a>
    <a href="https://www.linkedin.com/in/mao-seavik-003a0a372">
      <img src="https://img.shields.io/badge/LinkedIn-Mao_Seavik-18181B?style=for-the-badge&logo=linkedin&logoColor=38BDF8&labelColor=09090B" alt="LinkedIn" />
    </a>
    <img src="https://komarev.com/ghpvc/?username=Seavik2142&style=for-the-badge&color=27272A&labelColor=09090B&label=PROFILE+VIEWS" alt="Profile Views" />
  </p>
</div>

---

### Overview

I am an **AI Engineer and Backend Software Developer** based in Phnom Penh, Cambodia, currently pursuing a B.Sc. in Computer Studies at **Norton University**. My work centers on adapting open-source language models for domain-specific reasoning and building production web and mobile software.

- **LLM Fine-Tuning & Inference:** Supervised fine-tuning (`SFT` / `TRL`), parameter-efficient adapters (`PEFT` / `LoRA`), and quantized `GGUF` deployments on `Qwen2.5` architectures.
- **Backend & API Systems:** Asynchronous REST APIs, relational data modeling, and service integrations built with `Python`, `FastAPI`, `Flask`, and `PostgreSQL`.
- **Full-Stack & Mobile Engineering:** Modern web dashboards, Telegram Mini Apps, and cross-platform mobile applications using `TypeScript`, `React`, `Next.js`, and `Flutter`.

---

### Published Language Models ([Hugging Face · `@Maoseavik`](https://huggingface.co/Maoseavik))

| Model Repository | Base Architecture | Method & Format | Domain Application |
| :--- | :--- | :--- | :--- |
| [**`Maoseavik/agri-qwen3b-lora`**](https://huggingface.co/Maoseavik/agri-qwen3b-lora) | `Qwen/Qwen2.5-3B-Instruct` | `SFT · TRL · LoRA` | Crop disease diagnosis, treatment planning & agricultural Q&A |
| [**`Maoseavik/agrisystem-qwen2.5-3b-gguf`**](https://huggingface.co/Maoseavik/agrisystem-qwen2.5-3b-gguf) | `Qwen/Qwen2.5-3B-Instruct` | `Quantized GGUF` | Low-latency CPU and edge inference via `llama.cpp` & Ollama |
| [**`Maoseavik/agrisystem-qwen2.5-3b-adapter`**](https://huggingface.co/Maoseavik/agrisystem-qwen2.5-3b-adapter) | `Qwen/Qwen2.5-3B-Instruct` | `PEFT Adapter` | Structured symptom-to-treatment agricultural reasoning |
| [**`Maoseavik/agri-expert-adapter`**](https://huggingface.co/Maoseavik/agri-expert-adapter) | `Qwen/Qwen2.5-1.5B-Instruct` | `PEFT · SafeTensors` | Compact conversational assistant for resource-constrained hardware |

---

### Selected Engineering Projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/Seavik2142/ChhlatAI">ChhlatAI</a> — Conversational Commerce &amp; Copilot Inbox</h4>
      <p>Unified social-commerce CRM connecting Telegram, Messenger, Instagram, and TikTok with <b>Google Gemini</b> agents, automated Bakong KHQR invoicing, and receipt verification.</p>
      <p><code>TypeScript</code> <code>Python</code> <code>FastAPI</code> <code>Google Gemini</code> <code>React</code> <code>PostgreSQL</code> <code>Docker</code></p>
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://agricultureexp.space">AgriSystem AI</a> — Agricultural Expert System</h4>
      <p>Bilingual (Khmer/English) agricultural advisory platform powered by custom fine-tuned <b>Qwen2.5-3B LoRA &amp; GGUF</b> models with symptom matching and localized weather risk alerts.</p>
      <p><code>Python</code> <code>Qwen2.5-3B</code> <code>PEFT / LoRA</code> <code>Flask</code> <code>PostgreSQL</code> <code>Hugging Face</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/Seavik2142/mini_app">Digital Keys PRO</a> — Telegram Mini App Storefront</h4>
      <p>High-speed Telegram WebApp storefront engineered for instant digital software key provisioning, automated inventory management, and seamless checkout. <a href="https://mini-app-alpha-roan.vercel.app">Live Demo ↗</a></p>
      <p><code>TypeScript</code> <code>React</code> <code>Node.js</code> <code>Telegram SDK</code> <code>PostgreSQL</code> <code>Docker</code></p>
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/Seavik2142/driving-system">Driving License Prep</a> — Mobile Examination Suite</h4>
      <p>Cross-platform mobile learning and mock-examination application built with Flutter and Dart to practice traffic rules, road signs, and timed theory tests.</p>
      <p><code>Flutter</code> <code>Dart</code> <code>Mobile UI</code> <code>Cross-Platform</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/Seavik2142/ksnmusic">KSN Music</a> — Audio Streaming Platform</h4>
      <p>Full-stack web audio streaming application built with Laravel and modern JavaScript, featuring smart playlists, persistent playback controls, and catalog indexing.</p>
      <p><code>Laravel</code> <code>PHP</code> <code>JavaScript</code> <code>Tailwind CSS</code> <code>MySQL</code></p>
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/Seavik2142/School_Manage">Academic &amp; Property Management Systems</a></h4>
      <p>Administrative software suites engineered with Python and PostgreSQL to streamline student records, scheduling, billing, and property operations.</p>
      <p><code>Python</code> <code>JavaScript</code> <code>PostgreSQL</code> <code>PL/pgSQL</code> <code>REST API</code></p>
    </td>
  </tr>
</table>

---

### Technical Stack

| Domain | Technologies & Tools |
| :--- | :--- |
| **AI & Machine Learning** | ![PyTorch](https://img.shields.io/badge/PyTorch-18181B?style=flat-square&logo=pytorch&logoColor=EE4C2C) ![Hugging Face](https://img.shields.io/badge/Hugging_Face-18181B?style=flat-square&logo=huggingface&logoColor=FACC15) ![Transformers](https://img.shields.io/badge/Transformers-18181B?style=flat-square&logo=huggingface&logoColor=FACC15) ![PEFT / LoRA](https://img.shields.io/badge/PEFT_%C2%B7_LoRA_%C2%B7_TRL-18181B?style=flat-square) ![Google Gemini](https://img.shields.io/badge/Google_Gemini-18181B?style=flat-square&logo=googlegemini&logoColor=8E75B2) ![Qwen2.5](https://img.shields.io/badge/Qwen2.5_%C2%B7_GGUF-18181B?style=flat-square) |
| **Backend & APIs** | ![Python](https://img.shields.io/badge/Python-18181B?style=flat-square&logo=python&logoColor=3776AB) ![FastAPI](https://img.shields.io/badge/FastAPI-18181B?style=flat-square&logo=fastapi&logoColor=009688) ![Flask](https://img.shields.io/badge/Flask-18181B?style=flat-square&logo=flask&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-18181B?style=flat-square&logo=nodedotjs&logoColor=339933) ![Laravel](https://img.shields.io/badge/Laravel-18181B?style=flat-square&logo=laravel&logoColor=FF2D20) ![PHP](https://img.shields.io/badge/PHP-18181B?style=flat-square&logo=php&logoColor=777BB4) |
| **Frontend & Mobile** | ![TypeScript](https://img.shields.io/badge/TypeScript-18181B?style=flat-square&logo=typescript&logoColor=3178C6) ![JavaScript](https://img.shields.io/badge/JavaScript-18181B?style=flat-square&logo=javascript&logoColor=F7DF1E) ![React](https://img.shields.io/badge/React-18181B?style=flat-square&logo=react&logoColor=61DAFB) ![Next.js](https://img.shields.io/badge/Next.js-18181B?style=flat-square&logo=nextdotjs&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-18181B?style=flat-square&logo=flutter&logoColor=02569B) ![Dart](https://img.shields.io/badge/Dart-18181B?style=flat-square&logo=dart&logoColor=0175C2) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-18181B?style=flat-square&logo=tailwindcss&logoColor=06B6D4) |
| **Data & Infrastructure** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18181B?style=flat-square&logo=postgresql&logoColor=4169E1) ![MySQL](https://img.shields.io/badge/MySQL-18181B?style=flat-square&logo=mysql&logoColor=4479A1) ![Docker](https://img.shields.io/badge/Docker-18181B?style=flat-square&logo=docker&logoColor=2496ED) ![Git](https://img.shields.io/badge/Git-18181B?style=flat-square&logo=git&logoColor=F05032) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-18181B?style=flat-square&logo=githubactions&logoColor=2088FF) |

---

### Experience & Recognition

- **Backend Software Engineering Intern** — *KRU IT Solution & ETEC Center* (2026)  
  Engineered backend API services, relational database schemas, and server-side workflows within an agile engineering team.
- **Team Lead — AI Expert System & Innovation** — *Norton University · Dept. of Computer Studies* (2026)  
  Led a 4-member student engineering team across dataset curation, Qwen2.5-3B LoRA fine-tuning, and full-stack deployment for the bilingual Agriculture Expert System.
- **B.Sc. in Computer Studies (Software Development)** — *Norton University, Cambodia* (2023 – Present)  
  Awarded Foundation Year Certificate with distinguished standing; coursework in Artificial Intelligence, Software Architecture, and Distributed Systems.

---

### GitHub Activity & Telemetry

<div align="center">
  <img width="49%" src="https://raw.githubusercontent.com/Seavik2142/Seavik2142/main/profile-summary-card-output/tokyonight/1-repos-per-language.svg" alt="Repos Per Language" />
  <img width="49%" src="https://raw.githubusercontent.com/Seavik2142/Seavik2142/main/profile-summary-card-output/tokyonight/4-productive-time.svg" alt="Productive Time" />
</div>

<div align="center">
  <img width="100%" src="https://raw.githubusercontent.com/Seavik2142/Seavik2142/main/profile-summary-card-output/tokyonight/0-profile-details.svg" alt="GitHub Profile Summary" />
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Seavik2142/Seavik2142/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Seavik2142/Seavik2142/output/github-snake.svg" />
    <img alt="GitHub Contribution Snake" src="https://raw.githubusercontent.com/Seavik2142/Seavik2142/output/github-snake.svg" width="100%" />
  </picture>
</div>
