class GString:
	str = ""			#클래스 멤버 변수
	def Set(self, msg):
		self.str = msg
	def Print(self):
		print(str)		#self가 누락되면 전역변수 접근
