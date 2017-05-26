# put your code here.
document = open("test.txt")
word_count = {}

for line in document: 
    line = line.rstrip()
    line = line.split(" ")

    for word in line:
        current_count = word_count.get(word,0)
        word_count[word] = current_count + 1

for word, current_count in word_count.items():
    print word, current_count
