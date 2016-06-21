string1 = 'Some text'
String2 = "어떤 텍스트"
String3 = '{}도 {}도 지금 이것도 문자열'.format(string1,String2)

print (string1, String2, String3)

quote = ' 문법검사기 왈 "직접인용은 큰따옴표다!"'
emphasize = "'문법검사기'를 인용하다니"
# error = "엄마친구 아들이 "파이썬이 좋아" 라고 했대"

long_string = '''첫째줄은 좋은데
둘째줄도 괜찮을까?'''
# 따옴표 세개는 여러줄 문자열
quote  = "가끔은 '와 " + '"를 모두 쓰기도 해"'
quote2 = '''가끔은 '와 "를 모두 쓰기도 해"'''
print (long_string)
print(emphasize)
print (quote,quote2)

quote3 ="내가 니 애비다!"
print "다스베이더가 말했다.\n{}\n그 말을 들은 루크는 '깜짝' 놀랐다.".format(string1)