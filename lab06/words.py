import os

def read_words(filename):
    # se till att vi öppnar filen i rätt katalog (slå samman 
    # katalogen som scriptet ligger i med filnamnet på textfilen)
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # öppna filen (utf-8 behövs för att hantera åäö rätt)
    file = open(filepath, encoding='utf-8')

    # skriv ut filens innehåll
    #for line in file:
    #    print(line)

    word_list = []
    for line in file:
        for word in line.split():
            word_list.append(word.lower().strip('.,-!?" :;'))
    return word_list

def count_only(words, count_words):
    word_count = {}
    for count_word in count_words:
        word_count[count_word] = 0
        for word in words:
            if word == count_word:
                word_count[word] += 1
    return word_count

def count_all_except(words, stopwords):
    word_count = {}
    for w in words:
        if stopwords.count(w) == 0:
            if isinstance(word_count.get(w), int):
                word_count[w] += 1
            else:
                word_count[w] = 1
    return word_count

def filter_hist(hist, min_count):
    filtered_hist = {}
    for key in hist:
        if hist[key] >= min_count:
            filtered_hist[key] = hist[key]
    return filtered_hist

def sorted_hist(hist):
    l = []
    for key in hist:
        l.append((hist[key], key))
    l.sort(reverse = True)
    return l
# -----------------------------------------------------------

# namnet på filen som ska läsas
#filename = 'nilsholg.txt'

words = read_words('nilsholg.txt')
provinces = read_words('landskap.txt')
stopwords = read_words('undantagsord.txt')

# hist = count_only(words, provinces)
# print(hist['skåne'])

hist = count_all_except(words, stopwords)
# print(hist['gåskarlen'])
hist_sorted = sorted_hist(hist)

for i in range(10):
    print(hist_sorted[i])

count = 0
for t in filter_hist(hist, 100):
    count += 1
print(count)
