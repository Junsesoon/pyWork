## 211020 오준서
# 파이썬 7장 연습문제

# 문제1
# 다음과 같은 여러 줄의 문자열을 대상으로<email 양식 처리조건>에 맞게 정규표현식을 적용하여
# email양식이 올바른 것만 출력되도록 하시오.
# 조건1) 아이디: 첫자는 영문소문자, 단어길이 4자 이상
# 조건2) 호스트이름: 영문소문자 시작, 단어길이 3자 이상
# 조건3) 최상위 도메인: 영문소문자 3자리 이하
# 조건4) 정규표현식 기본 패턴: '메타문자@메타문자.메타문자'
email = """hong@12.com
you2@naver.com
12kang@hanmil.net
kimjs@gmail.com"""
from re import findall, match
# pat = compile('\\w{1,}@\\w{1,}.\\w{1,}')
for e in email.split(sep='\n'):
    if match('^[a-z]{1}\\w{3,}@[a-z]\\w{3,}', e) != None:
        print(e)


# 문제2
# 다음 emp 변수는 '입사년도이름급여'순으로 사원의 정보가 기록된 자료이다.
# emp 변수를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.
from re import findall
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
# 함수 정의
def name_pro(emp):
    names = []
    for emp in emp:
        emp1 = findall('[가-힣]{2,}',emp)
        names.append(emp1)
    return names

names = name_pro(emp)
print('names= ', names)



# 문제3
# 다음 emp 변수는 '입사년도이름급여'순으로 사원의 정보가 기록된 자료이다.
# emp 변수를 이용하여 사원의 급여 평균을 추출하는 함수를 정의하시오.
from re import findall
from statistics import mean
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
# 함수 정의
def pay_pro(emp):
    pay = []
    ext = []
    for emp in emp:
        ext = list(map(int,findall('[0-9]{3}$', emp)))
        pay.extend(ext) # append를 사용하면 [리스트끼리 묶여서 계산 불가]
    mpay = mean(pay)
    return mpay
# 함수 호출
pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)



# 문제4
# 전체 급여 평균과 평균이상 급여 수령자의 이름 및 급여를 출력하시오.
from re import findall
from statistics import mean
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
# 함수 정의
def pay_above(x):
    from statistics import mean
    import re
    # 변수 초기화
    names = []
    pay = []
    ext = []
    # 평균 급여 산출
    for emp in x:
        ext = list(map(int, findall('[0-9]{3}$', emp)))
        pay.extend(ext)  # append를 사용하면 [리스트끼리 묶여서 계산 불가]
    mpay = mean(pay)
    # 사원 이름 추출
    for emp in x:
        name = findall('[가-힣]{3,}',emp)
        names += name
    # 평균 이상 급여자 추출
    i = 0
    for above in pay:
        if above >= mpay:
            print('이름: {0} => {1}'.format(names[i],above))
            i += 1
        else:
            i += 1
# 함수 호출
pay_above(emp)



# 문제5
# 다음 texts 변수의 텍스트를 출력 결과와 같이 전처리 하시오.
# <출력 결과> : ['afabasabag', 'abttaa', 'uysfsfaa']
from re import findall, sub
texts=['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

text = [t.lower() for t in texts]
text_num = [sub('[0-9]','',t)for t in text] # 숫자 제거
text_sym = [sub('[,.?!:;@#$%^&*()]', '', t) for t in text_num] # 특수문자 제거
result = [''.join(t.split()) for t in text_sym]
print(result)