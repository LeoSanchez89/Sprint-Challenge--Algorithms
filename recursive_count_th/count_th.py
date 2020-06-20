'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    target = "th"
    word_size = len(word)
    target_size = len(target)

    if word_size < target_size:
        return 0
    if (word[0:target_size] == target):
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
    #     target_size += 1
    #     count += 1
    # return count_th(word[target_size - 1:])
  
    
