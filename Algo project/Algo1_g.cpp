#include <iostream>
using namespace std;

int prices[1000];

struct Info{
	
    int minVal, minIdx, maxVal, maxIdx, profit, buy, sell;

};

Info solve(int l, int r){
	
    if(l==r){
    	
        Info x;
        
        x.minVal=prices[l];
        x.maxVal=prices[l];
        x.minIdx=l;
        x.maxIdx=l;
        x.profit=-1000000;
        x.buy=l;
        x.sell=l;
        
        return x;
    }

    int mid=(l+r)/2;
    
    Info left=solve(l, mid);
    Info right=solve(mid+1, r);

    Info ans;

    if(left.minVal<=right.minVal){
    	
        ans.minVal=left.minVal;
        ans.minIdx=left.minIdx;
    }
	 else{
	 	
        ans.minVal=right.minVal;
        ans.minIdx=right.minIdx;
    }

    if(left.maxVal>=right.maxVal){
    	
        ans.maxVal=left.maxVal;
        ans.maxIdx=left.maxIdx;
    }
	else{
	 	
        ans.maxVal=right.maxVal;
        ans.maxIdx=right.maxIdx;
    }

    ans.profit=left.profit;
    ans.buy=left.buy;
    ans.sell=left.sell;


    if(right.profit>ans.profit){
    	
        ans.profit=right.profit;
        ans.buy=right.buy;
        ans.sell=right.sell;
    }


    int crossProfit=right.maxVal-left.minVal;
    
    if(crossProfit>ans.profit){
    	
        ans.profit=crossProfit;
        ans.buy=left.minIdx;
        ans.sell=right.maxIdx;
    }

    return ans;
}

int main(){
	
    int n;
    cout<<"Enter number of days: ";
    cin>>n;

    cout<<"Enter prices:"<<endl;
    
    for(int i=0; i<n; i++)
        cin>>prices[i];

    Info res=solve(0, n-1);

    if(res.profit<=0)
        cout<<"No profit possible"<<endl;
        
    else{
        cout<<"Buy on day "<<res.buy+1<<" Price: "<<prices[res.buy]<<endl;
        cout<<"Sell on day "<<res.sell+1<<" Price: "<<prices[res.sell]<<endl;
        cout<<"Profit: "<<res.profit<<endl;
    }

    return 0;
}
