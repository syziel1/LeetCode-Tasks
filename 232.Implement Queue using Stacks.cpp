#include <iostream>
#include <stack>
using namespace std;

class MyQueue {
private:
    stack<int> firstDown;
    stack<int> firstUp;
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        firstDown.push(x);
    }
    
    int pop() {
        if (firstUp.empty()) {
            while (!firstDown.empty()) {
                firstUp.push(firstDown.top());
                firstDown.pop();
            }
        }
        int front = firstUp.top();
        firstUp.pop();
        return front;
    }
    
    int peek() {
        if (firstUp.empty()) {
            while (!firstDown.empty()) {
                firstUp.push(firstDown.top());
                firstDown.pop();
            }
        }
        return firstUp.top();
    }
    
    bool empty() {
        return firstDown.empty() && firstUp.empty();
    }
};

int main() {
    MyQueue obj;
    obj.push(1);
    obj.push(2);
    int param_2 = obj.pop();
    int param_3 = obj.peek();
    bool param_4 = obj.empty();
    cout << param_2 << " " << param_3 << " " << param_4 << endl;
    return 0;
}
