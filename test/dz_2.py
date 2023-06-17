# Клас, що очищає рядок від знаків пунктуації
class Textprocessor:
# Створюємо функцію в якій аргументом є рядок та змінну яка містить  очищений рядок від знаків пунктуації.
    def get_clean_string(self, text):
        clean_text = ''
#За допомогою циклу проходимо по кожному символу і визначаємо, чи є він знаком пунктуації.
# Якщо символ TRUE додаємо його до очищенного рядка
        for symbol in text:
            if self.__is_punktian(symbol)== True:
                clean_text += symbol
        return clean_text
#Огортаєм статичним методом створюємо функцію аргументом якої є символ, який необхідно перевірити,
# а також створюємо змінну яка містить список знаків пунктуації.
    @staticmethod
    def __is_punktian(symbol):
        punkt = ['.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|',
             '-', '_', '+', '=', '*', '&', '%', '@', '#', '$', '–']
#Якщо символ не міститься у списку знаків то не відносимо його до знаків повертаємо True.
# В іншому випадку False
        if symbol not in punkt:
            return True
        else:
            False
#Створюємо класс загрузки очищеного рядка та використовує обєкт Textprocessor для обробки тексту
# та визначемо змінну для зберігання чистого тексту.
class TextLoader:
    def __init__(self):
        self.__text_processor = Textprocessor()
        self.__clean_string = ' '

#Cтворюємо метод, що приймає текст,як аргумент та присваює його змінній (clean_string), як екземпляру
    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)
#Прописуємо @property який при виклику геттера clean_string, виводить повідомлення  "Виводимо очищений текст:"
    @property
    def clean_string(self):
        print("Виводимо очищений текст:")
        return self.__clean_string

# Прописуємо сеттер який встановлює значення (__clean_string), яке дорівнює переданому value.
    @clean_string.setter
    def clean_string(self, value):
        self.__clean_string = value


#Створюємо клас для роботи с даними, з атрибутом, що ініціалізується  TextLoader
class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()
#Створюємо метод з аргументом який містить список із текстом і перебирає його,
# а також виводить очищенний текст на екран

    def process_texts(self, text_list):
        for text in text_list:
            self._text_loader.set_clean_text(text)
            print(self._text_loader.clean_string)

#Перевірка роботи кода
data_interface = DataInterface()
data_interface.process_texts(['У травні скоротилося навантаження зернових на мережі "Укрзалізниці" – '
'до 1.37 млн тонн.', 'Частка збіжжя скоротилася до 13% у загальному обсязі вантажів.',
 'Середньодобове навантаження – 44 тис. тонн.'])





