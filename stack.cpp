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