def popular_words(text, words):

    text = text.lower().split()
    dic_word = {}

    for word in words:
        dic_word[word] = text.count(word)

    return dic_word


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
