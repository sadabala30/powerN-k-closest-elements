class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        #sorted arr:1)bs something 2)two pointers
        #sorted res ie same order output: ie contiguous + fixed size so 3)window
        #so question is where does window start?: ie we need index not target
        #so we search for best window start index
        #k=4 so window size=4 always, no. of such windows is: n-k

        low,high =0,n-k
        while low<high:
            #We are not searching for: exact target. so no while low<=high:
            mid = low + (high-low)//2 #ie 0+1/2=0
            #case1: window starts from index 0 : [1,2,3,4]
            #case2: window starts from index 1: [2,3,4,5]
            #if window starts at index 0: we only compare ind0  ie mid ele with new right element if window shifts right ie ind4 ele ie mid+k th ele
            curr_num = x-arr[mid]  #no need of abs as array is already sorted
            shift_num = arr[mid+k]-x
            if curr_num>shift_num:
                #we can go for better window start by rejecting low region
                low = mid+1
            else: #ie curr_num==shift_num we will stick to lower index value
                high = mid
            # "Could mid still be valid?": YES (checked with dry run of eg)→ keep it

        return arr[low:low+k]

