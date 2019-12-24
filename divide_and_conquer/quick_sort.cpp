#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &A, int l, int r);
int quicksort(vector<int> &A, int l, int r);
int printVect(vector<int> A);

int main()
{
    vector<int> A{4, 1, 5, 2, 6, 9, 15, 11, 14, 20};

    cout << "Unsorted: ";
    printVect(A);
    quicksort(A, 0, A.size()-1);
    cout << "Sorted: ";
    printVect(A);
}

int quicksort(vector<int> &A, int l, int r)
{
    if(l < r)
    {
        int ipiv = partition(A, l, r);

        quicksort(A, l, ipiv-1);  // left
        quicksort(A, ipiv+1, r);  // right
    }
}

int partition(vector<int> &A, int l, int r)
{
    int piv = A[l];
    int i = l + 1;

    for(int j=i; j<=r; j++)
    {
        if(A[j] < piv)
        {
            swap(A[i], A[j]);
            i++;
        }
    }
    swap(A[l], A[i-1]);

    return i-1;
}

int printVect(vector<int> A)
{
    for(auto k=A.begin(); k!=A.end(); k++)
    {
        cout << *k << " ";
    }
    cout << endl;
}
