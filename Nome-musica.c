#include <stdio.h>
#include <string.h>
struct tipoMusica
{
    char nome[80];
    int ano;
};
struct tipoBanda
{
    char nome[80];
    int qtd;
    struct tipoMusica musicas[100];
};
void pesquisarNomeMusica(char pesquisa[80], struct tipoBanda bandas[50], int n)
{
    int pesq;
    int tem=0;
    for (int band = 0; band < n; band++)
    {
        for (int quant = 0; quant < bandas[band].qtd; quant++)
        {
            pesq = strcmp(pesquisa,bandas[band].musicas[quant].nome);
            if (pesq==0)
            {
                tem++;
                printf("%s : ano %d\n", bandas[band].nome, bandas[band].musicas[quant].ano);
            }
        }
    }
    if(tem==0){
        printf("Musica nao cadastrada");
    }
    return;
}