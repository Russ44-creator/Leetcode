# https://www.1point3acres.com/bbs/thread-1018819-1-1.html
'''
void graphColoring(int graph[num_nodes][num_nodes], int num_color, int v)
{
    //回溯分配颜色
    int i =0;
    if(v == num_nodes)//如果所有点已经分配过了
    {
        printSolution();//输出解决方案
        return;
    }
    for(i=0; i<num_color; i++)
    {
        if(isSafe(v, graph, i))//判断是否满足，不满足则略过
        {
            vertex[v].color=i;
            graphColoring(graph, num_color, v+1);
            vertex[v].color=0;
        }
    }

}

'''