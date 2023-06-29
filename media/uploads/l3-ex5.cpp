#include <stdio.h>

int main() {
    float altura, max, min, somaMulheres = 0;
    char sexo;
    int pessoas = 0, m = 0, h = 0;

    while (pessoas < 20) {
        printf("Altura da pessoa %d: ", pessoas + 1);
        scanf("%f", &altura);
        printf("Sexo da pessoa %d (M/F): ", pessoas + 1);
        scanf(" %c", &sexo);

        if (pessoas == 0) {
            max = altura;
            min = altura;
        } else {
            if (altura > max) {
                max = altura;
            }
            if (altura < min) {
                min = altura;
            }
        }

        if (sexo == 'F') {
            somaMulheres += altura;
            m++;

        }
		else if (sexo == 'M') {
            h++;
        }

        pessoas++;
    }

    float mediaAlturaMulheres = somaMulheres / m;
    float percentualDiferenca = ((float)h / m) * 100;

    printf("\nMaior altura do grupo: %.2f\n", max);
    printf("Menor altura do grupo: %.2f\n", min);
    printf("Média de altura das mulheres: %.2f\n", mediaAlturaMulheres);
    printf("Número de homens: %d\n", h);
    printf("Diferença percentual entre homens e mulheres: %.2f%%\n", percentualDiferenca);

    return 0;
}