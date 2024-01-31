// invariant: upon entry, color[index] is already colored.
bool helper(const vector<vector<int>>& g, vector<int>& color, int index, int k) {
    for (int child : g[index]) {
        if (color[child] == color[index]) return false;
    else if (color[child] != 0) continue;
    // color[child] == 0
    for (int c = 1; c <= k; c++) {
      if (c == color[index]) continue;
      color[child] = c;
      if (helper(g, color, child, k)) break;
      color[child] = 0;
    }
    // impossible to color child.
    if (color[child] == 0) return false;
  }
  return true;
}
vector<int> k_color(const vector<vector<int>>& g, int k) {
  int n = g.size();
  vector<int> color(n);
  for (int i = 0; i < n; i++) {
    if (color[i] == 0) color[i] = 1;
    if (!helper(g, color, i, k)) return {};
  }
  return color;
}