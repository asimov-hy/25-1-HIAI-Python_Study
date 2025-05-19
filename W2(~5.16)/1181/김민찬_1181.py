word_list = []

word_count = int(input())
for word in range(word_count):
    word=input()
    word_list.append(word)

# 짧은 것부터 -> 길이같으면 알파벳
word_list = sorted(set(word_list), key=lambda x: (len(x), x))
for word in word_list:
    print(word)