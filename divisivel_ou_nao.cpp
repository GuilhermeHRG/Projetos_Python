#include<stdio.h>
#include<locale.h>

int main ()
{
    printf("BEM VINDO!!");
    printf("\n-------------------------------------------");
    setlocale(LC_ALL,"");
    int num, div;
    printf("\nDigite um número: ");
    scanf("%d",&num);
    printf("\nDigite o divisor: ");
    scanf("%d",&div);
    if(num%div==0)
{
    printf("\n-------------------------------------------");
printf("\nO número %d é divisível por %d. ",num,div);
}

else
{
    printf("\n-------------------------------------------");
printf("\nO número %d não é divisível por %d. ",num,div);
}

printf("\n-------------------------------------------");
}
