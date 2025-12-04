#include <iostream>
using namespace std;


void swapValues(int &a, int &b){
	
    int temp=a;
    a=b;
    b=temp;
}

int partitionArray(int arr[], int low, int high){
	
    int pivot=arr[high];
    int i=low-1;

    for(int j=low; j<high; j++){
    	
        if(arr[j]<pivot){
		 
            i++;
            swapValues(arr[i], arr[j]);
        }
    }
    swapValues(arr[i+1], arr[high]);
    return (i+1);
}

void quickSort(int arr[], int low, int high){
	
    if(low<high){
    	
        int pivotIndex=partitionArray(arr, low, high);
        quickSort(arr, low, pivotIndex-1);
        quickSort(arr, pivotIndex+1, high);
    }
}

int main(){

    int n;
    cout<<"Enter number of elements at least 10: ";
    cin>>n;

    int arr[n];
    cout<<"Enter "<<n<<" elements:"<<endl;
    
    for(int i=0; i<n; i++)
        cin>>arr[i];

    cout<<"Original Array: ";
    for (int i = 0; i < n; i++)
        cout<<arr[i]<<" ";
        

    quickSort(arr, 0, n - 1);
    
    cout<<endl;
    
    cout<<"Sorted Array: ";
    for (int i = 0; i < n; i++)
        cout<<arr[i]<<" ";

	cout<<endl<<endl;
	
    cout<<"Time Complexity Analysis"<<endl<<endl;
    
    cout<<"Best Case: O(n log n)\nOccurs when pivot divides array into two equal halves.\nExample: Random or balanced input."<<endl;

    cout<<"Worst Case: O(n^2)\nOccurs when pivot always smallest or largest element.\nExample: Already sorted or reverse sorted input.";

    return 0;
}
