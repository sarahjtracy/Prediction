import csv

def makeNewFile():
	new = list()
	new += makeNew("OriginalBets/betting-2006.csv")
	new += makeNew("OriginalBets/betting-2010.csv")
	new += makeNew("OriginalBets/betting-2014.csv")
	new += makeNew("OriginalBets/betting-2018.csv")

	row = ["Team1", "Team2", "Result", "goalDiff", "extraTime", "team1Odd", "tieOdd", "team2Odd", "year", "isPlayoffs"]
	with open('betting.csv', 'wb') as csvfile:
		csvWriter = csv.writer(csvfile, delimiter=",")
		csvWriter.writerow(row)
		for row in new:
			csvWriter.writerow(row)

def makeNew(fileName):
	print fileName
	with open(fileName, 'rU') as csvfile:
		csvReader = csv.reader(csvfile, delimiter=",")
		new = list()
		for row in csvReader:
			treat = treatRow(row)
			if (type(treat) == list):
				new += [treat+[year, isPlayoffs]]
			elif (type(treat) == tuple): 
				(year, isPlayoffs) = treat
	return new

def treatRow(row):
	if (','.join(row) == ",,,,,,"):
		return
	elif (":" in row[0]):
		teams = row[1].split("-")
		team1 = teams[0].strip()
		team2 = teams[1].strip()
		score = row[2]
		extraTime = "ET" in score
		score = score.replace("ET", "")
		if ("pen" in score):
			result = "X"
			goalDiff = 0
		else:
			scores = score.split(":")
			team1Goals = int(scores[0])
			team2Goals = int(scores[1])
			if (team1Goals > team2Goals):
				result = team1
			else:
				result = team2
			goalDiff = team1Goals - team2Goals
		team1Odd = row[3]
		tieOdd = row[4]
		team2Odd = row[5]
		row = [team1, team2, result, goalDiff, extraTime, team1Odd, tieOdd, team2Odd]
		return row
	else:
		isPlayoffs = ("Play Offs" in row[0])
		if (isPlayoffs):
			year = row[0][7:11]
		else:
			year = "20" + row[0][7:9]
		return (year, isPlayoffs)

makeNewFile()
