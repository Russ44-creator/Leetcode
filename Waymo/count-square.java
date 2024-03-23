import java.util.*;
public class Main {

    public static void main (String[] args) {
        int[][] points = {
            {0, 0}, {0, 1}, {0, -1}, {1, 0}, {1, 1}, {1, 2}, {1, -1},
            {1, -2}, {2, 1}, {2, 2}, {2, -1}, {-1, 0}, {-1, 1},
            {-1, 2}, {-1, -1}, {-1, -2}, {-2, 1}, {-2, -1}
        };
        System.out.println(squareCount(points)); // 11
    }

    public static int squareCount(int[][] points) {
        int len = points.length;
        if (len < 4) // Need atleast 4 points to form square
            return 0;
    
        HashMap<Integer, List<Integer>> dictX = new HashMap();
        for (int i = 0; i < len; i++) {
            int x = points[i][0];
            int y = points[i][1];
        
            List<Integer> list = new ArrayList();
            if (dictX.containsKey(x))
                list = dictX.get(x);
            list.add(y);
            dictX.put(x, list);
        }
    
        int squareCount = 0;
        HashSet<Integer> visX = new HashSet();
        for (Integer x : dictX.keySet()) {
            List<Integer> listOfY = dictX.get(x);
            int totalY = listOfY.size();
        
            // Consider all pair of Y's for current X using two loops(inner and outer)
            for (int i = 0; i < totalY; i++) {
                int y1 = listOfY.get(i);
                for (int j = i + 1; j < totalY; j++) { 
                    int y2 = listOfY.get(j);
                
                    int lineLength = Math.abs(y2 - y1); // Possible Vertical lineLength
                
                    // Check if we have horizontal line of same length
                
                    int x2 = x + lineLength; // Towards right side
                    if (dictX.containsKey(x2) && !visX.contains(x2)) {
                        // Get all Y's for x2
                        List<Integer> secondListOfY = dictX.get(x2);
                        if (secondListOfY.contains(y1) && secondListOfY.contains(y2))
                            squareCount++;
                    }
                
                    x2 = x - lineLength; // Towards left side
                    if (dictX.containsKey(x2) && !visX.contains(x2)) {
                        // Get all Y's for x2
                        List<Integer> secondListOfY = dictX.get(x2);
                        if (secondListOfY.contains(y1) && secondListOfY.contains(y2))
                            squareCount++;
                    }
                }
            }
            // System.out.println(x + " " + squareCount);
            visX.add(x);
        }
        return squareCount;
    }
}

