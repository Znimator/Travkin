# Дана последовательность символов кириллицы и пробелов. Группу
# символов, разделенную с одной или обеих сторон пробелами и не содержащую
# внутри себя пробелов, назовем словом. Будем называть особым слово, в
# котором гласных букв больше, чем согласных. Перед каждым таким словом
# вставить символ *. Подсчитать количество вставленных символов

input_text = input("Введите последовательность символов: ")

def is_special_word(word):
    vowels = "аеёиоуыэюя"
    vowel_count = sum(1 for letter in word if letter in vowels)
    consonant_count = len(word) - vowel_count
    return vowel_count > consonant_count

words = input_text.split()

result_text = ""
inserted_count = 0

for word in words:
    if is_special_word(word):
        result_text += "*"
        inserted_count += 1
    result_text += word + " "


result_text = result_text.rstrip()

print("Результат:", result_text)
print("Количество вставленных символов:", inserted_count)