class Jar:
	def __init__(self, capacity=12):
		if int(capacity) < 0:
			raise ValueError
		else:
			self.__size = 0
			self.__capacity = capacity

	def __str__(self):
		return "\U0001F36A" * self.__size

	def deposit(self, n):
		if self.__size + n > self.__capacity:
			raise ValueError
		else:
			self.__size += n

	def withdraw(self, n):
		if n > self.__size:
			raise ValueError
		else:
			self.__size -= n

	@property
	def capacity(self):
		return self.__capacity

	@property
	def size(self):
		return self.__size
