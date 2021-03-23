class CounterManager:
	insCount = 0
	def __init__(self):		 #인스턴스 생성할 때 마다 1 증가
		CounterManager.insCount += 1 #클래스 객체의 변수
	def printInstanceCount(): 	#self를 정의하지 않았음
				#인스턴스 객체 개수 출력
		print("Instance Count: ", CounterManager.insCount)
a,b,c = CounterManager(), CounterManager(), CounterManager()
