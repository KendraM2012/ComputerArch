
class ALU:

    def __init__(self,R,postALUBuff,preALUBuff,opcodeStr,arg1,arg2,arg3):
        self.R = R
        self.postALUBuff = postALUBuff
        self.preALUBuff = preALUBuff
        self.opcodeStr = opcodeStr
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def run(self):
        if self.preALUBuff[0] == -1:
            pass
        i = 0
        if self.opcodeStr[i] == "ADD":
            self.postALUBuff = [self.R[self.arg1[i]]] + self.R[self.arg2[i]]
        if self.opcodeStr[i] == "SUB":
            self.postALUBuff = [self.R[self.arg1[i]]] - self.R[self.arg2[i]]
        if self.opcodeStr[i] == "ADDI":
             self.postALUBuff[0] = int(self.R[self.arg1[self.preALUBuff[0]]] + self.arg2[self.preALUBuff[0]])
             self.postALUBuff[1] = self.preALUBuff[0]
        if self.opcodeStr[i] == "SUBI":
            self.postALUBuff = [self.R[self.arg1[i]]] - self.R[self.arg2[i]]
        if self.opcodeStr[i] == "AND":
            self.postALUBuff = [self.R[self.arg1[i]]] & self.R[self.arg2[i]]
        if self.opcodeStr[i] == "OR":
            self.postALUBuff = [self.R[self.arg1[i]]] | self.R[self.arg2[i]]
        if self.opcodeStr[i] == "EOR":
            self.postALUBuff = [self.R[self.arg1[i]]] ^ self.R[self.arg2[i]]
        if self.opcodeStr[i] == "LSL":
            self.postALUBuff = [self.R[self.arg2[i]]] << self.R[self.arg3[i]]
        if self.opcodeStr[i] == "LSR":
            self.postALUBuff = ([self.R[self.arg2[i]]] %(1 << 64)) >> self.R[self.arg1[i]]
        if self.opcodeStr[i] == "ASR":
            self.postALUBuff = [self.R[self.arg1[i]]] >> self.R[self.arg2[i]]
        if self.opcodeStr[i] == "MOVK":
            self.postALUBuff += ([self.R[self.arg1[i]]] << (self.R[self.arg2[i]] *16))
        if self.opcodeStr[i] == "MOVZ":
            self.postALUBuff = [self.R[self.arg1[i]]] << (self.R[self.arg2[i]]*16)
        self.preALUBuff[0] = self.preALUBuff[1]
        self.preALUBuff[1] = -1
