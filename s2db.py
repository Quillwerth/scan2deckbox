import sys

def main():
	print(sys.argv)
	finName=sys.argv[1][0:sys.argv[1].find(".csv")]
	print(finName)
	fin = open(sys.argv[1],"r")
	fout = open("./" + finName + "-out.csv","w")
	foundBeginning = False
	fout.write("Count,Tradelist Count,Name,Edition,Card Number,Condition,Language,Foil\n")
	for lineIn in fin:
		rawSplit = lineIn.split(",") # Folder Name,Quantity,Trade Quantity,Card Name,Set Code,Set Name,Card Number,Condition,Printing,Language,Price Bought,Date Bought,LOW,MID,MARKET
		lineInArray = []
		isCombineSplitVal = False
		combineSplitVal = []
		for splitVal in rawSplit:
			print(splitVal)
			if splitVal.find('"') > -1:
				# Determine if we're within a quote string with commas, or a single string literal
				if splitVal.count('"') == 1:
					if not isCombineSplitVal:
						isCombineSplitVal = True
						combineSplitVal.append(splitVal)
					else:
						# finish combining splitVal
						combineSplitVal.append(splitVal)
						lineInArray.append(",".join(combineSplitVal))
						isCombineSplitVal = False
				else:
					lineInArray.append(splitVal)	
			else:
				lineInArray.append(splitVal)

		print(lineInArray)
		if not foundBeginning:
			if lineInArray[0].find("Folder Name") > -1:
				foundBeginning = True
			continue
		lineOutArray = [] # Count,Tradelist Count,Name,Edition,Card Number,Condition,Language,Foil
		lineOutArray.append(lineInArray[1]) # Count
		lineOutArray.append(lineInArray[1]) # Tradelist Count
		lineOutArray.append(lineInArray[3]) # Name
		lineOutArray.append(lineInArray[5]) # Set Name
		lineOutArray.append(lineInArray[6]) # Card Number
		lineOutArray.append("Near Mint") # I do not care about this being accurate
		lineOutArray.append("English")
		lineOutArray.append("foil\n" if lineInArray[8] == "Foil" else "\n")
		fout.write(",".join(lineOutArray))
	fin.close()
	fout.close()
	return 1





if __name__ == "__main__":
	main()