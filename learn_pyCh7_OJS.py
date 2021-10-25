## 211020 수업내용 오준서
# 파이썬 7장
# 정규 표현식 194page
# 문자열 찾기
from re import findall
st1 = '1234 abc홍길동 ABC_556_6 이사도시'

# 1) 숫자 찾기
print(findall('1234', st1))
print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
print(findall('\\d{3,}', st1))
# 2) 문자열 찾기
print(findall('[가-힣]{3,}', st1))
print(findall('[a-z]{3}', st1))
print(findall('[a-z|A-Z]{3,}', st1))
# 3) 특정 위치의 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
# 접두어/접미어
print(findall('^test', st2)) # 접두어
print(findall('st$', st2)) # 접미어
# 종료 문자 찾기: abc mbc
print(findall('.bc', st2))
print(findall('t.', st2))
# 시작 문자 찾기
# 4) 단어 찾기(\\w) - 한글+영문+숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3)
print(words)
# 5) 문자열 제외: x+(x가 1개 이상 반복)
print(findall('[^^*$]+',st3))

# 문자열 검사 197page
from re import match

# 1) 패턴과 일치된 경우
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)
if result :
    print('주민번호 일치')
else :
    print('잘못된 주민번호')

# 2) 패턴과 불일치된 경우
jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)
if result :
    print('주민번호 일치')
else :
    print('잘못된 주민번호')

# 문자열 치환 198page
from re import sub
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# 1) 특수문자 제거
text1 = sub('[\^*$]+', '', st3)
print(text1)

# 2) 숫자 제거
text2 = sub('[0-9]','', text1)
print(text2)

# 텍스트 처리 199page
from re import split, match, compile
multi_line="""http://www.naver.com
http://www.daum.net
www.hongkildon.com"""
# 1) 구분자를 이용하여 문자열 분리
web_site = split('\n', multi_line)
print(web_site)
# 2) 패턴 객체 만들기
pat = compile('http://')
# 3) 패턴 객체를 이용하여 정상 웹 주소 선택하기
sel_site = [site for site in web_site if match(pat, site)]
print(sel_site)

# 자연어 전처리 201page
from re import findall, sub

# 텍스트
texts = ['우리나라 대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

# 1단계: 소문자 변경
texts_rel = [t.lower() for t in texts]
print('texts_rel: ', texts_rel)
# 2단계: 숫자 제거
texts_re2 = [sub("[0-9]", '', text) for text in texts_rel]
print('texts_re2: ', texts_re2)
# 3단계: 문장부호 제거
texts_re3 = [sub('[,.?!:;]', '', text)for text in texts_re2]
print('texts_re3: ', texts_re3)
# 4단계: 특수문자 제거: re.sub()이용
spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str, '', text)for text in texts_re3]
print('texts_re4: ', texts_re4)
# 5단계: 영문자 제거
texts_re5 = [''.join(findall("[^a-z]",text))
for text in texts_re4]
print('texts_re5: ', texts_re5)
# 6단계: 공백제거
texts_re6 = ['  '.join(text.split()) for text in texts_re5]
print('texts_re6: ', texts_re6)

# 전처리 함수 203page
from re import findall, sub
# 텍스트 전처리
texts = [' 우리나라     대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

# 1) 텍스트 전처리 함수
def clean_text(text) :
    # 1~6단계
    texts_re = text.lower()
    texts_re2 = sub('[0-9]', '', texts_re)
    texts_re3 = sub('[,.?!;:]', '', texts_re2)
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3)
    texts_re5 = sub('[a-z]', '', texts_re4)
    texts_re6 = ' '.join(texts_re5.split())
    return texts_re6
# 2) 함수 호출
texts_result = [clean_text(text) for text in texts]
print(texts_result)
