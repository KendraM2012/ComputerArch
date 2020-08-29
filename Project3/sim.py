global_cycle = 0
from helpers import SetUp
import writeBack
import cache
import alu
import memory
import issue
class simClass():

    def __init__(self, instructions, opcode, opcodeStr, dataval, address, arg1, arg2, arg3, arg1Str,
                 arg2Str, arg3Str,numInstructs, destReg, src1Reg, src2Reg):
        self.instruction = instructions
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructions = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.opcodeStr = opcodeStr
        self.PC = 96
        self.cycle = 1
        self.cycleList =[0]
        self.R = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0]
        self.postMemBuff = [-1, -1]  # first number is value, second is instr index
        self.postALUBuff = [-1, -1]  # first number is value, second is instr index
        self.preMemBuff = [-1, -1]
        self.preALUBuff = [-1, -1]
        self.preIssueBuff = [-1, -1, -1, -1]

        self.WB = writeBack.WriteBack(self.R, self.postMemBuff, self.postALUBuff, destReg)
        self.cache = cache.Cache(numInstructs, instructions , dataval, address)
        self.ALU = alu.ALU(self.R, self.postALUBuff, self.preALUBuff, opcodeStr, arg1, arg2, arg3)
        self.MEM = memory.Memory(self.R, self.postMemBuff, self.preMemBuff, opcodeStr, arg1, arg2, arg3, dataval, address, self.numInstructions, self.cache,self.cycleList
                                 ,instructions)
        self.issue = issue.Issue(instructions, opcodeStr, dataval, address, arg1, arg2, arg3, self.numInstructions, destReg, src1Reg, src2Reg,
                                 self.R,self.preIssueBuff,self.preMemBuff,self.postMemBuff,self.preALUBuff,self.postALUBuff)
        #self.fetch = fetch.Fetch(instrucions, opcodeStr, dataval, address, arg1, arg2, arg3,self.numInstructions, destReg, src1Reg, src2Reg,
                            #     self.R, self.preIssueBuff, self.preMemBuff,self.postMemBuff, self.preALUBuff,self.postALUBuff,
                            #     self.PC, self.cache)

        self.outputFileName = SetUp.get_output_filename()


    def run(self):
        go = True
        while go:
            self.WB.run()
            self.ALU.run()
            #self.MEM.run()
            #self.issue.run()
            #go = self.fetch.run()
            self.printState()
            self.cycle += 1

    def printState(self):
        with open(self.outputFileName + "_pipeline.txt",'a') as outFile:
            outFile.write("--------------------\n")
            outFile.write("Cycle:" + str(self.cycle) + "\n")
            outFile.write("Pre_ALU Queue:\n")
            if self.preALUBuff[0] != -1:
                 outFile.write("\tEntry 0:" + "\t"+ "[" + self.opcodeStr[self.preALUBuff[0]] + "\t" + self.arg1Str[self.preALUBuff[0]] + self.arg2Str[self.preALUBuff[0]] + self.arg3Str[self.preAluBuff[0]] + "]\n")
            else:
                 outFile.write( "\tEntry 0:" + "\t\n")
            if self.preALUBuff[1] != -1:
                outFile.write("\tEntry 1:" + "\t"+ "[" + self.opcodeStr[self.preALUBuff[1]] + "\t" + self.arg1Str[self.preALUBuff[1]] + self.arg2Str[self.preALUBuff[1]] + self.arg3Str[self.preALUBuff[1]] + "]\n")
            else:
                outFile.write("\tEntry 1:" + "\t\n")

            outFile.write("Post_ALU Queue\n")
            if self.postALUBuff[0] != -1:
                outFile.write("\tEntry 0:" + "\t" + "[" + self.opcodeStr[self.postALUBuff[1]] + "\t" + self.arg1Str[self.postALUBuff[1]] + self.arg2Str[self.postALUBuff[1]] + self.arg3Str[self.postALUBuff[1]] + "]\n")
            else:
                outFile.write( "\tEntry 0:" + "\t\n")

            outFile.write( "Pre_MEM Queue\n")
            if self.preMemBuff[0] != -1:
                outFile.write( "\tEntry 0:" + "\t"+ "[" + self.opcodeStr[self.preMemBuff[0]] + "\t" + self.arg1Str[self.preMemBuff[0]] + self.arg2Str[self.preMemBuff[0]] + self.arg3Str[self.preMemBuff[0]] + "]\n")
            else:
                outFile.write( "\tEntry 0:" + "\t\n")
            if self.preMemBuff[1] != -1:
                outFile.write( "\tEntry 1:" + "\t"+"[" + self.opcodeStr[self.preMemBuff[1]] + "\t" + self.arg1Str[self.preMemBuff[1]] + self.arg2Str[self.preMemBuff[1]] + self.arg3Str[self.preMemBuff[1]] + "]\n")
            else:
                outFile.write( "\tEntry 1:" + "\t\n")

            outFile.write("Post_MEM Queue\n")
            if self.postMemBuff[0] != -1:
                outFile.write("\tEntry 0:" + "\t"+ "[" + self.opcodeStr[self.postMemBuff[1]] + "\t" + self.arg1Str[self.postMemBuff[1]] + self.arg2Str[self.postMemBuff[1]] + self.arg3Str[self.postMemBuff[1]] + "]\n")
            else:
                outFile.write( "\tEntry 0:" + "\t\n")
