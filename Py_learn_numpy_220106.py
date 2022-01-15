## numpy 라이브러리 사용

# 환경설정
all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]

import numpy as np
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)

#성능 차이 확인을 위해 100만개의 정수를 저장하는 Numpy배열과 파이썬 리스트 비교
import numpy as np
my_arr = np.arange(1000000)
my_list = list(range(1000000))

from datetime import datetime
start1 = datetime.now()
for _ in range(10): my_arr2 = my_arr * 2
print(datetime.now() - start1)

from datetime import datetime
start2 = datetime.now()
for _ in range(10): my_list2 = [x * 2 for x in my_list]
print(datetime.now() - start2)



# 4.1 The NumPy ndarray: A Multidimensional Array Object

## ndarray: N차원의 배열 객체. 대규모 데이터 집합을 담을 수 있는 빠르고 유연한 자료구조
## 배열은 스칼라 원소간의 연산에 다숑하는 무법과 비슷한 방식 사용

## 배치 계산 처리 방법
import numpy as np
data = np.random.randn(2, 3)
data

data * 10
data + data

data.shape
data.dtype


# 4.1.1 Creating ndarrays
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2

arr2.ndim   #차원
arr2.shape  #행과 열
arr2.size   #전체 원소 수
len(arr2)   #첫번째 차원의 갯수

arr1.dtype  #자료형 확인
arr2.dtype

np.zeros(10)        #주어진 길이나 모양에 0이 들어있는 배열 생성
np.zeros((3, 6))
np.zeros((2, 3, 2))

np.empty((2, 3, 2)) #초기화되지 않은 배열 생성

np.arange(15)       #range 내장함수의 배열 버전



# 4.1.2 Data Types for ndarrays
## dtype은 ndarray가 메모리에 있는 특정 데이터를 해석하기 위해 필요한 정보를
 # 담고 있는 특수한 객체
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr1.dtype
arr2.dtype
arr1
arr2

## astype 메서드로 배열의 dtype을 다른 형으로 변환(캐스팅)
arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)
float_arr.dtype

## 부동소수점수를 정수형 dtype으로 변환하면 소수점 아래 자리가 버려진다.
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr
arr.astype(np.int32)

## astype을 사용하여 숫자 형식의 문자열을 담고 있는 배열을 숫자로 변환
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)

## 다른 배열의 dtype 속성 이용
int_array = np.arange(10)
int_array
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
calibers.dtype
int_array.astype(calibers.dtype)

## 축약코드 사용
empty_uint32 = np.empty(8, dtype='u4') #부호가 없는 32비트 정수형
empty_uint32



# 4.1.3 Arithmetic with NumPy Arrays
## 배열의 중요한 특징은 for문 없이 데이터 일괄 처리 가능
 # -> 벡터화: 같은 크기의 배열 간의 산술 연산은 배열의 각 원소 단위로 적용
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
arr * arr
arr - arr

## 스칼라 인자가 포함된 산술 연산의 경우 배열 내의 모든 원소에 스칼라 인자 적용
1 / arr
arr ** 0.5

## 같은 크기를 가지는 배열 간의 비교 연산은 불리언 배열을 반환
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr2
arr2 > arr

## 브로드캐스팅: 크기가 다른 배열 간의 연산



# 4.1.4 Basic Indexing and Slicing
## 데이터의 부분집합이나 개별 요소를 선택하는 방법
arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8] = 12
arr
## 스칼라값 12를 대입하면 선택한 영역 전체로 전파(브로드캐스트)
 # 리스트와 중요한 차이점: 배열 조각은 원본 배열의 뷰
 # 즉 데이터는 복사되지 않고 뷰에 대한 변경은 그대로 원본 배열에 반영

## arr 배열의 슬라이스 생성
arr_slice = arr[5:8]
arr_slice

## arr_slice의 값을 변경하면 원래 배열인 arr의 값도 바뀌어 있음을 확인할 수 있다.
arr_slice[1] = 12345
arr

## [:]로 슬라이스 하면 배열의 모든 값을 할당
arr_slice[:] = 64
arr

## 뷰 대신 ndarray 슬라이스의 복사본을 얻고 싶다면 arr[5:8].copy()사용
arr[5:8].copy()
arr

## 다차원 배열 중 2차원 배열에서 각 색인에 해당하는 요소는 1차원 배열
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]

## 다차원 배열 중 2차원 배열에서 각 색인에 해당하는 요소는 1차원 배열
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]

## 개별요소는 재귀적으로 접근해야 한다. 또는 콤마로 구분된 색인 리스트를 넘긴다.
arr2d[0][2]
arr2d[0, 2]

## 다차원 배열에서 마지막 색인을 생략하면 반환되는 객체는 상위 차원의 데이터를 포함하고 있는
 # 한 차원 낮은 ndarray가 된다.
    # arr3d의 차원: 2x2x3
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d

    # arr3d[0]의 차원: 2x3
arr3d[0]

## arr3d[0]에는 스칼라값과 배열 모두 대입 가능
old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d
arr3d[0] = old_values
arr3d

## arr3d[1, 0]은 (1,0)으로 색인되는 1차원 배열과 그 값 반환
arr3d[1, 0]

## 이 값은 아래의 결과와 동일
x = arr3d[1]
x
x[0]

## 위 값은 아래의 결과와 동일
arr3d[1][0]

# indexing with slices
## ndarray 는 익숙한 문법으로 슬라이싱
arr
arr[1:6]

## arr2d의 경우 슬라이싱 방법이 상이
arr2d
arr2d[:2]

# 슬라이스는 축을 따라 선택 영역 내의 요소를 선택한다.
# arr2d[:2]는 'arr2d의 시작부터 두 번째 로우까지의 선택'이라고 이해할 것.

## 다차원 슬라이싱
arr2d[:2, 1:]

## 정수 색인과 슬라이스를 함께 사용해서 한 차원 낮은 슬라이스를 얻을 수 있다.
## 두번째 로우에서 처음 두 컬럼만 선택
arr2d[1, :2]

## 처음 두 로우에서 세 번째 컬럼만 선택
arr2d[:2, 2]

## 콜론만 쓰면 전체 축을 선택한다는 의미이므로 원래 차원의 슬라이스를 얻게 됨
arr2d[:, :1]

## 슬라이싱 구문에 값을 대입하면 선택 영역 전체의 값이 대입된다.
arr2d[:2, 1:] = 0
arr2d




# 4.1.5 Boolean Indexing
## 중복된 이름을 포함한 배열. randn함수를 이용하여 표준 정규분포 데이터 생성
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4) # 7x4 array
names
data

## names와 'Bob'문자열 비교하면 불리언 배열 반환
names == 'Bob'

## 이 불리언 배열을 배열의 색인으로 사용 가능
data[names == 'Bob'] # 'Bob'이 있는 index 0과 index 3에 해당하는 데이터
    # *불리언 배열은 반드시 색인하려는 축의 길이와 동일한 길이를 가져야 함.
    # 하지만 동일한 길이가 아니더라도 error는 발생하지 않으므로 주의!

## names == 'Bob'인 로우에서 2: 컬럼 선택
data[names == 'Bob', 2:] # row index 0, 3 & column index 2:
data[names == 'Bob', 3]

## ~연산자는 반대조건
names != 'Bob'
data[~(names == 'Bob')]

cond = names == 'Bob'
data[~cond]

# &(AND) 조건 과 |(OR)조건
# 불리언 배열에서는 and와 or를 사용할 수 없고 & 과 | 을 사용
mask = (names == 'Bob') | (names == 'Will')
mask
data[mask]
    # 배열에 불리언 색인을 이용해서 데이터를 선택하면 반환되는 배열의 내용이 바뀌지 않더라도
    # 항상 데이터 복사가 발생

    # 파이썬의 예약어인 and와 or은 불리언 배열에서는 사용할 수 없다!!!!
    # 대신 &(and)와 |(or)을 사용
    # data에 저장된 모든 음수를 0으로 대입

data[data < 0] = 0
data

## 1차원 불리언 배열을 사용해서 전체 로우나 컬럼을 선택하는 것은 쉽게 할 수 있다.
data[names != 'Joe'] = 7
data
    # *2차원 데이터에 대한 연산은 pandas를 이용해서 처리하는 것이 편리




# 4.1.6 Fancy Indexing
# Fancy Indexing은 정수 배열을 사용한 색인을 설명하기 위함.

## 8x4 배열
arr = np.empty((8, 4)) # 8x4 array
for i in range(8):
    arr[i] = i
arr

## 특정순서로 row 선택 시 해당 정수가 담긴 ndarray나 리스트를 넘김
arr[[4, 3, 0, 6]]

## 색인으로 음수를 사용하면 끝에서부터 로우 선택
arr[[-3, -5, -7]]

## 다차원 색인 배열을 넘기는 것은 다르게 동작. 각각의 색인 튜플에 대응하는 1차원 배열이 선택됨.
arr = np.arange(32).reshape((8, 4))
arr
arr[[1, 5, 7, 2], [0, 3, 1, 2]] # index [1,0], [5, 3], [7, 1], [2, 2]
    # 배열이 몇차원이든 팬시 색인의 결과는 항상 1차원

## 행렬의 행(로우)와 열(컬럼)에 대응하는 사각형 모양의 값이 선택되기 위해서는 아래와 같이 코딩
arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]] # row index 선택, column index 순서로 배열




# 4.1.7 Transposing Arrays and Swapping Axes
    # 배열 전치는 데이터를 복사하지 않고 데이터의 모양이 바뀐 뷰를 반환하는 특별한 기능

## ndarray는 transpose메서드와 T라는 이름의 특수한 속성 보유
arr = np.arange(15).reshape((3, 5))
arr
arr.T

## 행력의 내적은 np.dot를 이용
arr = np.random.randn(6, 3)
arr
np.dot(arr.T, arr)

## 다차원 배열의 경우 transpose 메서드는 튜플로 축 번호를 받아서 치환
arr = np.arange(16).reshape((2, 2, 4))
arr
arr.transpose((1, 0, 2)) # reshape된 arrary의 index배열. (1,0,2) --> (2, 2, 4)

    # 예시
a = np.ones((2,3,4))
a
np.transpose(a, (1,0,2)) # reshape된 arrary의 index배열. (1,0,2) --> (3, 2, 4)
np.transpose(a,(1,0,2)).shape
np.transpose(a,(2,1,0)) # reshape된 arrary의 index배열. (2, 1, 0) --> (4, 3, 2)
np.transpose(a,(2,1,0)).shape

# 두 개의 축 번호를 받아서 배열을 뒤 바꾼다.
arr
arr.swapaxes(1, 2)




## 4.2 Universal Functions: Fast Element-Wise Array Functions
    # 유니버설 함수 ufunc: ndarray안에 있는 데이터 원소별로 연산을 수행하는 함수
    # ufunc 함수는 sqrt나 exp같은 간단한 변형을 전체 원소에 적용 가능

