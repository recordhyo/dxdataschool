import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
#print(tips.head())


fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.set_style('darkgrid')
sns.regplot(x='total_bill',y='tip',data=tips,fit_reg=False, ax=ax1)
sns.regplot(x='total_bill',y='tip',data=tips,fit_reg=True, ax=ax2)
plt.show()