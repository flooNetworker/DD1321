#ifndef tproHASHFUNC_H
#define tproHASHFUNC_H

#include <stdint.h>
#include "lista.h"    // en headerfil för en modifierad dubbellänkad lista p3

struct artist {
    char artistid[20];
    char artistname[400];
    char songtitle[300];
    double length;
    int year;
};

typedef struct artist Artist;


uint32_t tilpro_hash(const char * s) ;

void put(Nod ** hashtable, char * key, char * value);
char * get(Nod ** hashtable, char * key);
void init(Nod ** vek);

int readartists(char * filename, Artist * artistarray);

#endif