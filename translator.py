from translate import Translator


translator = Translator(to_lang="zh")


try:
    with open("./text.txt", mode="r") as my_file:
        text = my_file.read()
        print(translator.translate(text))

except FileNotFoundError as err:
    print(err)        
    