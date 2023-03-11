def pattern_search(text: str, pattern: str) -> str:
    """Naive pattern search used to find a pattern within string.
    Performance is O(nk) -> "n" for input length times "k" for pattern length. Can
    approach O(n^2) if pattern not found (run through whole input times input iterations).
    """

    for index in range(len(text)):
        match_count = 0
        for char in range(len(pattern)):
            if pattern[char] == text[index + char]: # cycle through text with index as offset
                match_count += 1

            else:  # break inner for loop at first mismatch character
                break

        if match_count == len(pattern):
            return f'{pattern} found at index {index}'

    return 'pattern not found'