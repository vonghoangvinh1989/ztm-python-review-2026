from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("./test.txt", mode="r") as my_file:
        content = my_file.read()
        translation = translator.translate(content)
        with open("./test-ja.txt", mode="w", encoding="utf8") as my_file_translated:
            my_file_translated.write(translation)
except FileNotFoundError as e:
    print("check your file path silly!")
