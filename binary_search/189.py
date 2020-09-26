#재귀로 구현한 이진 탐색 소스코드
#이진 탐색은 정렬이 되어 있어야 가능

def binary_search(array,target,start,end) :
  if start > end :
    return None

  #중간점
  mid = (start + end) // 2

  #중간점이 찾는 값인 경우
  if array[mid] == target :
    return mid

  #중간점의 값보다 찾고자 하는 값이 작은 경우 -> 왼쪽 탐색
  elif array[mid] > target :
    return binary_search(array,target,start,mid-1)

  #중간점의 값보다 찾고자 하는 값이 큰 경우 -> 오른쪽 탐색
  else :
    return binary_search(array,target,mid+1,end)


# n : 원소의 개수 / target : 찾고자 하는 값
n,target = map(int,input().split())

#전체 원소 입력
array = list(map(int,input().split()))

#결과
result = binary_search(array,target,0,n-1)

if result == None :
  print("찾는 원소값이 존재하지 않습니다")
else :
  print(result + 1)