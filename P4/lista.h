#include <stdio.h>
#ifndef LISTA_H
#define LISTA_H

struct nod {
    char name[30];
    char tel[30];
    struct nod * next;
    struct nod * prev;

};
typedef struct nod Nod;

Nod *createNod(char Namn[], char tele[]);
void insertnod(Nod ** padr, Nod * tobeadded); //insert new node into
void removenod(Nod ** padr, Nod * toberemoved);
void printnod(Nod * p);
void printlist(Nod * p);
Nod * search(Nod * p, char namn[]);

#endif


