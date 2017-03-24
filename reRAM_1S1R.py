class ReRAM_1S1R:

	def __init__(self, wordlineCount, bitlineCount):
		self.__reRAMArray = [[0 for i in range(bitlineCount)] \
							 for j in range(wordlineCount)]
		self.__deviceType = '1S1R device'
		self.__wordlineCount = wordlineCount
		self.__bitlineCount = bitlineCount
	
	def getDevice(self):
		return self.__reRAMArray
	
	
	def getElement(self, wordlineAddr, bitlineAddr):
		if(wordlineAddr >= self.__wordlineCount):
			raise Exception("Invalid wordline provided. (wl <"+str(wordlineAddr)+") required")
		
		if(bitlineAddr >= self.__bitlineCount):
			raise Exception("Invalid bitline provided. (bl <"+str(bitlineAddr)+") required")
			
		return self.__reRAMArray[wordlineAddr][bitlineAddr]
	
	
	def updateElement(self, wordlineAddr, bitlineAddr, currState):
		if(wordlineAddr == 1 and bitlineAddr == -1):
			return 1
		elif(wordlineAddr == -1 and bitlineAddr == 1):
				return 0
		else:
			return currState
		
			
	def updateDevice(self, addr):
		'''
		@param address: wordline(s) followed by bitline(s) address(es)
		'''
		if(len(addr) != self.__wordlineCount + self.__bitlineCount):
				raise Exception('Invalid address passed \n Address length should be equal to wordlineCount + bitlineCount')
		else:
			''' Update the element array '''
			
			for wl in range(self.__wordlineCount):
				for bl in range(self.__bitlineCount):
					self.__reRAMArray[wl][bl] = self.updateElement(addr[wl],\
							addr[self.__wordlineCount+bl],self.__reRAMArray[wl][bl])
	
	
	def displayDevice(self):
		for wl in range(self.__wordlineCount):
			for bl in range(self.__bitlineCount):
				print(self.__reRAMArray[wl][bl] ," ",end="")
			print("")

			
if __name__ == "__main__":
	print('simulating a single array of 1S1R devices')
	U = ReRAM_1S1R(1,4)
	U.displayDevice()
	U.updateDevice([-1,1,1,1,1])
	U.displayDevice()
	U.updateDevice([1,-1,-1,-1,0])
	U.displayDevice()
	print(U.getElement(0,1))
	print(U.getElement(0,2))
	print(U.getElement(0,3))
	
	
	
