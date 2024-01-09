
class bisectMy:

    def bisect_left(self,arr, target):

        l, r = 0, len(arr)-1

        while l <= r:
            mid = (l+r)//2

            if target <= arr[mid]:
                r = mid-1
            else:
                l = mid+1

        return l
    

    def bisect_right(self, arr, target):

        l, r = 0, len(arr)-1
        
        while l <= r:
            mid = (l+r)//2

            if target >= arr[mid]:
                l = mid+1
            else:
                r = mid-1

        return l
    
    