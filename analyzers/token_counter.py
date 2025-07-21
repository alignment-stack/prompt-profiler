import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize import word_tokenize
from collections import Counter
import math

def analyze_tokens(text):
    words = word_tokenize(text)
    token_count = len(words)
    char_count = len(text)
    unique_words = set(words)
    redundancy = round((token_count - len(unique_words)) / token_count * 100, 2) if token_count else 0
    word_freq = Counter(words)
    probs = [freq / token_count for freq in word_freq.values()]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    efficiency = round(token_count / (entropy + 1), 2) if entropy else 0
    return {
        'words': words,
        'token_count': token_count,
        'char_count': char_count,
        'unique_word_count': len(unique_words),
        'redundancy_percent': redundancy,
        'entropy': round(entropy, 3),
        'efficiency': efficiency
    }
