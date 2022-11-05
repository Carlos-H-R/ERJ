#include <stdio.h>

int main()
{
	int i, v[3];
	
	for(i=0;i<3;i++)
	{
		printf("v%d",i);
		scanf("%d",&v[i]);
	}
	printf("v1 = %d, v2 = %d, v3 = %d",v[3],v[4],v[5]);
}
