def is_pangram(sentence):
    sentence = sentence.lower()
    for i in range(97,123):
        if(sentence.count(chr(i)) == 0):
            return(False)
    return(True)
