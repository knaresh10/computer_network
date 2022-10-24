// IMPLEMENTATION OF DISTANCE VECTOR:
#include <stdio.h>
#include <conio.h>
#define INFINITY 10000
int main()
{
    int adj[50][50], length[50][50], path[50][50], set[50], i, j, n, s, t, c;
    //    clrscr();
    printf("Enter No Of Routers\n");
    scanf("%d", &n);
    printf("Enter Adjacency Matrix \n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &adj[i][j]);

    //**********Intialization Part*********
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            if (adj[i][j] == 0 && i != j)
            {
                length[i][j] = INFINITY;
                path[i][j] = 0;
            }
            else
            {
                length[i][j] = adj[i][j];
                path[i][j] = j;
            }
            if (i == j)
                path[i][j] = 131;
        }

    //**********Iteration Part*********
    t = 1;
    while (t)
    {
        c = 0;
        for (s = 0; s < n; s++)
            for (j = 0; j < n; j++)
            {
                if (adj[s][j])
                    for (i = 0; i < n; i++)
                    {
                        if (length[s][j] + length[j][i] < length[s][i])
                        {
                            length[s][i] = length[s][j] + length[j][i];
                            path[s][i] = j;
                        }
                    }
            }
        for (s = 0; s < n; s++)
            for (i = 0; i < n; i++)
                if (length[s][i] == INFINITY)
                    c++;
        if (c == 0)
            t = 0;
        else
            t = 1;
    }
    printf("\nRouting table\n\n");
    for (i = 65; i < (n + 65); i++)
        printf(" %c ", i);
    printf("\n----------------------------------------------------\n");
    for (i = 0; i < n; i++)
        printf(" l p");
    printf("\n---------- ----- ------ ------ ------ ------ -------\n");
    for (i = 0; i < n; i++)
    {
        printf("%c", i + 65);
        for (s = 0; s < n; s++)
        {
            printf(" %3d%3c |", length[s][i], path[s][i] + 65);
        }
        printf("\n");
    }
}
