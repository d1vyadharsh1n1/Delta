from googletrans import Translator , LANGUAGES
a=input("Enter your sentence:")
translator=Translator()
b=translator.detect(a)
c=b.lang
for code, lang in LANGUAGES.items():
    if code==c:
        d=lang
    
print("This sentence is in:",d)
