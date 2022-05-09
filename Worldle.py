import random
import time
from colorama import Back, Fore, Style

# Открываем файл с базой данных
db = open('/home/alex/PycharmProjects/pythonProject/words_db')
words_list = str(db.read()).split(';')
db.close()

# Выводим описание
print(Back.WHITE + Fore.BLACK + '''Добро пожаловать в игру PyWordle! Правила игры: вы угадываете выбранное компьютером 
слово из 5 букв с 5 попыток. Если во введенном вами слове есть буква из загаданного слова, она отмечается желтым фоном. 
Если во введенном слове буква стоит на том же месте, что и в загаданном слове, она отмечается зеленым фоном. В конце 
выводятся очки, количество которых уменьшается с каждой попыткой. Приятной игры!''' + Style.RESET_ALL)

while True:
    # Определяем переменные
    answer = ""
    score = 50
    start_time = end_time = 0

    # Выбранное слово из списка
    sel_word = random.choice(words_list)
    print(sel_word)  # Не забыть убрать

    for nums_of_try, let in enumerate(sel_word):
        # Получение пользовательского слова
        start_time: float = time.time()
        print("\nВведите слово:")
        in_word = input().lower()

        # Проверка, 5 ли букв в слове?
        nn = len(in_word)
        if len(in_word) != 5:
            print("\nВведите слово из 5 букв!")
            print(f"Осталось попыток: {len(sel_word) - nums_of_try - 1}")
            continue

        # Если слово угадано сразу. выводим ответ и завершаем игру
        if in_word == sel_word:
            answer = Back.GREEN + Fore.BLACK + in_word + Style.RESET_ALL
            print(f'\nИгра окончена. Правильный ответ: {answer}. Начать заново? Y/N')
            break

        # Раскладываем слово по буквам и засовываем в список
        in_word_list = []
        for count, letter in enumerate(in_word):
            in_word_list.append(letter)
        # Выделяем текстом буквы
        for num, sel_letter in enumerate(in_word_list):
            if sel_word[num] == sel_letter:
                answer += (Back.GREEN + Fore.BLACK + sel_letter + Style.RESET_ALL)
            elif sel_word.__contains__(sel_letter):
                answer += (Back.YELLOW + Fore.BLACK + sel_letter + Style.RESET_ALL)
            else:
                answer += sel_letter

        print(f"Осталось попыток: {len(sel_word) - nums_of_try - 1}")

        print(answer)
        answer = ''
        score = score - (nums_of_try + 1) * 10

    end_time: float = time.time()
    duration = round((end_time - start_time), 1)
    print(f'\nИгра окончена. Ваш счет: {score}. Ваше время: {duration} cек. Начать заново? Да/Нет')

    if input().lower()[0] != ('y' or 'д'):
        break
