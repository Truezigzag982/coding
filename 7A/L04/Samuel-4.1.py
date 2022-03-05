def count_words(text):
    mydict = {}
    for word in text.split():
        mydict[word] = mydict.get(word, 0) + 1
    for key, value in mydict.items():
        print(key, ':', value)
    return mydict

def main():
    phargaph = input('pls writs a phargaph:) :  ')
    count_words(phargaph)

if __name__ == "__main__":
    main()