#12223829 JeongHyukChoi - OSS PRJ2-1

import pandas as pd
from pandas import Series, DataFrame

#get 2019_kbo_for_kaggle_v2.csv
csv_data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

#make data frame with columns

#문제1번 클래스
class Question1Analyzer:
    dfWithYYYY = {}
    def __init__(self, year):
        df = pd.DataFrame(csv_data, columns=["batter_name", "H", "avg", "HR", "OBP", "year"])
        for i in year:
            self.dfWithYYYY[i] = df[df["year"] == i]

    def convertWithH(self, year):
        dfWithYYYYByValue = self.dfWithYYYY[year].drop(["avg", "HR", "OBP", "year"], axis=1)
        dfWithYYYYByValue_sorted = dfWithYYYYByValue.sort_values(by="H", ascending=False)

        print(">> YEAR ", year," BY H, top 10")
        print(dfWithYYYYByValue_sorted["batter_name"].head(10), "\n")

    def convertWithAVG(self, year):
        dfWithYYYYByValue = self.dfWithYYYY[year].drop(["H", "HR", "OBP", "year"], axis=1)
        dfWithYYYYByValue_sorted = dfWithYYYYByValue.sort_values(by="avg", ascending=False)

        print(">> YEAR ", year," BY AVG, top 10")
        print(dfWithYYYYByValue_sorted["batter_name"].head(10), "\n")

    def convertWithHR(self, year):
        dfWithYYYYByValue = self.dfWithYYYY[year].drop(["H", "avg", "OBP", "year"], axis=1)
        dfWithYYYYByValue_sorted = dfWithYYYYByValue.sort_values(by="HR", ascending=False)

        print(">> YEAR ", year," BY HR, top 10")
        print(dfWithYYYYByValue_sorted["batter_name"].head(10), "\n")

    def convertWithOBP(self, year):
        dfWithYYYYByValue = self.dfWithYYYY[year].drop(["H", "HR", "avg", "year"], axis=1)
        dfWithYYYYByValue_sorted = dfWithYYYYByValue.sort_values(by="OBP", ascending=False)

        print(">> YEAR ", year," BY OBP, top 10")
        print(dfWithYYYYByValue_sorted["batter_name"].head(10), "\n")

    #실행 함수
    def run(self, year):
        self.convertWithH(year)
        self.convertWithAVG(year)
        self.convertWithHR(year)
        self.convertWithOBP(year)


#문제 2번 클래스
class Question2Analyzer:
    dfWithYYYYByPosition = {}
    year_info = 0
    def __init__(self, year, positionList):
        self.year_info = year
        df = pd.DataFrame(csv_data, columns=["batter_name", "cp", "war", "year"])
        dfWithYYYY = df[df["year"] == year]
        for i in positionList:
            self.dfWithYYYYByPosition[i] = dfWithYYYY[dfWithYYYY["cp"] == i]


    def convertWithPostition(self, position):
        dfWithYYYYByValue = self.dfWithYYYYByPosition[position].drop(["cp"], axis=1)
        dfWithYYYYByValue_sorted = dfWithYYYYByValue.sort_values(by="war", ascending=False)

        print(">> POSITION : ", position ,", YEAR : ", self.year_info, " top 10")
        print(dfWithYYYYByValue_sorted["batter_name"].head(1), "\n")


    #실행 함수
    def run(self, position):
        self.convertWithPostition(position)



#문제 3번 클래스
class Question3Analyzer:
    lst = []
    df = pd.DataFrame()

    def __init__(self, lst):
        self.lst = lst
        self.df = pd.DataFrame(csv_data, columns=self.lst)

    def getCorrFromLST(self):
        lstWithCorr = []
        temp = 0
        tempKey = ""
        isTemp = False
        for i in self.lst:
            if i != 'salary':
                if isTemp:
                    tempCorr = abs(self.df['salary'].corr(self.df[i]))
                    if temp < tempCorr:
                        temp = tempCorr
                        tempKey = i
                else:
                    isTemp = True
                    temp = abs(self.df['salary'].corr(self.df[i]))
                    tempKey = i


        print(">> The highest correlation with Salary is !")
        print(tempKey, ": ", temp)


    #실행 함수
    def run(self):
        self.getCorrFromLST()



#question1
year_q1 = [2015, 2016, 2017, 2018]
q1a = Question1Analyzer(year_q1)
for i in year_q1:
    q1a.run(i)


#question2
year_q2 = 2018
positionList_q2 = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
q2a = Question2Analyzer(year_q2, positionList_q2)
for i in positionList_q2:
    q2a.run(i)


#question3
lst_q3 = ["R", "H", "HR", "RBI", "SB", "war", "avg", "OBP", "SLG", "salary"]
q3a = Question3Analyzer(lst_q3)
q3a.run()
