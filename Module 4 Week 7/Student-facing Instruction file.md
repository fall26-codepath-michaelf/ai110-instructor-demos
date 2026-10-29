# Mini-RAG Demo

A simple demonstration of Retrieval-Augmented Generation (RAG) that showcases the difference between vanilla AI responses and grounded, context-aware answers.

## Overview

This application demonstrates a basic RAG system that:

- Loads documents from a local folder
- Retrieves relevant documents based on user queries
- Provides both vanilla AI answers and grounded answers using retrieved context
- Shows how retrieval improves answer quality and accuracy

## Features

- **Document Loading**: Automatically loads text documents from the `sample_docs/` folder
- **Simple Retrieval**: Uses keyword-based scoring to find relevant documents
- **Dual Response Mode**:
  - Vanilla answers without context
  - Grounded answers using retrieved documents
- **Interactive CLI**: Easy-to-use command-line interface

## Student Setup

1. Open this project in VS Code.
2. Open a terminal and `cd` into the project folder.
3. Open `sample_docs/mock_syllabus.txt`, `sample_docs/faq.txt`, and `retriever.py` in your editor.
4. Open ChatGPT in a browser tab.
5. Confirm the demo runs:

```bash
python demo.py
```

When prompted, type `password`.

Successful output should include:

```text
Welcome to the Mini-RAG Demo.
--- Without Retrieval (Vanilla AI) ---
--- Retrieving Context ---
--- With Retrieval (Grounded Answer) ---
```

## Steps

1. Look at `mock_syllabus.txt` in your editor.
2. Switch to the ChatGPT browser tab. Ask:

- `When is the final exam for CS 101 at College University, Summer 2025?`
- `What is the late policy for CS 101?`

Notice whether it guesses, asks for context, or refuses to answer. Compare that with the document-grounded answer in the next step.

3. Switch to the terminal. Run:

```bash
python demo.py
```

When prompted, type:

```text
When is the final exam?
```

Expected result: the grounded answer should reference `mock_syllabus.txt` and identify the final exam as **Thursday, July 31**.

Your grounded-answer section should include text similar to:

```text
--- With Retrieval (Grounded Answer) ---
Answer based on retrieved docs for 'When is the final exam?':
- From mock_syllabus.txt (...): ...Final Exam: Thursday, July 31...
```

Reflect on your own: Did the answer without retrieval provide that course-specific date? What text in the syllabus supports the grounded answer?

4. Run the demo again:

```bash
python demo.py
```

When prompted, type:

```text
How do I reset my password?
```

Expected result: the grounded answer should reference `faq.txt` and explain that password-reset links expire after **15 minutes** and require email verification.
5. Switch to `retriever.py` in your editor. The current `retrieve()` function splits the query into words and counts matches — but it counts *every* word, including common ones.

**Step 1:** Add a stopword set above the `retrieve` function:

```python
STOPWORDS = {"a", "an", "the", "is", "are", "was", "were", "do", "does",
             "how", "what", "when", "where", "which", "who", "why",
             "i", "my", "me", "you", "your", "it", "its", "this", "that",
             "in", "on", "at", "to", "for", "of", "by", "with", "from"}
```
**Step 2:** Replace the first line inside `retrieve()`:

```python
# Before:
query_words = query.lower().split()

# After:
query_words = [w for w in query.lower().split() if w not in STOPWORDS]
if not query_words:
    query_words = query.lower().split()
```

**Step 3:** Save the file. Run `python demo.py` again.

When prompted, type:

```text
When is the final exam?
```

Expected result: `mock_syllabus.txt` should still be retrieved, while unrelated results caused by common query words should be less likely to appear.

## End of Activity

You have completed the Mini-RAG demo. You compared an answer without documents to a grounded answer, then improved retrieval by filtering common words.
