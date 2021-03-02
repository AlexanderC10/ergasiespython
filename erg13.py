
f = open("words.txt", "r")

lines = f.read()
f.close()

lst = lines.split(" ")
used = []

for word1 in lst:
    len_word1 = len(word1)
    for word2 in lst:
        if word1 != word2:
            len_word2 = len(word2)
            if len_word1 + len_word2 == 20:
                stop = False
                for combo in used:
                    if word1 in combo and word2 in combo:
                        stop = True
                #print(word1, word2)
                if not stop:
                    used.append([word1, word2])

print (used)
