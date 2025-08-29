---

# 🪄 Text/Markdown → PowerPoint Web App

**Your Text, Your Style**
Turn long-form text, markdown, or prose into a fully styled PowerPoint presentation — powered by your favorite LLM and your own branded `.pptx/.potx` templates.

---

## 📌 Overview

This app allows anyone to generate a downloadable PowerPoint presentation from large blocks of text or markdown. Simply paste your content, upload a `.pptx` or `.potx` file as a style guide, and let your LLM of choice turn the content into structured slides — styled to match your template.

### ✨ Key Features

* ✅ Paste raw text or markdown
* ✅ Optional tone/guidance (e.g., “turn into an investor pitch deck”)
* ✅ Upload your `.pptx` or `.potx` file to match slide styles, fonts, and layout
* ✅ Bring your own LLM API key (OpenAI, Anthropic, Gemini, etc.)
* ✅ No AI-generated images — existing template images are reused
* ✅ Final output: downloadable, styled `.pptx` file

---

## 🛠️ How It Works

1. **Text Parsing:**
   Input text is analyzed and broken into logical slide sections.

2. **Structure Mapping:**
   LLM maps sections into title/content slides based on tone/guidance.

3. **Template Styling:**
   Fonts, colors, layouts, and images are extracted from your uploaded `.pptx/.potx` and applied to generated slides.

4. **Output Generation:**
   A downloadable PowerPoint (`.pptx`) file is created — no images generated with AI, just clean slides in your style.

---

## 🚀 Run Locally

### 1. Clone & set up environment:

```bash
git clone https://github.com/your-username/text-to-ppt-app.git
cd text-to-ppt-app
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the app:

```bash
uvicorn app.main:app --reload
```

### 4. Open your browser:

```
http://localhost:8000
```

---

## 🔐 Security

* Your **LLM API keys are never stored or logged**
* Uploads are used in-memory and not saved
* Only templates you upload are used for style — no external AI image generation

---

## 📂 Project Structure

```
text-to-ppt-app/
├── app/
│   ├── main.py            # FastAPI app entry point
│   ├── parser.py          # Text → slide structure logic
│   ├── ppt_generator.py   # Slide generation and styling
│   └── templates/         # HTML frontend (if applicable)
├── static/                # Optional frontend assets
├── requirements.txt
└── README.md
```

---

## 🧠 Optional Enhancements (Bonus)

* Auto-generate speaker notes
* Slide preview before download
* Preset guidance templates (e.g., “Sales Deck”, “Academic Summary”)
* Advanced error handling and retry logic

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙌 Contributing

PRs and issues are welcome! Please ensure code is clean, documented, and tested.

---
