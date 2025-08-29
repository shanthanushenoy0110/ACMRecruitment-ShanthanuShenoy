

def second_largest(arr):      
      largest=second=float("-inf")
      if len(arr)<=1:
            print("No second largest number")
            if len(arr)==1:
                  print(arr[0])
      else:
            for i in arr:
                  if i > largest:
                        second=largest
                        largest=i
                  elif i >second and i !=largest:
                        second=i
            if second==float("-inf"):
                  j="All the elements in the list are the same"
                  return j
            else:
                  return second
arr = list(map(int, input("Enter numbers: ").split()))

print("Second largest:", second_largest(arr))
