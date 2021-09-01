vector<int> tree[200010];
int up[200010][32];

void binary_lifting(int node, int parent) {
	int i;
	up[node][0] = parent;
	for (i = 1; i < 32; i++) {
		if (up[node][i - 1] != -1) {
			up[node][i] = up[up[node][i - 1]][i - 1];
		}
		else {
			up[node][i] = -1;
		}
	}
	for (auto child : tree[node]) {
		if (child != parent) {
			binary_lifting(child, node);
		}
	}
}