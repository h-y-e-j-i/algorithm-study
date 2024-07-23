import sys

n = int(sys.stdin.readline().strip())
main_word = sorted([c for c in  sys.stdin.readline().strip()])

similar_cnt = 0

for _ in range(n-1):
    sub_word = sorted([c for c in sys.stdin.readline().strip()])

    if main_word == sub_word:
        similar_cnt += 1
    elif len(main_word) - len(sub_word) == 1:
        if set(sub_word) == set(main_word):
            similar_cnt += 1
        else:
            ch = list(set(main_word)-set(sub_word))
            if len(ch) == 1:
                sub_word_tmp = sub_word.copy()
                sub_word_tmp.append(ch[0])
                sub_word_tmp = sorted(sub_word_tmp)

                if main_word == sub_word_tmp:
                    similar_cnt += 1
    elif len(sub_word)-len(main_word) == 1:
        if set(sub_word) == set(main_word):
            similar_cnt += 1
        else:
            ch = list(set(sub_word)-set(main_word))
            if len(ch) == 1:
                main_word_tmp = main_word.copy()
                main_word_tmp.append(ch[0])
                main_word_tmp = sorted(main_word_tmp)
                
                if sub_word == main_word_tmp:
                    similar_cnt += 1

    elif len(sub_word)==len(main_word):
        main_word_cnt = dict()
        sub_word_cnt = dict()

        for mw in main_word:
            if mw not in list(main_word_cnt.keys()):
                main_word_cnt[mw] = 1
            else:
                main_word_cnt[mw] += 1

        for sw in sub_word:
            if sw not in list(sub_word_cnt.keys()):
                sub_word_cnt[sw] = 1
            else:
                sub_word_cnt[sw] += 1

        correct_cnt = 0
        for mw in main_word:
            if mw in list(sub_word_cnt.keys()):
                if main_word_cnt[mw] < sub_word_cnt[mw]:
                    correct_cnt += main_word_cnt[mw]
                else:
                    correct_cnt += sub_word_cnt[mw]
        if len(main_word) - correct_cnt <= 1:
            similar_cnt+=1

print(similar_cnt)