#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int i=1;
	
	while(i <= 10){
		int j = 1;
		printf("%d, ",i);
		
		while(j <= 10){
			printf("%d ", j);
			j++;
		}
		i++;
		printf("\n");
	}
	
	return 0;
}
