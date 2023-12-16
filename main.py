with open("books/frankenstein.txt") as f:
    file_content = f.read()

words = file_content.split()

def count_letters(file):
    letters_count = {}
    for word in file:
        for letters in word:
            letters = letters.lower()
            if letters in letters_count:
                letters_count[letters] +=1
            else:
                letters_count[letters] = 1
    return letters_count   

dico_list = count_letters(words)


resultList = list(dico_list.items())

resultList.sort(key=lambda a: a[1],reverse = True)

print("--- Begin report of books/frankenstein.txt ---")
print("")
print(f"{len(words)} words found in the document")

for i in range (0, len(resultList)):
    if (resultList[i][0]).isalpha():
        print (f"The '{(resultList[i][0])}' character was found {(resultList[i][1])} times")

print("--- End report ---")

