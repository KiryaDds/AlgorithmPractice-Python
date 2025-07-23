// Завдання 8.5 by  Янголь Ярослав / Комп. мех / 2 курс
#include <iostream>

using namespace std;


// BubbleSort
int BubbleSort(int arr[], int n) {
    int temp;
    int exchange_amount = 0;
    for (int x = 0; x < n - 1; x++) {
        for (int y = 0; y < n - x - 1; y++) {
            if (arr[y] > arr[y + 1]) {
                temp = arr[y];
                arr[y] = arr[y + 1];
                arr[y + 1] = temp;
                exchange_amount++;
            }
        }
    }
    return exchange_amount;
}


int main(){

    int n;
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }
    cout << BubbleSort(nums, n);

    return 0;

}
