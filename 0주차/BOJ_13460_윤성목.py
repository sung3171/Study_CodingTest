# 백준_ 삼성 SW 역량 테스트 기출 문제 _ 구슬 탈출 2

import sys
from collections import deque
n,m=map(int,input().split())
board=[list(sys.stdin.readline().strip()) for _ in range(n)]

def move(r,c,dr,dc):
    cnt=0
    while 0<r+dr<n and 0<c+dc<m and board[r+dr][c+dc]!='#' and board[r][c]!='O':
        r+=dr
        c+=dc
        cnt+=1
    return r,c,cnt


def bfs():

    for r in range(n):
        for c in range(m):
            if board[r][c]=='B':
                br,bc=r,c
            if board[r][c]=='R':
                rr,rc=r,c
    ans=11
    visited=set()
    q=deque()
    q.append((rr,rc,br,bc,1))
    while q:
        rr,rc,br,bc,depth=q.popleft()
        if depth>10:
            continue
        for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]:
            nrr,nrc,rcnt=move(rr,rc,dr,dc)
            nbr,nbc,bcnt=move(br,bc,dr,dc)
            if board[nbr][nbc]=='O':
                continue
            if nrr==nbr and nrc==nbc:
                if rcnt>bcnt:
                    nrr-=dr
                    nrc-=dc
                if rcnt<bcnt:
                    nbr-=dr
                    nbc-=dc
            if board[nrr][nrc]=='O':
                ans=min(ans,depth)
                continue
            if (nrr,nrc,nbr,nbc) not in visited:
                q.append((nrr,nrc,nbr,nbc,depth+1))
                visited.add((nrr,nrc,nbr,nbc))
    return ans if ans<=10 else -1
print(bfs())
