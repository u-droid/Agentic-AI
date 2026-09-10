# Pythonic way
def pyreverse(arr):
    return arr[::-1]

# Basic
def reverse(arr):
    return [arr[index] for index in range(len(arr)-1,-1,-1)]

if __name__=="__main__":
    arr = [1,2,3,4,5]
    print(reverse(arr))

