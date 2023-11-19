import re

contraction_map = {
    "n't": "not",
    "'ve": "have",
    "'ll": "will",
    "'m": "am",
    "d'": "did",
    "re": "are",
    "'s": "is",
    "ca": "can",
}

def expand_contractions(text):
    pattern = r"(.*?)([n't|'ve|'ll|'m|d'|re|'s|ca])"
    expanded_text = re.sub(pattern, r"\1\2", text)
    return expanded_text

def expand_contractions(text, contraction_map):
    for contraction, expansion in contraction_map.items():
        text = text.replace(contraction, expansion)
    return text