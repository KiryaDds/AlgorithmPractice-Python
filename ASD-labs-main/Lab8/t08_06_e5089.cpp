// Завдання 8.6 by  Янголь Ярослав / Комп. мех / 2 курс
#include <iostream>
#include <string.h>

#define N 100

using namespace std;


// Selection sort
void Selection_sort(char arr[N][101], int n){
    char temp[101];
    for (int x = n - 1; x > 0; x--) {
        int max_ind = 0;
        for (int y = 1; y <= x; y++) {
            if (strcmp(arr[max_ind], arr[y]) < 0) {
                max_ind = y;
            }
        }
        strcpy(temp, arr[x]);
        strcpy(arr[x], arr[max_ind]);
        strcpy(arr[max_ind], temp);
    }
}


int main(){

    int n;
    cin >> n;
    char nums[N][101];
    for (int i = 0; i < n; i++){
        cin >> nums[i];
    }

    Selection_sort(nums, n);
    for (int i = 0; i < n; i++){
        cout << nums[i] << endl;
    }

    return 0;

}
