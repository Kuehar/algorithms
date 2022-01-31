class Solution {
    public boolean validMountainArray(int[] arr) {
        int N = arr.length;
        int i = 0;
        
        // before reaching peak.
        while(i+1 < N && arr[i] < arr[i+1]){
            i++;
        }
        
        // peak can't be first or last.
        if(i==0 || i==N-1){
            return false;
        }
        
        // after reaching peak.
        while(i+1 < N && arr[i] > arr[i+1]){
            i++;
        }
        
        return i == N-1;
    }
}
// Runtime: 3 ms, faster than 38.67% of Java online submissions for Valid Mountain Array.
// Memory Usage: 55 MB, less than 6.47% of Java online submissions for Valid Mountain Array.
