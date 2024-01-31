// Some code
//Currency Exchange
//calculate the max exchange rate with at most k steps (1,n-1) from c1 to currency c2
    //max exchange rate for k+1 steps from c1 to c2 = Max(rate(c, c2)* max exchangerate 
    // from c1 to c in at most k steps, k steps c1 to c2) 
    // (c2 will be unused currency in previous k steps)
//rate1*rate2> originalRate

//memo[k, current] max exchenge rate from original currency to current currency with k steps
// = memo[k-1, whatever currency that not used]*rate(current/whatever currency), memo[k-1, current]
public class Solution {
    public static int targetCurr;
    public static double maxTransactionRate(String[] currencies, double[][] table, String target, String currencyAtHand){
        HashMap<String, Integer> names  = new HashMap<>();
        double[][] memo = new double[currencies.length][currencies.length];
        
       // double[][] loggedtable = new double[table.length][table.length];
        for(int i = 0; i < currencies.length; i++){
            names.put(currencies[i],i); 
              
        }
        int current = names.get(currencyAtHand);
        for(int i = 0; i < currencies.length; i++){
            memo[1][i] = table[current][i];
        }
        HashSet<Integer> exchanged = new HashSet<>();
        targetCurr = names.get(target);
       
        exchanged.add(current);
       for(int j = 2; j < table.length; j++){
           for(int i = 0; i < table.length; i++){
                if(!exchanged.contains(i)){    
                    //try add the currency to exchange line
                    exchanged.add(i);
                    memo[j][i] = Math.max(memo[j-1][i], memo[j-1][current]*table[current][i]);
                    exchanged.remove(i);
                }
            }
       }
        
        return memo[table.length-1][targetCurr];
        //whether to add currency in exchange line: log(rate(c/c1))+log(rate(c2/c))-log(rate(c2/c1))>0
        
        
    }
 
    public static void main(String[] args) {
        String[] currencies = new String[]{"USD","CAD","EUR","CNY"};
        double[][] table = new double[][]{{1,1.3,1,6.49},{0.72,1,0.9,5.5},{1.1,1.1,1,7.3},{0.18,0.2,0.136,1}};
        System.out.print(maxTransactionRate(currencies, table, "CNY","USD"));
        
   }
   
}