#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashfunc.h"

extern const int HASHVEKSIZE;

int main() {
    Artist * artister = malloc(sizeof(Artist) * 1000000);
    // calloc är ett alternativ till malloc som initierar vektorn till noll
    //   Artist * artister = calloc(1000000, sizeof(Artist));

    Nod ** myhashvek = malloc(sizeof(Nod *) * HASHVEKSIZE);
    init(myhashvek);

    int antalartister = readartists("sang-artist-data.txt", artister);

    for (int i = 0; i < antalartister; i += 1) {
        put(myhashvek, artister[i].artistname, artister[i].songtitle);

    }

    char namnet[30] = "Faster Pussy cat";
    char * s = get(myhashvek, namnet);
    printf(" -> value = %s\n",s);
    printf("expecting %s\n", namnet);



    free(artister);
    free(myhashvek);

    return 0;
}