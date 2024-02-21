#include <stdio.h>
//struct para o tipoLogradouro
struct tipoLogradouro{
    char tipo[80];
    char nome[80];
    char complemento[80];
};

// funcao principal

void criaLinhaCSV(struct tipoLogradouro info,char linha[240]){
    
    int i=0; //variavel para auxiliar no percurso das strings: tipo, nome e complemento
    int j=0;

    int contT=0; //contador para o tamanho da string Tipo da struct tipoLogradouro

    int contN=0; //contador para o tamanho da string Nome da struct tipoLogradouro

    int contC=0; //contador para o tamanho da string Complemento da struct tipoLogradouro

    for(int a=0;info.tipo[a]!='\0';a++){

        //for para percorrer a string Tipo e contar seu tamanho
        contT++;
    }
    for(int a=0;info.nome[a]!='\0';a++){

        //for para percorrer a string Nome e contar seu tamanho
        contN++;
    }
    for(int a=0;info.complemento[a]!='\0';a++){

        //for para percorrer a string Complemento e contar seu tamanho
        contC++;
    }
    for( ;i<contT;i++){

        //for para atribuir na linha i o char i do Tipo;
        linha[j]=info.tipo[i];
        j++;
    }

    linha[j]=';'; //o i atualmente é a posicao do ";", por isso, essa atribuicao

    i=0; //o i agora vai percorrer a próxima string, começando do 0
    j++;
    for( ;i<contN;i++){

        //for para atribuir na linha i o char i do Nome;
        linha[j]=info.nome[i];
        j++;
    }

    linha[j]=';'; //o i atualmente é a posicao do ";", por isso, essa atribuicao

    i=0; //o i agora vai percorrer a próxima string, começando do 0
    j++;
    for( ;i<contC;i++){

        //for para atribuir na linha i o char i do Complemento;
        linha[j]=info.complemento[i];
        j++;
    }
    linha[j]='\0'; //o i atualmente é a posicao do "\0", por isso, essa atribuicao

    return; //fim do programa
}