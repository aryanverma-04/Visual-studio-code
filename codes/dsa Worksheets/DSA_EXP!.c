#include <stdio.h>
#include <stdlib.h>

int element, i, loc, size, n, j, choice;
int a[100];

void insertion(int a[], int x)
{

    printf("array before Insertion: ");
    for (i = 0; i < size; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\nEnter an element to insert\n");
    scanf("%d", &element);
    printf("Enter a position to insert an element %d\n", element);
    scanf("%d", &loc);
    loc--;
    for (i = size - 1; i >= loc; i--)
    {
        a[i + 1] = a[i];
    }
    a[loc] = element;
    printf("List after Insertion: ");
    for (i = 0; i < size + 1; i++)
    {
        printf("%d ", a[i]);
    }
    size++;
}

void deletion(int a[], int x)
{

    printf("array before deletion\n");
    for (i = 0; i < size; i++)
    {
        printf("%d ", a[i]);
    }
    printf("\nEnter an element to delete\n");
    scanf("%d", &n);
    for (i = 0; i < size; i++)
    {
        if (a[i] == n)
        {
            for (j = i; j < (size - 1); j++)
            {
                a[j] = a[j + 1];
            }
            break;
        }
    }
    if (i != 5)
    {

        printf("List after deletion\n");
        for (i = 0; i < (size - 1); i++)
        {
            printf("%d ", a[i]);
        }
        size--;
    }
    else
    {
        printf("Element is not present in this array");
    }
}

void searching(int a[], int n)
{

    printf("Enter the number you want to search  :->");
    scanf("%d", &n);
    int ans = 0;
    for (int i = 0; i < size; i++)
    {
        if (a[i] == n)
        {
            printf("The index of the key is %d", i);
            ans = 1;
            break;
        }
    }
    if (ans != 1)
    {
        printf("Element not found ");
    }
}

int main()
{

    printf("Enter the size of array\n");
    scanf("%d", &size);
    printf("Enter elements of array \n");
    for (i = 0; i < size; i++)
    {
        scanf("%d", &a[i]);
    }
    do
    {

        printf("\n\nType 1 for insertion \n ");
        printf("Type 2 for deletion \n ");
        printf("Type 3 for searching \n ");
        printf("Type 4 for Exit \n  ");

        printf("Enter your choice :->");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            insertion(a, 100);

            break;
        case 2:
            deletion(a, 100);
            break;

        case 3:
            searching(a, 100);
            break;
        case 4:
            printf("You are quiting  ");
            break;

        default:
            printf("Wrong choice");
        }

    } while (choice != 4);

    return 0;
}
