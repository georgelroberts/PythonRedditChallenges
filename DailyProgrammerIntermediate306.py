# Gray code, so named after discoverer Frank Gray, is a binary numeral system where two successive values differ in only one bit (binary digit). 
# Write a program that can generate a Gray code sequence of n bits in length. 

# My implementation is based on the mathematica definition for conversion:
# http://mathworld.wolfram.com/GrayCode.html

def main():
	noBits=3
	greyString=[]
	for i in range(0,2**noBits):
		binaryNo=format(i, 'b').zfill(noBits)
		greyString.append(binToGray(binaryNo, noBits))
	for item in greyString:
		print(item)

def binToGray(binary, noBits):
	# Working with a list is easier than a string because python strings are immutable
	binaryLst=list(binary)
	for i in range(0,noBits-1):
		if binaryLst[noBits-i-2]=='1':
			binaryLst[noBits-i-1]=str(1-int(binaryLst[noBits-i-1]))
	return ''.join(binaryLst)

if __name__=="__main__":
	main()
