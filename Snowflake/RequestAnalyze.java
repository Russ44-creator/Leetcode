package 面经;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// Sliding window
public class RequestAnalyze {
  public static int[] getDroppedRequests(int[] requests) {
    int curTime = -1, reqCount = 0;
    List<Integer> droppedRequests = new ArrayList<>();
    Queue<Integer> queuedRequests10s = new LinkedList<>();
    /*
     * iterate through the requests:
     * 1. if there are equal or more than 3 requests for the current time, drop all
     * the following requests for this second
     * 2.1 else, pop all the requests that arrive earlier than 10s from the head of
     * the queue
     * 2.2 if there are equal or more than 20 requests in the queue, drop all the
     * following requests for this second
     * 3. add request into the queue
     */
    for (int i = 0; i < requests.length; i++) {
      int reqTime = requests[i];
      if (reqTime != curTime) {
        curTime = reqTime;
        reqCount = 0;
      }
      if (reqCount >= 3) {
        droppedRequests.add(reqTime);
      } else {
        while (!queuedRequests10s.isEmpty() && queuedRequests10s.peek() <= curTime - 10) {
          queuedRequests10s.poll();
        }
        if (queuedRequests10s.size() >= 20) {
          droppedRequests.add(reqTime);
        } else {
          queuedRequests10s.add(reqTime);
          reqCount++;
        }
      }
    }
    int[] ans = new int[droppedRequests.size()];
    for (int i = 0; i < ans.length; i++) {
      ans[i] = droppedRequests.get(i);
    }
    return ans;
  }

  public static void main(String[] args) {
    int[] requests1 = new int[] { 1, 1, 2, 3, 3, 3 };
    int[] requests2 = new int[] { 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 12, 12, 12 };
    int[] requests3 = new int[] { 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9, 12, 12, 12, 12,
        13, 14, 15, 16 };
    int[] requests4 = new int[] {};

    for (int i : getDroppedRequests(requests4)) {
      System.out.println(i + " ");
    }
  }
}
