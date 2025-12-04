#include <iostream>
using namespace std;

long long power(long long a, int n, int &c){
	
    if(n==0)
        return 1;
        
    if(n==1)
        return a;

    long long half=power(a, n/2, c);

    if(n%2==0){
		c+=1;
        return half*half;
	}
    else{
		c+=2;	
        return a*half*half;
	}
}

int main(){
	
    long long a;
    int n, c=0;

    cout<<"Enter base (a): ";
    cin>>a;
    
    cout<<"Enter exponent (n): ";
    cin>>n;

    cout<<a<<"^"<<n<<" = "<<power(a, n, c)<<endl;

    cout<<"Total multiplications performed: "<<c<<endl;

    cout<<"\n--- Answers ---"<<endl;

    cout<<"(a) Pseudocode:"<<endl;
    cout<<"Algorithm Power(a, n)"<<endl;
    cout<<"  if n == 0 then return 1"<<endl;
    cout<<"  if n == 1 then return a"<<endl;
    cout<<"  half <- Power(a, floor(n/2))"<<endl;
    cout<<"  if n is even then"<<endl;
    cout<<"     return half * half"<<endl;
    cout<<"  else"<<endl;
    cout<<"     return a * half * half"<<endl;

    cout<<"\n(b) Recurrence Relation:"<<endl;
    cout<<"Let M(n) = number of multiplications for exponent n"<<endl;
    cout<<"M(1) = 0"<<endl;
    cout<<"M(n) = M(floor(n/2)) + 1 if n is even"<<endl;
    cout<<"M(n) = M(floor(n/2)) + 2 if n is odd"<<endl;
    cout<<"For simplicity (n = 2^k): M(n) = M(n/2) + 1"<<endl;
    cout<<"=> M(n) = log2(n)"<<endl;

    cout<<"\n(c) Comparison with brute-force algorithm:"<<endl;
    cout<<"Brute-force method performs (n - 1) multiplications."<<endl;
    cout<<"Divide-and-conquer (fast exponentiation) performs about log2(n) multiplications."<<endl;
    cout<<"Hence, divide-and-conquer is exponentially faster than brute-force for large n."<<endl;

    return 0;
}
