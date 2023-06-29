#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int n, i = 1;
	int f;
	scanf("%d", &n);
	
	while(i <= n){
		int soma = 1;
		
		scanf("%d", &f);
		int j = 1;
		
		while (j <= f){
			soma *= j;
			j++;
		}
		printf("valor: %d | fatorial: %d\n",f,soma);
		i++;
	}
	
	return 0;
}
