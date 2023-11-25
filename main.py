import numpy as np
import pandas as pd



def second():
	data = pd.read_csv('data/HW_CLUSTERING_SHOPPING_CART_v2225a2.csv')
	data = data.drop("ID", axis=1)
	unformattedAnswers = data.corr()
	answers = np.round(unformattedAnswers, 2)

	np.fill_diagonal(answers.values, np.nan)
	row_labels = answers.index.tolist()
	col_labels = answers.columns.tolist()
	colMax = "Milk"
	rowMax = "Milk"
	maxVal = -2
	for (i, j), value in np.ndenumerate(answers):
		if maxVal<abs(value):
			maxVal = abs(value)
			colMax = j
			rowMax = i
	#if "Chips" in answers.columns and "Cereal" in answers.columns:
	#	print(answers.at["Chips", "Cereal"])
	#else:
	#	print("One or both of the columns 'Chips' and 'Cereal' do not exist in the DataFrame")

	print(colMax)
	print(rowMax)
	print(maxVal)
	print(answers.iat[3,0])
	return answers


if __name__ == "__main__":
	#print(second())
	second()