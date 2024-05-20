def compute_closest_to_zero(num):
  positive=[]
  negative=[]
  for i in num:
    if i<0:
      negative.append(i)
    else:
      positive.append(i)
      positive.sort(reverse=True)
        
ts = [7,13,8,4,3,6,7,-10,-7,-12,-3,-9,-1,-6]
print(compute_closest_to_zero(ts))
