# Author --dahai--

import operationFunc as operFun

info = """
    ==========================
           24点计算程序
       '+' , '-' , '*' , '/'
       @dahai 20200408
    ==========================
"""
signList = ['+' , '-' , '*' , '/']
print(info)
numInput = input("请输入四个数字：")
numLens = 4

numList = [0,0,0,0]
numCnt = 0
checkFlag = False

numList_orign = [1,2,3,4]
for ij in range(4):
    numList_orign[ij] = int(numInput[ij * 2])

for ii in range(4):
    # if checkFlag == True:
    #     break
    numList = list(numList_orign)
    # if checkFlag == True:
    #     break
    numTmp =  numList[ii]
    numList[ii] = numList[0]
    numList[0] = numTmp

    for jj in range(1,4):
        numTmp = numList[jj]
        numList[jj] = numList[1]
        numList[1] = numTmp
        for kk in range(2):
            numTmp = numList[3]
            numList[3] = numList[2]
            numList[2] = numTmp
            numCnt += 1
            print("[%s: %s, %s, %s, %s] %s,%s" %(numCnt,numList[0],numList[1],numList[2],numList[3], ii, jj))

            for i in range(4):
                op_i = signList[i]
                # if checkFlag == True:
                #     break

                for j in range(4):
                    op_j = signList[j]
                    # if checkFlag == True:
                    #     break
                    for k in range(4):
                        op_k = signList[k]
                        # 选择符号
                        operSelectList = [op_i , op_j , op_k]
                        checkFlag = operFun.bracketModProc(numList , operSelectList)
                        # if checkFlag == True:
                        #     break

sum = 0
for i in operFun.checkCnt:
    sum = i + sum

print(numInput)
if sum == 0:
    operFun.colorPrint("这种组合无解..." , 1)
    print(operFun.checkCnt)
else:
    operFun.colorPrint(("这种组合有%s种解..." %sum),1)
    print(operFun.checkCnt)

