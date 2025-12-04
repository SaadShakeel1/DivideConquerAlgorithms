#include <iostream>
using namespace std;

float findMedian(int A[], int B[], int n){
	
    if(n==1)
        return(A[0]+B[0])/2.0;

    if(n==2)
        return (max(A[0], B[0])+ min(A[1], B[1]))/2.0;

    int m1, m2;

    if(n%2==0){
    	
        m1=(A[n/2]+A[n/2-1])/2;
        m2=(B[n/2]+B[n/2-1])/2;
        
    }
	else{
		
        m1=A[n/2];
        m2=B[n/2];
    }

    if(m1==m2)
        return m1;

    if(m1<m2){
    	
        if(n%2==0)
        
            return findMedian(A+n/2-1, B, n-n/2+1);
        else
            return findMedian(A+n/2, B, n-n/2);
    } else {
        if (n % 2 == 0)
            return findMedian(A, B + n/2 - 1, n - n/2 + 1);
        else
            return findMedian(A, B + n/2, n - n/2);
    }
}

int main(){
	
    int n;
    cout<<"Enter number of elements in each array: ";
    cin>>n;

    int A[100], B[100];
    cout<<"Enter sorted elements of first array:"<<endl;
    
    for(int i=0; i<n; i++)
        cin>>A[i];

    cout<<"Enter sorted elements of second array:"<<endl;
    
    for(int i=0; i<n; i++)
        cin>>B[i];

    float median=findMedian(A, B, n);
    cout<<"Median value of combined data: "<<median<<endl;

    return 0;
}
