import numpy as np
import pandas as pd
from typing import List


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

def getDistance(rowA,rowB):
	distance = 0
	for i in rowA.keys():
		distance += abs(rowA.iat[i]-rowB.iat[i])
	return distance



class Cluster:
	proximity = []
	center = None
	points = []
	merged = False
	def __init__(self,row):
		pass
	def addPoint(self,point):
		self.points.append(point)
	def combineNext(self):
		min = self.proximity.keys()
		self.proximity()
	def findCenter(self):
		emptyRow = self.points[0].copy(deep=False)
		
	
	def inputDistance(self, row):
		pass

		
			


class Point():
	row = None
	pointCluster = None
	def __init__(self,row,pointCluster):
		row = row
		pointCluster = pointCluster
class Pair():
	clusterA = Cluster
	clusterB = Cluster
	distance = float("inf")
	def __init__(self,clusterA,clusterB):
		clusterA = clusterA
		clusterB = clusterB
		self.distance = getDistance(clusterA,clusterB)
	def isUsed(self):
		return self.clusterA.merged or self.clusterB.merged
	def getDist(self):
		return self.distance
class orderedList():
	clusterList = []
	currentIndex = 0
	def __init__(self):
		clusterList = []
	def getNext(self):
		for self.currentIndex in range(len(self.clusterList)):
			if self.clusterList[self.currentIndex].isUsed():
				continue
			self.currentIndex+=1
			return self.clusterList[self.currentIndex-1]

		return None
	def addClusterPair(self,clusterA,clusterB):
		newPair = Pair(clusterA,clusterB)
		if len(self.clusterList)==0:
			self.clusterList.append(newPair)
		else:
			for pairIndex in len(self.clusterList):
				if self.clusterList[pairIndex].getDist()>=newPair.getDist():
					self.clusterList.insert(pairIndex,newPair)
					break



def combineCluster(clusterA,clusterB):
	for point in clusterB.points:
		clusterA.points.append(point)
	return clusterA




def QuestionB():
	data = pd.read_csv('data/HW_CLUSTERING_SHOPPING_CART_v2225a2.csv')
	clusters = []
	#currentCluster = 0
	clusterList = []
	for i in range(len(data)):
		clusterList.append(Cluster(data.iloc[i]))
	while(True):
		clusters.append(runCluster(clusters[-1]))

def runCluster(clusterList: List[Cluster]):
	newClusterList = []
	for i in range(len(clusterList)):
		if clusterList[i].merged:
			continue

		minDist = float("inf")
		minIndex = 0

		for j in range(i,len(clusterList)):# Can probably do I -> J since all the ones before would be clustered

			if i == j or clusterList[j].merged:
				continue
			currentDist = getDistance(clusterList[i],clusterList[j])
			if minDist >= currentDist:
				minDist = currentDist
			minIndex = j
		newCluster = combineCluster(clusterList[i],clusterList[minIndex])
		clusterList[i].merged = True
		clusterList[minIndex].merged = True
		newClusterList.append(newCluster)
	return newClusterList



if __name__ == "__main__":
	#print(second())
	second()