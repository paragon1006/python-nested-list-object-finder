#example arrays
num=[[2,4],[6,8],[10,12]]
Carinventory=["3",["1","ford","mustang gt","2017","$80,000","2"],["2","jeep","grand cherokee","2015","$67,000","7"],["3","skoda","rapid","2017","$43,489","5"]]
def searcher(finder,nest):#function defining
	try: #to prevent errors for ruining code
		n=len(nest) #counts how many times to run loop
		for i in range(0,n):  #runs loop "n" times ^(refer there)
			if finder in nest[i]:#looks for our searching value
				templist=nest[i] #creates temporary list for finding position of "searched value"
				templist.index(finder) #searches position of ^(refer there) 
				print("found[%d][%d]"%(i,templist.index(finder))) #prints location in sublist
				print(nest[i]) #prints all data in sublist
		return "" #removes addition of "none while running program
	except: #what if program goes wrong \/(refer there)
		return "error" #prints error to let user know there was an error somewhere
print(searcher(2,num)) #example run 1
print(searcher(input("what are you looking for: "),Carinventory)) #example run 2