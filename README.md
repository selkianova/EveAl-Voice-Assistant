# EveAl Voice Assistant

A Python-based voice assistant designed to process spoken input, execute local system commands, and generate natural language responses using the ChatGPT API. 

## Features
* **Natural Language Processing:** Integrates OpenAI's ChatGPT API for dynamic, conversational responses.
* **Speech-to-Text & Text-to-Speech:** Processes voice input and responds with synthesized speech.
* **System Automation:** Includes rule-based commands for executing local tasks, such as launching applications and opening specific web pages.
* **Time-Based Operations:** Capable of handling time-sensitive queries and task responses.

## Tech Stack
* **Language:** Python
* **Integrations:** OpenAI API (ChatGPT)
* **Core Concepts:** API Integration, Automation, Natural Language Generation

## Project History & Legacy
*I originally conceptualized and built the core of EveAl in late 2023 / early 2024 using the legacy `text-davinci-003` engine, long before native voice-assistant features were widely integrated into commercial LLMs. Recently, I have refactored and updated the codebase to support the modern `openai >= 1.0.0` client architecture and `gpt-3.5-turbo` models to maintain performance and modern API standards.*
