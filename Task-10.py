def check_common_characters(word1,word2):
    compare =list(set(word1)&set(word2))
    for c in compare:
        print(c)
check_common_characters("tebogo","thabo")
