import random
import numpy as np

# 定义全局变量
# 定义立方体的每一层
first_layer = list(range(1, 26))  # 生成1-25的list
second_layer = list(range(26, 51))
third_layer = list(range(51, 76))
fourth_layer = list(range(76, 101))
fifth_layer = list(range(101, 126))


# 定义随机过程
def random_cube(case):
    """对于每种比例每层有三种随机可能，根据传入的case值随机进行选取随机的种类，case [1, 2, 3]"""
    """本函数产生随机结果的是数组下标，下标范围为[0,24]"""
    # 定义每一层的下标
    k1 = [10, 11, 12, 13, 14]
    k2_k3_left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    k2_k3_right = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    # 定义每一层soft和stiff分布的下标的集合
    soft_index = []
    stiff_index = []
    if case == 1:
        # 定义k1的数量
        k1_soft_num = 1
        k2_k3_soft_num = 5
        random.shuffle(k1)
        random.shuffle(k2_k3_left)
        for idx in range(0, k1_soft_num):
            soft_index.append(k1[idx])
        for idx in range(0, k2_k3_soft_num):
            soft_index.append(k2_k3_left[idx])
        # 右下标和左下标对称
        for i in soft_index:
            if 4 >= i >= 0:
                soft_index.append(i + 20)
            elif 9 >= i >= 5:
                soft_index.append(i + 10)

    if case == 2:
        # 定义k1的数量
        k1_soft_num = 3
        k2_k3_soft_num = 4
        random.shuffle(k1)
        random.shuffle(k2_k3_left)
        for idx in range(0, k1_soft_num):
            soft_index.append(k1[idx])

        for idx in range(0, k2_k3_soft_num):
            soft_index.append(k2_k3_left[idx])
        # 右下标和左下标对称
        for i in soft_index:
            if 4 >= i >= 0:
                soft_index.append(i + 20)
            elif 9 >= i >= 5:
                soft_index.append(i + 10)

    if case == 3:
        # 定义k1的数量
        k1_soft_num = 5
        k2_k3_soft_num = 3
        random.shuffle(k1)
        random.shuffle(k2_k3_left)
        for idx in range(0, k1_soft_num):
            soft_index.append(k1[idx])

        for idx in range(0, k2_k3_soft_num):
            soft_index.append(k2_k3_left[idx])
        # 右下标和左下标对称
        for i in soft_index:
            if 4 >= i >= 0:
                soft_index.append(i + 20)
            elif 9 >= i >= 5:
                soft_index.append(i + 10)

    # 返回存储的软材料下标集合
    return soft_index


# 定义随机执行次数times(job数)


for times in range(1, 2):
    """脚本执行次数"""
    # job的num等于times
    num = times
    fileName = 'G:\RandomCube\\44per'
    """abaqus的脚本输入最好不要定义函数，因为缩进问题abaqus会报空格错误"""
    """定义随机过程"""
    # 定义软材料和硬材料的列表
    stiffList = []  # 硬材料
    softList = []  # 软材料

    # 定义软材料的比例
    soft_ratio = 0.44  # 0.2

    # 每层利用random_cube返回的软材料下标进行软材料筛选

    # 定义第一层软材料的分布
    first_layer_softList = []
    # 产生随机数并选取随机方式 [1, 2, 3]
    random_case1 = [1, 2, 3]
    random_case2 = [1, 2, 3]
    random_case3 = [1, 2, 3]
    # 随机置乱
    random.shuffle(random_case1)
    random.shuffle(random_case2)
    random.shuffle(random_case3)
    case1 = random_case1[0]
    case2 = random_case2[0]
    case3 = random_case3[0]
    # 接受返回的软材料分布列表
    first_layer_softList_idx = random_cube(case1)
    for idx in first_layer_softList_idx:
        first_layer_softList.append(first_layer[idx])
    print(first_layer_softList)

    # 定义第二层软材料的分布
    second_layer_softList = []
    # 产生随机数并选取随机方式 [1, 2, 3]
    case = random.randint(1, 3)
    # 接受返回的软材料分布列表
    second_layer_softList_idx = random_cube(case2)
    for idx in second_layer_softList_idx:
        second_layer_softList.append(second_layer[idx])
    print(second_layer_softList)

    # 定义第三层软材料的分布
    third_layer_softList = []
    # 产生随机数并选取随机方式 [1, 2, 3]
    case = random.randint(1, 3)
    # 接受返回的软材料分布列表
    third_layer_softList_idx = random_cube(case3)
    for idx in third_layer_softList_idx:
        third_layer_softList.append(third_layer[idx])
    print(third_layer_softList)

    # 定义第四层软材料的分布
    fourth_layer_softList = []
    # 第四层与第二层一致
    fourth_layer_softList_idx = second_layer_softList_idx
    for idx in fourth_layer_softList_idx:
        fourth_layer_softList.append(fourth_layer[idx])

    # 定义第五层软材料的分布
    fifth_layer_softList = []
    # 第五层与第一层一致
    fifth_layer_softList_idx = first_layer_softList_idx
    for idx in fifth_layer_softList_idx:
        fifth_layer_softList.append(fifth_layer[idx])

    # 定义软材料和硬材料的列表
    softList = []
    stiffList = []

    # 存储软材料列表
    for i in first_layer_softList:
        softList.append(i)

    for i in second_layer_softList:
        softList.append(i)

    for i in third_layer_softList:
        softList.append(i)

    for i in fourth_layer_softList:
        softList.append(i)

    for i in fifth_layer_softList:
        softList.append(i)

    # 存储硬材料列表
    for i in range(1, 126):
        if i not in softList:
            stiffList.append(i)



    # 定义层
    second = []
    third = []
    fourth = []
    fifth = []

    # 定义标签化列表 stiff=1 soft=0
    labelList = []

    # 第一层1-25个方格
    first = [
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25,
        21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 25]
    # 层方向上相差 25，50，75，100
    # 深度方向
    for i in range(len(first)):
        second.append(first[i] + 25)

    for i in range(len(first)):
        third.append(first[i] + 50)

    for i in range(len(first)):
        fourth.append(first[i] + 75)

    for i in range(len(first)):
        fifth.append(first[i] + 100)

    # 归一化为labelList
    for i in range(len(first)):
        labelList.append(first[i])

    for i in range(len(first)):
        labelList.append(second[i])

    for i in range(len(first)):
        labelList.append(third[i])

    for i in range(len(first)):
        labelList.append(fourth[i])

    for i in range(len(first)):
        labelList.append(fifth[i])

    print("labelList=", labelList, len(labelList))
    # stiff:1  soft:0

    """定义将标签化列表标签化, stiff:1  soft:0"""
    # 定义15x15x15的标签label
    label = []
    for item in labelList[:]:
        if item in stiffList:
            label.append(1)
        else:
            label.append(0)

    print("标签化后的label:", label, len(label))



    # 定义5x5x5的标签label_cube
    label_cube = []
    for item in range(1, 126):
        if item in stiffList:
            label_cube.append(1)
        else:
            label_cube.append(0)

    print("标签化后的label_cube:", label_cube, len(label_cube))

    """定义日志文件(job名+次序),stiffList,softList,只含有0，1的标签；单独将stiffList和softList写入文件"""

    # 输出列表内容
    # 填入job名

    jobName = 'job-' + str(num)
    print(jobName)

    # 写入日志文件log.txt
    with open(fileName + '/log.txt', 'a+') as f:
        try:
            f.write('#######################################' + "[  " + jobName + '  ]' + '  soft的比例：' + str(
                soft_ratio) + '###############################################################################' + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('first_layer_softList = ' + str(first_layer_softList) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('sec_layer_softList = ' + str(second_layer_softList) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('third_layer_softList = ' + str(third_layer_softList) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('fourth_layer_softList = ' + str(fourth_layer_softList) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('fifth_layer_softList = ' + str(fifth_layer_softList) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('# ' + str(jobName) + '\n')
            f.write('count = ' + str(num) + '\n')
            f.write('stiffList = ' + str(stiffList) + '\n')
            f.write('softList = ' + str(softList) + '\n')
            f.write('\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('label_cube = ' + str(label_cube) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('labelList = ' + str(labelList) + '\n')
            f.write(
                '-----------------------------------------------------------------------------------------------------------------' + '\n')
            f.write('label = ' + str(label) + '\n')
            f.write(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n')
            f.write(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n')
            f.write(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n')
            f.close()
        except Exception as e:
            print(e)

    # 将label标签写入文件
    f1 = open(fileName + '/label.txt', 'a', encoding='utf8')

    for item in label:
        f1.write(str(item) + ' ')
    f1.write('\n')
    f1.close()


    # 将label_cube标签写入文件
    f3 = open(fileName + '/label_cube.txt', 'a')

    for item in label_cube:
        f3.write(str(item) + ' ')
    f3.write('\n')
    f3.close()
    '''
    # 读取文件并保存为数组
    np_arr = np.loadtxt('G:/SameLayer_3DCNNTest/label.txt')
    print(np_arr.shape, np_arr)
    '''
    '''写入创建Job的脚本'''
    f4 = open(fileName + '/Job.txt', 'a')
    f4.write('from abaqus import *')
    f4.write('\n')
    f4.write('from abaqusConstants import *')
    f4.write('\n')
    f4.write('import random')
    f4.write('\n')
    f4.write('p = mdb.models[\'Advanced-Shpb--Explict-Cube-Soft_40per\'].parts[\'shijian\']')
    f4.write('\n')
    f4.write(
        'listAll = [124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]')
    f4.write('\n')
    f4.write('for i in listAll:')
    f4.write('\n')
    f4.write('    del p.sectionAssignments[i]')
    f4.write('\n')
    f4.write('\n')
    # 写入列表
    f4.write('# ' + str(jobName) + '\n')
    f4.write('count = ' + str(num) + '\n')
    f4.write('stiffList = ' + str(stiffList) + '\n')
    f4.write('softList = ' + str(softList) + '\n')
    # 赋予属性
    f4.write('for iter in stiffList:' + '\n')
    f4.write('    setName = \'Cube-{}\'.format(iter)' + '\n')
    f4.write(
        '    p.SectionAssignment(region=p.sets[setName], sectionName=\'stiff\', offset=0.0,offsetType=MIDDLE_SURFACE, offsetField=\'\',thicknessAssignment=FROM_SECTION)')
    f4.write('\n')
    f4.write('\n')
    f4.write('for iter in softList:' + '\n')
    f4.write('    setName = \'Cube-{}\'.format(iter)' + '\n')
    f4.write(
        '    p.SectionAssignment(region=p.sets[setName], sectionName=\'soft\', offset=0.0,offsetType=MIDDLE_SURFACE, offsetField=\'\',thicknessAssignment=FROM_SECTION)' + '\n')

    f4.write('\n')
    f4.write('jobName = ' + '\'Job-' + str(num) + '\'')
    f4.write('\n')
    f4.write('mdb.Job(name=jobName, model=\'Advanced-Shpb--Explict-Cube-Soft_40per\',' + '\n')
    f4.write('    description=\'\', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0,' + '\n')
    f4.write('    queue=None, memory=90, memoryUnits=PERCENTAGE, explicitPrecision=SINGLE,' + '\n')
    f4.write('    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF,' + '\n')
    f4.write('    contactPrint=OFF, historyPrint=OFF, userSubroutine=\'\', scratch=\'\',' + '\n')
    f4.write('    resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=8,' + '\n')
    f4.write('    activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=8)' + '\n')
    f4.write('mdb.jobs[jobName].writeInput(consistencyChecking=OFF)' + '\n')
