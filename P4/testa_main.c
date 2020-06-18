#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "hashfunc.h"

extern const int HASHVEKSIZE;


int main() {

    Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
    init(myhashvek);

    put(myhashvek, "Mimmi", "0737568014");
    put(myhashvek, "Liam", "0736789099");
    put(myhashvek, "Sofia", "0709872433");
    put(myhashvek, "Oliver", "0765656722");

    char namnet[30] = "Mimmi";
    char * s = get(myhashvek, namnet);
    printf(" -> value = %s\n",s);
    printf("expecting %s\n", namnet);

    uint32_t hash_key= tilpro_hash(key);

    Nod *temp=search(hashtable[hash_key],key);
    Nod *nyNod = (Nod *) malloc(sizeof(Nod));

    if (temp==NULL) { //om artisen inte finns
        strncpy(nyNod->tel, value, 30);
        strncpy(nyNod->name, key, 30);
        insertnod(&hashtable[hash_key], nyNod);
    }
    else
        hashtable[hash_key]=temp->tel;
}


}



