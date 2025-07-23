// Завдання 8.7 by  Янголь Ярослав / Комп. мех / 2 курс
#include <iostream>

using namespace std;


// BubbleSort
void InsertionSort(int arr[], int n) {

    int temp, mem_ind;
    for (int x = 1; x < n; x++) {
        int flag = 0;
        temp = arr[x];
        mem_ind = x;
        while (mem_ind > 0) {
            if (arr[mem_ind - 1] > temp) {
                arr[mem_ind] = arr[mem_ind - 1];
                flag = 1;
            }
            else {
                break;
            }
            mem_ind--;
        }
        arr[mem_ind] = temp;
        if (flag == 1){
            for (int i = 0; i < n; i++){
                cout << arr[i] << " ";
            }
            cout << endl;
        }
    }

}


int main(){

    int n;
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }
    InsertionSort(nums, n);

    return 0;

}
