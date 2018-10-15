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

y = df['Percent Increase'].values
x = df['PreviousTotal'].values

plt.scatter(x, y, color="red", label='Ward 8')

plt.scatter(df_MJ['PreviousTotal'].values, df_MJ['Percent Increase'].values, color='blue', label='Mary Jo Tedder')

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "gray")

means = df.groupby('Ward#')[['Percent Increase', 'PreviousTotal']].mean()
std = df.groupby('Ward#')[['Percent Increase', 'PreviousTotal']].std()
count = df.groupby('Ward#')[['Percent Increase', 'PreviousTotal']].count()


tstat, pvalue = stats.ttest_ind_from_stats(means['Percent Increase'].values, std['Percent Increase'].values, count['Percent Increase'].values,
                                     means['PreviousTotal'].values, std['PreviousTotal'].values, count['PreviousTotal'].values)

print(tstat)
print(pvalue)

r_score = r2_score(y, x, multioutput='variance_weighted')

print(r_score)
pear_corr = df['Percent Increase'].corr(df['PreviousTotal'])
pear_corr2 = stats.pearsonr(x, y)

print(pear_corr)
print(pear_corr2)
plt.ylabel('Percent Increase in Previous verse Current Assessment')
plt.xlabel('Previous Assessment')

plt.show()


