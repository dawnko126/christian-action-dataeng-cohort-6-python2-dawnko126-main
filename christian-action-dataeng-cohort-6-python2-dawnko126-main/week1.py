#Week 1 Test

# For file with only numbers, you should only return one thing(i.e.the first 10 characters)

# For file with story,you NEED to return two things(i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]


def editor(fname):
    #YOUR CODE STARTS HERE
def editor(fname):
    with open(fname, 'r') as file:
        content = file.read().strip()

    if content.isdigit():
        return content[:10]
    else:
        content = content.lower()
        words = content.split()

        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        top_five_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        top_five = [word[0] for word in top_five_words]

        return content, top_five












