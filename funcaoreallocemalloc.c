#include <stdlib.h>
#include <stdio.h>

void main ()
{

    int *ptr_a;

    ptr_a = malloc(sizeof(int));
    ptr_a = (int*)realloc(ptr_a, sizeof(int));

    if (ptr_a == NULL)
    {

    printf("Memória insuficiênte.\n");
    exit();

    }

    printf("endereço de ptr_a.\n");
    *ptr_a = 22;
    printf("Conteúdo do ptr_a.\n");

    free(ptr_a);

return 0;    
}
