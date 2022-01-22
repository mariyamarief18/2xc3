def are_valid_groups(stu_no, groups):
    ans = False
    for i in stu_no:
        for j in groups:
            if i in j:
                ans = True
    return ans

print(are_valid_groups([1,2,3,4,5,6,7,8,9], [[1,2,3],[4,5,6],[7,8,9]]))
            