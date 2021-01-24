// 1721. Swapping Nodes in a Linked List (Medium)
ListNode* swapNodes(ListNode* head, int k) {
    if (head == NULL || head->next == NULL) { return head; }
    vector<int> array;

    ListNode* curr = head;
    while (curr != NULL) {
        array.push_back(curr->val);
        curr = curr->next;
    }
    int inverse = array.size() - k;
    swap(array[k-1], array[inverse]);

    curr = new ListNode(array[0]);
    ListNode* newHead = curr;
    for (int i = 1; i < array.size(); i++) {
        ListNode* nextNode = new ListNode(array.at(i), NULL);
        curr->next = nextNode;
        curr = nextNode;
    }
    head = newHead;
    return head;
}
// Time complexity: O(N)
// Space complexity: O(N)

// memory-efficient method (you can swap the values of the nodes in C++)
ListNode* swapNodes(ListNode* head, int k) {
    if (head == NULL || head->next == NULL) { return head; }

    int size = 0;
    ListNode* curr = head;
    while (curr != NULL) {
        size++;
        curr = curr->next;
    }

    int inverse = size - k + 1;
    int i = 1; // the list is 1-indexed
    ListNode* ptr1, *ptr2;

    curr = head;
    while (curr) {
        if (i == k) { ptr1 = curr; }
        if (i == inverse) { ptr2 = curr; }
        curr = curr->next;
        i++;
    }
    swap(ptr1->val, ptr2->val);
    return head;
}
// Time complexity: O(N)
// Space complexity: O(1)

// 1367. Linked List in Binary Tree (Medium)
// Easy explanation:
bool isSubPath(ListNode* head, TreeNode* root) {
    return DFS(head, root);
}
bool match(ListNode* head, TreeNode* root) {
    if (head == NULL) { return true; }
    if (root == NULL || (head->val != root->val)) { return false; }
    return match(head->next, root->left) || match(head->next, root->right);
}
bool DFS(ListNode* head, TreeNode* root) {
    if (root == NULL) { return false; }
    if (match(head, root)) { return true; }
    return DFS(head, root->left) || DFS(head, root->right);
}
// More condensed code:
bool isSubPath(ListNode* head, TreeNode* root) {
    if (head == NULL) { return true; }
    if (root == NULL) { return false; }
    return DFS(head, root)
        || isSubPath(head, root->left) || isSubPath(head, root->right);
}
bool DFS(ListNode* head, TreeNode* root) {
    if (head == NULL) { return true; }
    if (root == NULL) { return false; }
    return head->val == root->val
        && (DFS(head->next, root->left) || DFS(head->next, root->right));
}

// Time complexity: O(N * min(treeHeight, listLength))
// Space complexity: O(treeHeight)

// 1290. Convert Binary Number in a Linked List to Integer (Easy)
int getDecimalValue(ListNode* head) {
    if (head->next == NULL) { return head->val; }
    int size = 0;
    ListNode* curr = head;
    while (curr) {
        size += 1;
        curr = curr->next;
    }
    int sum = 0;
    curr = head;
    for (int i = 0; i < size; i++) {
        sum += curr->val * pow(2, size-i-1);
        curr = curr->next;
    }
    return sum;
}
// shorter version (one loop only)
int getDecimalValue(ListNode* head) {
    if (head->next == NULL) { return head->val; }
    int sum = head->val;
    while(head->next) {
        sum = sum*2 + head->next->val;
        head = head->next;
    }
    return sum;
}

// Time complexity: O(n)
// Space complexity: O(1)

// 1019. Next Greater Node In Linked List (Medium)
vector<int> nextLargerNodes(ListNode* head) {
    vector<int> ans;
    if (head == NULL) { return ans; }
    while (head) {
        ans.push_back(head->val);
        head = head->next;
    }
    stack<int> s;
    for (int i = ans.size() - 1; i > -1; i--) {
        int val = ans[i];
        while (!s.empty() && s.top() <= val) {
            s.pop();
        }
        ans[i] = s.empty() ? 0 : s.top();
        s.push(val);
    }
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(N)

// 237. Delete Node in a Linked List (Easy)
void deleteNode(ListNode* node) {
    if (node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
}
// Time complexity: O(1)
// Space complexity: O(1)

// 234. Palindrome Linked List (Easy)
bool isPalindrome(ListNode* head) {
    if (head == NULL || head->next == NULL) { return true; }
    ListNode* curr = head;
    std::stack<int> s;

    while (curr) {
        s.push(curr->val);
        curr = curr->next;
    }
    while (head) {
        int t = s.top();
        s.pop();
        if (t != head->val) { return false; }
        head = head->next;
    }
    return true;
}
// Time complexity: O(n)
// Space complexity: O(n)

// 206. Reverse Linked List (Easy)
ListNode* reverseList(ListNode* head) {
    ListNode* curr = head;
    ListNode* prev = NULL;

    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head = prev;
    return head;
}
// Time complexity: O(n)
// Space complexity: O(1)

// 203. Remove Linked List Elements (Easy)
ListNode* removeElements(ListNode* head, int val) {
    if (head == NULL) { return head; }

    // check for all integers with value val at the front
    while (head && head->val == val) { head = head->next; }
    if (head == NULL) { return head; }

    ListNode* curr = head;
    ListNode* prev = NULL;
    while (curr) {
        if (curr->val == val) {
            prev->next = curr->next;
        } else {
            prev = curr;
        }
        curr = prev->next;
    }
    return head;
}
// Time complexity: O(n)
// Space complexity: O(1)

// 160. Intersection of Two Linked Lists (Easy)
// Two-pointers solution
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    ListNode* currA = headA;
    ListNode* currB = headB;
    int lenA = 0;
    int lenB = 0;
    while (currA) {
        lenA++;
        currA = currA->next;
    }
    while (currB) {
        lenB++;
        currB = currB->next;
    }
    int diff = abs(lenA - lenB);
    ListNode* bigger = headA;
    ListNode* smaller = headB;
    if (lenA < lenB) { bigger = headB; smaller = headA; }
    for (int i = 0; i < diff; i++) { bigger = bigger->next; }
    while (bigger && smaller) {
        if (bigger == smaller) { return bigger; }
        bigger = bigger->next;
        smaller = smaller->next;
    }
    return nullptr;
}
// More elegant two-pointers solution
// Reference: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    ListNode* currA = headA;
    ListNode* currB = headB;
    while (currA != currB) {
        currA = (currA != NULL) ? currA->next : headB;
        currB = (currB != NULL) ? currB->next : headA;
    }
    return currA;
}

// Time complexity: O(m + n)
// Space complexity: O(1)

// 141. Linked List Cycle (Easy)
bool hasCycle(ListNode *head) {
    if (head == nullptr || head->next == nullptr) { return false; }
    ListNode* curr = head;
    std::unordered_map<ListNode*, int> visited;
    while (curr->next) {
        if (visited[curr->next] == 1) return true;
        visited[curr] = 1;
        curr = curr->next;
    }
    return false;
}
// Time complexity: O(n)
// Space complexity: O(n)

// 92. Reverse Linked List II (Medium)
ListNode* reverseBetween(ListNode* head, int m, int n) {
    if (head == NULL || head->next == NULL || m == n) return head;
    ListNode* curr = head;
    ListNode *before=NULL, *after=NULL, *prev=NULL;
    ListNode *start, *end;

    int i = 1;
    while (curr) {
        // store the original next destination
        ListNode* next = curr->next;
        // update our pointers
        if (i == m - 1) { before = curr; }
        else if (i == n + 1) { after = curr; }
        else if (i == m) { start = curr; }
        else if (i == n) { end = curr; }
        // reverse the sublist
        if (i > m && i <= n) { curr->next = prev; }
        // updated regardless of list reversal
        prev = curr;
        curr = next;
        i++;
    }
    if (before != NULL) {
        before->next = end;
    } else {
        head = end;
    }
    start->next = after;
    return head;
}

// 83. Remove Duplicates from Sorted List (Easy)
ListNode* deleteDuplicates(ListNode* head) {
    if (head == NULL) { return head; }
    ListNode* prev = head;
    prev->next = head->next;

    ListNode* curr = head->next;
    while (curr) {
        if (prev->val == curr->val) {
            prev->next = curr->next;
        } else {
            prev = curr;
        }
        curr = curr->next;
    }
    return head;
}
// Time complexity: O(n)
// Space complexity: O(1)


// 61. Rotate List (Medium)
ListNode* rotateRight(ListNode* head, int k) {
    if (head == NULL || k == 0) { return head; }

    ListNode* left = NULL;
    ListNode* right = head;

    ListNode* curr = head;
    int size = 0;
    // figure out the size of the linked list
    while (curr != NULL) {
        size += 1;
        curr = curr->next;
    }
    k = k % size; // in case k is greater than size, take the remainder
    if (k == 0 || size == 1) { return head; }

    curr = head;
    int i = 0;
    // figure out where the end of our left and right sublist are
    ListNode* endOfRight = NULL;
    ListNode* endOfLeft = NULL;
    int splitPoint = size - k;

    while (curr != NULL) {
        if (i < splitPoint) { endOfRight = curr; }
        else if (i == splitPoint) { left = curr; }
        else { endOfLeft = curr; }
        curr = curr->next;
        i += 1;
    }

    endOfRight->next = NULL;
    // check whether the end of our left sublist is null or not
    if (endOfLeft) { endOfLeft->next = head; }
    else { left->next = head; }
    // reset the head
    head = left;
    return head;
}
// Time complexity: O(n)
// Space complexity: O(1)

// 21. Merge Two Sorted Lists (Easy)
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode* res = new ListNode(0);
    ListNode* curr = res;
    while (l1 || l2) {
        // if either pointers are null, we've reached the end
        // time for one list to join the other
        if (l1 == NULL) { curr->next = l2; break; }
        if (l2 == NULL) { curr->next = l1; break; }
        // if there's value in the first list that is less than or equal
        // to that in the second list, then tie curr's next to the node in the first list
        if (l1->val <= l2->val) {
            curr->next = l1;
            l1 = l1->next;
        } else {
            curr->next = l2;
            l2 = l2->next;
        }
        curr = curr->next;
    }
    return res->next;
}
// Time complexity: O(n)
// Space complexity: O(1)
