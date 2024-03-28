import string

textual_material = ["The Itsy Bitsy spider crawled up the water spout",
              "Down came the rain and washed the spider out",
              "Out came the sun and dried up all the rain",
              "and the Itsy Bitsy spider went up the spout again!"]

stopwords = ["a", "the", "of", "for", "any", "up", "out", "and", "not", "is", "say"]


# Let's convert all the lines in our text file to lowercase and get rid of punctuation marks at the same time.
text = []
for line in textual_material:
    line = line.lower()
    line = line.strip(string.punctuation)
    text.append(line)

# We will maintain the concordance information in a dictionary.
concordance = {}
# We are processing each line individually.
for line_count in range(len(text)):
    # Let's first extract the words from the line.
    words = text[line_count].split(" ")
    # Now let's process the words one by one.
    for word in words:
        # If the word is not in the stop_words, I will add it to the concordance.
        if word not in stopwords:
            # If it hasn't been entered into our concordance dictionary before.
            if word not in concordance:
                # The key of our concordance dictionary should be our word, and the value should be a list.
                concordance[word] = []
                # The first element of this list will indicate the frequency of our word in the text.
                # We set it to 1 since it's the first occurrence.
                concordance[word].append(1)
                # The second element of the list is another list.
                concordance[word].append([])
                # This list will contain one or more tuples.
                # Each tuple will represent (line_number, context).

                context = ""
                words2 = textual_material[line_count].split(" ")
                for word2 in words2:
                    temp_word = word2.strip(string.punctuation).lower()
                    if temp_word == word.lower():
                        word_uppercase = word2.upper()
                        context = context + word_uppercase + " "
                    else:
                        context = context + word2 + " "
                t = (line_count+1, context)
                concordance[word][1].append(t)
            else:
                # If this word has already entered our dictionary, we increment its count by one.
                concordance[word][0] = concordance[word][0] + 1
                # And we add a new (line_number, context) tuple to the inner list.

                context = ""
                words2 = textual_material[line_count].split(" ")
                for word2 in words2:
                    temp_word = word2.strip(string.punctuation).lower()
                    if temp_word == word.lower():
                        word_uppercase = word2.upper()
                        context = context + word_uppercase + " "
                    else:
                        context = context + word2 + " "
                t = (line_count+1, context)
                concordance[word][1].append(t)

# We just need to iterate over the dictionary and print each key-value pair appropriately.
for word in concordance:
    print (word, ": Total Number: {}".format(concordance[word][0]))
    for line_number in range(concordance[word][0]):
        print ("Line : {} {}".format(concordance[word][1][line_number][0],concordance[word][1][line_number][1]))
    print()
