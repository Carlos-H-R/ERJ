int binsrc(int c,int i,int f,int vet[]){
    int m = (i+f)/2;
    if(c==vet[m]){return m;}
    else if(c>vet[m]){
        i=m;
        binsrc(c,i,f,vet[]);
    }
    else{
        f=m;
        binsrc(c,i,f,vet[]);
    }
}

//apenas o modulo da busca binaria.
//J´aengloba o Ex3.