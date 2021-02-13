// 1302. Deepest Leaves Sum (Medium)
class Solution {
private:
    int sum = 0;
    int maxLevel = 0;
public:
    int deepestLeavesSum(TreeNode* root) {
        if (!root) return 0;
        sumHelper(root, 0);
        return sum;
    }
    void sumHelper(TreeNode* root, int level) {
        if (!root) return;
        if (level > maxLevel) {
            maxLevel = level;
            sum = 0;
        } 
        if (level == maxLevel) {
            sum += root->val;
        }
        sumHelper(root->left, level+1);
        sumHelper(root->right, level+1);
    }
};
// Time complexity: O(N)
// Space complexity: O(N)

// 617. Merge Two Binary Trees (Easy)
TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
    if (!root1 && !root2) { return root1; }
    else if (root1 && !root2) { return root1; }
    else if (!root1 && root2) { return root2; }
    root1->val += root2->val;
    root1->left = mergeTrees(root1->left, root2->left);
    root1->right = mergeTrees(root1->right, root2->right);
    return root1;
}
// Time complexity: O(N)
// Space complexity: O(N) worst case; O(logN) average case;

// 226. Invert Binary Tree (Easy)
TreeNode* invertTree(TreeNode* root) {
    if (!root) { return root; }
    TreeNode* left = root->left;
    TreeNode* right = root->right;
    root->left = right;
    root->right = left;
    invertTree(root->left);
    invertTree(root->right);
    return root;
}
// Time complexity: O(N)
// Space complexity: O(N) worst case; O(logN) average case;

// 124. Binary Tree Maximum Path Sum (Hard)
int currMax;
int maxPathSum(TreeNode* root) {
    currMax = INT_MIN;
    maxPathHelper(root);
    return currMax;
}
int maxPathHelper(TreeNode* root) {
    if (!root) return 0;
    int left = max(maxPathHelper(root->left), 0);
    int right = max(maxPathHelper(root->right), 0);
    currMax = max(currMax, left + right + root->val);
    return max(left, right) + root->val;
}
// Time complexity: O(N)
// Space complexity: O(N) worst case; O(logN) average case;

// 108. Convert Sorted Array to Binary Search Tree (Easy)
TreeNode* sortedArrayToBST(vector<int>& nums) {
    if (nums.size() == 0) {
        return NULL;
    }
    return helper(nums, 0, nums.size()-1);
}
TreeNode* helper(vector<int>& nums, int lo, int hi) {
    if (lo <= hi) {
        int mid = (lo + hi) / 2;
        TreeNode* curr = new TreeNode(nums[mid]);
        curr->right = helper(nums, mid+1, hi);
        curr->left = helper(nums, lo, mid-1);
        return curr;
    }
    return NULL;
}
// Time complexity: O(N)
// Space complexity: O(logN)

// 116. Populating Next Right Pointers in Each Node (Medium)
Node* connect(Node* root) {
    if (!root || (!root->left && !root->right)) { return root; }
    queue<Node*> q;
    bfs(root, q, 0);
    return root;
}
void bfs(Node* root, queue<Node*> q, int level) {
    q.push(root);
    Node* curr;
    int size = 0;
    while (!q.empty()) {
        size = q.size();
        curr = q.front();
        q.pop();
        if (curr->left && curr->right) {
            q.push(curr->left);
            q.push(curr->right);
        }

        size--;
        for (int i = 0; i < size; i++) {
            curr->next = q.front();
            q.pop();
            curr = curr->next;
            if (curr->left && curr->right) {
                q.push(curr->left);
                q.push(curr->right);
            }
        }
        curr->next = NULL;
    }
}
// Time complexity: O(M) for M nodes in the treee
// Space complexity: O(N) for using a queue


// 104. Maximum Depth of Binary Tree (Easy)
int maxDepth(TreeNode* root) {
    if (root == NULL) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}
// Time complexity: O(N)
// Space complexity: O(logN)

// 94. Binary Tree Inorder Traversal (Medium)
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> res;
    helper(root, res);
    return res;
}
void helper(TreeNode* root, vector<int>& res) {
    if (root != NULL) {
        helper(root->left, res);
        res.push_back(root->val);
        helper(root->right, res);
    }
}
// Time complexity: O(N)
// Space complexity: O(N)
