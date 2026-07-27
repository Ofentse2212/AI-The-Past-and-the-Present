# Conversational AI Evolution Lab

A side-by-side exploration of how conversational AI evolved from rule-based pattern matching to modern generative language models.

This Python project compares **ELIZA**, an early rule-based chatbot, with **Qwen2.5-0.5B-Instruct**, a compact large language model accessed through Hugging Face Transformers. A Tkinter interface lets both systems answer the same prompt so their different approaches are easy to observe.

## Why this project matters

Understanding how AI systems produce answers is important when building technology that people can trust. This project turns that history into an interactive learning experience: ELIZA follows explicit patterns and reflections, while the language model generates responses from learned statistical relationships.

It began as a class project and grew into a practical demonstration of responsible, human-centred AI design.

## What it demonstrates

- Rule-based natural-language processing with NLTK's ELIZA patterns
- Transformer-based text generation with Qwen2.5
- A side-by-side desktop interface built with Tkinter
- Background processing to keep the interface responsive while the model generates
- Clear comparison of deterministic rules and probabilistic generation

## Technology

- Python
- Tkinter
- NLTK
- Hugging Face Transformers
- PyTorch
- Qwen2.5-0.5B-Instruct

## Getting started

### 1. Create a virtual environment

~~~bash
python -m venv .venv
source .venv/bin/activate
~~~

On Windows:

~~~powershell
.venv\Scripts\activate
~~~

### 2. Install the dependencies

~~~bash
pip install -r requirements.txt
~~~

### 3. Run the comparison interface

~~~bash
python chat_comparison.py
~~~

The language model is downloaded the first time the application runs. Generation can be slower on a computer without a compatible GPU.

## Project structure

| File | Purpose |
| --- | --- |
| `chat_comparison.py` | Tkinter interface that displays both chatbot responses |
| `LLM.py` | Loads Qwen2.5 and generates modern LLM responses |
| `eliza.py` | Defines the rule-based ELIZA conversation patterns |
| `requirements.txt` | Lists the Python dependencies |

## Responsible-use note

This is an educational comparison, not a therapy, counselling, or advice service. Both systems can produce unhelpful or incorrect responses. Do not enter private or sensitive information, and do not rely on the output for medical, financial, legal, or safety decisions.

## Future improvements

- Add response-time and response-quality comparisons
- Move model loading into a visible startup state
- Add conversation export for classroom analysis
- Include more rule-based and open-source language models
- Add automated tests for ELIZA patterns and interface logic

## Author

Built by **Ofentse** as part of a growing portfolio focused on practical technology, responsible AI, and solutions with social impact.
