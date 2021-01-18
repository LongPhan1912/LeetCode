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


// 61. Linked List (Medium)
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
