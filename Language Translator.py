from googletrans import Translator,LANGUAGES

print("Languages with its code:")
for code,lang in LANGUAGES.items():
    print(code,lang)
translator=Translator()
n=input("Enter your sentence:")
m=input("Enter the source language code:")
p=input("Enter the destination language code:")
a=translator.translate(n,src=m,dest='en')
print(a.text)







