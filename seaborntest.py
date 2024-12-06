import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(context='poster', style="white")

days = list(range(1,9))
celsius_min = [19.6, 24.1, 26.7, 28.3,
27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0,
34.9, 35.6, 38.4, 39.2]
sns.lineplot(x=days, y=celsius_min)
sns.lineplot(x=days, y=celsius_max)
plt.xlabel('Day')
plt.ylabel('Degrees Celsius')
plt.savefig('seaborn_lineplot.png', dpi=300)


