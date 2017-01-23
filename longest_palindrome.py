# searching the longest palindrome in a given string, returns tuple of indxes of a input string (start, end)


def length(slice): a, b = slice; return b - a
def grow(text, start, end):
    while(start > 0 and end < len(text)
         and text[start-1].upper() == text[end].upper()):
        start -= 1; end += 1
    return (start, end)
def longest_palindrome(tex):
    if tex == '': return (0,0)
    cand = [grow(tex, start, end)
           for start in range(len(tex))
           for end in (start,start + 1)]
    return max(cand, key=length)
