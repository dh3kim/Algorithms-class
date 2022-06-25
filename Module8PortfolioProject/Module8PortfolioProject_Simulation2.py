# Final project
# Structures for multi-dimensional lists
import random, time
import statistics

# simulation setup: 
# the number of iterations, data structures, and length of rows
iterSize = 100
NStruc = 5
NObsList = [10000, 30000, 60000]

for NObs in NObsList:
    # Sample placeholder
    timeSample = [None]*iterSize*NStruc
    
    for iter in range(iterSize):
        # Number of columns 
        NVar = 5
        
        # Data Structure 1 (DS1)
        # Placeholders
        XOne = [None] * NObs
        XTwo = [None] * NObs
        XThree = [None] * NObs
        XFour = [None] * NObs
        YData = [None] * NObs
        
        #Insert data
        for i in range(NObs):
            XOne[i] = float(random.randint(0,4))
            XTwo[i] = random.random()*100
            XThree[i] = float(random.randint(0,1))
            XFour[i] = random.random()*50
            YData[i] = 1 + 3 * XOne[i] + 5 * XTwo[i] - 6 * XThree[i] + \
                       9 * XFour[i] + random.random()
        
        # Two string variables
        for i in range(len(XThree)):
            if XThree[i] < 0.5:
                XThree[i] = "M"
            else:
                XThree[i] = "W"
        
        for i in range(len(XOne)):
            if XOne[i] == 0.0:
                XOne[i] = "AAA"
            elif XOne[i] == 1.0:
                XOne[i] = "BBB"
            elif XOne[i] == 2.0:
                XOne[i] = "CCC"
            elif XOne[i] == 3.0:
                XOne[i] = "DDD"
            else:
                XOne[i] = "EEE"
        
        # time
        start = time.time()

        XOne_unique = list(set(XOne))
        XThree_unique = list(set(XThree))
        YByGroup = []
        for XValOne in XOne_unique:
            for XValThree in XThree_unique:
                YVal = []
                for i in range(NObs):
                    if XOne[i] == XValOne and XThree[i] == XValThree:
                        YVal.append(YData[i])
                YVal_mean = sum(YVal)/len(YVal)
                YByGroup.append([XValOne, XValThree, YVal_mean])
                
        # Record time
        timeSample[iter] = {'Struc':'DS1', 'Time': time.time() - start}
        
        # Data Structure 2 (DS2)
        DS2 = [None] * NObs * NVar
        for i in range(NObs):
            DS2[i] = float(random.randint(0,4))
            DS2[i + NObs] = random.random()*100
            DS2[i + NObs*2] = float(random.randint(0,1))
            DS2[i + NObs*3] = random.random()*50
            DS2[i + NObs*4] = 1 + 3 * DS2[i] + 5 * DS2[i + NObs] - 6 * DS2[i + NObs*2] + \
                              9 * DS2[i + NObs*3] + random.random()
        for i in range(NObs):
            if DS2[i + NObs*2] < 0.5:
                DS2[i + NObs*2] = "M"
            else:
                DS2[i + NObs*2] = "W"
        
        for i in range(NObs):
            if DS2[i] == 0.0:
                DS2[i] = "AAA"
            elif DS2[i] == 1.0:
                DS2[i] = "BBB"
            elif DS2[i] == 2.0:
                DS2[i] = "CCC"
            elif DS2[i] == 3.0:
                DS2[i] = "DDD"
            else:
                DS2[i] = "EEE" 
        # time
        start = time.time()
        # 0:NObs-1, NObs:(NObs*2)-1, NObs*2: (NObs*3) - 1, 
        XOne_unique = list(set(DS2[0:NObs-1]))
        XThree_unique = list(set(DS2[NObs*2:(NObs*3)-1]))
        YByGroup_DS2 = []
        for XValOne in XOne_unique:
            for XValThree in XThree_unique:
                YVal = []
                for i in range(NObs):
                    if DS2[i] == XValOne and DS2[i + NObs*2] == XValThree:
                        YVal.append(DS2[i + NObs*4])
                YVal_mean = sum(YVal)/len(YVal)
                YByGroup_DS2.append([XValOne, XValThree, YVal_mean])
                
        timeSample[iter + iterSize] = {'Struc':'DS3', 'Time': time.time() - start}
        
        # DS3
        DS3 = [[None]*NObs for _ in range(NVar)]
        for i in range(NObs):
            DS3[0][i] = float(random.randint(0,4))
            DS3[1][i] = random.random()*100
            DS3[2][i] = float(random.randint(0,1))
            DS3[3][i] = random.random()*50
            DS3[4][i] = 1 + 3 * DS3[0][i] + 5 * DS3[1][i] - 6 * DS3[2][i] + \
                        9 * DS3[3][i] + random.random()
         
        for i in range(NObs):
            if DS3[2][i] < 0.5:
                DS3[2][i] = "M"
            else:
                DS3[2][i] = "W"
        
        for i in range(NObs):
            if DS3[0][i] == 0.0:
                DS3[0][i] = "AAA"
            elif DS3[0][i] == 1.0:
                DS3[0][i] = "BBB"
            elif DS3[0][i] == 2.0:
                DS3[0][i] = "CCC"
            elif DS3[0][i] == 3.0:
                DS3[0][i] = "DDD"
            else:
                DS3[0][i] = "EEE"             
        
        start = time.time()
        XOne_unique = list(set(DS3[0]))
        XThree_unique = list(set(DS3[2]))
        YByGroup_DS3 = []
        for XValOne in XOne_unique:
            for XValThree in XThree_unique:
                YVal = []
                for i in range(NObs):
                    if DS3[0][i] == XValOne and DS3[2][i] == XValThree:
                        YVal.append(DS3[4][i])
                YVal_mean = sum(YVal)/len(YVal)
                YByGroup_DS3.append([XValOne, XValThree, YVal_mean])
                
        timeSample[iter + iterSize*2] = {'Struc':'DS3', 'Time': time.time() - start}
        
        #DS4
        DS4 = [[None]*NVar for _ in range(NObs)]
        for i in range(NObs):
            DS4[i][0] = float(random.randint(0,4))
            DS4[i][1] = random.random()*100
            DS4[i][2] = float(random.randint(0,1))
            DS4[i][3] = random.random()
            DS4[i][4] = 1 + 3 * DS4[i][0] + 5 * DS4[i][1] - 6 * DS4[i][2] + \
                        9 * DS4[i][3] + random.random()
        
        for i in range(NObs):
            if DS4[i][2] < 0.5:
                DS4[i][2] = "M"
            else:
                DS4[i][2] = "W"
        
        for i in range(NObs):
            if DS4[i][0] == 0.0:
                DS4[i][0] = "AAA"
            elif DS4[i][0] == 1.0:
                DS4[i][0] = "BBB"
            elif DS4[i][0] == 2.0:
                DS4[i][0] = "CCC"
            elif DS4[i][0] == 3.0:
                DS4[i][0] = "DDD"
            else:
                DS4[i][0] = "EEE"
                
        start = time.time()        
        XOne_unique = list(set([item[0] for item in DS4]))
        XThree_unique = list(set([item[2] for item in DS4]))
        YByGroup_DS4 = []
        for XValOne in XOne_unique:
            for XValThree in XThree_unique:
                YVal = []
                for i in range(NObs):
                    if DS4[i][0] == XValOne and DS4[i][2] == XValThree:
                        YVal.append(DS4[i][4])
                YVal_mean = sum(YVal)/len(YVal)
                YByGroup_DS4.append([XValOne, XValThree, YVal_mean])
                
        timeSample[iter + iterSize*3] = {'Struc':'DS4', 'Time': time.time() - start}
        
        #DS5
        DS5 = [None] * NObs
        for i in range(NObs):
            v0 = float(random.randint(0,4))
            v1 = random.random()*100
            v2 = float(random.randint(0,1))
            v3 = random.random()
            v4 = 1 + 3 * v0 + 5 * v1 - 6 * v2 + 9 * v3 + random.random()
            
            if v2 < 0.5:
                v2 = "M"
            else:
                v2 = "W"
        
            if v0 == 0.0:
                v0 = "AAA"
            elif v0 == 1.0:
                v0 = "BBB"
            elif v0 == 2.0:
                v0 = "CCC"
            elif v0 == 3.0:
                v0 = "DDD"
            else:
                v0 = "EEE"   
            
            DS5[i] = {'C1': v0, 'C2': v1, 'C3': v2, 'C4': v3, 'C5': v4}

        
        start = time.time()
        XOne_unique = list(set([item['C1'] for item in DS5]))
        XThree_unique = list(set([item['C3'] for item in DS5]))
        YByGroup_DS5 = []
        for XValOne in XOne_unique:
            for XValThree in XThree_unique:
                YVal = []
                for i in range(NObs):
                    if DS5[i]['C1'] == XValOne and DS5[i]['C3'] == XValThree:
                        YVal.append(DS5[i]['C5'])
                YVal_mean = sum(YVal)/len(YVal)
                YByGroup_DS5.append([XValOne, XValThree, YVal_mean])
                
        timeSample[iter + iterSize*4] = {'Struc':'DS4', 'Time': time.time() - start}
        
    for struc in range(NStruc):
        Sample = [timeSample[i + iterSize*struc]['Time'] for i in range(iterSize)]
        if NObs == NObsList[0] and struc == 0:
            print("##########################################")
            print("Data struc.","Mean ", "Median ", "Sta. dev.")
            print("##########################################")
        if struc == 0:
            print("Length of rows", NObs)
        print("DS", struc+1, "     ", round(statistics.mean(Sample),3), " ",\
              round(statistics.median(Sample),3), " ", \
              round(statistics.stdev(Sample),3))

