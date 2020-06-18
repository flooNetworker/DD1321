#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lista.h"


//create newnode by given data, allocate space for  pointer (nynod) and store name and phone
Nod *createNod(char Namn[], char tele[]){
    Nod * nyNod =(Nod* ) malloc(sizeof(Nod));
    strncpy(nyNod -> tel,tele, 30);
    strncpy(nyNod -> name,Namn, 30);

    return nyNod;

}

//insert node tobeadded (return value of createNod) into linked list
void insertnod(Nod ** padr, Nod * tobeadded) {


    if (*padr==NULL){
        tobeadded->next = *padr;
        tobeadded->prev = NULL;
        *padr = tobeadded;
    }
    else {
        tobeadded -> next = *padr;
        tobeadded -> next -> prev = tobeadded;
        *padr = tobeadded;
        tobeadded -> prev = NULL;

    }
}

//remove node toberemoved from linked list
void removenod(Nod **padr, Nod * toberemoved){

    //If empty list
    if (*padr == NULL || toberemoved ==NULL){
        return;
    }

    //If the node to be removed is the head
    if (toberemoved->prev == NULL) {
        *padr = toberemoved->next;

        if (toberemoved->next != NULL)
            toberemoved->next->prev = NULL;
    }

        //If the node to be removed is the tail
    else if (toberemoved->next ==NULL){
        toberemoved ->prev -> next = NULL;
    }

    else {
        Nod * current = *padr;

        //start from head, go through list
        while (current != NULL){

            //if the next node is the node to be removed
            if (current->next == toberemoved) {
                current->next = current->next->next;      //re-point next of the current node to the node after toberemoved
                current->next->prev = current;           //re-point prev of the current node to the node before toberemoved

                break;
            }
            else {
                current = current->next;    //else take next node

            }

        }
    }

    free(toberemoved);

}


//print out single nod
void printnod(Nod *p) {
    printf("%s ", p -> name );
    printf("%s ", p -> tel );
    printf("\n");

}

//print out list of nodes
void printlist(Nod * p){
    Nod *temp = p;
    while (temp!=NULL) {
        printf("%s ", temp -> name );
        printf("%s ", temp -> tel );
        printf("\n");


        temp = temp->next;
    }
    printf("\n");

}

Nod * search(Nod * p, char tel[]){

    if (p==NULL){
        printf("No linked list exist");
        return NULL;
    }

    Nod *temp = p;
    char a[30];

    while (temp!=NULL) {
        strncpy(a, temp -> tel, 30);
        int result = strcmp(a, tel);

        if (result==0){
            printf("Phone numnber: %s found in linked list", tel);
            printf("\n");
            return temp;

        }
        if(temp->next != NULL)
            temp = temp->next;
    }

    printf("Phone number %s not found in linked list, please check again", tel);
    return NULL;

}

