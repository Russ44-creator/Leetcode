import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import static org.junit.Assert.*;
//hashmap <row, set<col>>
//1,1
//black: 1:<1>
//white: -1:<-1>


// B W W B B W W B B .... 
//0 1 2 3 4 5 6 
//invalid input on the grid
//after win player 
public class Connect6 {
    public int currentPlayer;
    public HashMap<Integer, Set<Integer>> occupiedBlack;
    public HashMap<Integer, Set<Integer>> occupiedWhite;
    public int turnsLeft; 
    public Connect6(int k) {
        // de goes here
        this.currentPlayer = 1;
        this.turnsLeft = 1;
        this.occupiedBlack = new HashMap<>();
        this.occupiedWhite = new HashMap<>();
        
    }

    public String getTurn() {
        // Code goes here
        
        String turn = this.currentPlayer == 1?"black":"white";
        return turn;
    }
    // throw new IllegalArgumentException(
    public boolean placeBlack(int x, int y) {
        // Code goes here
        if(this.occupiedBlack.containsKey(x) && this.occupiedBlack.get(x).contains(y) ||(
            this.occupiedWhite.containsKey(x) && this.occupiedWhite.get(x).contains(y)
        )){
            throw new IllegalArgumentException("Occpied grid. Please enter again");
        }
        if(!this.occupiedBlack.containsKey(x)){
            this.occupiedBlack.put(x, new HashSet<>());
            
        }
        this.occupiedBlack.get(x).add(y);
        
        boolean win = checkWin(x, y);
        this.turnsLeft--;
        if(this.turnsLeft == 0){
            this.currentPlayer = 0;
            this.turnsLeft = 2;
        }
        
        return win;
        
    }
    
    public boolean placeWhite(int x, int y) {
        // Code goes here
        if(this.occupiedBlack.containsKey(x) && this.occupiedBlack.get(x).contains(y) ||(
            this.occupiedWhite.containsKey(x) && this.occupiedWhite.get(x).contains(y)
        )){
            throw new IllegalArgumentException("Occpied grid. Please enter again");
        }
        if(!this.occupiedWhite.containsKey(x)){
            this.occupiedWhite.put(x, new HashSet<>());
            
        }
        this.occupiedWhite.get(x).add(y);
        boolean win = checkWin(x, y);
        this.turnsLeft--;
        if(this.turnsLeft == 0){
            this.currentPlayer = 1;
            this.turnsLeft = 2;
        }
        return win;
    }
    //check wininng : (i,j)
    //row (i,j-5)->(i,j+5) 
        //check same play
    //col 
    //diagnal
    //antidiagnal
//hashmap : piecies
//int palyer: whose turn
//function to check winning status
    private boolean checkWin(int x, int y){
        
        int[] xMove = new int[]{0,1,1,1};
        int[] yMove = new int[]{1,0,1,-1};
        for(int i = 0; i < 4; i++){
            int count = 0;
            int xStart = x-6*xMove[i];
            int yStart = y-6*yMove[i];
            
            for(int j = 0; j < 11; j++){
                xStart = xStart+xMove[i];
                yStart = yStart+yMove[i];
                if(this.currentPlayer == 1){
                    if(this.occupiedBlack.containsKey(xStart) && this.occupiedBlack.get(xStart).contains(yStart)){
                        count++;
                    }
                    else{
                        count=0;
                    }
                    if(count == 6)return true;
                }
                else{
                     if(this.occupiedWhite.containsKey(xStart) && this.occupiedWhite.get(xStart).contains(yStart)){
                        count++;
                    }
                    else{
                        count=0;
                    }
                    if(count == 6)return true;
                }
            }
            
        }
        return false;
    }
    
    
    public static void main(String args[] ) throws Exception {
        Connect6.runSimpleTest();
    }

    public static void runSimpleTest() {
        Connect6 board = new Connect6(100);

        assertEquals("black", board.getTurn());
        board.placeBlack(50, 50);

        assertEquals("white", board.getTurn());
        board.placeWhite(51, 50);
        board.placeWhite(51, 51);

        assertEquals("black", board.getTurn());
        board.placeBlack(50, 51);
        board.placeBlack(50, 49);

        assertEquals("white", board.getTurn());
        board.placeWhite(52, 50);
        board.placeWhite(53, 51);

        assertEquals("black", board.getTurn());
        assertFalse(board.placeBlack(50, 52));
        assertFalse(board.placeBlack(50, 53));

        assertEquals("white", board.getTurn());
        assertFalse(board.placeWhite(53, 50));
        assertFalse(board.placeWhite(54, 51));

        assertEquals("black", board.getTurn());
        assertTrue(board.placeBlack(50, 48)); // Black wins along row 50
    }
}