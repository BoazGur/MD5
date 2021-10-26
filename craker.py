import socket,time,threading,math
class craker():
	def __init__(self,ip='0.0.0.0',port=13370):
		self.port = port
		self.ip = ip
		
		s = socket.socket()
		s.conect(ip,port)
		s.send("howdy").encode()
		self.ans = s.recv(1024).decode()

		s.close()

		self.port = self.port + int(self.ans)
		server_soc = socket.socket()
		server_soc.bind(self.ip,self.port)
		server_soc.lisen(1)
		client_soc,adrr = server_soc.accept()

		self.ans = server_soc.recv(1024).decode

	def compare(self,start,end,md5):
		#letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		global letters
		
		
		

	def thread(self):
		start = self.ans.split(",")[0]
		end = self.ans.split(",")[1]
		md5 = self.ans.split(",")[-1]
		gcd=math.gcd(base26LetterToBase10(start),base26LetterToBase10(end))

		threads = []
		for i in range(gcd):
			t = threading.Thread(target=compare,arg=(i,))
			threads.append(t)
			t.start()
		for t in threads:
			t.join()

	def division_to_groups(start,end):
		start_num=base26LetterToBase10(start)
		end_num=base26LetterToBase10(end)

		gcd=math.gcd(start_num,end_num)
		hop= (end_num-start_num)/gcd # difference
		if hop>1:
			hop-=1

		groups=[]#(start,end) 
		for i in range(gcd):
			groups.append((start_num,start_num+hop))
			start_num+=1



def base10ToBase26Letter(num):
    ''' Converts any positive integer to Base26(letters only) with no 0th 
    case. Useful for applications such as spreadsheet columns to determine which 
    Letterset goes with a positive integer.
    '''
    if num <= 0:
        return ""
    elif num <= 26:
        return chr(96+num)
    else:
        return base10ToBase26Letter(int((num-1)/26))+chr(97+(num-1)%26)

def base26LetterToBase10(string):
    ''' Converts a string from Base26(letters only) with no 0th case to a positive
    integer. Useful for figuring out column numbers from letters so that they can
    be called from a list.
    '''
    string = string.lower()
    if string == " " or len(string) == 0:
        return 0
    if len(string) == 1:
        return ord(string)-96
    else:
        return base26LetterToBase10(string[1:])+(26**(len(string)-1))*(ord(string[0])-96)
def main():
	print(base26LetterToBase10("aab"))
	print(type(base26LetterToBase10("aab")))
	print(base10ToBase26Letter(704))
	

if __name__ == "__main__":
	main()