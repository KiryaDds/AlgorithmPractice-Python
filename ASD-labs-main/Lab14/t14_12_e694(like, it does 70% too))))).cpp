// Завдання 14.12 by  Янголь Ярослав / Комп. мех / 2 курс

#include <iostream>
#include <vector>

using namespace std;

class Queue {
private:
    vector<long int> items;

public:
    bool empty() {
        return items.empty();
    }
    
    void push(long int item) {
        items.push_back(item);
    }

    long int pop() {
        if (!empty()) {
            long int item = items[0];
            items.erase(items.begin());
            return item;
        }
        return -1;
    }
        
    long int min_item() {
        if (!empty()) {
            long int min_item = items[0];
            for (int i = 1; i < items.size(); i++) {
                if (items[i] < min_item) {
                    min_item = items[i];
                }
            }
            return min_item;
        }
        return -1;
    }
};

int main() {
    long int n, a, b, c, x_i;
    cin >> n >> a >> b >> c >> x_i;
    long int sum_min = 0;
    Queue qe;

    for (long int i = 0; i < n; i++) {
        x_i = ((a * x_i * x_i + b * x_i + c) / 100) % 1000000;
        if (x_i % 5 < 2) {
            qe.pop();
            if (!qe.empty()) {
                sum_min += qe.min_item();
            }
        }
        else {
            qe.push(x_i);
            sum_min += qe.min_item();
        }
    }
    cout << sum_min << endl;
    return 0;
}