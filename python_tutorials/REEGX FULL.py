#                      REGEX
# _________________________________________________________________
#                     REFERENCES

# HTTPS://WWW.DEBUGGEX.COM/CHEATSHEET/REGEX/PYTHON
# HTTPS://DOCS.PYTHON.ORG/2/LIBRARY/RE.HTML
# HTTPS://WWW.SHORTCUTFOO.COM/APP/DOJOS/PYTHON-REGEX/CHEATSHEET
# _________________________________________________________________

import re

s='This world is full of fools and  flaws. millions and millions people pass through the cycle. $only few ##fools will know, what the reality is!'

# -----------------------------------------------------------------
# The special characters are:
# -----------------------------------------------------------------
# '.'
# R=re.compile(r'.')
# print(R.findall(s))
# -----------------------------------------------------------------
# '^'
# R=re.compile(r'^[\w]*')
# print(R.findall(s))

# -----------------------------------------------------------------
# '^'
# R=re.compile(r'[\W]$')
# print(R.findall(s))

# -----------------------------------------------------------------
# '*'
# R=re.compile(r'.*')
# print(R.findall(s))

# R=re.compile(r'([\w][^\s*]*)')
# print(R.findall(s))

# -----------------------------------------------------------------
# '+'
# R=re.compile(r'([\w][^\s]+)')
# print(R.findall(s))

# -----------------------------------------------------------------
# '?'
# R=re.compile(r'([\w]?)')
# print(R.findall(s))

# R=re.compile(r'll?')
# print(R.findall(s))

# -----------------------------------------------------------------

# '*?', '+?', '??'
# R=re.compile(r'll??')
# print(R.findall(s))

# R=re.compile(r'll+?')
# print(R.findall(s))

# R=re.compile(r'([\w][^\s]+)')
# R=re.compile(r'([\w][^\s]+?)')
# print(R.findall(s))

# R=re.compile(r'll.*?')
# print(R.findall(s))

# -----------------------------------------------------------------

str1='1121231234'
# {m,n}!?

# R=re.compile(r'[\d]{3}')
# R=re.compile(r'[\d]{3,}')
# R=re.compile(r'[\d]{3,5}')
# R=re.compile(r'[\d]{,5}')

# R=re.compile(r'\d{2,3}')
# R=re.compile(r'\d{2,3}?')
# R=re.compile(r'\d{2,3}!?')

# print(R.findall(str1))

# -----------------------------------------------------------------
# '\' special character escape
# str2='ch\d*mo.?'

# R=re.compile(r'ch\\d\*mo\.\?')
# print(R.findall(str2))

# -----------------------------------------------------------------
# '[|]' set

# str3='BhanuBhanushali'
# R=re.compile(r'[\w]')
# R=re.compile(r'[\w]+')
# R=re.compile(r'[\w]*')
# R=re.compile(r'[\w]?')
# R=re.compile(r'[A-Z]')
# print(R.findall(str3))

# str3='12312345'
# R=re.compile(r'[1-2]')
# R=re.compile(r'[1-2]+')
# R=re.compile(r'[1-2]+?')
# R=re.compile(r'[1-2]+!?')
# R=re.compile(r'[^1-2]+')
# print(R.findall(str3))

# str2=r'c\ad**mo^?'
# R=re.compile(r'[ch\d*mo.?]+')
# R=re.compile(r'[c\\ad**mo^?]+')
# R=re.compile(r'[^^]+')
# print(R.findall(str2))

# str4='BhanuBhAnushali'
# R=re.compile(r'Bh[A|a]n')
# print(R.findall(str4))

# -----------------------------------------------------------------

# (...) groups

str5='One One Two Three 4 4 5 six 7ven'
# R=re.compile(r'(\w)')
# R=re.compile(r'(\w+)')
# R=re.compile(r'(\w+)!?')
# R=re.compile(r'([\w])\1')
# R=re.compile(r'([0-9]).\1')
# print(R.findall(str5))


# -----------------------------------------------------------------

    # EXTENSION NOTATION

str6='''One One Two Three
4 4 5 six 7ven'''

    # i	Ignore case
# R = re.compile(r'(?i:.[A-Z]+)')

    # m	^ and $ match start and end of line
# R=re.compile(r'(?im:[a-z7]+)')

    # s	. matches newline as well
# R=re.compile(r'(?s:[\s])')

    # x	Allow spaces and comments
# R = re.compile(r'(?x:[\w]+)')

    # L	Locale character classes
    # u	Unicode character classes
    # (?iLmsux)	Set flags within regex

    # A non-capturing version of regular parentheses.
# R = re.compile(r'([\d]).*\1')
# R = re.compile(r'(?:[\d]).*\1')
# print(R.findall(str6))


# -------------------------------------------------------------

str7='1122233444444'
# R = re.compile(r'(?P<X>[\d])(?P=X)*')
# R = re.compile(r'(?P<X>[\d])(?P=X){2,}')
# R = re.compile(r'(?P<X>[\d]){3,}')
# R = re.compile(r'(?P<X>[\d])(?P=X)?')
# R = re.compile(r'(?P<X>[\d])(?P=X){2,}!?')

# commemts using hash '#'
# R = re.compile(r'(?#bhai)(?P<X>[\d])(?P=X){2,}!?')


str8='take this $12 and give me back $2. Thats how i will earn a 1 $'

# R = re.compile(r'1(?=2)')

# lookahead assertion
# R = re.compile(r'(t|T)(?=h|H)')

# negative lookahead assertion ?!
# R = re.compile(r'(\$)(?!\d)')

# --------------------------------
# POSITIVE LOOKBEHIND ASSERTION. (?<=...) SEARCH FOR $ BEFORE NUMBER
# R = re.compile(r'(?<=\$)(\d)')

# negative lookbehind assertion. search number which is not having number before it
# R = re.compile(r'(?<!\$)(\d)')
# R = re.compile(r'(?<!t...\s)\$')

# Match "yes" pattern if id or name exists, otherwise match "no" pattern
# R = re.compile(r'(?P<name>[\d])(?(name)\1|\$)')
# R = re.compile(r'(?P<name>[\d])(?(name)\d|\$)')
# R = re.compile(r'(?P<name>this).*(?(name)will|\w)')

# print(R.findall(str8))

# -------------------------------------------------------------
# Special Sequences

str9='BCXPA 3515  Q '

# \A Match only at start of string
# R = re.compile(r'\ABC.*')
# print(R.findall(str9))

# \b Match empty string, only at beginning or end of a word, \b is defined as the boundary between a \w and a \W character
# R = re.compile(r'Q\b')
# R = re.compile(r'(\w+)\b')
# print(R.findall(str9))

# \B Match empty string, only when it is not at beginning or end of word, opposite of \b
# R = re.compile(r'\B(\w.+)\B')
# print(R.findall(str9))

# \d Match digits # same as [0-9]
# \D Match any non digit # same as [^0-9]
# \s Match whitespace characters # same as [ \t\n\r\f\v]
# \S Match non whitespace characters #same as [^ \t\n\r\f\v]
# \w Match unicode word characters # same as [a-zA-Z0-9_]
# \W Match any character not a Unicode word character # same as [^a-zA-Z0-9_]

# \Z Match only at end of string
# R = re.compile(r'.*3515\Z')
# R = re.compile(r'\d\w.*\Z')
# print(R.findall(str9))

# STANDARD ESCAPES
# \a      \b      \f      \n
# \r      \t      \v      \x
# \\

# ___________________________________________________________________________
#                    RE MODULE
# METHODS  :  https://www.tutorialspoint.com/python/python_reg_expressions.htm
# ___________________________________________________________________________

# RE.COMPILE(PATTERN, FLAGS) COMPILE A REGULAR EXPRESSION OF PATTERN, WITH FLAGS

# s='BCXPA3515Q'
# R=re.compile('^[A-Z]{5}[\d]{4}[A-Z]$')
# print(R.findall(s))
# print(R.match(s))

# -------------------------------------------------------------
# RE.MATCH(PATTERN, STRING) MATCH PATTERN ONLY AT BEGINNING OF STRING

# s='BCXPA3515Q'
# m=re.match('^[A-Z]{5}[\d]{4}[A-Z]$',s)
# m=re.match('^([A-Z]{5})([\d]{4})',s)
# m=re.match('^([A-Z]{5})([\d]{4})([A-Z])$',s)
# print(m.string)
# print(m.start())
# print(m.end())
# print(m)
# if m:
#     print("matchObj.group() : ", m.group())
#     print("matchObj.group(1) : ", m.group(1))
#     print("matchObj.group(2) : ", m.group(2))
#     print("matchObj.group(3) : ", m.group(3))
# else:
#     print('nothing found')

# -------------------------------------------------------------

# RE.SEARCH(PATTERN, STRING)
# THIS FUNCTION SEARCHES FOR FIRST OCCURRENCE OF RE PATTERN WITHIN STRING WITH OPTIONAL FLAGS.
# RETURNS A MATCH OBJECT ON SUCCESS, NONE ON FAILURE.
# RE.SEARCH(PATTERN, STRING, FLAGS=0)


# s='BCXPA3515Q'

# searchObj = re.search( r'^([A-Z]{5})([\d]{4})([A-Z])$', s, re.M|re.I)

# if searchObj:
#     print("matchObj.group() : ", searchObj.group())
#     print("matchObj.group(1) : ", searchObj.group(1))
#     print("matchObj.group(2) : ", searchObj.group(2))
#     print("matchObj.group(3) : ", searchObj.group(3))
# else:
#     print('nothing found')


# id='B1CDEF2354'
# if(re.search(r'[A-Za-z0-9]{10}', id) and re.search(r'([A-Z].*){2}', id) and re.search(r'([0-9].*){3}', id)):
#     print('Valid')
# else:
#     print('invalid')


# --------------------------------------------------------------------------------
# Matching Versus Searching
#   match checks for a match only at the beginning of the string,
#   while search checks for a match anywhere in the string
#
# s='BCXPA3515Q'
# searchObj = re.search( r'([\d]{4})', s, re.M|re.I)
# if searchObj:
#     print(searchObj.group())
# else:
#     print('nothing found')
# matchObj=re.match('([\d]{4})',s)
# if matchObj:
#     print(matchObj.group())
# else:
#     print('nothing found')
# --------------------------------------------------------------------------------

# -------------------------------------------------------------
# re.split(pattern, string) Split string by occurrences of patern


# -------------------------------------------------------------
# re.sub(pattern, str2, string) Replace leftmost non-overlapping occurrences of pattern in string with str2
# substituting all occurrences unless max provided.
# returns modified string.

# s='BCXPA3515Qa'
# def replfunc(m):
#     return m.group(1).lower()+str(int(m.group(2))-2)+m.group(3)
# print(re.sub('([A-Z]+)([0-9]+)(\w)',replfunc,s))

# print(re.sub('([A-Z]+)([0-9]+)(\w)',lambda m:m.group(1).lower()+str(int(m.group(2))+2)+m.group(3),s))

# RE.SUBN(PATTERN, STR2, STRING) REPLACE LEFT MOST OCCURRENCES OF PATTERN IN STRING WITH STR2,
# BUT RETURN A TUPLE OF (NEWSTRING, # SUBS MADE)

# -------------------------------------------------------------
# re.fullmatch(pattern, string) Match pattern if whole string matches regular expression

# s='BCXPA3515Qa'

# fullMatchObj=re.fullmatch('([A-Z]{5})([\d]{4})([\w])', s)
# fullMatchObj=re.fullmatch('([A-Z]{5})([\d]{4})([\w]){1,}', s)
# if fullMatchObj:
#     print(fullMatchObj.group())
# else:
#     print('nothing found')

# -------------------------------------------------------------
# re.findall(pattern, string) Return all non-overlapping matches of pattern in string, as a list of strings

# s='BCXPA3515Qa'
# print(re.findall(pattern='([\w])',string=s))
# print(re.findall(pattern='([\w]+)',string=s))

# -------------------------------------------------------------
# re.finditer(pattern, string) Return an iterator yielding match objects over
# non-overlapping matches of pattern in string

s='BCXPA3515Qa'
for pattern in re.finditer(pattern='([a-zA-Z]{1,})',string=s):
    print(pattern,pattern.group(0))

# -------------------------------------------------------------

# -------------------------------------------------------------
# re.purge() Clear the regular expression cache

print(re.purge())

# **************************************************************