# https://www.acmicpc.net/problem/1966
# 프린터 큐

import sys

answers = list()

num_of_tc = int(sys.stdin.readline().strip())
for tc_idx in range(num_of_tc):    
    num_of_docs, doc_idx = list(map(int, sys.stdin.readline().strip().split()))    

    input_prior_docs = list(map(int, sys.stdin.readline().strip().split()))    
    prior_docs = list()
    for i in range(num_of_docs):
        prior_docs.append(input_prior_docs[i])
    # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
    # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다.
    for i in range(num_of_docs):
        max_prior = max(prior_docs)
        max_prior_idx = prior_docs.index(max_prior)
        left_docs = prior_docs[:max_prior_idx]
        right_docs = prior_docs[max_prior_idx:]
        if max_prior_idx > doc_idx:
            doc_idx = len(right_docs)-1+(doc_idx+1)
        else:
            doc_idx -= len(left_docs)

        prior_docs = right_docs+left_docs

        if doc_idx == 0:            
            answers.append(i+1)
            break
        else : 
            # 
            prior_docs.pop(0)
            doc_idx -= 1

print('\n'.join(map(str, answers)))
