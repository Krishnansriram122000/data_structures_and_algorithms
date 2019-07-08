#include<iostream>
using namespace std;

template<typename q>
class bubble
{ 	q arr[25];
	int n;
   	public:
   	void read();
   	void print();
  	void sort();
	void insertion();
	void selection();
};

template<typename q>
void bubble<q>::read(){
	
 	cout<<"Enter the no of terms:";
	cin>>n;	
	for(int i=0;i<n;cin>>arr[i],i++);
	
}

template<typename q>	
void bubble<q>::print(){
	for(int i=0;i<n;cout<<arr[i]<<"\t",i++);
}

template<typename q>
void bubble<q>::sort(){
	for(int i=n-1;i>=0;i--)
		for(int j=0;j<i;j++)
			if(arr[j]>arr[j+1]){
				q t;
				t=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=t;
				this->print();cout<<"\n";}
}

template<typename q>
void bubble<q>::insertion(){
	for(int i=1;i<n;i++){
		q temp;
		temp=arr[i];
		cout<<temp<<'\n';
		for(int j=i-1;temp<arr[j] && j>=0;j--){
			q t;
			t=arr[j];
			arr[j]=arr[j+1];
			arr[j+1]=t;
			}
		}
}

template<typename q>
void bubble<q>::selection(){
	for(int i=0;i<n;i++){
		int index;
		q min;
		min=arr[i];
		for(int j=i;j<n;j++)
			if(arr[j]<min){min=arr[j];index=j;}
		cout<<min<<'\t'<<i<<'\t'<<index<<'\n';
		if(index!=i){
		q t;
		t=arr[i];
		arr[i]=arr[index];
		arr[index]=t;}
		this->print();
		cout<<"\n";
		}
	}	
			
main()
{  	bubble <float>op;
	op.read();
	op.sort();
	op.insertion();
	op.selection();
	op.print();
}
		
				
