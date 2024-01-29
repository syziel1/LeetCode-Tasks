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