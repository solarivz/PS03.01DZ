import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def get_translate_words(text):
    # Переводим на русский
    translated_text = GoogleTranslator(source='en', target='ru').translate(text)
    return(translated_text)

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict_en = get_english_words()
        word_ru = get_translate_words(word_dict_en.get("english_words"))
        word_definition_ru = get_translate_words(word_dict_en.get("word_definition"))

        # Начинаем игру
        print(f"Значение слова - {word_definition_ru}")
        user = input("Что это за слово? ")
        if user == word_ru:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_ru}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н")
        if play_again != "д":
            print("Спасибо за игру!")
            break


word_game()


