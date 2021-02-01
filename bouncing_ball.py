def bouncing_ball(h,b,w):
    if (h > 0) and (b>0 and b<1) and (w<h):
        count=0
        while h > 0 and (w<h):
            count=count+1 ## for 1 bounce
            h=(h*b)
        return (count*2)-1 ## for bounce and up and down
    else:
        return -1
