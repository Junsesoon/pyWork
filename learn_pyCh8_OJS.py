## 211021 수업내용 오준서
# 파이썬 8장 파일처리와 패키지설치 211page

# 간단한 예외처리
# 1) 예외 발생 코드
print('프로그램 시작!!!')
x= [10, 30, 25.2, 'num', 14, 51]

for i in x :
    print(i)
    y= i**2 # 예외 발생
    print('y= ', y)
print('프로그램 종료')

# 2) 예외 처리 코드
print('프로그램 시작!!!')
for i in x:
    try:
        y = i**2
        print('i=', i, 'y= ', y)
    except :
        print('숫자 아님: ', i)

print('프로그램 종료')



# 중첩 예외처리
# 유형별 예외처리
print('\n유형별 예외처리')
try:
    div = 1000/2.53
    print('div=%5.2f' %(div))
    div = 1000 / 0 # 1차: 산술적 예외
    f = open('d:/coding/pyEdu/ch8_meterial/data/test.txt') # 2차: 파일 열기
    num = int(input('숫자 입력: ')) # 3차: 기타 예외
    print('num =', num)

# 다중 예외처리 클래스
except ZeroDivisionError as e: # 산술적 예외처리
    print('오류 정보: ', e)
except FileNotFoundError as e: # 파일 열기 예외처리
    print('오류 정보: ', e)
except Exception as e : # 기타 예외 처리
    print('오류 정보: ', e)
finally :
    print('finally 영역 - 항상 실행되는 영역')



# 텍스트 파일 입출력
# 1) 현재 작업디렉터리
import os
print('\n현재 경로 :', os.getcwd())
# 2) 예외처리
try :
    # 3) 파일 읽기
    ftest1 = open('ch8_meterial/data/ftest.txt', mode = 'r')
    print(ftest1.read())
    # 4) 파일 쓰기
    ftest2 = open('ch8_meterial/data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~')
    # 5) 파일 쓰기 + 내용 추가
    ftest3 = open('ch8_meterial/data/ftest2.txt', mode = 'a')
    ftest3.write('\nmy second text ~~~')
except Exception as e:
    print('Error 발생: ', e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()



# 텍스트 자료 읽기 220page
# 파일 읽기 관련 함수
try:
    # 1) read() : 전체 텍스트 자료 읽기
    ftest = open('ch8_meterial/data/ftest.txt', mode = 'r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    # 2) readlines() :
    ftest = open('ch8_meterial/data/ftest.txt', mode = 'r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단 수:', len(lines))

    # 3) list -> 문장 추출
    docs =[] # 문장 저장
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)

    # 4) readline() : 한줄 읽기
    ftest = open('ch8_meterial/data/ftest.txt', mode = 'r')
    line = ftest.readline()
    print(line)
    print(type(line))
except Exception as e:
    print('Error 발생: ', e)
finally:
    ftest.close()



# os 모듈의 파일과 디렉터리 관련 함수 224page
import os
# 현재 작업 디렉터리 경로 확인
os.getcwd()
# 작업 디렉터리 변경: data로 이동
os.chdir('ch8_meterial/data')
# 현재 작업 디렉터리 목록: list반환
os.listdir(('.'))
# 디렉터리 생성: test 생성
os.mkdir('test')
os.listdir('.')
# 디렉터리 이동 # test 폴더로 이동
os.chdir('test')
os.getcwd()
# 여러 디렉터리 생성 # test2, test3 생성
os.makedirs('test2/test3')
os.listdir('.')
# 디렉터리 이동: test 이동
os.chdir('test2')
os.listdir('.')
# 디렉터리 삭제: test3 삭제
os.rmdir('test3')
os.listdir('.')
# 상위 디렉터리 이동: 상위 디렉터리 2개 이동
os.chdir('../..')
os.getcwd()
# 여러 개의 디렉터리 삭제: test, test2 삭제
os.removedirs('test/test2')



# os.path 모듈의 경로 관련 함수 226page
import os.path # window 파일 경로를 조작하는 모듈
# 현재 경로 확인
os.getcwd()
# 경로 변경
os.chdir('d:/coding/pyEdu')
os.getcwd()
#lecture 디렉터리의 step01_try_except.py 파일 절대경로
os.path.abspath('pyEdu/ch7_learn_OJS.py')
# step01_try_except.py 파일의 디렉터리 이름
os.path.dirname('pyEdu/ch7_learn_OJS.py')
# workspace 디렉터리 유무 확인
os.path.exists('D:/coding/pyEdu/ch8_meterial/data')
# step01_try_except.py 파일 유무 확인
os.path.isfile('d:/coding/pyEdu/ch7_learn_OJS.py')
# 디렉터리 유무 확인
os.path.isdir('d:/coding/pyEdu')
# 디렉터리와 파일 분리
os.path.split('d:/test/test1.txt')
# 디렉터리와 파일 결합
os.path.join('d:/test','test1.txt')
# 파일 크기
os.path.getsize('d:/coding/pyEdu/ch7_learn_OJS.py')





## 211022 수업내용 오준서
# 파일처리와 패키지설치
# 텍스트 자료 수집 229page
import os
# 1) 텍스트 디렉터리 경로 지정
print(os.getcwd())
txt_data = 'c:/james/pyEducation/ch8_meterial/txt_data/'
# 2) 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)
# 3) 각 디렉터리의 텍스트 자료 수집 함수
def textPro(sub_dir):
    first_txt = []
    second_txt = []
    # 3-1 디렉터리 구성
    for sdir in sub_dir :
        dirname = txt_data + sdir
        file_list = os.listdir(dirname)
        # 3-2 파일 구성
        for fname in file_list:
            file_path = dirname + '/' + fname
            # 3-3 file 선택
            if os.path.isfile(file_path):
                try:
                    # 3-4 텍스트 자료 수집
                    file = open(file_path, 'r')
                    if sdir == 'first':
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외발생 :', e)
                finally:
                    file.close()
    return first_txt, second_txt # 텍스트 자료 반환
# 4) 함수 호출
first_txt, second_txt = textPro(sub_dir)
# 5) 수집한 텍스트 자료 확인
print('first_tex 길이 =', len(first_txt))
print('second tex 길이= ', len(second_txt))
# 6) 텍스트 자료 결합
tot_texts = first_txt + second_txt
print('tot_texts 길이=', len(tot_texts))
# 7) 전체 텍스트 내용
print(tot_texts)
print(type(tot_texts))

# pickle 저장과 읽기 예
# 1) pickle 모듈 import
import pickle # file save
# 2) file save: write binary
pfile_w = open('c:/james/pyEducation/ch8_meterial/data/tot_texts.pck', mode='wb')
pickle.dump(tot_texts, pfile_w)
# 3) file load: read binary
pfile_r = open('c:/james/pyEducation/ch8_meterial/data/tot_texts.pck', mode='rb')
tot_texts_read = pickle.load(pfile_r)
print('tot_texts길이 =', len(tot_texts_read))
print(type(tot_texts_read))
print(tot_texts_read)



# 이미지 파일 이동
import os
from glob import glob
# 1) image 파일 경로
print(os.getcwd())
img_path = 'c:/james/pyEducation/ch8_meterial/images/'
img_path2 = 'c:/james/pyEduation/ch8_meterial/images2/'
# 2) 디렉터리 존재 유무
if os.path.exists(img_path):
    print('해당 디렉터리가 존재함')
    # 3) image 파일 저장, 파일 이동 디렉터리 생성
    images = []
    os.mkdir(img_path2)
    # 4) images 디렉터리에서 png 검색
    for pic_path in glob(img_path + '*.png'):  # png 검색
        # 5) 경로와 파일명 분리, 파일명 추가
        img_path = os.path.split(pic_path)
        images.append(img_path[1]) # png 파일명 추가
        # 6) 이진파일 읽기
        rfile = open(file=pic_path, mode = 'rb')
        output = rfile.read()
        # 7) 이진파일 쓰기 -> 폴더 이동
        wfile = open(img_path2+img_path[1], mode='wb')
        wfile.write(output)
    rfile.close();
else:
    print('해당 디렉터리가 없음')
print('png file =', images)

# csv 파일 처리 240page
# 1) pandas 패키지 import
import pandas as pd
import os# 현재 작업 디렉토리 확인
print(os.getcwd())
# 2) csv 파일 읽기
score = pd.read_csv('c:/james/pyEducation/ch8_meterial/data/score.csv')
print(score.info())
print(score.head())
# 3) 칼럼 추출
kor = score.kor
eng = score['eng']
mat = score['mat']
dept = score['dept']
# 4) 과목별 최고 점수
print('max kor = ', max(kor))
print('max eng = ', min(eng))
print('max mat = ', min(mat))
# 5) 과목별 최하 점수
print('min kor = ', min(kor))
print('min eng = ', min(eng))
print('min mat = ', min(mat))
# 6) 과목별 평균 점수
from statistics import mean
print('국어 점수 평균: ', round(mean(kor),3))
print('영어 점수 평균: ', round(mean(eng),3))
print('수학 점수 평균: ', round(mean(mat),3))
# 7) dept 빈도수
dept_count = {} # 빈 set
for key in dept :
    dept_count[key] = dept_count.get(key, 0) + 1

print(dept_count)