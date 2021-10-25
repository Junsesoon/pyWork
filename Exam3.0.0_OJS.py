## 211012 오준서 평가답안제출

## 문제11번
# 다음의 R 코드를 python 코드로 수정하여 제출하시오.
# num=100
# if(num > 100 {
# print("100보다 큽니다.")
# } else if{(num >50){
# print("50보다 큽니다.")
# } else {
# print("50이하입니다.")
# }
num = 100
if num > 100 :
    print("100보다 큽니다.")
elif num > 50 :
    print("50보다 큽니다.")
else :
    print("50이하입니다.")

#! test zone
# num = 101



## 문제12번
# for 와 range를 이용하여 구구단을 만들고 구구단의 결과를 프린트하는 아래의 파이썬 코드를
# 아래와 같이 만들었는데 실행이 되지 않는다. 실행이 되도록 코드를 수정하라.
# for i in range(2,10)
# for j in range(1, 10)
# print(i*j, end= " ")
# print('')
for i in range(2, 10) : #콜론(:) 빠짐
    for j in range(1, 10) : #indent 안맞음
        print(i*j, end= " ")
        print(' ')



## 문제13번
# 아래의 멀티라인 문자열을 대상으로 다음을 실행하시오.
multiline = """It ain't over 
til it's over.
by Yogi Berra"""

# 조건1) 공백으로 분류 한 줄의 문장 한 개를 출력되도록 coding 하시오.
# sents = [] #삭제사유: 조건2에 적용실패
words = []
for sen in multiline.split(sep = '\n') :
    # sents.append(sen)
    for word in sen.split() :
        words.append(word)
result = ' '.join(words)
print(result)

# 조건2) 문자열 처리 함수를 이용하여 Lovely라는 단어가 출력되도록 coding 하시오.
lovely = (words[3][2],words[2][0:3],words[3][2],words[6][1])
result2 = ''.join(lovely)
result2 = result2.upper()
result2.split