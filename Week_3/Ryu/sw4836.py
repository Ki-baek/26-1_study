import sys
sys.stdin = open('input.txt', 'r')	
input = sys.stdin.readline


T=int(input())

for tc in range(1,T+1):
    N=int(input())

    myMap=[[0]*10 for _ in range(10)] #10*10 0으로 채워진거 생성
    Pupple_cnt=0
    
    for _ in range(N):
        r1,c1,r2,c2,color=map(int,input().split())
    
        for y in range(r1,r2+1):
            for x in range(c1,c2+1):
                myMap[y][x]+=color
        
    for Y in range(10):
        for X in range(10):
            if myMap[Y][X]==3:
                Pupple_cnt+=1
    
    print(f"#{tc} {Pupple_cnt}")


                
      
