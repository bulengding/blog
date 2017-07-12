import httplib
import urllib2
import urllib
import math

demo_request_url = "https://ssl.zc.qq.com/cgi-bin/chs/qqmailreg/check_mail?email=rrrddd@qq.com"


def IsPreCharactersAllz(string_source = "", index = 0) :
  string_length = len(string_source)
  index_tmp = -1;
  for char in string_source :
    index_tmp = index_tmp + 1;
    if (index_tmp < index and (char != 'z')) :
      return True
  if (len(string_source) == 1) :
    return string_source[0] == 'z'
  return False;

def ReplaceChar(string_source = "", index = 0, replaced_char = 'a') :
  charlist =list(string_source)
  charlist[index] = replaced_char
  return ''.join(charlist)

def GetNextChar(char_current = 'a') :
  tmp_int = ord(char_current)
  tmp_int = tmp_int + 1
  return chr(tmp_int)

def GenerateNextString(string_source = "") :
  string_length = len(string_source)
  string_ret = string_source
  last_char = string_ret[string_length -1]
  if (last_char == 'z') :
    if (IsPreCharactersAllz(string_ret, string_length-1)) :
      string_ret = string_ret + 'a';
    else:
      string_ret = ReplaceChar(string_ret, string_length-2, string_ret[string_length-2] + 1)
  else :
    string_ret = ReplaceChar(string_ret, string_length-1, GetNextChar(string_ret[string_length-1]))
  return  string_ret

def stringToint(string_source = "a") :
  index = len(string_source)
  int_value = 0
  for char_item in string_source:
    index = index -1
    int_value = int_value + (pow(26, index) * (ord(char_item) - 97))
  return int_value

def inttostring(int_source = 789):
  str_list = []
  origin_source = int_source
  while(True):
    if (int_source < 26) :
      break
    char_tmp1 = int_source % (26)
    int_source = int_source / 26
    str_list.insert(0, chr(char_tmp1 + 97))
  if (int_source != 0) :
    str_list.insert(0, chr(int_source + 97))
  return ''.join(str_list);

def GenerateNextString2(string_source = "") :
  int_value = stringToint(string_source)
  int_value  = int_value + 1
  return inttostring(int_value)
           

def IncreaseString(string_source = "") :
  if (len(string_source) == 1) :
       if (string_source[0] < 'z'):
           return chr(ord(string_source[0]) + 1)
       else :
           return "aa"
  else :
      if (string_source[-1] == 'z') :
          return IncreaseString(string_source[:-1]) + 'a';
      else :
          tmp1 = string_source[:-1]
          last_int = ord(string_source[-1])
          last_increased = chr(last_int + 1)
          return tmp1 + last_increased


string_out = "aa"


while(True):
  string_out = IncreaseString(string_out)
  request_url = "http://ssl.zc.qq.com/cgi-bin/chs/qqmailreg/check_mail?email=" + string_out + "@qq.com"

  request = urllib2.Request(request_url)
  opener = urllib2.build_opener()
  feeddata = opener.open(request).read()
  print string_out + " result is : " + feeddata;
