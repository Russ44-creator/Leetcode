public class WordSearch {

    // Part 1
    //给你一个list of words， 给你一个string。 输出是bool， 是不是string包含有一个word from that word list，
    // 字母次序不限。比如asdfciat 包括了cat

    // Convert query and words to frequency array and compare.
    // Complexity: time O(Q + W * N), space O(N), where Q = query.length(), W = word.length(), N = words.size()
    public static boolean containsWord(String query, List<String> words) {
        int[] freq = toCharFreq(query);
        return words.stream()
            .anyMatch(word -> contains(freq, toCharFreq(word)));
    }

    private static boolean contains(int[] freq, int[] wordFreq) {
        for (int i = 0; i < 26; i++) {
            if (wordFreq[i] > freq[i]) {
                return false;
            }
        }
        return true;
    }

    private static int[] toCharFreq(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        return freq;
    }


    // Part 2
    // After catching your classroom students cheating before, you realize your students are getting craftier and
    // hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be
    // either immediately below or immediately to the right of the previous letter.

    //Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates.
    // If there are multiple matches, return any one.
    //grid1 = [
    //        ['c', 'c', 'x', 't', 'i', 'b'],
    //        ['c', 'c', 'a', 't', 'n', 'i'],
    //        ['a', 'c', 'n', 'n', 't', 't'],
    //        ['t', 'c', 's', 'i', 'p', 't'],
    //        ['a', 'o', 'o', 'o', 'a', 'a'],
    //        ['o', 'a', 'a', 'a', 'o', 'o'],
    //        ['k', 'a', 'i', 'c', 'k', 'i'],
    //    ]
    //word1 = "catnip"
    //word2 = "cccc"
    //word3 = "s"
    //word4 = "bit"
    //word5 = "aoi"
    //word6 = "ki"
    //word7 = "aaa"
    //word8 = "ooo"
    //grid2 = [['a']]
    //word9 = "a"
    //find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
    //find_word_location(grid1, word2) =>
    //       [(0, 1), (1, 1), (2, 1), (3, 1)]
    //      OR [(0, 0), (1, 0), (1, 1), (2, 1)]
    //      OR [(0, 0), (0, 1), (1, 1), (2, 1)]
    //      OR [(1, 0), (1, 1), (2, 1), (3, 1)]
    //find_word_location(grid1, word3) => [(3, 2)]
    //find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
    //find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
    //find_word_location(grid1, word6) => [(6, 4), (6, 5)]
    //find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
    //find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
    //find_word_location(grid2, word9) => [(0, 0)]
    //Complexity analysis variables:
    //r = number of rows
    //    c = number of columns
    //w = length of the word

    // Start from each position, DFS with backtracking for the word
    // Time: O(r * c * 4 * 3^(w-1)) = O (r * c * 3^w)
    // Space: O(1)

    public static List<List<Integer>> findWordLocation(char[][] grid, String word) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return null;
        }
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (findWord(grid, i, j, word, 0, new ArrayList<>(), res)) {
                    return res;
                }
            }
        }
        return null;
    }

    private static final int[][] DIRS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    // Recursively search for word[wordIdx...] starting from grid[i][j]
    private static boolean findWord(char[][] grid, int i, int j, String word, int wordIdx,
                                    List<List<Integer>> path,
                                    List<List<Integer>> res) {
        if (wordIdx == word.length()) { // word found
            res.addAll(path);
            return true;
        }
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != word.charAt(wordIdx)) {
            return false;
        }

        // grid[i][j] == word[wordIdx]
        char tmp = grid[i][j];
        path.add(Arrays.asList(i, j));
        grid[i][j] = '#'; // avoid re-visiting (i,j)

        boolean found = false;
        for (int[] dir : DIRS) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (findWord(grid, x, y, word, wordIdx + 1, path, res)) {
                found = true;
                break;
            }
        }

        // Always backtrack to restore grid
        path.remove(path.size() - 1);
        grid[i][j] = tmp;
        return found;
    }


    public static void main(String[] args) {
        System.out.println("Part 1 Test:");
        System.out.println(containsWord("asdtcif", Arrays.asList("cat"))); // true
        System.out.println(containsWord("asdtcif", Arrays.asList("tag"))); // false

        System.out.println("Part 2 Test:");

        char[][] grid1 = {
            {'c', 'c', 'x', 't', 'i', 'b'},
            {'c', 'c', 'a', 't', 'n', 'i'},
            {'a', 'c', 'n', 'n', 't', 't'},
            {'t', 'c', 's', 'i', 'p', 't'},
            {'a', 'o', 'o', 'o', 'a', 'a'},
            {'o', 'a', 'a', 'a', 'o', 'o'},
            {'k', 'a', 'i', 'c', 'k', 'i'}
        };
        String word1 = "catnip";
        String word2 = "cccc";
        String word3 = "s";
        String word4 = "bit";
        String word5 = "aoi";
        String word6 = "ki";
        String word7 = "aaa";
        String word8 = "ooo";
        char[][] grid2 = {{'a'}};
        String word9 = "a";

        System.out.println(findWordLocation(grid1, word1));
        System.out.println(findWordLocation(grid1, word2));
        System.out.println(findWordLocation(grid1, word3));
        System.out.println(findWordLocation(grid1, word4));
        System.out.println(findWordLocation(grid1, word5));
        System.out.println(findWordLocation(grid1, word6));
        System.out.println(findWordLocation(grid1, word7));
        System.out.println(findWordLocation(grid1, word8));

        System.out.println(findWordLocation(grid2, word9));
    }

}