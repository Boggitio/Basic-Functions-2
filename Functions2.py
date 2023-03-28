import math

#1 - This function checks if a word is a palindrome and returns the answer.
def isPali(s):
    s = s.lower()
    #print(s)
    if s == s[::-1]:
        return "It is a palindrome."
    else:
        return "It is not a palindrome."
#WordChosen =(str(input("Check which word is a palindrome?   ")))
#print(isPali(WordChosen))


#2 - This functions reads a phrase entered as input, finds the longest word, counts the letters in it and returns the
                                                                    #longest word and the amount of letters in it.
def longword(phrase):
    #phrase = input("Formulate a phrase: ")
    longest = max(phrase.split(), key=len)
    letterscount = len(longest)
    return(longest, letterscount)
    #print("And the amount of letters in it is: ", len(longest))


#3 - This function checks if two given words are anagrams of each other and returns the answer.
def isAnagram(Word1, Word2):
    Word1 = Word1.lower().replace(" ", "")
    Word2 = Word2.lower().replace(" ", "")

    if len(Word1) != len(Word2):
        return "These words ARE NOT anagrams of each other as they do not have the same number of letters in them."
    if sorted(Word1) == sorted(Word2):
        return "These words ARE anagrams of each other."
    else:
        return "These words ARE NOT anagrams of each other."
#Word1 = str(input("Specify a word:   "))
#Word2 = str(input("Specify which word you want to check if it is an anagram of the first word:   "))
#check = isAnagram(Word1, Word2)
#print(check)

#4 - This function finds the sum of two given numbers and returns the result.
def SumofN(x, y):
   # x = int(input("Specify the first number to add "))
  #  y = int(input("Specify the second number "))

    SumofN = x + y
    return(f"The result of the sum is   {SumofN}")


#5 - This functions asks for 4 numbers as an input, adds them to a list and then uses the list to find out the
                                                        # arithmetic average and returns it as a result.
def NMA(x, y, z, n):
    # x = int(input("Specify first number to be added to the list:  "))
    # y = int(input("Specify second number to be added to the list:  "))
    # z = int(input("Specify third number to be added to the list:  "))
    # n = int(input("Specify fourth number to be added to the list:  "))

    nlist = [x, y, z, n]
    resultsum = sum(nlist[0:4])
    #print(resultsum)
    avg = resultsum / len(nlist)
    #print(avg)
    return(f"Sum of the list of numbers is {resultsum} and the average is {avg}.")



