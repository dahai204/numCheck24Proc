# Author --dahai--

import  operationFunc as operFun
import  time

info =  """
    ==========================
           24点计算程序
       '+' , '-' , '*' , '/'
       @dahai 20200408
    ==========================
"""

def check24Func(numInput , numLens):
    signList = ['+', '-', '*', '/']
    numList = [0,0,0,0]
    numCheckCnt = 0
    checkFlag = False
    operFun.checkCnt = [0,0,0,0,0]


    numList_orign = [1,2,3,4]
    for ij in range(4):
        numList_orign[ij] = int(numInput[ij])

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
                numCheckCnt += 1
                # print("[%s: %s, %s, %s, %s] %s,%s" %(numCheckCnt,numList[0],numList[1],numList[2],numList[3], ii, jj))

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


print(info)
# numInput = input("请输入四个数字：")
numLens = 4
# for ij in range(numLens):
#     numList_orign[ij] = int(numInput[ij])

numInput = [0, 0, 0, 0]

for i_0 in range(1):
    time_0_start = time.time()
    for i_1 in range(1):
        time_1_start = time.time()
        print(("[i_1 = %d]" % i_1).center(80, "+"))
        for i_2 in range(1):
            time_2_start = time.time()
            print(("[i_2 = %d]" %i_2).center(50, "="))
            for i_3 in range(8,19):
                time_3_start = time.time()
                numInput[0] = i_0+1
                numInput[1] = i_1+1
                numInput[2] = i_2+1
                numInput[3] = i_3+1
                check24Func(numInput , numLens)
        #         time_3_end = time.time()
        #         operFun.colorPrint(("耗时：%s..." %(time_3_end - time_3_start)), 1)
        #     time_2_end = time.time()
        #     operFun.colorPrint(("耗时：%s..." % (time_2_end - time_2_start)), 1)
        # time_1_end = time.time()
        # operFun.colorPrint(("耗时：%s..." % (time_1_end - time_1_start)), 1)
    time_0_end = time.time()
    operFun.colorPrint(("耗时：%s..." % (time_0_end - time_0_start)), 1)