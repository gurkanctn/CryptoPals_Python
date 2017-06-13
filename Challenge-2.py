"""
Gürkan Çetin, 12 June 2017
https://github.com/gurkanctn/CryptoPals_Python

This is my attempt at the Crypto Pals Challenge Set-1, Challenge-2.

It's quite possible that I took the challenge wrong and my use of high level
Python functions might be against the expectations of the challange. Whatever.
(Python allows low level stuff but not as low as assembly or C would get. So,
the way I used binascii() might not be what the challenge is expecting.)

MORE INFO ON CRYPTO PALS CHALLENGES:
https://cryptopals.com/sets/1/challenges/2
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

def deHex2(str1):  #Converts a string of Hex to an array of Base64
    inputBin = binascii.unhexlify(str1)
    #myResult = binascii.b2a_base64(inputBin) #Temporary, work variable
    myResult2 = []
    for i in range(len(inputBin)):
        #print (chr(myResult[i]), ":", myResult[i])
        if inputBin[i]!=10:
            myResult2.append(inputBin[i])
    return myResult2

def myXOR(str1,str2): #returns a string in Base64 of two strings of Base64
    Result = []
    temp1 = deHex2(str1)
    print("_____\ntemp1  :",temp1)
    temp2 = deHex2(str2)
    print("temp2  :",temp2)
    if len(str1)==len(str2):   
        for i in range(len(temp1)):  # TBD
            Result.append(temp1[i] ^ temp2[i])
#            print(chr(Result[i]))
    else:
        print( "lengths must be equal")
    return (Result)

#Result = binascii.a2b_base64(Result)
"""Convert a block of base64 data back to binary and return the binary data. More than one line may be passed at a time.
binascii.b2a_base64(data, *, newline=True)
Convert binary data to a line of ASCII characters in base64 coding. The return value is the converted line, including a newline char if newline is true. The output of this function conforms to RFC 3548.
Changed in version 3.6: Added the newline parameter."""

#_____________________________________________

input1="1c0111001f010100061a024b53535009181c"
print ("input1  : \n  ", input1)
input2 = "686974207468652062756c6c277320657965"
print ("input2  : \n  ", input2)

Answer = "746865206b696420646f6e277420706c6179"
print ("Answer  : \n  ", Answer)
#______________________________________________

myAnswer = myXOR(input1, input2)
print ("myAnswer: \n  ",myAnswer) #Values seem to be OK, check PADDING!!

myAnswer2=""
myAnswer3=""
for i in range (len(myAnswer)):
    myAnswer2+=chr(myAnswer[i])

if len(myAnswer2) % 4:
   myAnswer2 += '=' * (4 - len(myAnswer2) % 4) 

print ("myAnswer in ASCII: \n  ",myAnswer2)

#for i in range (len(myAnswer)):
#    myAnswer3+=binascii.a2b_base64(myAnswer2[i])

#print ("myAnswer in b64: \n  ",myAnswer3)
    
myAnswer3=binascii.a2b_base64(myAnswer2)   #INCORRECT PADDING!!!
myAnswer3=binascii.b2a_base64(myAnswer3)   #NOT CORRECT!

print ("my FINAL ANSWER in BASE64 readable: ",myAnswer3)

# CHECK IF CHALLENGE COMPLETED SUCCESSFULLY
if myAnswer3 == Answer:
	print ("\nWELL DONE!!! Challenge-2 Complete")
else:
	print("TRY AGAIN...")
