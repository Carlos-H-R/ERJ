#include <stdio.h>

int main()
{
	int months[12];
	int d,m,y,days,i;
	
	printf("Para saber qual o dia do ano, digite a data\n");
	printf("Dia: ");
	scanf("%d",&d);
	printf("Mes: ");
	scanf("%d",&m);
	printf("Ano: ");
	scanf("%d",&y);
	days = 0;
	
	if ((y%4 == 0) || ((y%100 == 0) && (y%400 == 0)))
	{
		int months[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
	}
	else
	{
		int months[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
	}
	
	for (i=0;i<m-1;i++)
	{
		days = days + months[i];
	}
	printf("%d",days);
	
	return 0;
}
