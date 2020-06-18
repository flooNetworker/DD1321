#include "hashfunc.h"
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

const int HASHVEKSIZE = 2097152;    // 2 upphöjt till 20 ungefär 1 miljon
//const int HASHVEKSIZE = 2097152     // 2 upphöjt till 21
//const int HASHVEKSIZE = 4194304     // 2 upphöjt till 22

uint32_t tilpro_hash(const char * s) {
    uint32_t hash = 0;
    size_t i = 0;
    while (s[i] != '\0') {
        hash += s[i++];
        hash += hash << 10;
        hash ^= hash >> 6;
    }
    hash += hash << 3;
    hash ^= hash >> 11;
    hash += hash << 13;

    hash = hash & ( HASHVEKSIZE - 1 );
    return hash;
}

void put(Nod ** hashtable, char * key, char * value) {
    uint32_t hash_key= tilpro_hash(key);

    Nod *nyNod = (Nod *) malloc(sizeof(Nod));
    strncpy(nyNod->tel, value, 30);
    strncpy(nyNod->name, key, 30);

    insertnod(&hashtable[hash_key], nyNod);

}

char * get(Nod ** hashtable, char * key) {

    uint32_t hash_key= tilpro_hash(key);

    Nod *temp=search(hashtable[hash_key],key);
    char a[30];

    if (temp==NULL)
        return NULL;

    else {
        return strncpy(a, temp->tel, 30);
    }


   }

void init(Nod ** vek) {
    for (int i=0; i<HASHVEKSIZE;i++){
        vek[i]=NULL;
    }
}


//  Läser artister från filename och lägger dem i artistarray
//  returnerar antalet inlästa artister
int readartists(char * filename, Artist * artistarray) {
    char linebuffer[425];

    FILE * fil = fopen(filename, "r");

    int currentartist = 0;

    while (fgets (linebuffer, 425, fil) != NULL) {

        Artist * artist = artistarray + currentartist;

        int i = 0;
        int j = 0;
        // kolumner är TAB-separerade
        while (linebuffer[i] != '\t')
            i++;

        strncpy(artist -> artistid, linebuffer, j);

        i += 1;
        j = i;
        while (linebuffer[i] != '\t')
            i++;

        strncpy(artist -> artistname, linebuffer + j, i - j);

        i += 1;
        j = i;
        while (linebuffer[i] != '\t')
            i++;

        strncpy(artist -> songtitle, linebuffer + j, i - j);

        i += 1;
        // atof - array to float
        artist -> length = atof(linebuffer + i);

        while (linebuffer[i] != '\t')
            i++;

        i += 1;
        // atoi - array to integer
        artist -> year = atoi(linebuffer + i);

        currentartist += 1;
    }
    return currentartist;
}