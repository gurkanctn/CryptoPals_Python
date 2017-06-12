"""
Gürkan Çetin, 12 June 2017
github\gurkanctn

My first attempt at Crypto Pals Challenge set.

It's quite possible that I took the challenge wrong and my use of high level
Python functions might be against the expectations of the challange. Whatever.
(Python allows low level stuff but not as low as assembly or C would get. So,
the way I used binascii() might not be what the challenge is expecting.)

THIS IS CHALLENGE #2

MORE INFO ON CRYPTO PALS CHALLENGES: https://cryptopals.com/sets/1/challenges/1
_______________________________________
"Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination. 

If your function works properly, then when you feed it the string: 
1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against: 
686974207468652062756c6c277320657965
... should produce: 
746865206b696420646f6e277420706c6179"
_______________________________________
"""
import binascii
# import ggCrypt     #  Cannot call functions from library?!?!

def deHex(str1):  #returns a string in Base64
    inputBin = binascii.unhexlify(str1)
    myResult = binascii.b2a_base64(inputBin) #Temporary, work variable
    myResult2 = ""
    for i in range(len(myResult)):
        #print (chr(myResult[i]), ":", myResult[i])
        if myResult[i]!=10:
            myResult2+= chr(myResult[i])
    return myResult2

def myXOR(str1,str2): #returns a string in Base64 of two strings of Base64
    Result = ""
    temp1 = deHex(str1)
    print("_____\ntemp1  :",temp1)
    temp2 = deHex(str2)
    print("temp2  :",temp2)
    if len(str1)==len(str2):   
        for i in range(10):  # TBD
            Result += chr(ord(temp1[i]) ^ ord(temp2[i]))
            print((Result[i]))
    """ The ^ operator yields the bitwise XOR (exclusive OR) of its
    arguments, which must be integers."""
    #else:
    #    print( "lengths must be equal")
    return deHex(Result)


input1="1c0111001f010100061a024b53535009181c"
print ("input1  : \n  ", input1)
input2 = "686974207468652062756c6c277320657965"
print ("input2  : \n  ", input2)

Answer = "746865206b696420646f6e277420706c6179"
print ("Answer  : \n  ", Answer)

myAnswer = myXOR(input1, input2)
print ("myAnswer: \n  ",myAnswer)

# CHECK IF CHALLENGE COMPLETED SUCCESSFULLY
if myAnswer == Answer:
	print ("\nWELL DONE!!! Challenge-2 Complete")
else:
	print("TRY AGAIN...")
