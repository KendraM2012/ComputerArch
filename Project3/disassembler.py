from helpers import SetUp
import os
import masking_constants as MASKs
import sys


class Disassembler:
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    destReg = []
    src1Reg = []
    src2Reg = []
    dataval = []
    rawdata = []
    address = []
    addressdata = []
    numInstructs = 0

    def __init__(self):
        self.rnMask = MASKs.rnMask
        self.bMask = MASKs.bMask
        self.jAddrMask = MASKs.jAddrMask
        self.specialMask = MASKs.specialMask
        self.rmMask = MASKs.rmMask
        self.rdMask = MASKs.rdMask
        self.imMask = MASKs.imMask
        self.shmtMask = MASKs.shmtMask
        self.addrMask = MASKs.addrMask
        self.addr2Mask = MASKs.addr2Mask
        self.imsftMask = MASKs.imsftMask
        self.imdataMask = MASKs.imdataMask

    def run(self):

        instructions = []
        instructions = SetUp.import_data_file()
        outputFilename = SetUp.get_output_filename()

        print("raw output filename is", outputFilename)

        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))

        opcode = []

        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            if opcode[i] == 1112: #ADD
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1624: #SUB
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1104: #AND
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1360: #ORR
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ORR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1690: #LSR
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]) + ", ")
                self.arg2Str.append("R" + str(self.arg1[i]) + ", ")
                self.arg3Str.append("#" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1691: #LSL
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]) + ", ")
                self.arg2Str.append("R" + str(self.arg1[i]) + ", ")
                self.arg3Str.append("#" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1872: #EOR
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif 160 <= opcode[i] <= 191: #B
                self.instrSpaced.append(SetUp.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & self.bMask), 26))
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("#" + str(self.arg1[i]))
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append(-2)
                self.src1Reg.append(-3)
                self.src2Reg.append(-4)
            elif opcode[i] == 1160 or opcode[i] == 1161: #ADDI
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "")
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg2[i])
                self.src2Reg.append(-5)
            elif opcode[i] == 1672 or opcode[i] == 1673: #SUBI
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "")
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg2[i])
                self.src2Reg.append(-6)
            elif 1440 <= opcode[i] <= 1447: #CBZ
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter(((int(instructions[i], base=2) & self.addr2Mask) >> 5), 19))
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg3.append('')
                self.arg1Str.append("R" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
                self.src1Reg.append(arg2[i])
                self.src2Reg.append(-7)
                self.destReg.append(-8)
            elif 1448 <= opcode[i] <= 1455: #CBNZ
                # CBNZ offsetArg, conditionArg
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter(((int(instructions[i], base=2) & self.addr2Mask) >> 5), 19))
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg3.append('')
                self.arg1Str.append("R" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
                self.src1Reg.append(arg2[i])
                self.src2Reg.append(-9)
                self.destReg.append(-10)
            elif 1684 <= opcode[i] <= 1687: #MOVZ
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVZ")
                self.arg1.append((int(instructions[i], base=2) & self.imsftMask) >> 17)
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))
                self.destReg.append(arg3[i])
                self.src1Reg.append(-11)
                self.src2Reg.append(-12)

            elif 1940 <= opcode[i] <= 1943: #MOVK
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVK")
                self.arg1.append((int(instructions[i], base=2) & self.imsftMask) >> 17)
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))
                self.destReg.append(arg3[i])
                self.src1Reg.append(-13)
                self.src2Reg.append(-14)
            elif opcode[i] == 1984: #STUR
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.imMask) >> 12)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]) + ", ")
                self.arg2Str.append("[R" + str(self.arg1[i]) + ", ")
                self.arg3Str.append("#" + str(self.arg2[i]) + "]")
                self.src1Reg.append(arg1[i])
                self.src2Reg.append(-15)
                self.destReg.append(arg3[i])
            elif opcode[i] == 1986: #LDUR
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.imMask) >> 12)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]) + ", ")
                self.arg2Str.append("[R" + str(self.arg1[i]) + ", ")
                self.arg3Str.append("#" + str(self.arg2[i]) + "]")
                self.src1Reg.append(arg1[i])
                self.src2Reg.append(-16)
                self.destReg.append(arg3[i])
            elif opcode[i] == 1692: #ASR
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]))
                self.src1Reg.append(arg2[i])
                self.src2Reg.append(-17)
                self.destReg.append(arg3[i])
            elif opcode[i] == 0:
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("NOP")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.src1Reg.append(-18)
                self.src2Reg.append(-19)
                self.destReg.append(-20)

            elif opcode[i] == 2038 and (int(instructions[i], base=2) & self.specialMask) == 2031591:
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.src1Reg.append(-21)
                self.src2Reg.append(-22)
                self.destReg.append(-23)
                print("breaking")
                break
            else:
                self.opcodeStr.append("unknown")
                self.arg2.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.src1Reg.append(-24)
                self.src2Reg.append(-25)
                self.destReg.append(-26)
                print("i =:  " + str(i))
                print("opcode =:  " + str(opcode[i]))
                sys.exit("You have found an unknown instruction, investigate NOW")


            # now read the memory lines

        k = 0 #used to calculate how far from the B instruct
        for i in range ((self.numInstructs), (len(instructions))):
            #reads lines from break instruction to end of input file
            self.rawdata.append(instructions[i]) #adds the binary to rawdata list
            self.dataval.append(SetUp.imm_32_bit_unsigned_to_32_bit_signed_converter(int(instructions[i], base=2))) #converts to 2comp
            self.addressdata.append(str(int(self.address[i])))
        return  {#"instructions": instructions,
            "opcode":opcode,
            "opcodeStr":self.opcodeStr,
            "arg1":self.arg1,
            "arg1Str":self.arg1Str,
            "arg2":self.arg2,
            "arg2Str":self.arg2Str,
            "arg3":self.arg3,
            "arg3Str":self.arg3Str,
            "dataval":self.dataval,
            "address":self.address,
            "numInstructs":self.numInstructs,
            "instructions":instructions,
            "destReg":self.destReg,
            "src1Reg":self.src1Reg,
            "src2Reg":self.src2Reg}
    def print(self):
        # the following lines write the disassembly out to a file
        outFile = open(SetUp.get_output_filename() + "_dis.txt", 'w')

        for i in range(self.numInstructs):
            outFile.write(str(self.instrSpaced[i]) + '\t' + str(self.address[i]) + '\t' + str(self.opcodeStr[i])
                          + '\t' + str(self.arg1Str[i]) + str(self.arg2Str[i]) + str(self.arg3Str[i]) + "\n")

        for i in range(len(self.dataval)):
            outFile.write(str(self.rawdata[i]) + '\t'+str(self.addressdata[i])+ '\t' +str(self.dataval[i]) +"\n")

        outFile.close()
