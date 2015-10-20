"""

      Task1_6.py   -

      This solution attempts to read from twain.txt and display the most
      frequent 100 words that are 5 characters or greater



      Additional tips:
      1. Create a dictionary to store words and word counts

      2. Iterate over the file as shown in the slide for this task.

      3. Use the split() method to break one line into a list of strings

      4. Iterate over the list of strings, check if the word is in the
         dictionary already

      5. If it is, increment the count value for that word

      6. If it is not, add it to the dictionary

      7. To sort the dictionary, convert it to a list of tuples using dict.items()
         This will yield a structure as follows:
            [ ( key1, value1 ), ( key2, value2 ), ( key3, value3 ) ]

      8. To sort based on the values, we'll need a key function to help sort. We
         need to sort by the values, or in other words, the second item in the tuple.
         The following should do this:
                     key = lambda a: a[1]

      9. Sort using sorted(list, key, order)   <-- plug step 7 and step 8 into this and set the reverse flag

      10. sorted() returns a new list of tuples in sorted order.   Iterate over this new
          list and create a list of only the words that are 5 characters or longer.
          You can do this with a for loop, but can you do it with a list comprehension?

      11. Print the first 100 of the items in this new list.
"""

dictionary = {}

for line in open('twain.txt', encoding='utf8'):
    words = line.split()

    for w in words:
        if w in dictionary:
            dictionary[w] += 1
        else:
            dictionary[w] = 1

sorted_words = sorted(dictionary.items(), key=lambda a:a[1], reverse=True)
print(sorted_words)
five_letters = [(word, count) for word, count in sorted_words if len(word) >= 5]
print(five_letters[:100])