#include <stdlib.h>
#include <stdio.h>
#include <string.h>


struct nod {
    char name[30];
    int tel;
    struct nod * prev;
    struct nod * next;
};

typedef struct nod my_node; // defining data structure for my structure nod, renaming it my_node

int main(){

    my_node *p = malloc(sizeof(my_node)); // allocating memory for pointer *p

    p -> next =  malloc(sizeof(my_node)); //allcoating memory for the place p point to, the pointer p points to the
    p -> next -> prev = p;
    free(p); // free space of pointer after use, (no trash collector)

    printf("klar");



}
