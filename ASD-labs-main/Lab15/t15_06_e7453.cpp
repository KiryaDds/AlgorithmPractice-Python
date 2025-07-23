// Завдання 15.6 by  Янголь Ярослав / Комп. мех / 2 курс


#include <iostream>

using namespace std;

class Node
{

public:

    int data;
    Node *next;
    Node() : next(NULL) {};
    Node(int data, Node* next = NULL) : data(data), next(next) {};

};

class List
{
/* Кільцевий список */
public:

    Node *head;
    List() : head(NULL) {};

    void AddToTail(int val)
    {

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

    int size()
    {
        
        int size = 1;
        Node* current = head;
        while (current->next != NULL) {
            size++;
            current = current->next;
        }
        return size;

    }

    void RotateRight(int k)
    {

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
        int i = size - k;
        while (i--) {
            current = current->next;
        }
        head = current->next;
        current->next = NULL;

    }

    void Print()
    {

        Node* current = head;
        while (current != NULL) {
            cout << current->data << " ";
            current = current->next;
        }

    }

};

int main() {

    int n;
    cin >> n;
    List list;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        list.AddToTail(x);
    }

    string str_k;
    while (cin >> str_k) {
        if (str_k.empty()) {
            break;
        }
        int k;
        k = stoi(str_k);
        list.RotateRight(k);
        list.Print();
        cout << endl;
    }

    return 0;

}
