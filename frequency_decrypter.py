import pandas as pd
import string

# English letter frequency ordered from most to least common
letter_frequency = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D",
                    "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B",
                    "V", "K", "X", "Q", "J", "Z"]

letter_frequency_fr = ["E","A","S","I","N","T","R","L","U","O","D","C","M",
"P","V","G","F","Q","H"	,"B","X","J","Y","Z","K","W"]

def decrypt_text(text, mapping):
    return "".join(mapping.get(word,"?") for word in text.split())

try:
    with open("CHIPPARI Hadrien.txt", "r", encoding="utf-8") as file:
        encrypted_text_list = file.read().lower().split()
        alphabet_digits = [char for char in string.ascii_uppercase + string.digits]

        df = pd.DataFrame({'word': encrypted_text_list})
        word_frequencies = df['word'].value_counts(normalize=True) * 100  # Convertion en pourcentage de la fréquence des clés

        sorted_words = word_frequencies.index.tolist()

        word_to_letter = {sorted_words[i]:alphabet_digits[i] for i in range(min(len(sorted_words), len(alphabet_digits)))}
        print(word_to_letter)

        decrypted_text = decrypt_text(" ".join(encrypted_text_list), word_to_letter)

        print(decrypted_text)
except FileNotFoundError as error:
    print(f'error : {error}')


