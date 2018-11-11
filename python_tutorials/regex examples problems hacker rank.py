# mail='shashank@companymail.c_o'
# mail='shashank@9mail.com'
# mail='shashank@gmail.9om'
# mail='shashank@gma_il.com'
# mail='shashank@mail.moc'
# # mail='shashank@company-mail.com'
# # mail='shashank@companymail.c_o'
# import re
# if (re.match('^[a-zA-Z]([\-\._]*[a-zA-Z])*@([a-zA-Z]+)(\.)[a-zA-Z]{1,3}$', mail)):
#     print('hi')



# s='rabcdeefgyYhFjkIoomnpOeorteeeeet'
# import re
# v = "aeiou"
# c = "qwrtypsdfghjklzxcvbnm"
#
# print(re.findall(r"(?<=[%s])([%s]{2,})[%s]"%(c, v, c),s,flags=re.I))


# s='122111'
# import re
# m = re.search(r'(P<abc>: [a-zA-Z0-9])\1+', s)
# print(m.groupdict() if m else -1)

s='''
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>'''

import re
matchObj=re.findall('<(\w+)(\s([\w]+))?',s)
print(matchObj)
