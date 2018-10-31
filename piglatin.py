def strip_and_listify(str1, char2):
    split_string = str1.strip().split(char2)
    stripped_string = []
    for i in split_string:
        if i[0] == " ":
            holding_spot = i[1:-1]
        else:
            holding_spot = i[:-1]
        stripped_string.append(holding_spot)
    return stripped_string



consonant_clusters = "bl–, cl–, fl–, gl–, pl–, sl-, br–, cr–, dr–, fr–, gr–,pr–, tr–, sc–, sk–, sm–, sn–, sp–, st–, sw–, tw–, qu–"

consonant_clusters_fixed = strip_and_listify(consonant_clusters, ",")

def pig_latin_translator(string, terminator):
    split_string = string.split()
    print(split_string)
    vowel_suffix = 'yay'
    consonant_suffix = 'ay'
    vowels = ['a', 'e', 'i', 'o', 'u']
    final_string = ""
    for word in split_string:
        if word.startswith(tuple(consonant_clusters_fixed)):
            p_latin_root = word[2:]
            p_latin_suffix = word[0:2]
            p_latin_word_cluster = p_latin_root + p_latin_suffix + 'ay'
            final_string += p_latin_word_cluster + " "
        elif word.startswith(tuple(vowels)):
            p_latin_word_vowel = word + 'yay'
            final_string += p_latin_word_vowel + " "
        else:
            p_latin_root = word[1:]
            p_latin_suffix = word[0]
            p_latin_word_consonant = p_latin_root + p_latin_suffix + 'ay'
            final_string += p_latin_word_consonant + " "
    final_string = final_string[:-1] + terminator
    final_string_output = final_string.capitalize().replace(',','')
    return final_string_output



# Testing
print(pig_latin_translator("This is a test", "."))
