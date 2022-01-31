public int[] squareEven(int[] array, int length) {
  // Check for edge cases.
  if(array == null){
    return null;
  }
  
  // Create a resultant Array which would hold the result.
  int result[] = new int[length];
  
  // iterate through the original array.
  for(int i=0;i<length;i++){
    
    // Get the element from slot i of the input Array.
    int element = array[i];
    
    // if the index is an even number, then we need to square element.
    
    if(i%2 == 0){
      element *= element;
    }
    
    // Write element into the result array.
    result[i] = element;
  }
  
  // Return the result array.
  return result;
}
