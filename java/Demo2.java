class Demo2 {
	public static int getMax(int[] array) {
		int max = 0, i = 0;
	
		max = array[0];
		for (i = 1; i < array.length; i++) {
			if (max < array[i])	{
				max = array[i];
			}
		}

		return max;
	}
	/**
	 *	让每一个元素与后面的元素相比较，如果大（小）的就互换  
	 *	换一次之后第一个元素就是最大（最小）
	 *
	 */
	public static void selectSort(int[] array) {
		int temp;
		int i = 0, j = 0;
		for (i = 0; i < array.length; i++) {
			for (j = i + 1; j < array.length; j++) {
				if (array[i] < array[j]) {
					temp = array[i];
					array[i] = array[j];
					array[j] = temp;
				}
			}
		}
	}
	/**
	 *	让相邻元素作比较，如果大（小）的话就互换
	 *  换完一次之后最大（最小）的元素在尾部，
	 *  之后的比较就没必要在和尾部的元素做比较
	 */
	public static void bubbleSort(int[] array) {
		int temp;
		int i = 0, j = 0;
		for (i = 0; i < array.length; i++) {
			for (j = 0; j < array.length - 1 - i; j++) {
				if (array[j] < array[j + 1]) {
					temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
				}
			}
		}
	}
	public static void main(String[] args) {
		int i = 0;
		int[] array = {12, 5, 7, 10, 15};

		bubbleSort(array);
		for (i = 0; i < array.length; i++) {
			System.out.print(array[i] + " ");
		}

		System.out.println("");

	}
}
