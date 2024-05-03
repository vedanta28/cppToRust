#include<bits/stdc++.h>
void transpose(int a[3][3],size_t n){
    for(size_t i=0;i<n;i++){
        for(size_t j=i;j<n;j++){
            int temp=a[i][j];
            a[i][j]=a[j][i];
            a[j][i]=temp;
        }
    }
}
void print(int a[3][3],size_t n){
    for (size_t i = 0; i < n; i++){
        for (size_t j = 0; j < n; j++){
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
}
int main(){
    int a[3][3]={{1,2,3},{4,5,6},{7,8,9}};
    transpose(a,3);
    print(a,3);
}
