#include <iostream>
using namespace std;

int n; 
int cards[100];

bool isEquivalent(int i, int j){
	
    return cards[i]==cards[j];
}

int findCandidate(int left, int right){
	
    if(left==right)
        return left;

    int mid=(left+right)/2;

    int leftCand=findCandidate(left, mid);
    int rightCand=findCandidate(mid+1, right);

    if(leftCand==-1) 
		return rightCand;
    if(rightCand==-1) 
		return leftCand;

    int countLeft=0, countRight=0;


    for (int i = left; i <= right; i++) {
        if (isEquivalent(i, leftCand))
            countLeft++;
    }

    for(int i=left; i<=right; i++){
    	
        if(isEquivalent(i, rightCand))
            countRight++;
    }

    if(countLeft>(right-left+1)/2)
        return leftCand;
    else if(countRight>(right-left+1)/2)
        return rightCand;
    else
        return -1;
}

bool hasMajority(int candidate){
	
    int count=0;
    for(int i=0; i<n; i++){
    	
        if(isEquivalent(i, candidate))
            count++;
    }
    return (count>n/2);
}

int main(){
	
    cout<<"Enter number of cards: ";
    cin>>n;

    cout<<"Enter account number of each card:"<<endl;
    
    for(int i=0; i<n; i++)
    
        cin>>cards[i];

    int candidate=findCandidate(0, n - 1);

    if(candidate==-1){
    	
        cout<<"No majority account found."<<endl;
        return 0;
    }

    if(hasMajority(candidate))
        cout<<"Yes, more than n/2 cards belong to the same account."<<endl;
        
    else
        cout<<"No, there is no such majority account."<<endl;

    return 0;
}
