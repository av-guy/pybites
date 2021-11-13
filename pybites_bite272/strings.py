from typing import List
from collections import Counter


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    words = {}
    for word in sentence1:
        value = words.setdefault((lowered := word.lower()), 1)
        if word in sentence2 or lowered in sentence2:
            value += 1
        words[lowered] = value
    return [item for item in sorted(
        [values[0] for values in sorted(words.items(), key=lambda item: item[1], reverse=True)][:2],
        key=len
    ) if words[item] > 1]
