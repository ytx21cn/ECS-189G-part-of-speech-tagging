import matplotlib.pyplot as plt

# Task 1: plotting the learning curve

# gather information

errorRatesByWord = {
	1000: 0.281651170326794,
	100: 0.512451080589276,
	1500: 0.234962734003041,
	1700: 0.219084178777077,
	200: 0.47715432360346,
	500: 0.383478325896752,
	50: 0.611212204302415,
};

errorRatesBySentence = {
	1000: 0.948235294117647,
	100: 0.993529411764706,
	1500: 0.920588235294118,
	1700: 0.911176470588235,
	200: 0.989411764705882,
	500: 0.975294117647059,
	50: 0.997058823529412,
};

# doing plotting procedure

# consulted: https://stackoverflow.com/a/16935984/7686917
plt.plot(*zip(*sorted(errorRatesByWord.items())))
plt.plot(*zip(*sorted(errorRatesBySentence.items())))

plt.xlabel('Number of lines from the corpus')
plt.ylabel('Percent error')

plt.title('Learning Curve')

plt.show()
