"""

      Task1_6.py   -

      This solution attempts to read from twain.txt and display the most
      frequent 100 words that are 5 characters or greater

"""

wordcount = {}

for line in open('twain.txt', encoding='utf8'):
    words = line.split()

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

sortedwords = sorted(wordcount.items(), key=lambda a:a[1], reverse=True)
five_letters = [(word, count) for word, count in sortedwords if len(word) >= 5]
print(five_letters[:100])