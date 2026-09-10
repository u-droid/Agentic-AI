def check_duplicates(nums):
    hash = {}
    for value in nums:
        if value in hash:
            print(f"Found duplicate({value}) in nums:: {nums}")
            return True
        hash[value] = 1
    print(f"There is no duplicate in:: {nums}")
    return False

if __name__=="__main__":
    assert check_duplicates([1,2,3,4,5])==False
    assert check_duplicates([1,2,3,2])==True
