def skola(n):
    status=list([0]*n)
    for ucenik in range(0,n):
        for vrata in range(0,n):
            if (vrata+1)%(ucenik+1)==0:
                status[vrata]=int(not status[vrata])
    return (sum(status))
# 0-vrata zatvorena, 1-vrata otvorena
print(skola(6))