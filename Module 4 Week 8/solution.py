"""Instructor solution for the Mini-RAG input guardrail activity."""

import re

MIN_QUERY_CHARS = 3
MAX_QUERY_CHARS = 200
MAX_QUERY_WORDS = 30

INJECTION_PATTERNS = [
    r"ignore (all |any )?(previous|prior|above) (instructions|prompts?)",
    r"disregard (all |any )?(previous|prior|above)",
    r"reveal (your |the )?(system )?prompt",
    r"you are now\b",
]


class InvalidQueryError(ValueError):
    """Raised when a question should not continue to the RAG system."""


def validate_query(query: str) -> str:
    """Return a cleaned question, or raise InvalidQueryError explaining why not."""
    if not isinstance(query, str):
        raise InvalidQueryError("Query must be text.")

    query = "".join(character for character in query if character.isprintable() or character in "\t\n ")
    query = " ".join(query.split())

    if not query:
        raise InvalidQueryError("Please enter a question.")
    if len(query) < MIN_QUERY_CHARS:
        raise InvalidQueryError(
            f"Question is too short (minimum {MIN_QUERY_CHARS} characters)."
        )
    if len(query) > MAX_QUERY_CHARS:
        raise InvalidQueryError(
            f"Question is too long ({len(query)} characters, maximum {MAX_QUERY_CHARS})."
        )
    if len(query.split()) > MAX_QUERY_WORDS:
        raise InvalidQueryError(
            f"Question has too many words (maximum {MAX_QUERY_WORDS})."
        )
    if not re.search(r"[a-zA-Z0-9]", query):
        raise InvalidQueryError("Question must contain letters or numbers.")

    lowered = query.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, lowered):
            raise InvalidQueryError(
                "That looks like an attempt to override instructions. "
                "Please ask a question about the documents."
            )

    return query
