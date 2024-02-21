#include <stdio.h>
struct tipoFiliacao{
    char nome[80];
    char nomeMae[80];
    char nomePai[80];
};
struct tipoFiliacao separaLinhaCSV(char linha[240]){
    struct tipoFiliacao fil ={
        
    };
    int i;
    for(i=0;linha[i]!=',';i++){
        fil.nome[i]=linha[i];
    }
    i++;
    int j=0;
    for(i;linha[i]!=',';i++){
        fil.nomeMae[j]=linha[i];
        j++;
    }
    i++;
    j=0;
    for(i;linha[i]!='\0';i++){
        fil.nomePai[j]=linha[i];
        j++;
    }
    return fil;
}