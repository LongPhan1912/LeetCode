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
