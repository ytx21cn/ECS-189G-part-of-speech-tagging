import matplotlib.pyplot as plt

# Task 1: plotting the learning curve

# gather information

errorRatesByWord = {
	10000: 0.0814367973676995,
	1000: 0.281651170326794,
	20000: 0.0655831692300023,
	2000: 0.175810753545878,
	40000: 0.0540917815389984,
	5000: 0.108258344342797,
	500: 0.383478325896752,
};

errorRatesBySentence = {
	10000: 0.749411764705882,
	1000: 0.948235294117647,
	20000: 0.703529411764706,
	2000: 0.896470588235294,
	40000: 0.655882352941176,
	5000: 0.8,
	500: 0.975294117647059,
};

# doing plotting procedure

# consulted: https://stackoverflow.com/a/16935984/7686917
plt.plot(*zip(*sorted(errorRatesByWord.items())))
plt.plot(*zip(*sorted(errorRatesBySentence.items())))

plt.xlabel('Number of lines from the corpus')
plt.ylabel('Percent error')

plt.title('Learning Curve')

plt.show()
