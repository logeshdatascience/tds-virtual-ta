# 🎓 Virtual TA API – IITM Online BSc (TDS Jan 2025)

A FastAPI-based virtual teaching assistant that responds to student questions using information from TDS course content and Discourse posts.

---

## 📌 Features

- Accepts questions via `POST /api/` with optional base64 image attachments.
- Returns a relevant answer and related Discourse links (if known).
- Built using FastAPI, deployed publicly.
- Handles text questions and specific predefined cases (extendable).

---

## 📬 Example Request

```bash
curl "https://your-api-url.com/api/" \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Should I use gpt-4o-mini or gpt3.5 turbo?\"}"
