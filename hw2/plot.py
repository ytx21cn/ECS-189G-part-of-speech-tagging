import matplotlib.pyplot as plt

# Task 1: plotting the learning curve

# gather information

errorRatesByWord = {
	1000: 0.0965129453233184,
	100: 0.206206614944875,
	1500: 0.0818481290649548,
	2000: 0.0766507964204701,
	200: 0.20720528671925,
	500: 0.126468382904274,
	50: 0.228085106382979,
};

errorRatesBySentence = {
	1000: 0.766,
	100: 0.91,
	1500: 0.726,
	2000: 0.709411764705882,
	200: 0.86,
	500: 0.824,
	50: 1,
};

# doing plotting procedure

# consulted: https://stackoverflow.com/a/16935984/7686917
plt.plot(*zip(*sorted(errorRatesByWord.items())))
plt.plot(*zip(*sorted(errorRatesBySentence.items())))

plt.xlabel('Number of lines from the corpus')
plt.ylabel('Percent error')

plt.title('Learning Curve')

plt.show()
