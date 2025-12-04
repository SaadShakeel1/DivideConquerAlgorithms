#include <iostream>
using namespace std;


int findPeak(int arr[], int n){
	
    int low=0;
    int high=n-1;

    while(low<high){
    	
        int mid=(low+high)/2;

        if(arr[mid]<arr[mid+1]){

            low=mid+1;
        }
		 else{
         
            high=mid;
        }
    }

    return low;
}

int main(){
	
    int n;

    cout<<"Enter size of array: ";
    cin>>n;

    int arr[100];

    cout<<"Enter "<<n<<" distinct numbers : "<<endl;
    
    for(int i=0; i<n; i++)
        cin>>arr[i];
        
    int peakIndex=findPeak(arr, n);

    cout<<"Peak found at index: "<<peakIndex<<endl;
    cout<<"Peak value: "<<arr[peakIndex]<<endl;

    
    return 0;
}
