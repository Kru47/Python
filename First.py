keywords=["if", "while", "for", "int", "char", "string"]
operators=["=", "+", "-", "%", "/", "*"]
delimiters=[";", ",", " ", "(", ")", "=", "+", "-", "%", "/", "*", ">", "<", ">=", "==", "<=" ]
Keywordtoken=[]
IdentifierToken=[]
OperatorToken=[]
DelimiterToken=[]

str = input("Enter string")
first = 0
last = 0
TokenVar = 0

for i in range(0, len(str), 1):

   if str[i] in delimiters:
     if str[i] in operators:
         '''Do Nothing'''
     else:
         DelimiterToken.append(str[i])
     print("Encounterd", str[i])
     last = i
     print(str[first:last])

     if str[first:last] in keywords:
         if str[first:last] in Keywordtoken:
                   '''Do nothing'''
                   first=i+1
         else:
             Keywordtoken.    append(str[first:last])
             first = i + 1


     else:
         if str[first:last].isdigit():
             '''Do nothing'''
             first=i+len(str[first:last])
         else:

             IdentifierToken.append(str[first:last])
             first = i + 1
   if str[i] in operators:
       OperatorToken.append(str[i])

print(OperatorToken)
print(Keywordtoken)
print(IdentifierToken)
print(DelimiterToken)



