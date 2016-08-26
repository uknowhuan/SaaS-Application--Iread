# coding=utf-8
'''
Created on 2014-12-19

@author: guan
'''
import data.register as register
import data.login as login
import data.content as content
import data.key_word as kw
# Begin
'''
url to method
'''
urls = {
    '/mobile/register'          : register.register,

    '/mobile/login'             : login.login,
    
    '/mobile/content'            : content.get_list,

    '/mobile/key_word'          : kw.key_word_list,
    '/mobile/key_word/add'      : kw.key_word_add,
    '/mobile/key_word/delete'   : kw.key_word_delete,
    #'/mobile/key_word/update'   : kw.key_word_update,
}

# End
