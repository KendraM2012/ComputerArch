
class WriteBack():
    def __init__(self,R,postMemBuff,postALUBuff,destReg):
        self.R = R
        self.postMemBuff = postMemBuff
        self.postALUBuff = postALUBuff
        self.destReg = destReg


    def run(self):

       if self.postALUBuff[0] != -1 and self.postALUBuff[1] != -1:
           self.R[self.destReg[self.postALUBuff[1]]] = self.postALUBuff[0]
           self.postALUBuff[0] = -1
           self.postALUBuff[1] = -1

       if self.postMemBuff[0] != -1 and self.postMemBuff[1] != -1:
            self.R[self.destReg[self.postMemBuff[1]]] = self.postMemBuff[0]
            self.postMemBuff[0] = -1
            self.postMemBuff[1] = -1
       print(self.postALUBuff)
       print(self.postMemBuff)
