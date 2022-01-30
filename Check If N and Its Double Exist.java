class Solution {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        for(int i:arr){
            if(seen.contains(i*2) || i%2 == 0 && seen.contains(i/2)){
                return true;
            }
            seen.add(i);
        }
        return false;
    }
}
// Runtime: 2 ms, faster than 66.05% of Java online submissions for Check If N and Its Double Exist.
// Memory Usage: 44.4 MB, less than 5.42% of Java online submissions for Check If N and Its Double Exist.
