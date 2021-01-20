// 1673. Find the Most Competitive Subsequence (Medium)
vector<int> mostCompetitive(vector<int>& nums, int k) {
    vector<int> ans;
    for (int i = 0, capacity = 0; i < nums.size(); i++) {
        while (capacity < ans.size() && nums[i] < ans.back()) {
            ans.pop_back();
        }
        if (ans.size() < k) { ans.push_back(nums[i]); }
        if (i >= nums.size() - k) { capacity++; }
    }
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(k) for k items in vector

// 1441. Build an Array With Stack Operations (Easy)
vector<string> buildArray(vector<int>& target, int n) {
    vector<string> ans;
    int j = 0;
    n = min(n, target[target.size()-1]);
    for (int i = 1; i <= n; i++) {
        ans.push_back("Push");
        if (i == target[j]) {
            j++;
        } else {
            ans.push_back("Pop");
        }
    }
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(N)

// 1047. Remove All Adjacent Duplicates In String (Easy)
string removeDuplicates(string S) {
    stack<char> s;
    for (char c : S) {
        if (s.empty()) { s.push(c); }
        else {
            char carrotTop = s.top();
            if (carrotTop == c) { s.pop(); }
            else { s.push(c); }
        }
    }
    string res = "";
    while (!s.empty()) {
        char c = s.top();
        s.pop();
        res += c;
    }
    reverse(res.begin(), res.end());
    return res;
}
// Time complexity: O(N)
// Space complexity: O(N)

// 739. Daily Temperatures (Medium)
vector<int> dailyTemperatures(vector<int>& T) {
    stack<int> s;
    vector<int> ans;
    int count;
    for (int i = T.size() - 1; i > -1; i--) {
        while (!s.empty() && T[i] >= T[s.top()]) { s.pop(); }
        count = (s.empty()) ? 0 : s.top() - i;
        s.push(i);
        ans.push_back(count);
    }
    reverse(ans.begin(), ans.end());
    return ans;
}
// Time complexity: O(N)
// Space complexity: O(N + W) where W is the size of the stack

// 856. Score of Parentheses (Medium)
int scoreOfParentheses(string S) {
    stack<int> s;
    s.push(0);
    
    for (int i = 0; i < S.length(); i++) {
        char c = S[i];
        if (c == '(') { s.push(0); }
        else {
            int oneBefore = s.top();
            s.pop();
            int twoBefore = s.top();
            s.pop();
            s.push(twoBefore + max(2*oneBefore, 1));
        }
    }
    
    return s.top();
}
// Time complexity: O(N)
// Space complexity: O(W) where W is the size of the stack

// 682. Baseball Game (Easy)
int calPoints(vector<string>& ops) {
    stack<int> s;
    int sum = 0;
    for (auto call : ops) {
        if (call == "C" && !s.empty()) {
            int top = s.top();
            s.pop();
            sum -= top;
        } else if (call == "D") {
            int timesTwo = s.top()*2;
            s.push(timesTwo);
            sum += timesTwo;
        } else if (call == "+") {
            int one = s.top();
            s.pop();
            int two = s.top();
            int lastTwoSum = one + two;
            s.push(one);
            s.push(lastTwoSum);
            sum += lastTwoSum;
        } else {
            int elem = stoi(call);
            s.push(elem);
            sum += elem;
        }
    }
    return sum;
}
// Time complexity: O(N)
// Space complexity: O(N)

// 20. Valid Parentheses (Easy)
bool isValid(string s) {
    stack<char> jack;
    for (char c : s) {
        if (jack.empty()) {
            jack.push(c);
        } else {
            if ((jack.top() == '(' && c == ')') 
                || (jack.top() == '{' && c == '}')
                || (jack.top() == '[' && c == ']')) {
                jack.pop();
            } else {
                jack.push(c);
            }
        }
    }
    return jack.empty();
}