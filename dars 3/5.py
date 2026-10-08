words = [
"python" ,
"java" ,
"python" ,
"c" ,
"python" ,
"java" ,
"c" ,
"python"
]

count_words = {}
for word in words:
    count_words[word] = count_words.get(word, 0) +1

    print (count_words)