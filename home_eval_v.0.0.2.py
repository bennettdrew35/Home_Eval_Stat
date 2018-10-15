import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

path = r"/Users/drewbennett/Desktop/Home_Evaluationv.4.xlsx"

df = pd.read_excel(path, sheet_name="Ward 8")

df = df[(df['Percent Increase'] >= 0) & (df['Percent Increase'] <= 0.99)]

df_MJ = df[df['OWNER1'] == 'TEDDER, MARY JO TRUST']
df_lille = df[df['STREET'] == 'LILLE RD']

print(df_MJ[['HNUM', 'STREET']])
print(df_MJ[['CurrentTotal', 'PreviousTotal', 'Percent Increase']])

x = df['PreviousTotal'].values
y = df['Percent Increase'].values

plt.scatter(x, y, color="red", label='Ward 8')
plt.scatter(df_lille['PreviousTotal'].values, df_lille['Percent Increase'].values, color='green', label='Lille Rd')
plt.scatter(df_MJ['PreviousTotal'].values, df_MJ['Percent Increase'].values, color='blue', label='Mary Jo Tedder')
plt.hlines(df['Percent Increase'].median(), 0, df['PreviousTotal'].max(), "gray",
           label='Median % Increase Ward 8 Assessment')
plt.hlines(df_lille['Percent Increase'].median(), 0, df['PreviousTotal'].max(), "black",
           label='Median % Increase Lille Rd Assessment')
print(df['Percent Increase'].median())
means = df.groupby('Ward#')[['Percent Increase', 'PreviousTotal']].mean()
std = df.groupby('Ward#')[['Percent Increase', 'PreviousTotal']].std()
count = df.groupby('Ward#')[['Percent Increase', 'PreviousTotal']].count()


tstat, pvalue = stats.ttest_ind_from_stats(means['Percent Increase'].values, std['Percent Increase'].values, count['Percent Increase'].values,
                                     means['PreviousTotal'].values, std['PreviousTotal'].values, count['PreviousTotal'].values)


r_score = r2_score(x, y, multioutput='variance_weighted')

pear_corr = df['Percent Increase'].corr(df['PreviousTotal'])
pear_corr_lille = df_lille['Percent Increase'].corr(df_lille['PreviousTotal'])
pear_corr2 = stats.pearsonr(x, y)

plt.xlim([0, df['PreviousTotal'].max()])
plt.ylim([0, 1])
print(pear_corr)
print(pear_corr_lille)

plt.ylabel('Percent Increase in Previous verse Current Assessment')
plt.xlabel('Previous Assessment')
plt.title('Percent Increase in Assessment vs. Previous Assessment')
plt.legend(loc='best')
plt.show()


