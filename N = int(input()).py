#def average (numbers):
 #   return sum(numbers)/len(numbers)
#numbers= [10,20,30,40,50]
#print("average = ",average(numbers))

#def longest_word(words):
 #   longest=""
  #  for word in words:
   #     if len(word)>len(longest):
    #        longest = word 
    #return longest
#words = ["apple","banana","cherry","date"]
#print("te longest word is ",longest_word(words))

#def is_prime(number):
 #   if number <= 1 :
  #      return False 
   # for i in range (2,int(number**0.5)+1):
    #    if number % i == 0 :
     #       return False 
      #  else :
     #       return True 
#print("is prime ?",is_prime(36))
#print("is prime ?",is_prime(29))

#numbers = [1,2,3,4,5,6]
#square_list= list(map(lambda x :x**2,numbers))
#print("square list is ",square_list)

def square(numbers):
    sqr=[]
    for number in numbers:
       n= number**2 
       sqr.append(n)
    return sqr 
numbers=[1,2,3,4,5,6]
print(square(numbers))



        
