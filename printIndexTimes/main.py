st='INDIA'
st=st.lower()
print(st)
for i in range(1,len(st)+1):
    print(i*st[i-1],end='')

# #include<stdio.h>
# #include<string.h>
# #include<ctype.h>
# int main(){
#     char *str;
#     scanf("%s",str);
#     for(int i=0;str[i]!='\0';i++){
#         int n=i+1;
#         while(n--){
#             printf("%c",tolower(str[i]));
#         }
#     }
# }