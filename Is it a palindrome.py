def is_palindrome(s):
    if s == '': return True
    else:
        s = s.lower()
        ind = 0
        while ind != len(s)-1:
            if s[ind] != s[len(s)-1-ind]: return False
            ind += 1
        return True