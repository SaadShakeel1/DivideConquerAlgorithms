#include <iostream>
using namespace std;

int mergeAndCount(int arr[], int left, int mid, int right){
	
    int n1=mid-left+1;
    int n2=right-mid;

    int leftArr[n1], rightArr[n2];
    
    for(int i=0; i<n1; i++)
        leftArr[i]=arr[left+i];
        
    for(int j=0; j<n2; j++)
        rightArr[j]=arr[mid+1+j];

    int i=0, j=0, k=left;
    int count=0;
    
    while(i<n1 && j<n2){
    	
        if(leftArr[i]<=rightArr[j]){
        	
            arr[k++]=leftArr[i++];
        } 
		else{
            cout<<"("<<leftArr[i]<<", "<<rightArr[j]<<")	";
            count=count+(n1-i); 
            arr[k++]=rightArr[j++];
        }
    }

    while(i<n1)
        arr[k++]=leftArr[i++];
    while(j<n2)
        arr[k++]=rightArr[j++];

    return count;
}

int countInversions(int arr[], int left, int right){
    if(left>=right)
        return 0;

    int mid=(left+right)/2;
    int inversions=0;

    inversions+=countInversions(arr, left, mid);
    inversions+=countInversions(arr, mid+1, right);
    inversions+=mergeAndCount(arr, left, mid, right);

    return inversions;
}

int main(){
	
    int n;
    cout<<"Enter size of array at least 10: ";
    cin>>n;

    int arr[n];
    cout<<"Enter "<<n<<" elements:"<<endl;
    for(int i=0; i< n; i++)
        cin>>arr[i];
	
	cout<<endl;
    cout<<"Original Array: "<<endl;
    
    for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
        
	cout<<endl;
	cout<<"Inversion Pairs"<<endl;
    int totalInversions=countInversions(arr, 0, n-1);

	cout<<endl;
    cout<<"Total number of inversions: "<<totalInversions<<endl;

    return 0;
}
