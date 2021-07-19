'''
Program considers all the segment inputs to be the coordinate point in quadrants of cartesian plane where respective x or y axis will be the last position of the tortoise in plane.
Starting position of tortoise for any segment I is considered to be (first value of I segment, 0) and it moves horizontally initially.
Tortoise rotates 90 degree clockwise after each segment.
'''
def getHorizontalSeg(coordinates, current):
    for i in range(0, current-1, 2):
        a = coordinates[i][2] <= coordinates[current][0] and coordinates[current][0] <= coordinates[i][3]
        b = coordinates[current][2] <= coordinates[i][1] and coordinates[i][1] <= coordinates[current][3]
        if a and b: return (i,current)
    return None

def getVerticalSeg(coordinates, current):
    for i in range(1, current-1, 2):
        a = coordinates[i][2] <= coordinates[current][1] and coordinates[current][1] <= coordinates[i][3]
        b = coordinates[current][2] <= coordinates[i][0] and coordinates[i][0] <= coordinates[current][3]
        if a and b: return (i,current)
    return None
    
def getSegment(arr, l):
    coordinates = [[arr[0][-1], 0, min(arr[0]), max(arr[0])]]
    for i in range(1,l):
        seg = None
        if i%2 == 1:
            coordinates.append([coordinates[-1][0], arr[i][-1], min(arr[i]), max(arr[i])])
            seg = getHorizontalSeg(coordinates, i)
        else:
            coordinates.append([arr[i][-1], coordinates[-1][1], min(arr[i]), max(arr[i])])
            seg = getVerticalSeg(coordinates, i)
        if seg is not None: return seg
    return -1

if __name__ == "__main__" :
    arr = []
    l = int(input("Enter no of segments :"))
    print("Input each segment with space separated values.")
    for i in range(l):
        a = list(map(int, input().split()))
        arr.append(a)
    ans = getSegment(arr, l) 
    if ans == -1: print("No segments crossed.")
    else: print("Segment No. " + str(ans[0]+1) + " is crossed by Segment No. "+ str(ans[1]+1))
