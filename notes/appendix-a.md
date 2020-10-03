# 코딩 테스트를 위한 파이썬 문법

- 파이썬은 코드가 짧은 편
- 코딩 테스트에서 중요한 내용 위주로 수록
- 코딩 테스트용 코드는 함수만으로 문제풀이에 필요한 기능을 모듈화하는 경우가 많음
- 클래스와 같은 문법을 제외하고 코딩 테스트 합격에 필요한 문법 위주로 소개

## 1. 자료형

- 자료형에 대한 이해는 프로그래밍의 길에 있어서 첫걸음

### 1.1. 수 자료형

- 코딩 테스트에서 가장 기본적인 자료형
- 실제 코딩 테스트에서는 대부분 정수형을 다루는 문제가 출제
- 실수형을 다루는 문제는 출제 빈도가 낮음

#### 1.1.1. 정수형

- 정수를 다루는 자료형: 양의 정수, 음의 정수, 0
- 코딩 테스트의 알고리즘 문제는 대부분 입력과 출력 데이터가 정수형

```python
a = 1000 # 양의 정수
b = -7   # 음의 정수
c = 0    # 0
```

#### 1.1.2. 실수형

- 소수점 아래의 데이터를 포함하는 수 자료형
- 파이썬은 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리
- 소수부나, 정수부가 0인 실수는 0을 생략할 수 있음

```python
a = 157.93  # 양의 실수
b = -1837.2 # 음의 실수
c = 5.      # 소수부 0을 생략한 실수
d = -.7     # 정수부 0을 생략한 실수
```

`e`나 `E`를 이용한 지수 표현 방식: e 다음에 오는 수는 10의 지수부

> `1e9` == 10의 9제곱 == 1,000,000,000
>
> 유효숫자e<sup>지수</sup> = 유효숫자 × 10<sup>지수</sup>

지수 표현 방식은 코딩 테스트에서 많이 사용된다.

1. 최단 경로로 가능한 최댓값이 10억 미만이라면 무한(INF) 표현에 10억(`1e9`)을 사용할 수 있음
1. 큰수를 표현할 때 10억을 코드에 직접 입력하기 보다는 `1e9`로 표현하여 실수를 방지

> 큰수 표현시 `987,654,321`을 이용해 `1e9`와 유사한 큰수를 사용하기도 한다.

```python
a = 1e9     # 1000000000.0
b = 752.5e1 # 752.5
c = 3954e-3 # 3.954
```

부동소수점 문제(issue)

- 오늘날 가장 널리 쓰이는 IEEE754 표준에서는 실수형 저장에 4바이트 또는 8바이트 고정 크기의 메모리를 할당
- 이로 인해 현대 컴퓨터 시스템은 실수 정보 표현의 정확도에 한계가 있음
- 2진수에서는 `0.3`과 `0.6`을 더한 값인 `0.9`를 정확히 표현할 수 없음

```python
a = 0.3 + 0.6  # 0.8999999999999999

if a == 0.9
  print(True)
else
  print(False) # False
```

소수점 값을 비교할 경우 `round()` 함수 이용

> round(실수형 데이터, 반올림하고자 하는 위치 - 1)

```python
round(123.456, 2)      # 123.46
```

- 코딩 테스트에서는 실수형 데이터를 비교할 때 소수점 다섯 번째 자리에서 반올림한 결과가 같으면 정답으로 인정하는 식으로 처리

```python
a = 0.3 + 0.6

if round(a, 4) == 0.9:
  print(True)          # True
else
  print(False)
```

#### 1.1.3. 수 자료형의 연산

- 사칙연산: `+`, `-`, `×`, `/`
- 사칙연산 중 `/` 사용시 주의할 점: 나눠진 결과를 기본적으로 실수형으로 처리
- 나머지연산자: `%`
- 몫 연산자: `//`. 나눠진 결과에서 몫만을 얻고자 할 때 사용
- 거듭제곱 연산자: `**`

```python
a = 7
b = 3

print(a / b)  # 2.3333333333333335
print(a % b)  # 1
print(a // b) # 2

a = 5
b = 3
print(a ** b) # 125
```

### 1.2. 리스트 자료형

#### 1.2.1. 리스트 만들기

- 대괄호(`[]`)안에 원소를 넣어 초기화하며, 쉼표(`,`)로 원소를 구분
- 리스트 원소에 접근할 때는 인덱스(index) 값을 괄호 안에 넣음
- 인덱스는 `0`부터
- 빈 리스트 선언시 `list()` 혹은 `[]` 사용 가능

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 인덱스 4에 접근
print(a[4]) # 5

# 빈 리스트 선언
a = list()
print(a)   # []
a = []
print(a)   # []
```

코딩 테스트에서 주로 크기가 N인 1차원 리스트를 초기화해야 하는데 다음 방식으로 초기화 하면 편리하다.

```python
# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

#### 1.2.2. 리스트의 인덱싱과 슬라이싱

- 인덱싱(Indexing): 인덱스값을 입력하여 리스트의 특정 원소에 접근하는 것
- 파이썬의 인덱스 값은 양의 정수와 음의 정수 모두 사용 가능(음의 정수는 원소를 거꾸로 탐색)

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])                    # 9
print(a[-3])                    # 7
a[3] = 7
print(a)                        # [1, 2, 3, 7, 5, 6, 7, 8, 9]
```

- 슬라이싱(Slicing): 리스트에서 연속적인 위치를 갖는 원소들을 가져올 때 이용
- 대괄호 안에 콜론(`:`)을 넣어서 시작 인덱스와 끝 인덱스(-1)을 설정할 수 있음

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])                   # [2, 3, 4]
```

#### 1.2.3. 리스트 컴프리헨션

- 리스트 컴프리헨션: 리스트를 초기화하는 방법 중 하나
- 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화 할 수 있음

```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)                               # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

위 코드를 일반 문법으로 작성하면 아래와 같다.

```python
array = []
for i in range(20):
  if i % 2 == 1:
    array.append(i)

print(array)
```

```python
# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)                        # [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

코딩 테스트에 2차원 리스트를 초기화할 때 매우 효과적으로 사용 가능

```python
# N × M 크기의 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]
print(array) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

특정 크기의 2차원 리스트를 초기화 할 때는 반드시 리스트 컴프리헨션을 이용해야 한다.

```python
# N × M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array = [[0] * n] * m
print(array) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

array[1][1] = 5
print(array) # [[0, 5, 0], [0, 5, 0], [0, 5, 0], [0, 5, 0]]
```

내부적으로 포함된 4개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되어 오류가 발생한다.

#### 1.2.4. 리스트 관련 기타 메서드

주요 함수표

| 함수명      | 사용법            | 설명                               | 시간 복잡도 |
|-----------|------------------|-----------------------------------|----------|
| append()  | `변수명.append()` | 리스트에 원소를 하나 삽입                    | O(1) |
| sort()    | `변수명.sort()`  | 기본 정렬 기능으로 오름차순 정렬           | O(NlogN) |
|           | `변수명.sort(reverse=True)` | 내림차순 정렬               | O(NlogN) |
| reverse() | `변수명.reverse()` | 리스트 원소의 순서를 모두 뒤집음             | O(N) |
| insert()  | `insert(삽입할 위치 인덱스, 삽입값)` | 특정 인덱스 위치에 원소를 삽입 | O(N) |
| count()   | `변수명.count(특정값)` | 리스트에서 특정값ㅇ르 갖는 데이터의 개수 반환 | O(N) |
| remove()  | `변수명.remove(특정값)` | 특정값을 갖는 원소를 하나만 제거          | O(N) |

```python
a = [1, 4, 3]
print("기본 리스트: ", a)                   # 기본 리스트: [1, 4, 3]

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)                        # 삽입: [1, 4, 3, 2]

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)                 # 오름차순 정렬: [1, 2, 3, 4]

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)                 # 내림차순 정렬: [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)                  # 원소 뒤집기: [1, 2, 3, 4]

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)            # 인덱스 2에 3 추가: [1, 2, 3, 3, 4]

# 특정값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3)) # 값이 3인 데이터 개수: 2

# 특정값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)          # 값이 1인 데이터 삭제 [2, 3, 3, 4]
```

`insert()`, `append()`, `remove()`

- `insert()`: 원소의 개수가 N개면, 시간 복잡도는 O(N). 원소 삽입 후, 리스트의 원소 위치를 조정하기 때문에 남발하면 '시간 초과'가 될 수 있음
- `append()`: O(1)로 수행됨
- `remove()`: `insert()`와 마찬가지로 O(N)

특정한 값의 원소를 모두 제거할 경우 아래의 방법을 이용한다.

```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

# remove_set에 포함되지 않은 값만 저장
result = [i for i in a if i not in remove_set]
print(result)                                  # [1, 2, 4]
```

### 1.3. 문자열 자료형

#### 1.3.1. 문자열 초기화

- 문자열 변수 초기화에는 큰따옴표(`"`)와 작은따옴표(`'`) 이용
- 큰따옴표와 작은따옴표는 내부에 각각 작은따옴표와 큰따옴표를 사용할 수 있음
- 이스케이프 문자(`\`)를 이용해서 큰따옴표나 작은따옴표를 문자열에 포함시킬 수 있음

```python
data = 'Hello World'
print(data)                         # Hello World

data = "don't you know \"Python\"?"
print(data)                         # don't you know "Python"?
```

#### 1.3.2. 문자열 연산

- 덧셈(`+`)을 이용해 문자열을 연결할 수 있음
- 문자열 변수를 양의 정수와 곱하여 문자열을 반복할 수 있음

```python
a = "Hello"
b = "World"

print(a + " " + b) # Hello World

a = "String"
print(a * 3)       # StringStringString
```

- 파이썬의 문자열은 내부적으로 리스트처럼 처리됨
- 문자열은 여러 개의 문자가 합쳐진 리스트라고 볼 수 있음
- 문자열 데이터에도 인덱싱과 슬라이싱을 할 수 있음

```python
a = "ABCDEF"
print(a[2 : 4]) # CD
```

### 1.4. 튜플 자료형

- 리스트와 유사하지만 확실한 차이점이 있음
- 한 번 선언된 값을 변경할 수 없음
- 튜플은 소괄호(`()`)를 이용

```python
a = (1, 2, 3, 4)
print(a)         # (1, 2, 3, 4)
a[2] = 7
                 # Traceback (most recent call last):
                 #  File "<stdin>", line 1, in <module>
                 # TypeError: 'tuple' object does not support item assignment
```

- 그래프 알고리즘을 구현할 때 자주 사용
- 다익스트라 알고리즘 등 최단 경로 알고리즘에서는 우선순위 큐를 활용하는데 큐에 한 번 들어간 값은 불변
- 변경되면 안되는 값을 변경하는 경우를 체크할 수 있음
- 리스트에 비해 공간 효율성이 좋음
- 각 원소의 성질이 서로 다를 때 주로 사용
- 예: 다익스트라 알고리즘에서 서로 다른 성질의 데이터를 `(비용, 노드 번호)` 형태로 묶어 관리함

### 1.5. 사전 자료형

#### 1.5.1. 사전 자료형 소개

- 키(key)와 값(value)의 쌍을 데이터로 갖는 자료형
- 변경 불가능한 데이터를 키로 사용할 수 있음
- 사전 자료형은 내부적으로 해시 테이블(Hash Table)을 이용, O(1)의 시간복잡도
- 키-값 쌍으로 구성된 데이터를 처리하는데 리스트보다 훨씬 빠르게 동작할 수 있음

> 변경 불가능한 자료형: 수, 문자열, 튜플 자료형처럼 한 번 초기화되면 변경이 불가능한 자료형을 의미한다. 튜플 자료형이 사전 자료형의 키로 사용되기도 하는데 이는 "Q22. 블록 이동하기"에서 사용됨

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)             # {'바나나': 'Banana', '사과': 'Apple', '코코넛': 'Coconut'}
```

- 사전 자료형은 코딩 테스트에서 자주 사용됨
- 학생의 번호가 1~10,000,000인 경우에 10,000명의 학생이 선택됐을 때 10,000개의 데이터만 사전 자료형에 대입하면 훨씬 적은 메모리 공간을 사용할 수 있음
- 사전 자료형의 조회는 '원소 in 사전' 형태를 사용하며 리스트와 튜플에서도 사용 가능한 문법

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
  printf("사과를 키로 갖는 데이터가 존재합니다.") # 사과를 키로 갖는 데이터가 존재합니다.
```

#### 1.5.2. 사전 자료형 관련 함수

- `keys()`: 키 데이터만 뽑아서 리스트로 이용
- `values()`: 값 데이터만 뽑아서 리스트로 이용

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)            # ['사과', '바나나', '코코넛']
print(value_list)          # ['Banana', 'Apple', 'Coconut']

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])         # Apple
                           # Banana
                           # Coconut
```

### 1.6. 집합 자료형

#### 1.6.1. 집합 자료형 소개

- 리스트 혹은 문자열을 이용해서 만들 수 있음
- 중복을 허용하지 않음
- 순서가 없음
- 키 없이 값 데이터만을 담는다.
- 특정 원소 조회의 시간 복잡도는 O(1)

사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.

```python
# 집합 자료형 초기화1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)                       # {1, 2, 3, 4, 5}

# 집합 자료형 초기화2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)                       # {1, 2, 3, 4, 5}
```

#### 1.6.2. 집합 자료형의 연산

- 합집합, 교집합, 차집합 연산

```python
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)             # {1, 2, 3, 4, 5, 6, 7}
# 교집합
print(a & b)             # {3, 4, 5}
# 차집합
print(a - b)             # {1, 2}
```

#### 1.6.3. 집합 자료형 관련 함수

- `add()`: 집합 데이터에 값 추가
- `update()`: 여러 개의 값을 한꺼번에 추가
- `remove()`: 특정 값을 제거
- `add()`와 `remove()`는 모두 O(1) 시간복잡도

## 2. 조건문

```python
if 조건문1:
  조건문1 True일때 실행
elif 조건문2:
  조건문1 False, 조건문2 True일때 실행
else:
  모든 조건이 False일때 실행
```

```python
score = 85

if score >= 90:
  pirnt("학점: A")
elif score >= 80:
  pirnt("학점: B")
elif score >= 70:
  pirnt("학점: C")
else:
  pirnt("학점: F")
```

조건이 참일 경우, 들여쓰기가 같은 코드는 함께 실행된다.

> 파이썬의 들여쓰기는 스페이스바 4번 입력이 사실상의 표준이다.

### 2.1. 비교 연산자

| 비교 연산자 | 설명                       |
|----------|---------------------------|
| X == Y   | X와 Y가 서로 같을 때 True     |
| X != Y   | X와 Y가 서로 다를 때 True     |
| X > Y    | X가 Y보다 클 때 True         |
| X < Y    | X가 Y보다 작을 때 True       |
| X >= Y   | X가 Y보다 크거나 같을 때 True  |
| X <= Y   | X가 Y보다 작거나 같을 때 True  |

### 2.2. 논리 연산자

| 논리 연산자 | 설명                       |
|----------|---------------------------|
| X and Y  | X와 Y가 모두 참일 때 True     |
| X or Y   | X와 Y 중에 하나만 참이어도 True |
| not X    | X가 False일 때 True         |

### 2.3. 파이썬의 기타 연산자

| 연산자              | 설명                       |
|-------------------|---------------------------|
| X in List         | 리스트 안에 X가 있으면 True    |
| X not in String   | 문자열 안에 X가 없으면 True    |

조건문이 True일 때 아무것도 처리하지 않고 싶다면 `pass`문을 사용할 수 있다.

```python
socre = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')      # 프로그램을 종료합니다.
```

조건문의 실행할 코드가 한 줄인 경우, 간략히 표현할 수 있다.

```python
score = 85

if score >= 80: result = "Success"
else: result = "Fail"
```

조건부 표현식

```python
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)                                 # Success
```

리스트에 있는 원소의 값을 변경해서 또 다른 리스트를 만들 때 조건부 표현식으로 간결하게 할 수 있다.

```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)                                  # [1, 2, 4]
```

> 파이썬은 `0 < x < 20`과 같은 연산도 가능하다. 하지만 이 책에서는 다른 언어에서처럼 논리 연산자를 사용한다.

## 3. 반복문

실제 사용 예시를 보면 for 문이 소스코드가 짧은 경우가 많다.

### 3.1. while문

무한 루프를 주의해야 한다.

```python
i = 1
result = 0

# i <= 9일 때 반복 실행
while i <= 9:
    result += i
    i += 1

print(result)        # 45
```

### 3.2. for문

- `for ~ in`이며 `in` 뒤에는 리스트, 튜플, 문자열 등이 사용됨
- for문에서 수를 나열할 때는 `range()`를 주로 쓴다.

> `range(시작값, 끝값 + 1)`

```python
result = 0

for i in range(1, 10):
    result += i

print(result)          # 45
```

`range(값)`으로 사용하면 시작값은 `0`이 된다. 리스트 조회시 주로 사용

```python
scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")
```

중첩된 반복문은 '플로이드 워셜 알고리즘', '다이내믹 프로그래밍' 등 알고리즘 문제에서 매우 많이 사용한다.

```python
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()
```

## 4. 함수

```python
def 함수명(매개변수):
    실행할 소스코드
    return 반환값
```

```python
def add(a, b):
    return a + b

print(add(3, 7)) # 10
```

`return` 없이 함수 작성도 가능하다.

함수 호출시 인자(Argument)를 넘겨줄 때 파라미터 변수를 직접 지정할 수 있다.

```python
def add(a, b):
    print('함수의 결과:', a + b)
add(b = 3, a = 7)             # 10
```

`global` 키워드로 변수를 지정하면 함수 밖에서 선언된 변수를 바로 참조할 수 있다.

```python
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)            # 10
```

람다 표현식(Lambda Expression)을 이용하면 함수를 간단하게 작성하여 적용할 수 있다. 파이썬의 정렬 라이브러리를 사용할 때, 람다 표현식은 정렬 기준(Key)을 설정할 때에도 자주 사용된다.

```python
def add(a, b):
    return a + b

# add() 매서드 사용
print(add(3, 7))                 # 10

# 람다 표현식 사용
print(lambda a, b: a + b)(3, 7)) # 10
```

## 5. 입출력

일반적인 입력 과정

- 먼저 데이터의 개수가 첫번째 줄에 주어짐
- 그 다음 줄에 처리할 데이터가 주어짐
- 학생 성적 내림차순 정렬 문제의 경우: 첫번째 줄에 학생 수, 두번째 줄에 학생의 정보를 공백으로 구분 출력

```txt
입력 예시
5
65 90 75 34 99

출력 예시
99 90 75 65 34
```

- `input()`: 데이터를 입력받을 때 사용, 한 줄의 문자열을 입력받도록 해줌
- 입력 받은 데이터를 정수형 데이터로 처리하려면 `int()` 함수로 형변환 해야함

여러 개의 데이터가 공백으로 구분돼 들어오는 경우가 많으므로 아래처럼 정수 자료형의 데이터로 리스트에 저장할 수 있다.

```python
list(map(int, input().split()))
```

위에서는 `map()`을 이용해 `int()` 함수를 적용한다.

입력을 위한 전형적인 소스 코드

```python
# 데이터 개수 입력
n = int(input())                        # 5
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))  # 60 90 75 34 99

data.sort(reverse = True)
print(data)                             # [99, 90, 75, 60, 34]
```

`n`, `m`, `k`가 공백으로 구분되어 입력된다는 내용이 명시됐을 경우 아래처럼 사용 가능하다.

```python
# n, m, k를 구분하여 입력
n, m, k = map(int, input().split()) # 3 5 7

print(n, m, k)                      # 3 5 7
```

입력을 최대한 빠르게 받아야 하는 경우(정렬, 이진 탐색, 최단경로 등), 많은 수의 데이터가 연속적으로 입력이 된다. 1,000만 개가 넘는 라인이 입력되는 경우, 입력만으로도 시간 초과가 생길 수 있다.

사용하는 언어별로 입력을 빠르게 받는 방법을 알아야 한다. C++은 `cin`보다 `scanf()` 사용이 권장된다.

파이썬의 경우 `input()` 대신 `sys.stdin.readline()` 함수를 이용한다.

```python
import sys
sys.stdin.readline().rstrip()
```

sys 라이브러리를 사용할 때는 한 줄 입력받은 후 `rstrip()` 함수를 꼭 호출해야 한다. `rstrip()`으로 `readline()`으로 입력된 엔터(Enter)가 줄바꿈 기호로 들어오는 것을 제거한다. 이것 역시 관행적으로 사용하는 코드다.

```python
import sys

# 문자열 입력받기
data = sys.stdin.readline().rstrip() # Hello World
print(data)                          # Hello World
```

변수를 문자열과 함께 출력하려면 `str()`을 사용한다.

```python
answer = 7

print("정답은 " + str(answer) + "입니다.") # 정답은 7입니다.
```

콤마를 이용하면 변수의 값 사이에 공백이 삽입된다.

```python
answer = 7

print("정답은", str(answer), "입니다.") # 정답은 7입니다.
```

f-string 문법

```python
answer = 7
printf("정답은 {answer}입니다.") # 정답은 7입니다.
```

## 6. 주요 라이브러리의 문법과 유의점

표준라이브러리: 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리

코딩 테스트에서는 대부분 표준 라이브러리를 사용할 수 있도록 허용하므로 표준 라이브러리를 사용하면 소스코드 작성량에 대한 부담을 줄일 수 있다.

코딩 테스트를 준비하며 반드시 알아야하는 라이브러리들

- 내장 함수: `print()`, `input()`, `sorted()` 등 필수 기능 포함
- itertools: 반복되는 형태의 데이터를 처리하는 기능을 제공. 순열과 조합 라이브러리 제공
- heapq: 힙(Heap) 기능을 제공. 우선순위 큐 기능을 구현하기 위해 사용
- bisect: 이진 탐색(Binary Search) 기능을 제공하는 라이브러리
- collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리
- math: 필수적인 수학적 기능을 제공하는 라이브러리. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 메서드부터 파이(pi)와 같은 상수를 포함

### 6.1. 내장 함수

대표적인 내장 함수

- `input()`
- `print()`
- `sum()`: iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환

```python
result = sum([1, 2, 3, 4, 5])
print(result)                 # 15
```

- `min()`: 파라미터가 2개 이상 들어왔을 때, 가장 작은 값을 반환
- `max()`: 파라미터가 2개 이상 들어왔을 때, 가장 큰 값을 반환

```python
result = min([7, 3, 5, 2])
print(result)              # 2

result = max([7, 3, 5, 2])
print(result)              # 7
```

- `eval()`: 수학 수식이 문자열 형식으로 입력되면, 해당 수식을 계산한 결과를 반환

```python
result = eval("(3 + 5) * 7)")
print(result)                 # 56
```

- `sorted()`: iterable 객체가 입력되면, 정렬된 결과를 반환. key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지 여부를 설정할 수 있음

```python
result = sorted([9, 1, 8, 5, 4]) # 오름차순
print(result)                                    # [1, 4, 5, 8, 9]

result = sorted([9, 1, 8, 5, 4], reverse = True) # 내림차순
print(result)                                    # [9, 8, 5, 4, 1]

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)        # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
```

리스트와 같은 iterable 객체는 기본으로 `sort()` 메서드를 내장하고 있다. 이를 이용하면 리스트 내부의 값을 정렬된 값으로 변환할 수 있다.

```python
data = [9, 1, 8, 5, 4]
data.sort()
print(data)            # [1, 4, 5, 8, 9]
```

### 6.2. itertools

- 반복되는 데이터를 처리하는 기능을 포함
- 코딩 테스트에서 유용하게 사용하는 클래스: `permutations`, `combinations`

`permutations`: 순열

- iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
- 클래스이므로 객체 초기화 이후 리스트 자료형으로 변환하여 사용함

```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기

print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```

`combinations`: 조합

- iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) 계산

```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

`product`: 순열(중복 허용)

- iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수(순열)를 계산
- 원소를 중복하여 뽑음
- `product` 객체를 초기화할 때는 뽑고자 하는 데이터의 값을 repeat 속성값으로 입력

```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

`combinations_with_replacement`

- iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산
- 원소를 중복하여 뽑음

```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, repeat=2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)

print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

### 6.3. heapq

- Heap 기능에 활용
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
- `PriorityQueue 라이브러리도 사용 가능하지만 코딩 테스트 환경에서는 보통 heapq가 빠름
- 파이썬의 힙은 최소 힙(Min Heap)이므로 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료(보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은' 원소)
- `heapq.heappush()`: 힙에 원소 삽입
- `heapq.heappop()`: 힙에서 원소 꺼내기

```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)                                   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- 파이썬에서는 최대 힙(Max Heap)을 제공하지 않음
- 최대 힙을 위해 원소의 부호를 임시로 변경하여 힙에 저장하고, 꺼낸 뒤 부호를 변경함

```python
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)                                   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### 6.4. bisect

- 이진 탐색을 쉽게 구현할 수 있도록 제공
- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용
- `bisect_left()`, `bisect_right()`가 중요하게 사용되며 시간 복잡도는 O(logN)
- `bisect_left(a, x)`: 정렬 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
- `bisect_right(a, x)`: 정렬 순서를 유지하면서 리스트 a에 데이터 x를 십입할 가장 오른쪽 인덱스를 찾음

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))  # 2
print(bisect_right(a, x)) # 4
```

- '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때 `bisect_left()`와 `bisect_right()`를 효과적으로 사용할 수 있음

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))       # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))      # 6
```

### 6.5. collections

- 유용한 자료구조를 제공하는 표준 라이브러리
- `deque`와 `Counter`가 코딩 테스트에 유용하게 사용

- 파이썬에서는 `deque`를 사용해 큐를 구현
- 별도로 제공되는 Queue 라이브러리가 있는데 일반적인 큐 자료구조를 구현하는 라이브러리는 아님
- 큐를 이용할 때는 `queue`를 이용해 큐를 구현하는 것을 명심

|                      | 리스트 | deque |
|----------------------|------|------|
| 가장 앞쪽에 원소 추가     | O(N) | O(1) |
| 가장 뒤쪽에 원소 추가     | O(1) | O(1) |
| 가장 앞쪽에 있는 원소 제거 | O(N) | O(1) |
| 가장 뒤쪽에 있는 원소 제거 | O(1) | O(1) |

- `deque`는 인덱싱, 슬라이싱 등의 기능이 없음
- 연속적으로 나열된 데이터의 시작이나 끝 부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적
- 스택이나 큐의 기능을 모두 포함하므로 스택 혹은 큐 자료구조의 대용으로 사용 가능

- `popleft()`: 첫번째 원소를 제거
- `pop()`: 마지막 원소 제거
- `appendleft(x)`: 첫번째 인덱스에 원소 x를 삽입
- `append(x)`: 마지막 인덱스에 원소 x를 삽입

```python
from collections import deque

data = deque([2, 3, 4, 5])
data.appendleft(1)
data.appen(5)

print(data)
print(list(data))
```

`Counter`: iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])  # 3
print(counter['green']) # 1
print(dict(counter))    # {'red': 2, 'blue': 3, 'green': 1}
```

### 6.6. math

- 팩토리얼, 제곱근, 최대공약수(GCD) 등을 계산해주는 기능을 포함
- `factorial(x)`: x! 값을 반환
- `sqrt(x)`: x의 제곱근을 반환
- `gcd(a, b)`: a와 b의 최대 공약수 반환
- `pi`, `e`: 각각 파이 값과 자연상수 e 값 반환

```python
import math

print(math.factorial(5)) # 120
print(math.sqrt(7))      # 2.645751310645907
print(math.gcd(21, 14))  # 7
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045
```

## 7. 자신만의 알고리즘 노트 만들기

- 저자의 파이썬 전용 팀 노트: [https://github.com/ndb796/Python-Competitive-Programming-Team-Notes](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes)
