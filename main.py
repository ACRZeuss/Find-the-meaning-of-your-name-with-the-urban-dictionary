import requests
from bs4 import BeautifulSoup
from googletrans import Translator

name = input("Adınız: ")
url = f"https://www.urbandictionary.com/define.php?term={name}"

translator = Translator()

def get_content():
    response = requests.get(url)
    content = response.content
    return content


def get_definition(content):
    soup = BeautifulSoup(content, "html.parser")
    definition = soup.find(class_="meaning").text
    definition_tr = translator.translate(definition, dest="tr").text
    return definition_tr


print(get_definition(get_content()))