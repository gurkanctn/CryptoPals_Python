"""
Gürkan Çetin, 12 June 2017
github\gurkanctn

My first attempt at Crypto Pals Challenge set.

It's quite possible that I took the challenge wrong and my use of high level
Python functions might be against the expectations of the challange. Whatever.
(Python allows low level stuff but not as low as assembly or C would get. So,
the way I used binascii() might not be what the challenge is expecting.)

THIS IS CHALLENGE #1

MORE INFO ON CRYPTO PALS CHALLENGES: https://cryptopals.com/sets/1/challenges/1
_______________________________________
"Convert hex to base64
The string: 
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Should produce: 
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

So go ahead and make that happen. You'll need to use this code for the rest of the exercises. 

Cryptopals Rule
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing."
_______________________________________
"""
import binascii

inputText="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print ("inputText     : \n", inputText)
Answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
print ("Correct Answer: \n ", Answer)

inputBin = binascii.unhexlify(inputText)
myResult = binascii.b2a_base64(inputBin) #Temporary, work variable

myResult2 = ""

for i in range(len(myResult)):
    #print (chr(myResult[i]), ":", myResult[i])
    if myResult[i]!=10:
        myResult2+= chr(myResult[i])
	
#print ("myResult  : ", myResult)  #just info
print ("myResult2 : \n ",myResult2)

if myResult2 == Answer:
	print ("\nWELL DONE!!! Challenge-1 Complete")
else:
	print("TRY AGAIN...")
		
"""Convert binary data to a line of ASCII characters in base64 coding. The return value is the converted line, including a newline char. The newline is added because the original use case for this function was to feed it a series of 57 byte input lines to get output lines that conform to the MIME-base64 standard. Otherwise the output conforms to RFC 3548."""

"""
REAL ALGORITHM follows:
The text to be encoded in converted into its respective decimal values, that is,
into their ASCII equivalent (i.e. a:97, b:98, etc.). Here’s the ASCII table.

The decimal values obtained in the above step are converted into their binary
equivalents (i.e. 97: 01100001).

All the binary equivalents are concatenated, obtaining a large set of binary 
numbers.

The large set of binary numbers is divided into equal sections, with each 
section containing only 6 bits.

The equal sets of 6 bits are converted into their decimal equivalents.

Finally, the decimal equivalents are converted into their Base64 values 
(i.e. 4: E). Here are the decimal values and their Base64 alphabet.

"""
