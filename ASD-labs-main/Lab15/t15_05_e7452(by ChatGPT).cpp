// Використайте цей файл, а не мій, пліііз


#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node() : next(nullptr) {};
    Node(int data, Node* next = nullptr) : data(data), next(next) {};
};

class List {
public:
    Node* head;
    Node* tail;

    List() : head(nullptr), tail(nullptr) {};
    
    void addToTail(int val) {
        if (head == nullptr) {
            head = new Node(val);
            tail = head;
        } else {
            tail->next = new Node(val);
            tail = tail->next;
        }
    }
    
    void Print(void) {
        Node* current = head;
        while (current != nullptr) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }
    
    void PrintReverse(void) {
        PrintReverseHelper(head);
        cout << endl;
    }
    
private:
    void PrintReverseHelper(Node* node) {
        if (node == nullptr) {
            return;
        }
        PrintReverseHelper(node->next);
        cout << node->data << " ";
    }
};

int main() {
    int n;
    cin >> n;
    List list;
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        list.addToTail(val);
    }
    list.Print();
    list.PrintReverse();
    return 0;
}