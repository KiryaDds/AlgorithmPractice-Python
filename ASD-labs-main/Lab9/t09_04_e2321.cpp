// Завдання 8.7 by  Янголь Ярослав / Комп. мех / 2 курс
#include <iostream>

using namespace std;


// Quick Sort
int QuickSort(int arr[], int a, int b) {

    if (a >= b) return 0;

    int pivot = arr[a + (b - a) / 2];
    int l = a;
    int r = b;

    while (1){
        while (arr[l] <= pivot){
            l++;
        }
        while (arr[r] >= pivot){
            r--;
        }
        if (l >= r) break;
        int temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;
        l++; r--;
    }

    QuickSort(arr, a, r);
    QuickSort(arr, r + 1, b);
    return 0;
}


int main(){

    int n;
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }
    QuickSort(nums, 0, n - 1);
    for (int i = 0; i < n; i++){
        cout << nums[i] << " ";
    }
    cout << endl;

    return 0;

}
