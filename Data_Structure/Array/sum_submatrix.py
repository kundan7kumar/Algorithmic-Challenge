def sum_submatrix(arr):
    sum = 0
    n=len(arr)
    for i in range(n):
        for j in range(n):
            left= (i+1)*(j+1)
            right = (n-i)*(n-j)
            sum+=(left*right*arr[i][j])
    return sum

arr = [[ 1, 1, 1 ],
           [ 1, 1, 1 ],
           [ 1, 1, 1 ]];
print(sum_submatrix(arr))