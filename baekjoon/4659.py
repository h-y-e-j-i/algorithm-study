import sys

while True:
    flag = 0
    word = sys.stdin.readline().strip()
    convert_to_num = list()
    convert_to_list = word.split()

    if word == 'end': break

    for w in word:
        if w in ['a', 'e', 'o', 'i', 'u']:
            convert_to_num.append('1')
        else:
            convert_to_num.append('0')

    convert_to_str = ''.join(convert_to_num)

    if '111' in convert_to_str or '000' in convert_to_str:
        flag = -1 

        word_splits = word.split('ee')

    for ch in "abcdfghijklmnpqrstuvwxyz":
        double_word = f"{ch}{ch}"
        if double_word in word:
            flag = -1


    if '1' not in convert_to_str:
        flag = -1 

    if flag == 0:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
