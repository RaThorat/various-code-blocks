#Following code produces a bar chart of combination of disciplines submitted by applicants during a funding round. 
#The interaction is given between technical science and other disciplines from various domain as an example. 
#This graph answers: 
#Are there disciplines that do particularly well in a particular subsidy round?


import matplotlib.pyplot as plt
%matplotlib inline 
import seaborn as sns; sns.set()

#Interaction of discipline technical sciences with other sciences

sns.set(font_scale=1.6)
chart = sns.catplot(
    data=df_305[df_305['Discipline'].isin(['Technical science'])],
    x='Disciplines',
    y='Value',
    hue='Attribute', 
    kind='bar',
    row='Domain',
    ci=None,
    aspect=5,
    height=3,
    legend=None,
    margin_titles=False,
)
for axes in chart.axes.flat:
    axes.set_xticklabels(axes.get_xticklabels(), rotation=45, horizontalalignment='right')
    chart.axes[1][0].legend()
    axes.set(xlabel=None, ylabel=None)
    plt.subplots_adjust(top=0.9)
    chart.fig.suptitle('Interaction of discipline Technical science with other sciences')
