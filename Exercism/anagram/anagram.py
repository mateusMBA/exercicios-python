def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        aux = 0
        for letter in set(candidate.lower()):
            if word.lower().count(letter) != candidate.lower().count(letter):
                aux = 1
                break
        if aux == 0 and word.lower() != candidate.lower() and len(word) == len(candidate):
            anagrams.append(candidate)
    return anagrams


