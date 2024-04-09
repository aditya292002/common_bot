class Solution {
public:
    string minRemoveToMakeValid(string s) {
        // removing right extra
        string ans = "";
        int left = 0;
        for(auto ch: s) {
            if(ch == '(') {
                left += 1;
                ans += "(";
            }
            else if(ch == ')') {
                if(left > 0) {
                    ans += ")";
                    left -= 1;
                }
            }
            else {
                ans += ch; 
            }
        }
        // removing left extra brackets
        s = ans;
        ans = "";
        int N = s.size();
        int right = 0;
        for(int i = N - 1; i >= 0; i++) {
            if(s[i] == ')') {
                right += 1;
                ans += ')';
            }
            else if(s[i] == '(') {
                if(right > 0) {
                    ans += "(";
                    right -= 1;
                }
            }
            else {
                ans += s[i];
            }
        }
        reverse(ans.being(), ans.end());
        return ans;
    }
};

// ((() -> ((() -> ()
// ())) -> ()