#6 Given a string ‘s’ and a string ‘f’, find no of times string f occurs in string s

def countFreq(pat, txt):
	M = len(pat)
	N = len(txt)
	res = 0
	for i in range(N - M + 1):

		j = 0
		while j < M:
			if (txt[i + j] != pat[j]):
				break
			j += 1

		if (j == M):
			res += 1
			j = 0
	return res
	
if __name__ == '__main__':
	s = input("Enter The String: ")
	f = input("Enter the Substring: ")
	print("The string ",f," appears in ",s ,countFreq(f, s)," times")