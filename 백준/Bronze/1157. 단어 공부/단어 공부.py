word = input().upper()
word_set = list(set(word))

count_list = []
for i in word_set:
    count_list.append(word.count(i))

max_num = max(count_list) 
if count_list.count(max_num) > 1:
    print('?')
else :
    print(word_set[count_list.index(max_num)])

