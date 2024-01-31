// Some code
import static org.junit.Assert.*;
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.internal.TextListener;
import java.util.*;


public class Solution {
    @Test
    public void testSample() {
        runTest(
            "A:1 B:2 C:3 D:3 E:3", 
            new String [] {
                "B:A",
                "C:A",
                "D:A,B",
                "E:B,C",
            },
            new String [] {
                "1,A",
                "2,B,C",
                "1,C,D",
                "2,D,E",
                "1,E",
            });
    }
    
    //A,1
    //B, 2; C,3
    //c,1; d,3
    //d,2;e,3
    //e,1 
  
    public static class Task{
        String name;
        int timeRemain;
        public Task(String name, int timeRemain){
            this.name = name;
            this.timeRemain = timeRemain;
        }
    }
    public static List<String> schedule(Map<String, Integer> codebases, Map<String, Set<String>> deps) {
        //TODO: implement it
        HashMap<String, List<String>> tasksAfter = new HashMap<>();
        Queue<Task> tasksHaveNoDep = new LinkedList<>();
        List<String> result = new ArrayList<>();
        //populating dependncies of a task
        for(Map.Entry<String, Integer> codebase : codebases.entrySet()){
            String before = codebase.getKey();
          
            if(!deps.containsKey(before)){
                Task task = new Task(before, codebase.getValue());
                tasksHaveNoDep.add(task);
            }
        }
        //populate the tasks that have dependencies
        for(Map.Entry<String, Set<String>> dep: deps.entrySet()){
            Set<String> befores = dep.getValue();
            for(String before : befores){
                if(!tasksAfter.containsKey(before)){
                    tasksAfter.put(before, new ArrayList<String>());
                    
                }
                List<String> after = tasksAfter.get(before);
                after.add(dep.getKey());
                tasksAfter.put(before, after);
               
                
                
                
            }
        }
     
       
        while(!tasksHaveNoDep.isEmpty()){
            int minTime = Integer.MAX_VALUE;
            List<Task> clearedTasks = new ArrayList<>();
           // System.out.print(tasksHaveNoDep.size()+"\n");
            while(!tasksHaveNoDep.isEmpty()){
                Task t = tasksHaveNoDep.poll();
               
                minTime = Math.min(t.timeRemain, minTime);
                 
                clearedTasks.add(t); 
                
                     
            }
            
            String currRound = "";
            currRound+=(minTime+",");
            for(Task clearedTask : clearedTasks){
                
                currRound+=(clearedTask.name+",");
                
                clearedTask.timeRemain = Math.max(0, clearedTask.timeRemain-minTime);
 
                if(clearedTask.timeRemain>0){
                    tasksHaveNoDep.add(clearedTask);
                }
                else{
                    if(!tasksAfter.containsKey(clearedTask.name))continue;
                    List<String> tasksToBeCleared = tasksAfter.get(clearedTask.name);
                    
                    
                    for(String taskToBeCleared :  tasksToBeCleared){
                         
                         Set<String> tasks = deps.get(taskToBeCleared);
                          
                         tasks.remove(clearedTask.name);
                         
                         deps.put(taskToBeCleared, tasks);
                        
                        if(deps.get(taskToBeCleared).isEmpty()){
                           
                            Task newClearedTask = new Task(taskToBeCleared, codebases.get(taskToBeCleared));
                            tasksHaveNoDep.add(newClearedTask);
                            
                           
                        }
                    }
                }
                
              
            }
            result.add(currRound);
          System.out.print(currRound+"\n");
           
            
        }
        
        return result;
    }
    
    
    public static void runTest(String codebases, String[] depdendency, String[] expected) {
        Map<String, Integer> c = new HashMap<>();
        Map<String, Set<String>> d = new HashMap<>();
        for (String codebase: codebases.split(" ")) {
            String[] tokens = codebase.split(":");
            if (tokens.length != 2) {
                continue;
            }
            c.put(tokens[0], Integer.parseInt(tokens[1]));
        }
        for (String dep: depdendency) {
            String[] tokens = dep.split(":");
            Set<String> set = new HashSet<>();
            d.put(tokens[0], set);
            for (String subToken : tokens[1].split((","))) {
                set.add(subToken);
            }
        }
        List<String> actual = Solution.schedule(c, d);
        assertEquals(expected.length, actual.size());
        
        if (expected.length == 0) {
            return;
        }
        
        for (int i = 0; i < expected.length; i++) {
            String[] expectedTokens = expected[i].split(",");
            String[] acutalTokens = actual.get(i).split(",");
            assertEquals(expectedTokens.length, acutalTokens.length);
            assertEquals(expectedTokens[0], acutalTokens[0]);
            assertEquals(
                new HashSet<>(Arrays.asList(Arrays.copyOfRange(expectedTokens, 1, expectedTokens.length))), 
                new HashSet<>(Arrays.asList(Arrays.copyOfRange(acutalTokens, 1, acutalTokens.length))));
        }
    }
    
    public static void main(String[] args) {
        JUnitCore junit = new JUnitCore();
        junit.addListener(new TextListener(System.err));
        junit.run(Solution.class);
    }
}