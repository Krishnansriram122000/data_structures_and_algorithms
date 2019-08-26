#include <iostream>
#include<string.h>
using namespace std;
struct node{
	float time,weight;
	float cost;
	string jobname;
	node(){};	
};
int main()
{	
	int y;
	cout<<"ENTER THE NUMBER OF JOBS:";
	cin>>y;
	node *x=new node[y];
	cout<<"JOB DESCRIPTION\tTIME ESTIMATED\tRATE THIS WORK\n";
	for(int i=0;i<y;i++)
	{
		cin>>x[i].jobname;
		cin>>x[i].time>>x[i].weight;
		x[i].cost=x[i].time/x[i].weight;
	
	}
	
	for(int i=y;i>0;i--)
		for(int j=0;j<i-1;j++)
			if(x[j].cost>x[j+1].cost)
			{
				node t;
				t=x[j];
				x[j]=x[j+1];
				x[j+1]=t;
			}
	cout<<"JOBS SCHEDULED BY SMITH'S RULE::\n";
	for(int i=0;i<y;i++)
	{
		cout<<x[i].jobname<<"\t"<<x[i].cost<<"\n";
	}
	return 0;
}