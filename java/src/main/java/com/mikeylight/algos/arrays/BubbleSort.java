class BubbleSort {
    static int[] bubbleSort(int[] numbers) {
        if(numbers == null || numbers.length == 1) {
            return numbers;
        }
        boolean isSorted = false;

        while(!isSorted) {
            isSorted = true;
            for(int i = 0; i < numbers.length - 1; i++) {
                if(numbers[i] > numbers[i + 1]) {
                    int hold = numbers[i + 1];
                    numbers[i + 1] = numbers[i];
                    numbers[i] = hold;
                    isSorted = false;
                }
            }
        }
        return numbers;
    }
}