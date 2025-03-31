import string

old_key = {'rhubarb', 'quince', 'watermelon', 'ximenia', 'nut', 'zucchini',
'blackberry', 'vine', 'cranberry',
 'durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry',
'tangerine', 'satsuma',
 'kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado',
'xigua', 'ugly',
 'waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel',
'raspberry', 'guava',
 'indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry',
'hawthorn', 'apple',
 'nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry',
'quandong', 'zest',
 'wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg',
'persimmon', 'mandarin', 'olive',
 'lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit',
'gooseberry', 'vanilla',
 'mulberry', 'kumquat', 'peach', 'feijoa'}

def Quick_Sort(lst:list)->list:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x==pivot]
    right = [x for x in lst if x > pivot ]
    return Quick_Sort(left) + middle + Quick_Sort(right)

def decrypt_text(text, mapping):
    return "".join(mapping.get(word, " ") for word in text.split())

try :
    with open("old.txt") as file:
        alphabet_digits = [char for char in string.ascii_uppercase + string.digits]
        encrypted_text_file = file.read().lower().split()
        excluded_word = [char for char in encrypted_text_file if char not in old_key]
        sorted_words = Quick_Sort(excluded_word)

        word_mapping ={sorted_words[i]: alphabet_digits[i] for i in range(min(len(sorted_words), len(alphabet_digits)))}
        print(word_mapping)
        with open("CHIPPARI Hadrien.txt","r")as file_message :
            encrypted_text_list = file_message.read().lower().split()
            decrypted_text = decrypt_text(" ".join(encrypted_text_list), word_mapping)
            print(decrypted_text)
except FileNotFoundError as e:
    print(e)
