package 面经;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
  TreeNode left;
  TreeNode right;
}

public class ConstructCompleteBinaryTree {
  public static TreeNode Construct(TreeNode root) {
    if (root == null)
      return null;
    // use BFS to count the number of nodes each level
    int allCount = 0;
    List<Integer> countPerLevel = new ArrayList<Integer>();
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
      int size = queue.size();
      countPerLevel.add(size);
      allCount += size;
      for (int i = 0; i < size; i++) {
        TreeNode cur = queue.poll();
        if (cur.left != null)
          queue.offer(cur.left);
        if (cur.right != null)
          queue.offer(cur.right);
      }
    }
    // calculate the ideal height of the tree
    int needAdd = 0, needDelete = allCount - 1;
    int minOperations = needDelete, idealHeight = 0; // height = 0 when there's only a root
    for (int i = 1; i < countPerLevel.size(); i++) {
      needDelete -= countPerLevel.get(i);
      needAdd += Math.pow(2, i - 1) - countPerLevel.get(i - 1);
      int operations = needAdd + needDelete;
      if (operations < minOperations) {
        minOperations = operations;
        idealHeight = i;
      }
    }
    // use BFS to construct a new tree node
    TreeNode newRoot = new TreeNode();
    queue.offer(newRoot);
    int curHeight = 0;
    while (curHeight < idealHeight - 1) {
      int size = queue.size();
      for (int i = 0; i < size; i++) {
        TreeNode cur = queue.poll();
        cur.left = new TreeNode();
        cur.right = new TreeNode();
        queue.offer(cur.left);
        queue.offer(cur.right);
      }
      curHeight += 1;
    }
    int lastLevelCount = countPerLevel.get(idealHeight);
    int i = 0;
    while (i < lastLevelCount) {
      TreeNode cur = queue.poll();
      cur.left = new TreeNode();
      i++;
      if (i == lastLevelCount)
        break;
      cur.right = new TreeNode();
      i++;
    }
    return newRoot;
  }
}
