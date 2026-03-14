def count_like_dislike(A, P):
    count = 0
    
    for i in range(len(A)):
        if A[i] == P[i]:
            count += 1
            
    return count


A = input().strip()
P = input().strip()

print(count_like_dislike(A, P))