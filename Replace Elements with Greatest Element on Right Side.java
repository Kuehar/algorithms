class Solution {
    public int[] replaceElements(int[] arr) {
         for (int i = arr.length - 1, mx = -1; i >= 0; --i)
            mx = Math.max(arr[i], arr[i] = mx);
        return arr;
    }
}
// Runtime: 3 ms, faster than 40.74% of Java online submissions for Replace Elements with Greatest Element on Right Side.
// Memory Usage: 54.2 MB, less than 5.51% of Java online submissions for Replace Elements with Greatest Element on Right Side.
