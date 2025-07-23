// Завдання 15.5 by  Янголь Ярослав / Комп. мех / 2 курс


#include <iostream>

using namespace std;

class Node
{

public:

    int data;
    Node *next;
    Node() : next(NULL) {};
    Node(int data, Node *next = NULL) : data(data), next(next) {};

};

class List
{
/* Двозв'язний список */
public:

    Node *head, *tail;
    List() : head(NULL), tail(NULL) {};
    
    void addToTail(int val)
    {
        if (head == NULL)
        {
            head = new Node(val);
            tail = head;
        }
        else
        {
            tail->next = new Node(val);
            tail = tail->next;
        }
    }
    
    void Print(void)
    {
        Node* current = head;
        while (current != NULL)
        {
            cout << current->data << " ";
            current = current->next;
        }
    }
    
    void PrintReverse(void)
    {
        ReversePrintIterator(head);
    }
    
private:

    void ReversePrintIterator(Node* current)
    {
        if (current == NULL)
        {
            return;
        }
        ReversePrintIterator(current->next);
        cout << current->data << " ";
    }
    
};


int main() {

    int n;
    cin >> n;
    List list;
    for (int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        list.addToTail(val);
    }

    list.Print();
    cout << endl;
    list.PrintReverse();
    cout << endl;

    return 0;

}
