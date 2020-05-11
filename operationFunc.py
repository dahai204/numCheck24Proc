# Author --dahai--


checkCnt = [0,0,0,0,0]
checkFlag = False
printFlag = False

def printFunc(str):
    if printFlag == True:
        print(str)

def colorPrint(str_input, backColorNum):
    title = "\033["
    end = "\033[0m"
    backColorStr = str(backColorNum + 40) + "m"
    str_colorPrint = title + backColorStr + str_input + end
    print(str_colorPrint)

#增加一些限定条件，去除一些相似的方法
def operationFunc(input_a, input_b, flag):
    if flag == "+":
        rslt = input_a + input_b
    elif flag == "-":
        rslt = input_a - input_b
        if rslt < 0:
            rslt = 20000            # 保证结果无法得出24
    elif flag == "*":
        return input_a * input_b
    elif flag == "/":
        if input_b == 0:
            # 增减除数不能为零的条件
            # print("divid num can't be zero...")
            input_b = 10000

        rslt = input_a / input_b
        if rslt < 1:           # 除法的结果尽量不小于1
            return 10000

    return rslt

def bracketModProc(numList, operaList):
    checkFlag = False
    checkContinue = True
    operaList_0 = ["+" , "+" ,"+" ,"+"]
    operaList_1 = ["*" , "*" ,"*" ,"*"]
    if  operaList == operaList_0 or operaList == operaList_1:
        checkContinue = False

    # 输入的四个 (0 - 9) 的数字
    a = numList[0]
    b = numList[1]
    c = numList[2]
    d = numList[3]

    # 运算符号
    oper_1 = operaList[0]
    oper_2 = operaList[1]
    oper_3 = operaList[2]

    # mod_1  ((a b) c) d
    data_1 = operationFunc(a,b,oper_1)
    data_2 = operationFunc(data_1,c,oper_2)
    data_3 = operationFunc(data_2,d,oper_3)
    if data_3 == 24:
        printFunc("已经找到正确的组合方式：")
        printFunc("mod_1: ((%d %s %d) %s %d) %s %d = 24" %(a , oper_1, b, oper_2,c, oper_3, d))
        checkCnt[0] += 1
        checkFlag = True

    if checkContinue == True:
        # mod_2  (a (b c)) d
        data_1 = operationFunc(b, c, oper_1)
        data_2 = operationFunc(a, data_1, oper_2)
        data_3 = operationFunc(data_2, d, oper_3)
        if data_3 == 24:
            printFunc("已经找到正确的组合方式：")
            printFunc("mod_2: (%d %s (%d %s %d)) %s %d = 24" %(a , oper_2, b, oper_1,c, oper_3, d))
            checkCnt[1] += 1
            checkFlag = True
        # mod_3  a ((b c) d)
        data_1 = operationFunc(b, c, oper_1)
        data_2 = operationFunc(data_1, d, oper_2)
        data_3 = operationFunc(a, data_2, oper_3)
        if data_3 == 24:
            printFunc("已经找到正确的组合方式：")
            printFunc("mod_3: %d %s ((%d %s %d) %s %d) = 24" %(a , oper_3, b, oper_1,c, oper_2, d))
            checkCnt[2] += 1
            checkFlag = True
        # mod_4  a (b (c d))
        data_1 = operationFunc(c, d, oper_1)
        data_2 = operationFunc(b, data_1, oper_2)
        data_3 = operationFunc(a, data_2, oper_3)
        if data_3 == 24:
            printFunc("已经找到正确的组合方式：")
            printFunc("mod_4: %d %s (%d %s (%d %s %d)) = 24" %(a , oper_3, b, oper_2,c, oper_1, d))
            checkCnt[3] += 1
            checkFlag = True
        # mod_5  (a b) (c d)
        data_1 = operationFunc(a, b, oper_1)
        data_2 = operationFunc(c, d, oper_2)
        data_3 = operationFunc(data_1, data_2, oper_3)
        if data_3 == 24:
            printFunc("已经找到正确的组合方式：")
            printFunc("mod_5: (%d %s %d) %s (%d %s %d) = 24" %(a , oper_1, b, oper_3,c, oper_2, d))
            checkCnt[4] += 1
            checkFlag = True

    return checkFlag
