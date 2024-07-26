import pandas as pd
import math
import csv

df=pd.read_csv('CareAreas.csv')
n=len(df)

df2=pd.read_csv('metadata.csv')
mainField_size=df2.loc[0][0]
subField_size=df2.loc[0][1]

f=open('mainField.csv','a',newline='')
writer=csv.writer(f)

f2=open('subField.csv','a',newline='')
writer2=csv.writer(f2)

temp=[]

def mainFieldCalculate():
    count=0
    for i in range(n):
        if i not in temp:
            x1=df.loc[i][1]
            x2=df.loc[i][2]
            y1=df.loc[i][3]
            y2=df.loc[i][4]

            mainField_x1=x1
            mainField_y1=y1

            mainField_x2=mainField_x1+mainField_size
            mainField_y2=mainField_y1+mainField_size
            data=[count,mainField_x1,mainField_x2,mainField_y1,mainField_y2]
            writer.writerow(data)
            temp.append(i)

            for i in range(n):
                if df.loc[i][1] <= mainField_x2:
                    if df.loc[i][3] <= mainField_y2:
                        temp.append(i)
            count=count+1

mainFieldCalculate()

x1=df.loc[0][1]
x2=df.loc[0][2]
y1=df.loc[0][3]
y2=df.loc[0][4]

length=x2-x1
noOfSubfields_length=math.ceil(length/subField_size)
breadth=y2-y1
noOfSubfields_breadth=math.ceil(breadth/subField_size)
print(length)
print(breadth)
print(noOfSubfields_breadth)
print(noOfSubfields_length)

def subFieldCalculate():
    s_count=0
    mf_count=0
    for k in range(n):
        x1=df.loc[k][1]
        x2=df.loc[k][2]
        y1=df.loc[k][3]
        y2=df.loc[k][4]
        for i in range(noOfSubfields_length):
            for j in range(noOfSubfields_breadth):
                subField_x1=x1+ (i*subField_size)
                subField_y1=y1+ (j*subField_size)

                subField_x2= subField_x1 + subField_size
                subField_y2= subField_y1 + subField_size

                data2=[s_count,subField_x1,subField_x2,subField_y1,subField_y2,0]
                writer2.writerow(data2)
                s_count=s_count+1
            mf_count=mf_count+1
                

subFieldCalculate()
