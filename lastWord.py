def length(a):
    l = 0
 
    
    x = a.strip()
 
    for i in range(len(x)):
        if x[i] == " ":
            l = 0
        else:
            l += 1
    return l

if __name__ == "__main__":
    str = input("Enter a string: ")
    print("The length of last word is",
          length(str))
