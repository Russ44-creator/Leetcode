public class maxHeap {
    private static void swap(int[] tree, int i, int j) {
        int temp = tree[i];
        tree[i] = tree[j];
        tree[j] = temp;
    }
    
    private static void heapify(int[] tree, int n, int i) {
        if (i >= n) {
            return;
        }
        int lefti = 2 * i + 1;
        int righti= 2 * i + 2;
        int maxi = i;
        if (lefti < n && tree[lefti] > tree[maxi]) {
            maxi = lefti;
        }
        if (righti < n && tree[righti] > tree[maxi]) {
            maxi = righti;
        }
        if (i != maxi) {
            swap(tree, i, maxi);
            heapify(tree, n, maxi);
        }
    }
    
    private static void buildHeap(int[] tree, int n) {
        int lastNode = n / 2 - 1;
        for (int i = lastNode; i >= 0; i --) {
            heapify(tree, n, i);
        }
    }
    
    public static void heapSort(int[] tree) {
        buildHeap(tree, tree.length);
        for (int i = tree.length - 1; i >= 0; i --) {
            swap(tree, 0, i);
            heapify(tree, i, 0);
        }
    }
    
    public static void main(String[] argrs) {
        int [] testArr = {4, 3, 8, 1, -1, 2, 5, 4};
        heapSort(testArr);
        // System.out.println(testArr);
        for (int i = 0; i < testArr.length; i++) {
            System.out.println(testArr[i]);
        }
    }

}
