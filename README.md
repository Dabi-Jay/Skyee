# Skyee - Dynamic Weather Application

Skyee is a responsive, modern weather application built with Django that fetches live meteorological data from the OpenWeather API. The platform features an intelligent, failure-immune backend routing system that dynamically adapts the application's landscape background based on the real-time weather conditions of the searched location.

## 🚀 Key Features

* **Live Data Sync:** Integrated with the OpenWeather API to fetch real-time temperature (Celsius), conditions, location metrics, and localized date/time tracking.
* **Dynamic Asset Pipeline:** Implements a backend mapping matrix that updates the background theme matching current weather clusters (Clear, Clouds, Rain/Thunderstorms).
* **Fail-Safe Exception Handling:** Structured with rigorous `try/except` safeguards to intercept network failures or invalid user inputs gracefully, rendering an elegant fallback UI (complete with contextual error messaging and custom asset states) rather than breaking.
* **Clean Architecture:** Written with strict separation of concerns, utilizing explicit Django context dictionary injections to feed clean, formatted values into front-end Jinja templates.

## 🛠️ Tech Stack & Dependencies

* **Backend:** Python 3.13+, Django Framework
* **Environment Management:** Pipenv (Virtual Environment)
* **Networking:** HTTP `requests` library for external REST API integration
* **Frontend:** Semantic HTML5, CSS3 (Glassmorphism UI styling), Vanilla JS for trigger alerts

---

## 💻 Code Architecture Overview

The core engine resides within a centralized controller view (`views.py`). Here is a high-level logical breakdown of how the application lifecycle processes data:
