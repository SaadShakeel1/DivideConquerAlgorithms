#include <iostream>
#include <cmath>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;

int divideAndConquer(int arr[], int low, int high, int &x, int &y){
	
    if(high-low==1){ 
        x=arr[low];
        y=arr[high];
        return arr[high]-arr[low];
    }
        
    if(low==high)
        return INT_MAX;

    int mid=(low+high)/2;
    int lx, ly, rx, ry, cx, cy;

    int leftMin=divideAndConquer(arr, low, mid, lx, ly);
    int rightMin=divideAndConquer(arr, mid+1, high, rx, ry);
    int crossMin=arr[mid+1]-arr[mid];
    cx=arr[mid];
    cy=arr[mid+1];

    int minVal=leftMin;
    x=lx; y=ly;

    if(rightMin<minVal){ 
        minVal=rightMin; 
        x=rx; 
        y=ry; 
    }
    if(crossMin<minVal){ 
        minVal=crossMin; 
        x=cx; 
        y=cy; 
    }

    return minVal;
}

int closestPair(int arr[], int n, int &x, int &y){
	
    sort(arr, arr+n);
    return divideAndConquer(arr, 0, n-1, x, y);
}

int main(){
	
    int arr[]={4, 2, 9, 15, 7, 11};
    
    int n=sizeof(arr) / sizeof(arr[0]);
    
    cout<<"Orignal Array: "<<endl;
    for(int i=0; i<n; i++)
		cout<<arr[i]<<" ";

    int x, y;
    int minDist=closestPair(arr, n, x, y);
    cout<<endl;

    cout<<"Minimum distance between closest pair: "<<minDist<<endl;
    cout<<"Closest Pair Elements: "<<x<<" and "<<y<<endl;
    
    
    
    cout<<endl<<endl<<"Part 2"<<endl;
    
    
    cout<<"This algorithm applies the divide-and-conquer approach."<<endl;
    cout<<"It has a time complexity of O(n log n) due to sorting and recursion."<<endl;
    cout<<"However after sorting, we can find the closest pair in O(n)"<<endl;
    cout<<"by checking consecutive elements directly which is faster."<<endl;
    cout<<"Hence while the divide-and-conquer version is correct,"<<endl;
    cout<<"it is not the most efficient for the 1D closest-pair problem."<<endl;

    

    return 0;
}
