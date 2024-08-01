def append_in_middle(s1,s2):

    #claculate the middle index of s1
  middle_index = len(s1)//2

  #create the new string by inserting s2 in the middle of s1
  s3= s1[:middle_index]+  s2 + s1[middle_index:]
  return s3

#user input
s1=input("give string 1:")
s2=input("give 2nd string:")

#creating the new string
s3=append_in_middle(s1,s2)

#printing the result
print("the new string is :",s3)