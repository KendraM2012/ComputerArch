import sys
from helpers import SetUp
import masking_constants as MASKs

class State():
    dataval = [] #not needed but for clarity that is part of state
    PC = 96
    cycle =1
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcode, dataval, addrs, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        #self.instructions = instrs
        self.opcode = opcode
        self.dataval = dataval
        self.address = addrs
        self.numInstructions = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str

    def getIndexOfMemAddress(self, currAddr):
        #TODO
        #this figures out which "i" is associated with a mem address like 96
        return int((currAddr - 96)/4)

    def incrementPC(self):
        self.PC = self.PC +4
    def printState(self):
        outputFileName = SetUp.get_output_filename()
        with open(outputFileName + "_sim.txt",'a') as outFile:
            i = self.getIndexOfMemAddress(self.PC)
            outFile.write("====================\n")
            outFile.write("cycle:" + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[i] +"\t"+ self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n")
            outFile.write("registers:\n")
            outStr = "r00:"
            for i in range(0, 8):
                outStr = outStr + "\t" +str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r08:"
            for i in range(8,16):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outStr = "r16:"
            for i in range(16, 24):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")
            outFile.write("\ndata:\n")
            outStr="\n"
            for i in range(len(self.dataval)):

                if(i % 8 == 0 and i != 0 or i == len(self.dataval)):
                    outFile.write(outStr + "\n")

                if i % 8 == 0:
                    outStr = str(self.address[i + self.numInstructions]) + ":" + str(self.dataval[i])

                if (i % 8 != 0):
                    outStr = outStr + "\t" + str(self.dataval[i])

            outFile.write(outStr + "\n")
            outFile.close()


class Simulator():

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.specialMask = MASKs.specialMask

    def run(self):
        foundBreak = False
        armState = State (self.opcode, self.dataval,self.address, self.arg1, self.arg2, self.arg3,
                          self.numInstructs, self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str)

        while (foundBreak == False):
            jumpAddr = armState.PC
            #get next instruction
            i = armState.getIndexOfMemAddress(armState.PC)
            #TODO test and delete the need for instructions
            #if self.instructions[i] == '00000000000000000000000000000000': #NOP this might be wrong
            if(self.opcode[i] == 0): #NOP
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue #go right back to top
            elif(self.opcode[i] >= 160 and self.opcode[i] <= 191): #B
                jumpAddr = jumpAddr + ((self.arg1[i] * 4) -4) #-4 takes care of PC late
            #TODO test and delete the need for instructions
            elif(self.opcode[i] == 1160 or self.opcode[i] == 1161):#ADDI
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] + self.arg1[i]
            elif(self.opcode[i] == 1672 or self.opcode[i] == 1673):#SUBI
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] - self.arg1[i]
            elif(self.opcode[i] == 1112):#ADD
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] + armState.R[self.arg1[i]]
            elif(self.opcode[i] == 1624):#SUB
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] - armState.R[self.arg1[i]]
            elif(self.opcode[i] == 1104):#AND
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] & armState.R[self.arg1[i]]
            elif(self.opcode[i] == 1360):
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] | armState.R[self.arg1[i]]
            elif(self.opcode[i] == 1690):
                armState.R[self.arg3[i]] = (armState.R[self.arg2[i]] % (1 << 64)) >> armState.R[self.arg1[i]]
            elif(self.opcode[i] == 1691):
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] << armState.R[self.arg1[i]]
            elif(self.opcode[i] == 1872):
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] ^ armState.R[self.arg1[i]]
            elif(1440 <= self.opcode[i] <= 1447):#CBZ
                if armState.R[self.arg2[i]] == 0:
                    jumpAddr = jumpAddr + self.arg1[i] * 4
            elif(1448 <= self.opcode[i] <= 1455):#CBNZ
                if armState.R[self.arg2[i]] != 0:
                    jumpAddr = jumpAddr + self.arg1[i] * 4
            elif(1684 <= self.opcode[i] <= 1687):#MOVZ
                armState.R[self.arg3[i]] = int(self.arg2[i] * 2 ** self.arg1[i])
            elif(1940 <= self.opcode[i] <= 1943):#MOVK
                armState.R[self.arg3[i]] = int(armState.R[self.arg3[i]] + self.arg2[i] * 2 ** self.arg1[i])
            #add the offset in address register to RN to get target address. Either load value in Rd into address
            #or get value at address and put into Rd
            elif(self.opcode[i] == 1986):#LUDR
                #NEEDSDONE
                #load value from arg1 (rn) + arg2 (imm), find address value in dataval and load into rd (arg3)
                index = 0
                for k in range(len(self.address)):
                    if int(self.address[k]) == armState.R[self.arg1[i]] + self.arg2[i] *4:
                        index = k
                armState.R[self.arg3[i]] = self.dataval[index]

            #stores can put values into any address after the break address and are not limited to the values originally
            #in data file, aka if there was no data originally you can store data and create values
            elif(self.opcode[i] == 1984):#STUR
                #NEEDS DONE
                #append or replace value in dataval[], store value from arg3 (rd) to arg1 (rn) + arg2 (imm)
                #adds register value in Rd in R[]
                #armState.R[self.arg3[i]]= int(self.arg3[i])
                #test if target in address[]
                target = armState.R[self.arg1[i]] + self.arg2[i]
                for a in range(len(self.address)):
                    # if yes, find index and place in dataval,
                    if (target == self.address[a]):
                        dataval[a] = self.arg3[i]
                        break
                    # if not append 0's until address and append address, append 0's in dataval before append value
                    elif(a == len(self.address)):
                        self.address.append(self.address[a]+4)
                        self.dataval[a].append(0)

            elif (self.opcode[i] == 1692):#ASR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] >> self.arg2[i]
            elif self.opcode[i] == 2038:#BREAK
                #and (in(self.instructions[i], base=2) & self.specialMask) == 2031591:
                foundBreak = True
            else:
                print("IN SIM -- UNKNOWN INSTRUCTION -------------- !!!!")
            armState.printState()
            armState.PC = jumpAddr
            armState.incrementPC()
            armState.cycle += 1
