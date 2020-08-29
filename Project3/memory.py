import cache
class Memory:
    def __init__(self,R,postMemBuff,preMemBuff,opcodeStr,arg1,arg2,arg3,dataval,address,numInstructions,
                 cache,cycleList, instructions):
        self.R = R
        self.postMemBuff = postMemBuff
        self.preMemBuff = preMemBuff
        self.opcodeStr = opcodeStr
        self.numInstructions = numInstructions
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.dataval = dataval
        self.address = address
        self.cache = cache
        self.cycleList = cycleList
        self.instructions = instructions

    def run(self):
        isSw = False
        isLD = False

        if self.opcodeStr[self.preMemBuff[0]] == "STUR":
            isSw = True

        if self.opcodeStr[self.preMemBuff[0]] == "LDUR":
            isLD = True

        data = cache.Cache.checkCache(self.preMemBuff[0],self.preMemBuff[0],isSw,self.R[self.preMemBuff[0]])

        if data and isLD:
            self.postMemBuff = data[1]
            self.postMemBuff[1] = self.preMemBuff[0]
        if data:
            self.preMemBuff[0] = self.preMemBuff[1]
            self.preMemBuff[1]
