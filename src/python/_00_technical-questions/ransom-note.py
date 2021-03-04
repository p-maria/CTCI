import doctest


# ---------------------------------------------------------------------
# Approach 1: Frequency Counter. Time: O(n + m).                    ***
# ---------------------------------------------------------------------
def solution(magazine: str, note: str) -> bool:
    """Return True if note can be constructed from magazine.

    Preconditions:
        magazine and note consist of lowercase English letters

    Examples:
        >>> solution('a', 'a')
        True
        >>> solution('abba', 'ba')
        True
        >>> solution('abba', 'aad')
        False
    """
    if len(magazine) < len(note):
        return False

    freq = [0] * 26
    for ch in magazine:
        freq[ord(ch) - 97] += 1
    for ch in note:
        i = ord(ch) - 97
        freq[i] -= 1
        if freq[i] < 0:
            return False

    return True


if __name__ == '__main__':
    doctest.testmod()
