// Використайте цей файл, а не мій, пліііз


#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node() : next(NULL) {};
    Node(int data, Node* next = NULL) : data(data), next(next) {};
};

class List {
public:
    Node* head;
    List() : head(NULL) {};
    void AddToTail(int val) {
        Node* node = new Node(val);
        if (head == NULL) {
            head = node;
        } else {
            Node* current = head;
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = node;
        }
    }
    void RotateRight(int k) {
        if (head == NULL || k == 0) {
            return;
        }
        int size = 1;
        Node* current = head;
        while (current->next != NULL) {
            size++;
            current = current->next;
        }
        k %= size;
        if (k == 0) {
            return;
        }
        current->next = head;
        int steps = size - k;
        while (steps--) {
            current = current->next;
        }
        head = current->next;
        current->next = NULL;
    }
    void Print() {
        Node* current = head;
        while (current != NULL) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }
};

int main() {
    int n;
    cin >> n;
    List list;
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        list.AddToTail(val);
    }
    string str;
    while (cin >> str) {
        if (str.empty()) {
            break;
        }
        int k;
        k = stoi(str);
        list.RotateRight(k);
        list.Print();
    }
    return 0;
}