def lengthOfLastWord(s):
    count = 0
    right_ptr = len(s)-1
    while right_ptr>=0:
        if s[right_ptr].isalpha():
            count+=1
        elif count > 0:
            break
        right_ptr-=1
    return count

def lengthOfLastWord2(s):
    all_words = s.split(' ')
    for i in range(len(all_words)-1, -1, -1):
        len_word = len(all_words[i])
        if len_word>0:
            return len_word


s = "   fly me   to   the moon  "
s = "a"
print(lengthOfLastWord(s))
print(lengthOfLastWord2(s))
