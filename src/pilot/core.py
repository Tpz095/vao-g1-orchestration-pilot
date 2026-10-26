"""Baseline behavior. A-001 and A-002 will extend this module."""


def normalize_label(text: str) -> str:
    """Return a trimmed, lowercase label with inner whitespace collapsed to single hyphens."""
    return "-".join(text.strip().lower().split())
