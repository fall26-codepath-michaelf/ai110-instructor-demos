"""Input guardrail scaffold for the Mini-RAG demo.

Students: ask an LLM to help you complete each TODO, then test each rule in
the terminal. This file checks a question before the retriever uses it.
"""

import re

MIN_QUERY_CHARS = 3
MAX_QUERY_CHARS = 200
MAX_QUERY_WORDS = 30

INJECTION_PATTERNS = [
    r"ignore (all |any )?(previous|prior|above) (instructions|prompts?)",
    r"disregard (all |any )?(previous|prior|above)",
    r"reveal (your |the )?(system )?prompt",
    r"you are now\\b",
]


class InvalidQueryError(ValueError):
    """Custom error used by validate_query. No changes are needed for this class."""


def validate_query(query: str) -> str:
    """Return a cleaned question or raise InvalidQueryError with a clear reason.

    Parameters:
        query: The raw question entered by a user.

    Returns:
        The cleaned question when it passes every guardrail.

    Raises:
        InvalidQueryError: If the question is invalid or appears to override
            the demo's instructions.
    """
    # TODO 1: Reject values that are not strings.

    # TODO 2: Remove control characters and collapse repeated whitespace.

    # TODO 3: Reject an empty question.

    # TODO 4: Enforce MIN_QUERY_CHARS, MAX_QUERY_CHARS, and MAX_QUERY_WORDS.

    # TODO 5: Reject questions with no letters or numbers.

    # TODO 6: Check the cleaned, lowercased question against every pattern in
    # INJECTION_PATTERNS. Raise InvalidQueryError when a pattern matches.

    # TODO 7: Return the cleaned question when it passes all checks.
    raise NotImplementedError("Complete the guardrail TODOs before running the demo.")
