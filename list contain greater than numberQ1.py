def numbers(list):
      i = 0
      while i < len(list):
          c=list[i]
          if c>20:
              list.remove(c)
          else:
              i+=1

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num= numbers(num_list)

print ("list that doesnot contain numbers great than 20,", num_list)