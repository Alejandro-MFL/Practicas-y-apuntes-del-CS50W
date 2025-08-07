#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char* getDate(void);
int autoCommit(char* message);

int main(int argc, char* argv[])
{
    //Comprovacion de si se añade mensaje concreto del commit
    char* mensaje = NULL;
    char* fecha = NULL;   
    mensaje = malloc(100);
    if (argc > 1)
    {
        mensaje = malloc(strlen(argv[1]) + 1);
        if (mensaje == NULL)
        {
            fprintf(stderr, "Error reservando memoria.\n");
            return 1;
        }
        strcpy(mensaje, argv[1]);
    }
    else
    {
        // Si no, Obtener fecha y hora y usar la de mensaje//
        fecha = getDate();  
        mensaje = fecha;
    }  
    
    //Comandos de Git
    int check = autoCommit(mensaje);

    printf(" Commit automatico '%s' completado con exito.\n", mensaje);

    free(mensaje);
    free(fecha);
    return check;
}
char* getDate(void) 
{
    time_t t;
    struct tm* tm_info;
    char* fecha = malloc(100);

    time(&t);
    tm_info = localtime(&t);
    strftime(fecha, 100, "%d-%m-%Y_%H:%M:%S", tm_info);    
    return fecha;
}

int autoCommit(char* message)
{
    //Comandos de Git
    char addChanges[] = "git add .";
    char commitchanges[200];
    char pushChanges[] = "git push";
    snprintf(commitchanges, sizeof(commitchanges), "git commit -m \"Commit: %s\"", message);
    //Los ejecuta
    int checkAdd = system(addChanges);
    if (checkAdd != 0)
    {
        printf("Error al ejecutar 'git add'\n");
        return 1;
    }
    if (system("git diff --cached --quiet") != 0)
    {
        int checkCommit = system(commitchanges);
        if (checkCommit != 0)
        {
            printf("Error al ejecutar 'git commit'\n");
            return 2;
        }
        int checkPush = system(pushChanges);
        if (checkCommit != 0)
        {
            printf("Error al ejecutar 'git push'\n");
            return 3;
        }
        return 0;
    }
    printf("no habia cambios\n");
    return 4;
    
}