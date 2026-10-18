#include <stdio.h>
#include <stdlib.h>

struct Node{
    int a;
    struct Node *next;
};

int main(){
    int size;
    printf("Enter number of nodes: ");
    scanf("%d",&size);
    if (size<=0){
        return 1;
    }

    struct Node *Head = NULL;
    struct Node *Tail = NULL;
    

    for (int i = 0; i<size; i++){
        struct Node *Temp = NULL;
        Temp = (struct Node*)malloc(sizeof(struct Node));
        printf("Enter Element: ");
        Temp ->next = NULL;
        scanf("%d",&(Temp->a));
        if (Head == NULL){
            Head = Temp;
            Tail = Temp;
        }
        else{
            Tail->next = Temp;
            Tail = Temp;
        }

    }
    struct Node *curr = Head;
    while (curr != NULL){
        printf("%d-> ", curr->a);
        curr = curr->next;
    }
    printf("NULL");

    curr = Head;
    while(curr!=NULL){
        struct Node *next = curr->next;
        free(curr);
        curr = next;

    }
    return 0;
}