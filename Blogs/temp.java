import java.util.HashMap;
import java.util.Map;

public class temp {
    static Map<String, String> hashMap = new HashMap<>();

    private static boolean dfs(String pattern, int pIndex, String s, int sIndex) {
        if (pIndex == pattern.length()) {
            return sIndex == s.length();
        }
        String curpattern = pattern.charAt(pIndex) + "";
        if (hashMap.containsKey(curpattern)) {
            String matchWord = hashMap.get(curpattern);
            if ((sIndex + matchWord.length() > s.length()) || !(s.substring(sIndex, sIndex + matchWord.length()).equals(matchWord))){
                if ((sIndex + matchWord.length() <= s.length())){
                    System.out.println(s.substring(sIndex, sIndex + matchWord.length()));
                    System.out.println(matchWord);
                }
                return false;
            }
            return dfs(pattern, pIndex + 1, s , sIndex + matchWord.length());
        }
        for (int endIndex = sIndex + 1; endIndex < s.length() + 1; endIndex ++) {
            String possibleWord = s.substring(sIndex, endIndex);
            if (hashMap.containsValue(possibleWord)){
                continue;
            }
            hashMap.put(curpattern, possibleWord);
            if (dfs(pattern, pIndex + 1, s, sIndex + possibleWord.length())) {
                return true;
            }
            hashMap.remove(curpattern);
        }
        return false;
    }
    
    public static boolean wordPatternMatch(String pattern, String s) {
        return dfs(pattern, 0, s, 0);
    }

    public static void main(String[] args) {
        System.out.println(wordPatternMatch("abab", "redblueredblue"));
    }
}
