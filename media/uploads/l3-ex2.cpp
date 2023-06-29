#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int n, i = 1;
	
	scanf("%d", &n);
			int soma= 0;
	while(i <= n){
		int soma= 0;
		int j = 1;
		
		while(j <= i){
			if(i % j == 0){
				soma += j;
			}
			j++;
		}
		if( (i * 2) == soma){
				printf("%d = perfeito\n", i);
			}
		i++;
	}
	
	return 0;
}
