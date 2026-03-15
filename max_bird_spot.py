t = int(input())

for _ in range(t):
    n = int(input())
    periods = list(map(int, input().split()))
    
    q = int(input())
    
    for _ in range(q):
        x, y = map(int, input().split())
        
        max_birds = 0
        
        for time in range(x, y + 1):
            count = 0
            
            for p in periods:
                if time % p == 0:
                    count += 1
            
            max_birds = max(max_birds, count)
        
        print(max_birds)