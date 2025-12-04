#include <iostream>
using namespace std;

void minMax(int arr[], int start, int end, int &mini, int &max){

    if(start==end){
        mini=arr[start];
        max=arr[start];
        return;
    }

    if(end==start+1){
        if(arr[start]<arr[end]){
            mini=arr[start];
            max=arr[end];
        } 
		else{
            mini=arr[end];
            max=arr[start];
        }
        return;
    }
    int mid=(start+end)/2;
    int leftMin, leftMax, rightMin, rightMax;

    minMax(arr, start, mid, leftMin, leftMax);
    minMax(arr, mid+1, end, rightMin, rightMax);

    if(leftMin<rightMin)
        mini=leftMin;
    else
        mini=rightMin;

    if(leftMax>rightMax)
        max=leftMax;
    else
        max=rightMax;
}

int main(){
	
    int n;
    cin>>n;

    if(n<10){
        cout<<"Size must be at least 10"<<endl;
        return 0;
    }

    int arr[n];
    cout<<"Enter "<<n<<" elements: ";
    
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    int minValue, maxValue;
    minMax(arr, 0, n-1, minValue, maxValue);
    
	cout<<endl;
    cout<<"Smallest element: "<<minValue<<endl;
    cout<<"Largest element: "<<maxValue<<endl;

    cout<<"\n--- Answers ---"<<endl;
    cout<<"(a) Pseudocode:"<<endl;
    cout<<"Algorithm MinMax(A, low, high)"<<endl;
    cout<<"  if low == high then"<<endl;
    cout<<"    min <- A[low], max <- A[low]"<<endl;
    cout<<"  else if high == low + 1 then"<<endl;
    cout<<"    if A[low] < A[high] then"<<endl;
    cout<<"      min <- A[low], max <- A[high]"<<endl;
    cout<<"    else"<<endl;
    cout<<"      min <- A[high], max <- A[low]"<<endl;
    cout<<"  else"<<endl;
    cout<<"    mid <- (low + high)/2"<<endl;
    cout<<"    (min1, max1) <- MinMax(A, low, mid)"<<endl;
    cout<<"    (min2, max2) <- MinMax(A, mid+1, high)"<<endl;
    cout<<"    min <- smaller(min1, min2)"<<endl;
    cout<<"    max <- larger(max1, max2)"<<endl;
    cout<<"  return (min, max)"<<endl;

    cout<<"\n(b) Recurrence Relation:"<<endl;
    cout<<"T(n) = 2T(n/2) + 2  for n > 2"<<endl;
    cout<<"T(2) = 1,  T(1) = 0"<<endl;
    cout<<"Solution: T(n) = 3n/2 - 2"<<endl;

    cout<<"\n(c) Comparison with brute-force:"<<endl;
    cout<<"Brute-force makes 2(n-1) comparisons."<<endl;
    cout<<"Divide-and-conquer makes about (3n/2 - 2) comparisons."<<endl;
    cout<<"Hence, divide-and-conquer is more efficient."<<endl;

    return 0;
}
