import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
Data = {'Student':['Amit','Bhavna','Chetan','Diya','Isha','farhan'],
       'Maths':[75,82,68,90,72,85],
       'Python':[80,78,70,92,75,88],
        'Attendance':[85,90,88,95,80,92],
        'City':['Pune','Mumbai','Pune','Nashik','Mumbai','Pune']}
df = pd.DataFrame(Data)
df
plt.plot(df['Student'],df['Python'])
plt.xlabel('Student')
plt.ylabel('Python marks')

plt.bar(df['Student'],df['Python'])
plt.xlabel('Student')
plt.ylabel('Python marks')

plt.scatter(df['Student'],df['Python'])
plt.xlabel('Student')
plt.ylabel('Python marks')

cr=df[['Maths','Python','Attendance']].corr()
cr
sns.heatmap(cr)
