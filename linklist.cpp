#include<iostream>
using namespace std;
template<class t>
class node{
public:
	t data;
	node<t>* next; 
	node(t x){
		data=x;
		next=NULL;
	}
};
template<class t>
class list{
	node<t>* head;
	public:
		list(){
			head=NULL;
		}
		void insbeg(t x){
			node<t>* n=new node<t>(x);
			n->next=head;
			head=n;
		}
		t findn(int);
		void dis();
};
template<class t>
void list<t>::dis(){
	for(node<t>* h=head;h!=NULL;cout<<h->data<<'\t',h=h->next);
}
template<class t>
t list<t>::findn(int x){
	node<t>* m=head;
	for(int i=0;i<x;m=m->next,i++);
	return m->data;
}
main(){
	typedef list<int> a;
	list<int> l;
	for(int i=1;i<10;l.insbeg(i*2),i*=2);
	l.dis();
	cout<<"\nThe element at 1 is "<<l.findn(1)<<"\n";
	list<a> y;
	y.insbeg(l);
	cout<<y.findn(0).findn(1);

}