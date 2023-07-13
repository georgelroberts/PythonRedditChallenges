# 1474 is a pandigital in Roman numerals (MCDLXXIV). 
# It uses each of the symbols I, V, X, L, C, D and M at least once. 
# Find the small handful of pandigital Roman numbers up to 2000. 

def main():
	mapRoman=[(1000,'M'), (900,'CM'),(500,'D'), (400,'CD'), (100,'C'), 
		(90,'XC'), (50,'L'), (40, 'XL'), (10, 'X'), (9,'IX'), (5,'V'), (4,'IV'),(1,'I')]

	for i in range(1,2000):
		curRom=numberToRoman(mapRoman,i)
		if "M" in curRom and "D" in curRom and "C" in curRom and "L" in curRom and "X" in curRom and "V" in curRom and "I" in curRom and len(curRom)==7:
			print(f"{i} ({curRom}),")

def numberToRoman(mapRoman,number):
	romanResult=""
	for num, rom in mapRoman:
		while number >=num:
			number-=num
			romanResult+=rom
	return(romanResult)

if __name__=="__main__":
	main()