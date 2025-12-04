#include <iostream>
using namespace std;

int countPairs(int arr[], int left, int mid, int right){
	
    int count=0;
    int j=mid+1;

    for(int i=left; i<=mid; i++){
    	
        while(j<=right && arr[i]>2*arr[j]){
            j++;
        }
        count+=(j-mid-1);
    }
    return count;
}

void mergeParts(int arr[], int left, int mid, int right){
	
    int n1=mid-left+1;
    int n2=right-mid;

    int L[1000], R[1000];
    
    for(int i=0; i<n1; i++)
        L[i]=arr[left+i];
        
    for(int j=0; j<n2; j++)
        R[j]=arr[mid+1+j];

    int i=0, j=0, k=left;
    
    while(i<n1 && j<n2){
    	
        if(L[i]<=R[j])
        
            arr[k++]=L[i++];
        else
            arr[k++]=R[j++];
    }

    while(i<n1)
        arr[k++]=L[i++];
    while(j<n2)
        arr[k++]=R[j++];
}

int countSignificantInversions(int arr[], int left, int right){
	
    if(left>=right)
        return 0;

    int mid=(left+right)/2;
    int count=0;

    count+=countSignificantInversions(arr, left, mid);
    count+=countSignificantInversions(arr, mid+1, right);
    count+=countPairs(arr, left, mid, right);

    mergeParts(arr, left, mid, right);
    return count;
}

int main(){
	
    int arr[]={5, 3, 8, 1, 9, 2};
    int n=6;

    cout<<"Original Array:"<<endl;
    
    for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
        
    cout<<endl;

    int result=countSignificantInversions(arr, 0, n-1);
    cout<<"Number of Significant Inversions: "<<result<<endl;

    return 0;
}
