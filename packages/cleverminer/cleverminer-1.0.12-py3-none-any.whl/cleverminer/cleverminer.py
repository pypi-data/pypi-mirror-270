import sys #line:58
import time #line:59
import copy #line:60
from time import strftime #line:62
from time import gmtime #line:63
import pandas as pd #line:65
import numpy #line:66
from pandas .api .types import CategoricalDtype #line:67
import progressbar #line:69
import re #line:70
class cleverminer :#line:71
    version_string ="1.0.12"#line:73
    def __init__ (OO00000O00O0OO00O ,**O000OOOOOO0O0OO00 ):#line:75
        OO00000O00O0OO00O ._print_disclaimer ()#line:76
        OO00000O00O0OO00O .stats ={'total_cnt':0 ,'total_ver':0 ,'total_valid':0 ,'control_number':0 ,'start_prep_time':time .time (),'end_prep_time':time .time (),'start_proc_time':time .time (),'end_proc_time':time .time ()}#line:85
        OO00000O00O0OO00O .options ={'max_categories':100 ,'max_rules':None ,'optimizations':True ,'automatic_data_conversions':True ,'progressbar':True ,'keep_df':False }#line:93
        OO00000O00O0OO00O .df =None #line:94
        OO00000O00O0OO00O .kwargs =None #line:95
        if len (O000OOOOOO0O0OO00 )>0 :#line:96
            OO00000O00O0OO00O .kwargs =O000OOOOOO0O0OO00 #line:97
        OO00000O00O0OO00O .verbosity ={}#line:98
        OO00000O00O0OO00O .verbosity ['debug']=False #line:99
        OO00000O00O0OO00O .verbosity ['print_rules']=False #line:100
        OO00000O00O0OO00O .verbosity ['print_hashes']=True #line:101
        OO00000O00O0OO00O .verbosity ['last_hash_time']=0 #line:102
        OO00000O00O0OO00O .verbosity ['hint']=False #line:103
        if "opts"in O000OOOOOO0O0OO00 :#line:104
            OO00000O00O0OO00O ._set_opts (O000OOOOOO0O0OO00 .get ("opts"))#line:105
        if "opts"in O000OOOOOO0O0OO00 :#line:106
            if "verbose"in O000OOOOOO0O0OO00 .get ('opts'):#line:107
                OOOOOO00OO0OOO00O =O000OOOOOO0O0OO00 .get ('opts').get ('verbose')#line:108
                if OOOOOO00OO0OOO00O .upper ()=='FULL':#line:109
                    OO00000O00O0OO00O .verbosity ['debug']=True #line:110
                    OO00000O00O0OO00O .verbosity ['print_rules']=True #line:111
                    OO00000O00O0OO00O .verbosity ['print_hashes']=False #line:112
                    OO00000O00O0OO00O .verbosity ['hint']=True #line:113
                    OO00000O00O0OO00O .options ['progressbar']=False #line:114
                elif OOOOOO00OO0OOO00O .upper ()=='RULES':#line:115
                    OO00000O00O0OO00O .verbosity ['debug']=False #line:116
                    OO00000O00O0OO00O .verbosity ['print_rules']=True #line:117
                    OO00000O00O0OO00O .verbosity ['print_hashes']=True #line:118
                    OO00000O00O0OO00O .verbosity ['hint']=True #line:119
                    OO00000O00O0OO00O .options ['progressbar']=False #line:120
                elif OOOOOO00OO0OOO00O .upper ()=='HINT':#line:121
                    OO00000O00O0OO00O .verbosity ['debug']=False #line:122
                    OO00000O00O0OO00O .verbosity ['print_rules']=False #line:123
                    OO00000O00O0OO00O .verbosity ['print_hashes']=True #line:124
                    OO00000O00O0OO00O .verbosity ['last_hash_time']=0 #line:125
                    OO00000O00O0OO00O .verbosity ['hint']=True #line:126
                    OO00000O00O0OO00O .options ['progressbar']=False #line:127
                elif OOOOOO00OO0OOO00O .upper ()=='DEBUG':#line:128
                    OO00000O00O0OO00O .verbosity ['debug']=True #line:129
                    OO00000O00O0OO00O .verbosity ['print_rules']=True #line:130
                    OO00000O00O0OO00O .verbosity ['print_hashes']=True #line:131
                    OO00000O00O0OO00O .verbosity ['last_hash_time']=0 #line:132
                    OO00000O00O0OO00O .verbosity ['hint']=True #line:133
                    OO00000O00O0OO00O .options ['progressbar']=False #line:134
        OO00000O00O0OO00O ._is_py310 =sys .version_info [0 ]>=4 or (sys .version_info [0 ]>=3 and sys .version_info [1 ]>=10 )#line:135
        if not (OO00000O00O0OO00O ._is_py310 ):#line:136
            print ("Warning: Python 3.10+ NOT detected. You should upgrade to Python 3.10 or greater to get better performance")#line:137
        else :#line:138
            if (OO00000O00O0OO00O .verbosity ['debug']):#line:139
                print ("Python 3.10+ detected.")#line:140
        OO00000O00O0OO00O ._initialized =False #line:141
        OO00000O00O0OO00O ._init_data ()#line:142
        OO00000O00O0OO00O ._init_task ()#line:143
        if len (O000OOOOOO0O0OO00 )>0 :#line:144
            if "df"in O000OOOOOO0O0OO00 :#line:145
                OO00000O00O0OO00O ._prep_data (O000OOOOOO0O0OO00 .get ("df"))#line:146
            else :#line:147
                print ("Missing dataframe. Cannot initialize.")#line:148
                OO00000O00O0OO00O ._initialized =False #line:149
                return #line:150
            OOOOO000OOOO0O000 =O000OOOOOO0O0OO00 .get ("proc",None )#line:151
            if not (OOOOO000OOOO0O000 ==None ):#line:152
                OO00000O00O0OO00O ._calculate (**O000OOOOOO0O0OO00 )#line:153
            else :#line:155
                if OO00000O00O0OO00O .verbosity ['debug']:#line:156
                    print ("INFO: just initialized")#line:157
                O0000OO00O0000000 ={}#line:158
                O000O0O0O00OOO00O ={}#line:159
                O000O0O0O00OOO00O ["varname"]=OO00000O00O0OO00O .data ["varname"]#line:160
                O000O0O0O00OOO00O ["catnames"]=OO00000O00O0OO00O .data ["catnames"]#line:161
                O0000OO00O0000000 ["datalabels"]=O000O0O0O00OOO00O #line:162
                OO00000O00O0OO00O .result =O0000OO00O0000000 #line:163
        OO00000O00O0OO00O ._initialized =True #line:165
    def _set_opts (O0OOOO0O000OOO00O ,O000000OO000O000O ):#line:167
        if "no_optimizations"in O000000OO000O000O :#line:168
            O0OOOO0O000OOO00O .options ['optimizations']=not (O000000OO000O000O ['no_optimizations'])#line:169
            print ("No optimization will be made.")#line:170
        if "disable_progressbar"in O000000OO000O000O :#line:171
            O0OOOO0O000OOO00O .options ['progressbar']=False #line:172
            print ("Progressbar will not be shown.")#line:173
        if "max_rules"in O000000OO000O000O :#line:174
            O0OOOO0O000OOO00O .options ['max_rules']=O000000OO000O000O ['max_rules']#line:175
        if "max_categories"in O000000OO000O000O :#line:176
            O0OOOO0O000OOO00O .options ['max_categories']=O000000OO000O000O ['max_categories']#line:177
            if O0OOOO0O000OOO00O .verbosity ['debug']==True :#line:178
                print (f"Maximum number of categories set to {O0OOOO0O000OOO00O.options['max_categories']}")#line:179
        if "no_automatic_data_conversions"in O000000OO000O000O :#line:180
            O0OOOO0O000OOO00O .options ['automatic_data_conversions']=not (O000000OO000O000O ['no_automatic_data_conversions'])#line:181
            print ("No automatic data conversions will be made.")#line:182
        if "keep_df"in O000000OO000O000O :#line:183
            O0OOOO0O000OOO00O .options ['keep_df']=O000000OO000O000O ['keep_df']#line:184
    def _init_data (OOO0OO0OO00O0OOOO ):#line:187
        OOO0OO0OO00O0OOOO .data ={}#line:189
        OOO0OO0OO00O0OOOO .data ["varname"]=[]#line:190
        OOO0OO0OO00O0OOOO .data ["catnames"]=[]#line:191
        OOO0OO0OO00O0OOOO .data ["vtypes"]=[]#line:192
        OOO0OO0OO00O0OOOO .data ["dm"]=[]#line:193
        OOO0OO0OO00O0OOOO .data ["rows_count"]=int (0 )#line:194
        OOO0OO0OO00O0OOOO .data ["data_prepared"]=0 #line:195
    def _init_task (O000OO0OO0OO0OOOO ):#line:197
        if "opts"in O000OO0OO0OO0OOOO .kwargs :#line:199
            O000OO0OO0OO0OOOO ._set_opts (O000OO0OO0OO0OOOO .kwargs .get ("opts"))#line:200
        O000OO0OO0OO0OOOO .cedent ={'cedent_type':'none','defi':{},'num_cedent':0 ,'trace_cedent':[],'trace_cedent_asindata':[],'traces':[],'generated_string':'','rule':{},'filter_value':int (0 )}#line:210
        O000OO0OO0OO0OOOO .task_actinfo ={'proc':'','cedents_to_do':[],'cedents':[]}#line:214
        O000OO0OO0OO0OOOO .rulelist =[]#line:215
        O000OO0OO0OO0OOOO .stats ['total_cnt']=0 #line:217
        O000OO0OO0OO0OOOO .stats ['total_valid']=0 #line:218
        O000OO0OO0OO0OOOO .stats ['control_number']=0 #line:219
        O000OO0OO0OO0OOOO .result ={}#line:220
        O000OO0OO0OO0OOOO ._opt_base =None #line:221
        O000OO0OO0OO0OOOO ._opt_relbase =None #line:222
        O000OO0OO0OO0OOOO ._opt_base1 =None #line:223
        O000OO0OO0OO0OOOO ._opt_relbase1 =None #line:224
        O000OO0OO0OO0OOOO ._opt_base2 =None #line:225
        O000OO0OO0OO0OOOO ._opt_relbase2 =None #line:226
        OOO0OO0O000O0OOOO =None #line:227
        if not (O000OO0OO0OO0OOOO .kwargs ==None ):#line:228
            OOO0OO0O000O0OOOO =O000OO0OO0OO0OOOO .kwargs .get ("quantifiers",None )#line:229
            if not (OOO0OO0O000O0OOOO ==None ):#line:230
                for OOOO0O0O000O000O0 in OOO0OO0O000O0OOOO .keys ():#line:231
                    if OOOO0O0O000O000O0 .upper ()=='BASE':#line:232
                        O000OO0OO0OO0OOOO ._opt_base =OOO0OO0O000O0OOOO .get (OOOO0O0O000O000O0 )#line:233
                    if OOOO0O0O000O000O0 .upper ()=='RELBASE':#line:234
                        O000OO0OO0OO0OOOO ._opt_relbase =OOO0OO0O000O0OOOO .get (OOOO0O0O000O000O0 )#line:235
                    if (OOOO0O0O000O000O0 .upper ()=='FRSTBASE')|(OOOO0O0O000O000O0 .upper ()=='BASE1'):#line:236
                        O000OO0OO0OO0OOOO ._opt_base1 =OOO0OO0O000O0OOOO .get (OOOO0O0O000O000O0 )#line:237
                    if (OOOO0O0O000O000O0 .upper ()=='SCNDBASE')|(OOOO0O0O000O000O0 .upper ()=='BASE2'):#line:238
                        O000OO0OO0OO0OOOO ._opt_base2 =OOO0OO0O000O0OOOO .get (OOOO0O0O000O000O0 )#line:239
                    if (OOOO0O0O000O000O0 .upper ()=='FRSTRELBASE')|(OOOO0O0O000O000O0 .upper ()=='RELBASE1'):#line:240
                        O000OO0OO0OO0OOOO ._opt_relbase1 =OOO0OO0O000O0OOOO .get (OOOO0O0O000O000O0 )#line:241
                    if (OOOO0O0O000O000O0 .upper ()=='SCNDRELBASE')|(OOOO0O0O000O000O0 .upper ()=='RELBASE2'):#line:242
                        O000OO0OO0OO0OOOO ._opt_relbase2 =OOO0OO0O000O0OOOO .get (OOOO0O0O000O000O0 )#line:243
            else :#line:244
                print ("Warning: no quantifiers found. Optimization will not take place (1)")#line:245
        else :#line:246
            print ("Warning: no quantifiers found. Optimization will not take place (2)")#line:247
    def mine (O0OO00000OOO0O0O0 ,**OO0O00O0OOOOO0000 ):#line:250
        if not (O0OO00000OOO0O0O0 ._initialized ):#line:251
            print ("Class NOT INITIALIZED. Please call constructor with dataframe first")#line:252
            return #line:253
        O0OO00000OOO0O0O0 .kwargs =None #line:254
        if len (OO0O00O0OOOOO0000 )>0 :#line:255
            O0OO00000OOO0O0O0 .kwargs =OO0O00O0OOOOO0000 #line:256
        O0OO00000OOO0O0O0 ._init_task ()#line:257
        if len (OO0O00O0OOOOO0000 )>0 :#line:258
            O000000OO0O000O00 =OO0O00O0OOOOO0000 .get ("proc",None )#line:259
            if not (O000000OO0O000O00 ==None ):#line:260
                O0OO00000OOO0O0O0 ._calc_all (**OO0O00O0OOOOO0000 )#line:261
            else :#line:262
                print ("Rule mining procedure missing")#line:263
    def _get_ver (OOOOOO000O0OOO0O0 ):#line:266
        return OOOOOO000O0OOO0O0 .version_string #line:267
    def _print_disclaimer (OOO0O000O0O0000OO ):#line:269
        print (f"Cleverminer version {OOO0O000O0O0000OO._get_ver()}.")#line:271
    def _automatic_data_conversions (O0000OOOO0OOOO0O0 ,O0O0O000O0O0000O0 ):#line:277
        print ("Automatically reordering numeric categories ...")#line:278
        for O0OO0OOO0OOO000OO in range (len (O0O0O000O0O0000O0 .columns )):#line:279
            if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:280
                print (f"#{O0OO0OOO0OOO000OO}: {O0O0O000O0O0000O0.columns[O0OO0OOO0OOO000OO]} : {O0O0O000O0O0000O0.dtypes[O0OO0OOO0OOO000OO]}.")#line:281
            try :#line:282
                O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]]=O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]].astype (str ).astype (float )#line:283
                if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:284
                    print (f"CONVERTED TO FLOATS #{O0OO0OOO0OOO000OO}: {O0O0O000O0O0000O0.columns[O0OO0OOO0OOO000OO]} : {O0O0O000O0O0000O0.dtypes[O0OO0OOO0OOO000OO]}.")#line:285
                O000O0O00OO0O0OO0 =pd .unique (O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]])#line:286
                OO0O00OOOOOOOO000 =True #line:287
                for OOO0OO0000000000O in O000O0O00OO0O0OO0 :#line:288
                    if OOO0OO0000000000O %1 !=0 :#line:289
                        OO0O00OOOOOOOO000 =False #line:290
                if OO0O00OOOOOOOO000 :#line:291
                    O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]]=O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]].astype (int )#line:292
                    if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:293
                        print (f"CONVERTED TO INT #{O0OO0OOO0OOO000OO}: {O0O0O000O0O0000O0.columns[O0OO0OOO0OOO000OO]} : {O0O0O000O0O0000O0.dtypes[O0OO0OOO0OOO000OO]}.")#line:294
                OOO0000OO00O0O0O0 =pd .unique (O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]])#line:295
                O0OO00O00O00000OO =CategoricalDtype (categories =OOO0000OO00O0O0O0 .sort (),ordered =True )#line:296
                O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]]=O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]].astype (O0OO00O00O00000OO )#line:297
                if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:298
                    print (f"CONVERTED TO CATEGORY #{O0OO0OOO0OOO000OO}: {O0O0O000O0O0000O0.columns[O0OO0OOO0OOO000OO]} : {O0O0O000O0O0000O0.dtypes[O0OO0OOO0OOO000OO]}.")#line:299
            except :#line:301
                if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:302
                    print ("...cannot be converted to int")#line:303
                try :#line:304
                    OOO0O0O0O0OO00OO0 =O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]].unique ()#line:305
                    if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:306
                        print (f"Values: {OOO0O0O0O0OO00OO0}")#line:307
                    OOO000O0O0O0OOO0O =True #line:308
                    O000O000000O0O0OO =[]#line:309
                    for OOO0OO0000000000O in OOO0O0O0O0OO00OO0 :#line:310
                        OO00O00OOO00O0OOO =re .findall (r"-?\d+",OOO0OO0000000000O )#line:313
                        if len (OO00O00OOO00O0OOO )>0 :#line:315
                            O000O000000O0O0OO .append (int (OO00O00OOO00O0OOO [0 ]))#line:316
                        else :#line:317
                            OOO000O0O0O0OOO0O =False #line:318
                    if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:319
                        print (f"Is ok: {OOO000O0O0O0OOO0O}, extracted {O000O000000O0O0OO}")#line:320
                    if OOO000O0O0O0OOO0O :#line:321
                        O00O0OO00OO00O0O0 =copy .deepcopy (O000O000000O0O0OO )#line:322
                        O00O0OO00OO00O0O0 .sort ()#line:323
                        OOOOO0OOOO0OOO0O0 =[]#line:325
                        for O0O0O0000000O0O0O in O00O0OO00OO00O0O0 :#line:326
                            OO00OOO000OOOO00O =O000O000000O0O0OO .index (O0O0O0000000O0O0O )#line:327
                            OOOOO0OOOO0OOO0O0 .append (OOO0O0O0O0OO00OO0 [OO00OOO000OOOO00O ])#line:329
                        if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:330
                            print (f"Sorted list: {OOOOO0OOOO0OOO0O0}")#line:331
                        O0OO00O00O00000OO =CategoricalDtype (categories =OOOOO0OOOO0OOO0O0 ,ordered =True )#line:332
                        O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]]=O0O0O000O0O0000O0 [O0O0O000O0O0000O0 .columns [O0OO0OOO0OOO000OO ]].astype (O0OO00O00O00000OO )#line:333
                except :#line:336
                    if O0000OOOO0OOOO0O0 .verbosity ['debug']:#line:337
                        print ("...cannot extract numbers from all categories")#line:338
    print ("Automatically reordering numeric categories ...done")#line:340
    def _prep_data (O00O0000000000O00 ,OOO0OOO000O0OOO00 ):#line:342
        print ("Starting data preparation ...")#line:343
        O00O0000000000O00 ._init_data ()#line:344
        O00O0000000000O00 .stats ['start_prep_time']=time .time ()#line:345
        if O00O0000000000O00 .options ['automatic_data_conversions']:#line:346
            O00O0000000000O00 ._automatic_data_conversions (OOO0OOO000O0OOO00 )#line:347
        O00O0000000000O00 .data ["rows_count"]=OOO0OOO000O0OOO00 .shape [0 ]#line:348
        for OOOOO000O0OOOO000 in OOO0OOO000O0OOO00 .select_dtypes (exclude =['category']).columns :#line:349
            OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ]=OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ].apply (str )#line:350
        try :#line:351
            OOO0O000OOO0OO00O =pd .DataFrame .from_records ([(OOOOOO00O0OO00OOO ,OOO0OOO000O0OOO00 [OOOOOO00O0OO00OOO ].nunique ())for OOOOOO00O0OO00OOO in OOO0OOO000O0OOO00 .columns ],columns =['Column_Name','Num_Unique']).sort_values (by =['Num_Unique'])#line:353
        except :#line:354
            print ("Error in input data, probably unsupported data type. Will try to scan for column with unsupported type.")#line:355
            OOOOOO0000O0000OO =""#line:356
            try :#line:357
                for OOOOO000O0OOOO000 in OOO0OOO000O0OOO00 .columns :#line:358
                    OOOOOO0000O0000OO =OOOOO000O0OOOO000 #line:359
                    print (f"...column {OOOOO000O0OOOO000} has {int(OOO0OOO000O0OOO00[OOOOO000O0OOOO000].nunique())} values")#line:360
            except :#line:361
                print (f"... detected : column {OOOOOO0000O0000OO} has unsupported type: {type(OOO0OOO000O0OOO00[OOOOO000O0OOOO000])}.")#line:362
                exit (1 )#line:363
            print (f"Error in data profiling - attribute with unsupported type not detected. Please profile attributes manually, only simple attributes are supported.")#line:364
            exit (1 )#line:365
        if O00O0000000000O00 .verbosity ['hint']:#line:368
            print ("Quick profile of input data: unique value counts are:")#line:369
            print (OOO0O000OOO0OO00O )#line:370
            for OOOOO000O0OOOO000 in OOO0OOO000O0OOO00 .columns :#line:371
                if OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ].nunique ()<O00O0000000000O00 .options ['max_categories']:#line:372
                    OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ]=OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ].astype ('category')#line:373
                else :#line:374
                    print (f"WARNING: attribute {OOOOO000O0OOOO000} has more than {O00O0000000000O00.options['max_categories']} values, will be ignored.\r\n If you haven't set maximum number of categories and you really need more categories and you know what you are doing, please use max_categories option to increase allowed number of categories.")#line:375
                    del OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ]#line:376
        for OOOOO000O0OOOO000 in OOO0OOO000O0OOO00 .columns :#line:378
            if OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ].nunique ()>O00O0000000000O00 .options ['max_categories']:#line:379
                print (f"WARNING: attribute {OOOOO000O0OOOO000} has more than {O00O0000000000O00.options['max_categories']} values, will be ignored.\r\n If you haven't set maximum number of categories and you really need more categories and you know what you are doing, please use max_categories option to increase allowed number of categories.")#line:380
                del OOO0OOO000O0OOO00 [OOOOO000O0OOOO000 ]#line:381
        if O00O0000000000O00 .options ['keep_df']:#line:382
            if O00O0000000000O00 .verbosity ['debug']:#line:383
                print ("Keeping df.")#line:384
            O00O0000000000O00 .df =OOO0OOO000O0OOO00 #line:385
        print ("Encoding columns into bit-form...")#line:386
        OO0O0OO00O00OOOOO =0 #line:387
        OOO0OOO0OO0OOOOOO =0 #line:388
        for OOOO0OOOO00O0OO00 in OOO0OOO000O0OOO00 :#line:389
            if O00O0000000000O00 .verbosity ['debug']:#line:391
                print ('Column: '+OOOO0OOOO00O0OO00 )#line:392
            O00O0000000000O00 .data ["varname"].append (OOOO0OOOO00O0OO00 )#line:393
            O0O00OO0OOO0000O0 =pd .get_dummies (OOO0OOO000O0OOO00 [OOOO0OOOO00O0OO00 ])#line:394
            OO0OOOOOOOOO0OO00 =0 #line:395
            if (OOO0OOO000O0OOO00 .dtypes [OOOO0OOOO00O0OO00 ].name =='category'):#line:396
                OO0OOOOOOOOO0OO00 =1 #line:397
            O00O0000000000O00 .data ["vtypes"].append (OO0OOOOOOOOO0OO00 )#line:398
            O0O0O0O000OO00000 =0 #line:401
            OOO0O0O0OO00O0O00 =[]#line:402
            O000O0OO00O0O0OO0 =[]#line:403
            for O0OO0OO000O00OOO0 in O0O00OO0OOO0000O0 :#line:405
                if O00O0000000000O00 .verbosity ['debug']:#line:407
                    print ('....category : '+str (O0OO0OO000O00OOO0 )+" @ "+str (time .time ()))#line:408
                OOO0O0O0OO00O0O00 .append (O0OO0OO000O00OOO0 )#line:409
                OO000O000OOOO0OO0 =int (0 )#line:410
                O000O00O0OO0O000O =O0O00OO0OOO0000O0 [O0OO0OO000O00OOO0 ].values #line:411
                OOOO00OOOOO0O0OO0 =numpy .packbits (O000O00O0OO0O000O ,bitorder ='little')#line:413
                OO000O000OOOO0OO0 =int .from_bytes (OOOO00OOOOO0O0OO0 ,byteorder ='little')#line:414
                O000O0OO00O0O0OO0 .append (OO000O000OOOO0OO0 )#line:415
                O0O0O0O000OO00000 +=1 #line:433
                OOO0OOO0OO0OOOOOO +=1 #line:434
            O00O0000000000O00 .data ["catnames"].append (OOO0O0O0OO00O0O00 )#line:436
            O00O0000000000O00 .data ["dm"].append (O000O0OO00O0O0OO0 )#line:437
        print ("Encoding columns into bit-form...done")#line:439
        if O00O0000000000O00 .verbosity ['hint']:#line:440
            print (f"List of attributes for analysis is: {O00O0000000000O00.data['varname']}")#line:441
            print (f"List of category names for individual attributes is : {O00O0000000000O00.data['catnames']}")#line:442
        if O00O0000000000O00 .verbosity ['debug']:#line:443
            print (f"List of vtypes is (all should be 1) : {O00O0000000000O00.data['vtypes']}")#line:444
        O00O0000000000O00 .data ["data_prepared"]=1 #line:446
        print ("Data preparation finished.")#line:447
        if O00O0000000000O00 .verbosity ['debug']:#line:448
            print ('Number of variables : '+str (len (O00O0000000000O00 .data ["dm"])))#line:449
            print ('Total number of categories in all variables : '+str (OOO0OOO0OO0OOOOOO ))#line:450
        O00O0000000000O00 .stats ['end_prep_time']=time .time ()#line:451
        if O00O0000000000O00 .verbosity ['debug']:#line:452
            print ('Time needed for data preparation : ',str (O00O0000000000O00 .stats ['end_prep_time']-O00O0000000000O00 .stats ['start_prep_time']))#line:453
    def _bitcount (O0000OO0OOOO0OO00 ,O0O00000OO000000O ):#line:455
        OO00O0O0OOOO0O00O =None #line:456
        if (O0000OO0OOOO0OO00 ._is_py310 ):#line:457
            OO00O0O0OOOO0O00O =O0O00000OO000000O .bit_count ()#line:458
        else :#line:459
            OO00O0O0OOOO0O00O =bin (O0O00000OO000000O ).count ("1")#line:460
        return OO00O0O0OOOO0O00O #line:461
    def _verifyCF (O0O0O00000OOO0O0O ,_O0O0O00OO0OOO0000 ):#line:464
        O000O00000OO0OO00 =O0O0O00000OOO0O0O ._bitcount (_O0O0O00OO0OOO0000 )#line:465
        OO0OOOOO0OO0OO0O0 =[]#line:466
        O0OO0O000O00OO00O =[]#line:467
        OOO00O0O0O000OOOO =0 #line:468
        O00OO00OOOOO0O0OO =0 #line:469
        O0O0O0OO0O00OO0O0 =0 #line:470
        OOO00OOOOOO0OOO00 =0 #line:471
        OOO00O00000OO00OO =0 #line:472
        OOOO0OO0O0OOOOO0O =0 #line:473
        OO0000O0000OOO0O0 =0 #line:474
        O0O000O0OOOO0OOOO =0 #line:475
        OOOOOO00OOO000000 =0 #line:476
        O00O0000O0O0O000O =None #line:477
        OO0OOO0O0000O0OOO =None #line:478
        O0OOO0000O0O000O0 =None #line:479
        if ('min_step_size'in O0O0O00000OOO0O0O .quantifiers ):#line:480
            O00O0000O0O0O000O =O0O0O00000OOO0O0O .quantifiers .get ('min_step_size')#line:481
        if ('min_rel_step_size'in O0O0O00000OOO0O0O .quantifiers ):#line:482
            OO0OOO0O0000O0OOO =O0O0O00000OOO0O0O .quantifiers .get ('min_rel_step_size')#line:483
            if OO0OOO0O0000O0OOO >=1 and OO0OOO0O0000O0OOO <100 :#line:484
                OO0OOO0O0000O0OOO =OO0OOO0O0000O0OOO /100 #line:485
        O0O0O00OOOOO0OOO0 =0 #line:486
        OO0OO0O00OO0000OO =0 #line:487
        O00O0OOOOOOO0OOOO =[]#line:488
        if ('aad_weights'in O0O0O00000OOO0O0O .quantifiers ):#line:489
            O0O0O00OOOOO0OOO0 =1 #line:490
            OOOOO0O0OOO00O0OO =[]#line:491
            O00O0OOOOOOO0OOOO =O0O0O00000OOO0O0O .quantifiers .get ('aad_weights')#line:492
        OO0OOO0O00O000O00 =O0O0O00000OOO0O0O .data ["dm"][O0O0O00000OOO0O0O .data ["varname"].index (O0O0O00000OOO0O0O .kwargs .get ('target'))]#line:493
        def OOO0000OOOOO00OOO (OO0000O0OOO0O000O ,O0OO00000O0OO0OOO ):#line:494
            OOOOOO0OOO00O0O00 =True #line:495
            if (OO0000O0OOO0O000O >O0OO00000O0OO0OOO ):#line:496
                if not (O00O0000O0O0O000O is None or OO0000O0OOO0O000O >=O0OO00000O0OO0OOO +O00O0000O0O0O000O ):#line:497
                    OOOOOO0OOO00O0O00 =False #line:498
                if not (OO0OOO0O0000O0OOO is None or OO0000O0OOO0O000O >=O0OO00000O0OO0OOO *(1 +OO0OOO0O0000O0OOO )):#line:499
                    OOOOOO0OOO00O0O00 =False #line:500
            if (OO0000O0OOO0O000O <O0OO00000O0OO0OOO ):#line:501
                if not (O00O0000O0O0O000O is None or OO0000O0OOO0O000O <=O0OO00000O0OO0OOO -O00O0000O0O0O000O ):#line:502
                    OOOOOO0OOO00O0O00 =False #line:503
                if not (OO0OOO0O0000O0OOO is None or OO0000O0OOO0O000O <=O0OO00000O0OO0OOO *(1 -OO0OOO0O0000O0OOO )):#line:504
                    OOOOOO0OOO00O0O00 =False #line:505
            return OOOOOO0OOO00O0O00 #line:506
        for O00O00OOOOOOO0O00 in range (len (OO0OOO0O00O000O00 )):#line:507
            O00OO00OOOOO0O0OO =OOO00O0O0O000OOOO #line:509
            OOO00O0O0O000OOOO =O0O0O00000OOO0O0O ._bitcount (_O0O0O00OO0OOO0000 &OO0OOO0O00O000O00 [O00O00OOOOOOO0O00 ])#line:510
            OO0OOOOO0OO0OO0O0 .append (OOO00O0O0O000OOOO )#line:511
            if O00O00OOOOOOO0O00 >0 :#line:512
                if (OOO00O0O0O000OOOO >O00OO00OOOOO0O0OO ):#line:513
                    if (O0O0O0OO0O00OO0O0 ==1 )and (OOO0000OOOOO00OOO (OOO00O0O0O000OOOO ,O00OO00OOOOO0O0OO )):#line:514
                        O0O000O0OOOO0OOOO +=1 #line:515
                    else :#line:516
                        if OOO0000OOOOO00OOO (OOO00O0O0O000OOOO ,O00OO00OOOOO0O0OO ):#line:517
                            O0O000O0OOOO0OOOO =1 #line:518
                        else :#line:519
                            O0O000O0OOOO0OOOO =0 #line:520
                    if O0O000O0OOOO0OOOO >OOO00OOOOOO0OOO00 :#line:521
                        OOO00OOOOOO0OOO00 =O0O000O0OOOO0OOOO #line:522
                    O0O0O0OO0O00OO0O0 =1 #line:523
                    if OOO0000OOOOO00OOO (OOO00O0O0O000OOOO ,O00OO00OOOOO0O0OO ):#line:524
                        OOOO0OO0O0OOOOO0O +=1 #line:525
                if (OOO00O0O0O000OOOO <O00OO00OOOOO0O0OO ):#line:526
                    if (O0O0O0OO0O00OO0O0 ==-1 )and (OOO0000OOOOO00OOO (OOO00O0O0O000OOOO ,O00OO00OOOOO0O0OO )):#line:527
                        OOOOOO00OOO000000 +=1 #line:528
                    else :#line:529
                        if OOO0000OOOOO00OOO (OOO00O0O0O000OOOO ,O00OO00OOOOO0O0OO ):#line:530
                            OOOOOO00OOO000000 =1 #line:531
                        else :#line:532
                            OOOOOO00OOO000000 =0 #line:533
                    if OOOOOO00OOO000000 >OOO00O00000OO00OO :#line:534
                        OOO00O00000OO00OO =OOOOOO00OOO000000 #line:535
                    O0O0O0OO0O00OO0O0 =-1 #line:536
                    if OOO0000OOOOO00OOO (OOO00O0O0O000OOOO ,O00OO00OOOOO0O0OO ):#line:537
                        OO0000O0000OOO0O0 +=1 #line:538
                if (OOO00O0O0O000OOOO ==O00OO00OOOOO0O0OO ):#line:539
                    O0O0O0OO0O00OO0O0 =0 #line:540
                    OOOOOO00OOO000000 =0 #line:541
                    O0O000O0OOOO0OOOO =0 #line:542
            if (O0O0O00OOOOO0OOO0 ):#line:544
                O0OOO0000O00OOOO0 =O0O0O00000OOO0O0O ._bitcount (OO0OOO0O00O000O00 [O00O00OOOOOOO0O00 ])#line:545
                OOOOO0O0OOO00O0OO .append (O0OOO0000O00OOOO0 )#line:546
        if (O0O0O00OOOOO0OOO0 &sum (OO0OOOOO0OO0OO0O0 )>0 ):#line:548
            for O00O00OOOOOOO0O00 in range (len (OO0OOO0O00O000O00 )):#line:549
                if OOOOO0O0OOO00O0OO [O00O00OOOOOOO0O00 ]>0 :#line:550
                    if OO0OOOOO0OO0OO0O0 [O00O00OOOOOOO0O00 ]/sum (OO0OOOOO0OO0OO0O0 )>OOOOO0O0OOO00O0OO [O00O00OOOOOOO0O00 ]/sum (OOOOO0O0OOO00O0OO ):#line:552
                        OO0OO0O00OO0000OO +=O00O0OOOOOOO0OOOO [O00O00OOOOOOO0O00 ]*((OO0OOOOO0OO0OO0O0 [O00O00OOOOOOO0O00 ]/sum (OO0OOOOO0OO0OO0O0 ))/(OOOOO0O0OOO00O0OO [O00O00OOOOOOO0O00 ]/sum (OOOOO0O0OOO00O0OO ))-1 )#line:553
        O0O0O0OO000OOOOOO =True #line:556
        for OO0000OO0OOOOOOOO in O0O0O00000OOO0O0O .quantifiers .keys ():#line:557
            if OO0000OO0OOOOOOOO .upper ()=='BASE':#line:558
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=O000O00000OO0OO00 )#line:559
            if OO0000OO0OOOOOOOO .upper ()=='RELBASE':#line:560
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=O000O00000OO0OO00 *1.0 /O0O0O00000OOO0O0O .data ["rows_count"])#line:561
            if OO0000OO0OOOOOOOO .upper ()=='S_UP':#line:562
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=OOO00OOOOOO0OOO00 )#line:563
            if OO0000OO0OOOOOOOO .upper ()=='S_DOWN':#line:564
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=OOO00O00000OO00OO )#line:565
            if OO0000OO0OOOOOOOO .upper ()=='S_ANY_UP':#line:566
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=OOO00OOOOOO0OOO00 )#line:567
            if OO0000OO0OOOOOOOO .upper ()=='S_ANY_DOWN':#line:568
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=OOO00O00000OO00OO )#line:569
            if OO0000OO0OOOOOOOO .upper ()=='MAX':#line:570
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=max (OO0OOOOO0OO0OO0O0 ))#line:571
            if OO0000OO0OOOOOOOO .upper ()=='MIN':#line:572
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=min (OO0OOOOO0OO0OO0O0 ))#line:573
            if OO0000OO0OOOOOOOO .upper ()=='RELMAX':#line:574
                if sum (OO0OOOOO0OO0OO0O0 )>0 :#line:575
                    O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=max (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 ))#line:576
                else :#line:577
                    O0O0O0OO000OOOOOO =False #line:578
            if OO0000OO0OOOOOOOO .upper ()=='RELMAX_LEQ':#line:579
                if sum (OO0OOOOO0OO0OO0O0 )>0 :#line:580
                    O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )>=max (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 ))#line:581
                else :#line:582
                    O0O0O0OO000OOOOOO =False #line:583
            if OO0000OO0OOOOOOOO .upper ()=='RELMIN':#line:584
                if sum (OO0OOOOO0OO0OO0O0 )>0 :#line:585
                    O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=min (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 ))#line:586
                else :#line:587
                    O0O0O0OO000OOOOOO =False #line:588
            if OO0000OO0OOOOOOOO .upper ()=='RELMIN_LEQ':#line:589
                if sum (OO0OOOOO0OO0OO0O0 )>0 :#line:590
                    O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )>=min (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 ))#line:591
                else :#line:592
                    O0O0O0OO000OOOOOO =False #line:593
            if OO0000OO0OOOOOOOO .upper ()=='AAD':#line:594
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )<=OO0OO0O00OO0000OO )#line:595
            if OO0000OO0OOOOOOOO .upper ()=='RELRANGE_LEQ':#line:597
                OO0O0O0O000O0O0O0 =O0O0O00000OOO0O0O .quantifiers .get (OO0000OO0OOOOOOOO )#line:598
                if OO0O0O0O000O0O0O0 >=1 and OO0O0O0O000O0O0O0 <100 :#line:599
                    OO0O0O0O000O0O0O0 =OO0O0O0O000O0O0O0 *1.0 /100 #line:600
                O0000000OOO00OO00 =min (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 )#line:601
                OO0O00OO00O0OO0O0 =max (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 )#line:602
                O0O0O0OO000OOOOOO =O0O0O0OO000OOOOOO and (OO0O0O0O000O0O0O0 >=OO0O00OO00O0OO0O0 -O0000000OOO00OO00 )#line:603
        OOO0OO000O000OOO0 ={}#line:604
        if O0O0O0OO000OOOOOO ==True :#line:605
            O0O0O00000OOO0O0O .stats ['total_valid']+=1 #line:607
            OOO0OO000O000OOO0 ["base"]=O000O00000OO0OO00 #line:608
            OOO0OO000O000OOO0 ["rel_base"]=O000O00000OO0OO00 *1.0 /O0O0O00000OOO0O0O .data ["rows_count"]#line:609
            OOO0OO000O000OOO0 ["s_up"]=OOO00OOOOOO0OOO00 #line:610
            OOO0OO000O000OOO0 ["s_down"]=OOO00O00000OO00OO #line:611
            OOO0OO000O000OOO0 ["s_any_up"]=OOOO0OO0O0OOOOO0O #line:612
            OOO0OO000O000OOO0 ["s_any_down"]=OO0000O0000OOO0O0 #line:613
            OOO0OO000O000OOO0 ["max"]=max (OO0OOOOO0OO0OO0O0 )#line:614
            OOO0OO000O000OOO0 ["min"]=min (OO0OOOOO0OO0OO0O0 )#line:615
            if sum (OO0OOOOO0OO0OO0O0 )>0 :#line:618
                OOO0OO000O000OOO0 ["rel_max"]=max (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 )#line:619
                OOO0OO000O000OOO0 ["rel_min"]=min (OO0OOOOO0OO0OO0O0 )*1.0 /sum (OO0OOOOO0OO0OO0O0 )#line:620
            else :#line:621
                OOO0OO000O000OOO0 ["rel_max"]=0 #line:622
                OOO0OO000O000OOO0 ["rel_min"]=0 #line:623
            OOO0OO000O000OOO0 ["hist"]=OO0OOOOO0OO0OO0O0 #line:624
            if O0O0O00OOOOO0OOO0 :#line:625
                OOO0OO000O000OOO0 ["aad"]=OO0OO0O00OO0000OO #line:626
                OOO0OO000O000OOO0 ["hist_full"]=OOOOO0O0OOO00O0OO #line:627
                OOO0OO000O000OOO0 ["rel_hist"]=[OOO0OOOOOO000O000 /sum (OO0OOOOO0OO0OO0O0 )for OOO0OOOOOO000O000 in OO0OOOOO0OO0OO0O0 ]#line:628
                OOO0OO000O000OOO0 ["rel_hist_full"]=[O00OO0O00000000OO /sum (OOOOO0O0OOO00O0OO )for O00OO0O00000000OO in OOOOO0O0OOO00O0OO ]#line:629
        return O0O0O0OO000OOOOOO ,OOO0OO000O000OOO0 #line:631
    def _verifyUIC (OO0O0OO0OOO00OOOO ,_OO00OOO00000OO0OO ):#line:633
        O000O0OOOOO0OOO00 ={}#line:634
        O0O00OOO0OO000OO0 =0 #line:635
        for O0O0O0O00O00O00OO in OO0O0OO0OOO00OOOO .task_actinfo ['cedents']:#line:636
            O000O0OOOOO0OOO00 [O0O0O0O00O00O00OO ['cedent_type']]=O0O0O0O00O00O00OO ['filter_value']#line:638
            O0O00OOO0OO000OO0 =O0O00OOO0OO000OO0 +1 #line:639
        O000O00OO00O0O000 =OO0O0OO0OOO00OOOO ._bitcount (_OO00OOO00000OO0OO )#line:641
        O0OO00O00000OO000 =[]#line:642
        OOO0OOO000O0OOOO0 =0 #line:643
        OOO0O000O0O00000O =0 #line:644
        O000OOOOO00OO0O0O =0 #line:645
        OO0O0000OO0OO0O0O =[]#line:646
        OO0O000O0OOO000OO =[]#line:647
        if ('aad_weights'in OO0O0OO0OOO00OOOO .quantifiers ):#line:648
            OO0O0000OO0OO0O0O =OO0O0OO0OOO00OOOO .quantifiers .get ('aad_weights')#line:649
            OOO0O000O0O00000O =1 #line:650
        O000OO00OO0OOOOOO =OO0O0OO0OOO00OOOO .data ["dm"][OO0O0OO0OOO00OOOO .data ["varname"].index (OO0O0OO0OOO00OOOO .kwargs .get ('target'))]#line:651
        for O000OO0O0O0OO0OO0 in range (len (O000OO00OO0OOOOOO )):#line:652
            O000O000O00O0O00O =OOO0OOO000O0OOOO0 #line:654
            OOO0OOO000O0OOOO0 =OO0O0OO0OOO00OOOO ._bitcount (_OO00OOO00000OO0OO &O000OO00OO0OOOOOO [O000OO0O0O0OO0OO0 ])#line:655
            O0OO00O00000OO000 .append (OOO0OOO000O0OOOO0 )#line:656
            OO0O0000000O0OOO0 =OO0O0OO0OOO00OOOO ._bitcount (O000O0OOOOO0OOO00 ['cond']&O000OO00OO0OOOOOO [O000OO0O0O0OO0OO0 ])#line:659
            OO0O000O0OOO000OO .append (OO0O0000000O0OOO0 )#line:660
        if (OOO0O000O0O00000O &sum (O0OO00O00000OO000 )>0 ):#line:662
            for O000OO0O0O0OO0OO0 in range (len (O000OO00OO0OOOOOO )):#line:663
                if OO0O000O0OOO000OO [O000OO0O0O0OO0OO0 ]>0 :#line:664
                    if O0OO00O00000OO000 [O000OO0O0O0OO0OO0 ]/sum (O0OO00O00000OO000 )>OO0O000O0OOO000OO [O000OO0O0O0OO0OO0 ]/sum (OO0O000O0OOO000OO ):#line:666
                        O000OOOOO00OO0O0O +=OO0O0000OO0OO0O0O [O000OO0O0O0OO0OO0 ]*((O0OO00O00000OO000 [O000OO0O0O0OO0OO0 ]/sum (O0OO00O00000OO000 ))/(OO0O000O0OOO000OO [O000OO0O0O0OO0OO0 ]/sum (OO0O000O0OOO000OO ))-1 )#line:667
        OO00OO0O0O0OO0O00 =True #line:670
        for O0OO0OOOO0O0O0O00 in OO0O0OO0OOO00OOOO .quantifiers .keys ():#line:671
            if O0OO0OOOO0O0O0O00 .upper ()=='BASE':#line:672
                OO00OO0O0O0OO0O00 =OO00OO0O0O0OO0O00 and (OO0O0OO0OOO00OOOO .quantifiers .get (O0OO0OOOO0O0O0O00 )<=O000O00OO00O0O000 )#line:673
            if O0OO0OOOO0O0O0O00 .upper ()=='RELBASE':#line:674
                OO00OO0O0O0OO0O00 =OO00OO0O0O0OO0O00 and (OO0O0OO0OOO00OOOO .quantifiers .get (O0OO0OOOO0O0O0O00 )<=O000O00OO00O0O000 *1.0 /OO0O0OO0OOO00OOOO .data ["rows_count"])#line:675
            if O0OO0OOOO0O0O0O00 .upper ()=='AAD_SCORE':#line:676
                OO00OO0O0O0OO0O00 =OO00OO0O0O0OO0O00 and (OO0O0OO0OOO00OOOO .quantifiers .get (O0OO0OOOO0O0O0O00 )<=O000OOOOO00OO0O0O )#line:677
        O0OOOO0OOO0OOO0OO ={}#line:679
        if OO00OO0O0O0OO0O00 ==True :#line:680
            OO0O0OO0OOO00OOOO .stats ['total_valid']+=1 #line:682
            O0OOOO0OOO0OOO0OO ["base"]=O000O00OO00O0O000 #line:683
            O0OOOO0OOO0OOO0OO ["rel_base"]=O000O00OO00O0O000 *1.0 /OO0O0OO0OOO00OOOO .data ["rows_count"]#line:684
            O0OOOO0OOO0OOO0OO ["hist"]=O0OO00O00000OO000 #line:685
            O0OOOO0OOO0OOO0OO ["aad_score"]=O000OOOOO00OO0O0O #line:687
            O0OOOO0OOO0OOO0OO ["hist_cond"]=OO0O000O0OOO000OO #line:688
            O0OOOO0OOO0OOO0OO ["rel_hist"]=[OOO0OOO00OOO000OO /sum (O0OO00O00000OO000 )for OOO0OOO00OOO000OO in O0OO00O00000OO000 ]#line:689
            O0OOOO0OOO0OOO0OO ["rel_hist_cond"]=[O0OOO0OO0O0000OO0 /sum (OO0O000O0OOO000OO )for O0OOO0OO0O0000OO0 in OO0O000O0OOO000OO ]#line:690
        return OO00OO0O0O0OO0O00 ,O0OOOO0OOO0OOO0OO #line:692
    def _verify4ft (O0OOO00OOO00O00O0 ,_O0O00O0OO0000O0O0 ):#line:694
        O000O0OO0OOOO0000 ={}#line:695
        OO00000OOOOO0O0OO =0 #line:696
        for OOO0OOO0OO0OO000O in O0OOO00OOO00O00O0 .task_actinfo ['cedents']:#line:697
            O000O0OO0OOOO0000 [OOO0OOO0OO0OO000O ['cedent_type']]=OOO0OOO0OO0OO000O ['filter_value']#line:699
            OO00000OOOOO0O0OO =OO00000OOOOO0O0OO +1 #line:700
        O0O000000O000000O =O0OOO00OOO00O00O0 ._bitcount (O000O0OO0OOOO0000 ['ante']&O000O0OO0OOOO0000 ['succ']&O000O0OO0OOOO0000 ['cond'])#line:702
        O00OOOO00O0OOOOO0 =None #line:703
        O00OOOO00O0OOOOO0 =0 #line:704
        if O0O000000O000000O >0 :#line:713
            O00OOOO00O0OOOOO0 =O0OOO00OOO00O00O0 ._bitcount (O000O0OO0OOOO0000 ['ante']&O000O0OO0OOOO0000 ['succ']&O000O0OO0OOOO0000 ['cond'])*1.0 /O0OOO00OOO00O00O0 ._bitcount (O000O0OO0OOOO0000 ['ante']&O000O0OO0OOOO0000 ['cond'])#line:714
        O0O00O0O0OO0OOO00 =1 <<O0OOO00OOO00O00O0 .data ["rows_count"]#line:716
        OO00O00O00000000O =O0OOO00OOO00O00O0 ._bitcount (O000O0OO0OOOO0000 ['ante']&O000O0OO0OOOO0000 ['succ']&O000O0OO0OOOO0000 ['cond'])#line:717
        OO00OOOOO00O0OO00 =O0OOO00OOO00O00O0 ._bitcount (O000O0OO0OOOO0000 ['ante']&~(O0O00O0O0OO0OOO00 |O000O0OO0OOOO0000 ['succ'])&O000O0OO0OOOO0000 ['cond'])#line:718
        OOO0OOO0OO0OO000O =O0OOO00OOO00O00O0 ._bitcount (~(O0O00O0O0OO0OOO00 |O000O0OO0OOOO0000 ['ante'])&O000O0OO0OOOO0000 ['succ']&O000O0OO0OOOO0000 ['cond'])#line:719
        OO0OOOO0OOOO0OO0O =O0OOO00OOO00O00O0 ._bitcount (~(O0O00O0O0OO0OOO00 |O000O0OO0OOOO0000 ['ante'])&~(O0O00O0O0OO0OOO00 |O000O0OO0OOOO0000 ['succ'])&O000O0OO0OOOO0000 ['cond'])#line:720
        O0OOO00OO0000OO00 =0 #line:721
        if (OO00O00O00000000O +OO00OOOOO00O0OO00 )*(OO00O00O00000000O +OOO0OOO0OO0OO000O )>0 :#line:722
            O0OOO00OO0000OO00 =OO00O00O00000000O *(OO00O00O00000000O +OO00OOOOO00O0OO00 +OOO0OOO0OO0OO000O +OO0OOOO0OOOO0OO0O )/(OO00O00O00000000O +OO00OOOOO00O0OO00 )/(OO00O00O00000000O +OOO0OOO0OO0OO000O )-1 #line:723
        else :#line:724
            O0OOO00OO0000OO00 =None #line:725
        O00000OOOO00O00OO =0 #line:726
        if (OO00O00O00000000O +OO00OOOOO00O0OO00 )*(OO00O00O00000000O +OOO0OOO0OO0OO000O )>0 :#line:727
            O00000OOOO00O00OO =1 -OO00O00O00000000O *(OO00O00O00000000O +OO00OOOOO00O0OO00 +OOO0OOO0OO0OO000O +OO0OOOO0OOOO0OO0O )/(OO00O00O00000000O +OO00OOOOO00O0OO00 )/(OO00O00O00000000O +OOO0OOO0OO0OO000O )#line:728
        else :#line:729
            O00000OOOO00O00OO =None #line:730
        O0O0OO0O0O0OO0OO0 =True #line:731
        for OOOO00O0OO0OO000O in O0OOO00OOO00O00O0 .quantifiers .keys ():#line:732
            if OOOO00O0OO0OO000O .upper ()=='BASE':#line:733
                O0O0OO0O0O0OO0OO0 =O0O0OO0O0O0OO0OO0 and (O0OOO00OOO00O00O0 .quantifiers .get (OOOO00O0OO0OO000O )<=O0O000000O000000O )#line:734
            if OOOO00O0OO0OO000O .upper ()=='RELBASE':#line:735
                O0O0OO0O0O0OO0OO0 =O0O0OO0O0O0OO0OO0 and (O0OOO00OOO00O00O0 .quantifiers .get (OOOO00O0OO0OO000O )<=O0O000000O000000O *1.0 /O0OOO00OOO00O00O0 .data ["rows_count"])#line:736
            if (OOOO00O0OO0OO000O .upper ()=='PIM')or (OOOO00O0OO0OO000O .upper ()=='CONF'):#line:737
                O0O0OO0O0O0OO0OO0 =O0O0OO0O0O0OO0OO0 and (O0OOO00OOO00O00O0 .quantifiers .get (OOOO00O0OO0OO000O )<=O00OOOO00O0OOOOO0 )#line:738
            if OOOO00O0OO0OO000O .upper ()=='AAD':#line:739
                if O0OOO00OO0000OO00 !=None :#line:740
                    O0O0OO0O0O0OO0OO0 =O0O0OO0O0O0OO0OO0 and (O0OOO00OOO00O00O0 .quantifiers .get (OOOO00O0OO0OO000O )<=O0OOO00OO0000OO00 )#line:741
                else :#line:742
                    O0O0OO0O0O0OO0OO0 =False #line:743
            if OOOO00O0OO0OO000O .upper ()=='BAD':#line:744
                if O00000OOOO00O00OO !=None :#line:745
                    O0O0OO0O0O0OO0OO0 =O0O0OO0O0O0OO0OO0 and (O0OOO00OOO00O00O0 .quantifiers .get (OOOO00O0OO0OO000O )<=O00000OOOO00O00OO )#line:746
                else :#line:747
                    O0O0OO0O0O0OO0OO0 =False #line:748
            O0O0O00OOO0O0OOOO ={}#line:749
        if O0O0OO0O0O0OO0OO0 ==True :#line:750
            O0OOO00OOO00O00O0 .stats ['total_valid']+=1 #line:752
            O0O0O00OOO0O0OOOO ["base"]=O0O000000O000000O #line:753
            O0O0O00OOO0O0OOOO ["rel_base"]=O0O000000O000000O *1.0 /O0OOO00OOO00O00O0 .data ["rows_count"]#line:754
            O0O0O00OOO0O0OOOO ["conf"]=O00OOOO00O0OOOOO0 #line:755
            O0O0O00OOO0O0OOOO ["aad"]=O0OOO00OO0000OO00 #line:756
            O0O0O00OOO0O0OOOO ["bad"]=O00000OOOO00O00OO #line:757
            O0O0O00OOO0O0OOOO ["fourfold"]=[OO00O00O00000000O ,OO00OOOOO00O0OO00 ,OOO0OOO0OO0OO000O ,OO0OOOO0OOOO0OO0O ]#line:758
        return O0O0OO0O0O0OO0OO0 ,O0O0O00OOO0O0OOOO #line:762
    def _verifysd4ft (OO00OOOOOOO000O0O ,_OO000OO0O0O0O00OO ):#line:764
        OO000000O0000OOO0 ={}#line:765
        OO00OOOO0OO00OOO0 =0 #line:766
        for OO0000O0OO0000O0O in OO00OOOOOOO000O0O .task_actinfo ['cedents']:#line:767
            OO000000O0000OOO0 [OO0000O0OO0000O0O ['cedent_type']]=OO0000O0OO0000O0O ['filter_value']#line:769
            OO00OOOO0OO00OOO0 =OO00OOOO0OO00OOO0 +1 #line:770
        O0OOO0O0000OO0O00 =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])#line:772
        O0O0OOOOOO00OOO0O =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])#line:773
        O00OOOO00O0OOO0O0 =None #line:774
        O000OO0OOOOOOO0OO =0 #line:775
        O0000O0OO0OOO0000 =0 #line:776
        if O0OOO0O0000OO0O00 >0 :#line:785
            O000OO0OOOOOOO0OO =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])*1.0 /OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])#line:786
        if O0O0OOOOOO00OOO0O >0 :#line:787
            O0000O0OO0OOO0000 =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])*1.0 /OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])#line:788
        OO0OOOOOOO00O0000 =1 <<OO00OOOOOOO000O0O .data ["rows_count"]#line:790
        O0OOO00OO0O0OOOOO =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])#line:791
        OO0O0000OOO00O0O0 =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['succ'])&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])#line:792
        OO0O0O00O000OOOOO =OO00OOOOOOO000O0O ._bitcount (~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['ante'])&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])#line:793
        OO0O0O0OO0OOO0OO0 =OO00OOOOOOO000O0O ._bitcount (~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['ante'])&~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['succ'])&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['frst'])#line:794
        OOOOOO0O0O00O0O0O =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])#line:795
        OOOO0OO0OO0OO0O00 =OO00OOOOOOO000O0O ._bitcount (OO000000O0000OOO0 ['ante']&~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['succ'])&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])#line:796
        O00O0O0000OO0O0O0 =OO00OOOOOOO000O0O ._bitcount (~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['ante'])&OO000000O0000OOO0 ['succ']&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])#line:797
        O000O0OO0OO0000OO =OO00OOOOOOO000O0O ._bitcount (~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['ante'])&~(OO0OOOOOOO00O0000 |OO000000O0000OOO0 ['succ'])&OO000000O0000OOO0 ['cond']&OO000000O0000OOO0 ['scnd'])#line:798
        O00OOOO000O0OOOOO =True #line:799
        for O000O000OOO00O00O in OO00OOOOOOO000O0O .quantifiers .keys ():#line:800
            if (O000O000OOO00O00O .upper ()=='FRSTBASE')|(O000O000OOO00O00O .upper ()=='BASE1'):#line:801
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O0OOO0O0000OO0O00 )#line:802
            if (O000O000OOO00O00O .upper ()=='SCNDBASE')|(O000O000OOO00O00O .upper ()=='BASE2'):#line:803
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O0O0OOOOOO00OOO0O )#line:804
            if (O000O000OOO00O00O .upper ()=='FRSTRELBASE')|(O000O000OOO00O00O .upper ()=='RELBASE1'):#line:805
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O0OOO0O0000OO0O00 *1.0 /OO00OOOOOOO000O0O .data ["rows_count"])#line:806
            if (O000O000OOO00O00O .upper ()=='SCNDRELBASE')|(O000O000OOO00O00O .upper ()=='RELBASE2'):#line:807
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O0O0OOOOOO00OOO0O *1.0 /OO00OOOOOOO000O0O .data ["rows_count"])#line:808
            if (O000O000OOO00O00O .upper ()=='FRSTPIM')|(O000O000OOO00O00O .upper ()=='PIM1')|(O000O000OOO00O00O .upper ()=='FRSTCONF')|(O000O000OOO00O00O .upper ()=='CONF1'):#line:809
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O000OO0OOOOOOO0OO )#line:810
            if (O000O000OOO00O00O .upper ()=='SCNDPIM')|(O000O000OOO00O00O .upper ()=='PIM2')|(O000O000OOO00O00O .upper ()=='SCNDCONF')|(O000O000OOO00O00O .upper ()=='CONF2'):#line:811
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O0000O0OO0OOO0000 )#line:812
            if (O000O000OOO00O00O .upper ()=='DELTAPIM')|(O000O000OOO00O00O .upper ()=='DELTACONF'):#line:813
                O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O000OO0OOOOOOO0OO -O0000O0OO0OOO0000 )#line:814
            if (O000O000OOO00O00O .upper ()=='RATIOPIM')|(O000O000OOO00O00O .upper ()=='RATIOCONF'):#line:817
                if (O0000O0OO0OOO0000 >0 ):#line:818
                    O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )<=O000OO0OOOOOOO0OO *1.0 /O0000O0OO0OOO0000 )#line:819
                else :#line:820
                    O00OOOO000O0OOOOO =False #line:821
            if (O000O000OOO00O00O .upper ()=='RATIOPIM_LEQ')|(O000O000OOO00O00O .upper ()=='RATIOCONF_LEQ'):#line:822
                if (O0000O0OO0OOO0000 >0 ):#line:823
                    O00OOOO000O0OOOOO =O00OOOO000O0OOOOO and (OO00OOOOOOO000O0O .quantifiers .get (O000O000OOO00O00O )>=O000OO0OOOOOOO0OO *1.0 /O0000O0OO0OOO0000 )#line:824
                else :#line:825
                    O00OOOO000O0OOOOO =False #line:826
        O00OO0O00O0O0O000 ={}#line:827
        if O00OOOO000O0OOOOO ==True :#line:828
            OO00OOOOOOO000O0O .stats ['total_valid']+=1 #line:830
            O00OO0O00O0O0O000 ["base1"]=O0OOO0O0000OO0O00 #line:831
            O00OO0O00O0O0O000 ["base2"]=O0O0OOOOOO00OOO0O #line:832
            O00OO0O00O0O0O000 ["rel_base1"]=O0OOO0O0000OO0O00 *1.0 /OO00OOOOOOO000O0O .data ["rows_count"]#line:833
            O00OO0O00O0O0O000 ["rel_base2"]=O0O0OOOOOO00OOO0O *1.0 /OO00OOOOOOO000O0O .data ["rows_count"]#line:834
            O00OO0O00O0O0O000 ["conf1"]=O000OO0OOOOOOO0OO #line:835
            O00OO0O00O0O0O000 ["conf2"]=O0000O0OO0OOO0000 #line:836
            O00OO0O00O0O0O000 ["deltaconf"]=O000OO0OOOOOOO0OO -O0000O0OO0OOO0000 #line:837
            if (O0000O0OO0OOO0000 >0 ):#line:838
                O00OO0O00O0O0O000 ["ratioconf"]=O000OO0OOOOOOO0OO *1.0 /O0000O0OO0OOO0000 #line:839
            else :#line:840
                O00OO0O00O0O0O000 ["ratioconf"]=None #line:841
            O00OO0O00O0O0O000 ["fourfold1"]=[O0OOO00OO0O0OOOOO ,OO0O0000OOO00O0O0 ,OO0O0O00O000OOOOO ,OO0O0O0OO0OOO0OO0 ]#line:842
            O00OO0O00O0O0O000 ["fourfold2"]=[OOOOOO0O0O00O0O0O ,OOOO0OO0OO0OO0O00 ,O00O0O0000OO0O0O0 ,O000O0OO0OO0000OO ]#line:843
        return O00OOOO000O0OOOOO ,O00OO0O00O0O0O000 #line:847
    def _verifynewact4ft (O00O0OO000OO00000 ,_OO0O0O0O00OO00000 ):#line:849
        O0000OO0O0OOO0000 ={}#line:850
        for OOOOO00OO0OOOOOO0 in O00O0OO000OO00000 .task_actinfo ['cedents']:#line:851
            O0000OO0O0OOO0000 [OOOOO00OO0OOOOOO0 ['cedent_type']]=OOOOO00OO0OOOOOO0 ['filter_value']#line:853
        O0O0OOO00O00OO00O =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond'])#line:855
        OOO000000O00O00OO =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond']&O0000OO0O0OOO0000 ['antv']&O0000OO0O0OOO0000 ['sucv'])#line:856
        O0OOOO0000O00OO0O =None #line:857
        OOOO0OOOOOOO0O0O0 =0 #line:858
        OOOOOOOOOOOOO0OOO =0 #line:859
        if O0O0OOO00O00OO00O >0 :#line:868
            OOOO0OOOOOOO0O0O0 =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond'])*1.0 /O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['cond'])#line:869
        if OOO000000O00O00OO >0 :#line:870
            OOOOOOOOOOOOO0OOO =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond']&O0000OO0O0OOO0000 ['antv']&O0000OO0O0OOO0000 ['sucv'])*1.0 /O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['cond']&O0000OO0O0OOO0000 ['antv'])#line:872
        OOO0O0O000O00OO00 =1 <<O00O0OO000OO00000 .rows_count #line:874
        O000OO0O0OO0OO000 =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond'])#line:875
        O0O0OO000OO0000OO =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&~(OOO0O0O000O00OO00 |O0000OO0O0OOO0000 ['succ'])&O0000OO0O0OOO0000 ['cond'])#line:876
        O0O0OOOOO000O0O00 =O00O0OO000OO00000 ._bitcount (~(OOO0O0O000O00OO00 |O0000OO0O0OOO0000 ['ante'])&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond'])#line:877
        O0O000OOO000OO000 =O00O0OO000OO00000 ._bitcount (~(OOO0O0O000O00OO00 |O0000OO0O0OOO0000 ['ante'])&~(OOO0O0O000O00OO00 |O0000OO0O0OOO0000 ['succ'])&O0000OO0O0OOO0000 ['cond'])#line:878
        O00000OO0OOO000O0 =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond']&O0000OO0O0OOO0000 ['antv']&O0000OO0O0OOO0000 ['sucv'])#line:879
        O0O0000000O00000O =O00O0OO000OO00000 ._bitcount (O0000OO0O0OOO0000 ['ante']&~(OOO0O0O000O00OO00 |(O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['sucv']))&O0000OO0O0OOO0000 ['cond'])#line:880
        OOO0O00OOOO0O000O =O00O0OO000OO00000 ._bitcount (~(OOO0O0O000O00OO00 |(O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['antv']))&O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['cond']&O0000OO0O0OOO0000 ['sucv'])#line:881
        OOO000000OO00OOOO =O00O0OO000OO00000 ._bitcount (~(OOO0O0O000O00OO00 |(O0000OO0O0OOO0000 ['ante']&O0000OO0O0OOO0000 ['antv']))&~(OOO0O0O000O00OO00 |(O0000OO0O0OOO0000 ['succ']&O0000OO0O0OOO0000 ['sucv']))&O0000OO0O0OOO0000 ['cond'])#line:882
        OOO0O000O0OO0O00O =True #line:883
        for O0O00O000OO0O0000 in O00O0OO000OO00000 .quantifiers .keys ():#line:884
            if (O0O00O000OO0O0000 =='PreBase')|(O0O00O000OO0O0000 =='Base1'):#line:885
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=O0O0OOO00O00OO00O )#line:886
            if (O0O00O000OO0O0000 =='PostBase')|(O0O00O000OO0O0000 =='Base2'):#line:887
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=OOO000000O00O00OO )#line:888
            if (O0O00O000OO0O0000 =='PreRelBase')|(O0O00O000OO0O0000 =='RelBase1'):#line:889
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=O0O0OOO00O00OO00O *1.0 /O00O0OO000OO00000 .data ["rows_count"])#line:890
            if (O0O00O000OO0O0000 =='PostRelBase')|(O0O00O000OO0O0000 =='RelBase2'):#line:891
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=OOO000000O00O00OO *1.0 /O00O0OO000OO00000 .data ["rows_count"])#line:892
            if (O0O00O000OO0O0000 =='Prepim')|(O0O00O000OO0O0000 =='pim1')|(O0O00O000OO0O0000 =='PreConf')|(O0O00O000OO0O0000 =='conf1'):#line:893
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=OOOO0OOOOOOO0O0O0 )#line:894
            if (O0O00O000OO0O0000 =='Postpim')|(O0O00O000OO0O0000 =='pim2')|(O0O00O000OO0O0000 =='PostConf')|(O0O00O000OO0O0000 =='conf2'):#line:895
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=OOOOOOOOOOOOO0OOO )#line:896
            if (O0O00O000OO0O0000 =='Deltapim')|(O0O00O000OO0O0000 =='DeltaConf'):#line:897
                OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=OOOO0OOOOOOO0O0O0 -OOOOOOOOOOOOO0OOO )#line:898
            if (O0O00O000OO0O0000 =='Ratiopim')|(O0O00O000OO0O0000 =='RatioConf'):#line:901
                if (OOOOOOOOOOOOO0OOO >0 ):#line:902
                    OOO0O000O0OO0O00O =OOO0O000O0OO0O00O and (O00O0OO000OO00000 .quantifiers .get (O0O00O000OO0O0000 )<=OOOO0OOOOOOO0O0O0 *1.0 /OOOOOOOOOOOOO0OOO )#line:903
                else :#line:904
                    OOO0O000O0OO0O00O =False #line:905
        O00OO000000OOO0O0 ={}#line:906
        if OOO0O000O0OO0O00O ==True :#line:907
            O00O0OO000OO00000 .stats ['total_valid']+=1 #line:909
            O00OO000000OOO0O0 ["base1"]=O0O0OOO00O00OO00O #line:910
            O00OO000000OOO0O0 ["base2"]=OOO000000O00O00OO #line:911
            O00OO000000OOO0O0 ["rel_base1"]=O0O0OOO00O00OO00O *1.0 /O00O0OO000OO00000 .data ["rows_count"]#line:912
            O00OO000000OOO0O0 ["rel_base2"]=OOO000000O00O00OO *1.0 /O00O0OO000OO00000 .data ["rows_count"]#line:913
            O00OO000000OOO0O0 ["conf1"]=OOOO0OOOOOOO0O0O0 #line:914
            O00OO000000OOO0O0 ["conf2"]=OOOOOOOOOOOOO0OOO #line:915
            O00OO000000OOO0O0 ["deltaconf"]=OOOO0OOOOOOO0O0O0 -OOOOOOOOOOOOO0OOO #line:916
            if (OOOOOOOOOOOOO0OOO >0 ):#line:917
                O00OO000000OOO0O0 ["ratioconf"]=OOOO0OOOOOOO0O0O0 *1.0 /OOOOOOOOOOOOO0OOO #line:918
            else :#line:919
                O00OO000000OOO0O0 ["ratioconf"]=None #line:920
            O00OO000000OOO0O0 ["fourfoldpre"]=[O000OO0O0OO0OO000 ,O0O0OO000OO0000OO ,O0O0OOOOO000O0O00 ,O0O000OOO000OO000 ]#line:921
            O00OO000000OOO0O0 ["fourfoldpost"]=[O00000OO0OOO000O0 ,O0O0000000O00000O ,OOO0O00OOOO0O000O ,OOO000000OO00OOOO ]#line:922
        return OOO0O000O0OO0O00O ,O00OO000000OOO0O0 #line:924
    def _verifyact4ft (OO0OO0OO000OOOOO0 ,_OO0O00OOO000000OO ):#line:926
        O0OOOOO0OO0OOO0OO ={}#line:927
        for OO000O0O00000O0O0 in OO0OO0OO000OOOOO0 .task_actinfo ['cedents']:#line:928
            O0OOOOO0OO0OOO0OO [OO000O0O00000O0O0 ['cedent_type']]=OO000O0O00000O0O0 ['filter_value']#line:930
        O0OO00000O0O0000O =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv-']&O0OOOOO0OO0OOO0OO ['sucv-'])#line:932
        OOO0O0O00OOO00000 =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv+']&O0OOOOO0OO0OOO0OO ['sucv+'])#line:933
        OOO0O0OO0OO0OO0O0 =None #line:934
        OOOOOO0OO000O00O0 =0 #line:935
        OO000OO0OOOO0O0O0 =0 #line:936
        if O0OO00000O0O0000O >0 :#line:945
            OOOOOO0OO000O00O0 =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv-']&O0OOOOO0OO0OOO0OO ['sucv-'])*1.0 /OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv-'])#line:947
        if OOO0O0O00OOO00000 >0 :#line:948
            OO000OO0OOOO0O0O0 =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv+']&O0OOOOO0OO0OOO0OO ['sucv+'])*1.0 /OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv+'])#line:950
        OO0000OO00O00O0O0 =1 <<OO0OO0OO000OOOOO0 .data ["rows_count"]#line:952
        O000OO000O00OO0O0 =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv-']&O0OOOOO0OO0OOO0OO ['sucv-'])#line:953
        O0000OO0OOOO0O00O =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['antv-']&~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['sucv-']))&O0OOOOO0OO0OOO0OO ['cond'])#line:954
        OO00OO00OOO0OO00O =OO0OO0OO000OOOOO0 ._bitcount (~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['antv-']))&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['sucv-'])#line:955
        OOOOO0OOO0000OOOO =OO0OO0OO000OOOOO0 ._bitcount (~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['antv-']))&~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['sucv-']))&O0OOOOO0OO0OOO0OO ['cond'])#line:956
        O0O00O0O00000O00O =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['antv+']&O0OOOOO0OO0OOO0OO ['sucv+'])#line:957
        OOOO0O00O00OOOOOO =OO0OO0OO000OOOOO0 ._bitcount (O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['antv+']&~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['sucv+']))&O0OOOOO0OO0OOO0OO ['cond'])#line:958
        OOO0O00OOOOOOOOOO =OO0OO0OO000OOOOO0 ._bitcount (~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['antv+']))&O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['cond']&O0OOOOO0OO0OOO0OO ['sucv+'])#line:959
        O00O00O0OOO0OO0O0 =OO0OO0OO000OOOOO0 ._bitcount (~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['ante']&O0OOOOO0OO0OOO0OO ['antv+']))&~(OO0000OO00O00O0O0 |(O0OOOOO0OO0OOO0OO ['succ']&O0OOOOO0OO0OOO0OO ['sucv+']))&O0OOOOO0OO0OOO0OO ['cond'])#line:960
        OO00OO0OO0000O0OO =True #line:961
        for OOOOO00OOOOOO0O00 in OO0OO0OO000OOOOO0 .quantifiers .keys ():#line:962
            if (OOOOO00OOOOOO0O00 =='PreBase')|(OOOOO00OOOOOO0O00 =='Base1'):#line:963
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=O0OO00000O0O0000O )#line:964
            if (OOOOO00OOOOOO0O00 =='PostBase')|(OOOOO00OOOOOO0O00 =='Base2'):#line:965
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=OOO0O0O00OOO00000 )#line:966
            if (OOOOO00OOOOOO0O00 =='PreRelBase')|(OOOOO00OOOOOO0O00 =='RelBase1'):#line:967
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=O0OO00000O0O0000O *1.0 /OO0OO0OO000OOOOO0 .data ["rows_count"])#line:968
            if (OOOOO00OOOOOO0O00 =='PostRelBase')|(OOOOO00OOOOOO0O00 =='RelBase2'):#line:969
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=OOO0O0O00OOO00000 *1.0 /OO0OO0OO000OOOOO0 .data ["rows_count"])#line:970
            if (OOOOO00OOOOOO0O00 =='Prepim')|(OOOOO00OOOOOO0O00 =='pim1')|(OOOOO00OOOOOO0O00 =='PreConf')|(OOOOO00OOOOOO0O00 =='conf1'):#line:971
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=OOOOOO0OO000O00O0 )#line:972
            if (OOOOO00OOOOOO0O00 =='Postpim')|(OOOOO00OOOOOO0O00 =='pim2')|(OOOOO00OOOOOO0O00 =='PostConf')|(OOOOO00OOOOOO0O00 =='conf2'):#line:973
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=OO000OO0OOOO0O0O0 )#line:974
            if (OOOOO00OOOOOO0O00 =='Deltapim')|(OOOOO00OOOOOO0O00 =='DeltaConf'):#line:975
                OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=OOOOOO0OO000O00O0 -OO000OO0OOOO0O0O0 )#line:976
            if (OOOOO00OOOOOO0O00 =='Ratiopim')|(OOOOO00OOOOOO0O00 =='RatioConf'):#line:979
                if (OOOOOO0OO000O00O0 >0 ):#line:980
                    OO00OO0OO0000O0OO =OO00OO0OO0000O0OO and (OO0OO0OO000OOOOO0 .quantifiers .get (OOOOO00OOOOOO0O00 )<=OO000OO0OOOO0O0O0 *1.0 /OOOOOO0OO000O00O0 )#line:981
                else :#line:982
                    OO00OO0OO0000O0OO =False #line:983
        OOOO0O0O00000O000 ={}#line:984
        if OO00OO0OO0000O0OO ==True :#line:985
            OO0OO0OO000OOOOO0 .stats ['total_valid']+=1 #line:987
            OOOO0O0O00000O000 ["base1"]=O0OO00000O0O0000O #line:988
            OOOO0O0O00000O000 ["base2"]=OOO0O0O00OOO00000 #line:989
            OOOO0O0O00000O000 ["rel_base1"]=O0OO00000O0O0000O *1.0 /OO0OO0OO000OOOOO0 .data ["rows_count"]#line:990
            OOOO0O0O00000O000 ["rel_base2"]=OOO0O0O00OOO00000 *1.0 /OO0OO0OO000OOOOO0 .data ["rows_count"]#line:991
            OOOO0O0O00000O000 ["conf1"]=OOOOOO0OO000O00O0 #line:992
            OOOO0O0O00000O000 ["conf2"]=OO000OO0OOOO0O0O0 #line:993
            OOOO0O0O00000O000 ["deltaconf"]=OOOOOO0OO000O00O0 -OO000OO0OOOO0O0O0 #line:994
            if (OOOOOO0OO000O00O0 >0 ):#line:995
                OOOO0O0O00000O000 ["ratioconf"]=OO000OO0OOOO0O0O0 *1.0 /OOOOOO0OO000O00O0 #line:996
            else :#line:997
                OOOO0O0O00000O000 ["ratioconf"]=None #line:998
            OOOO0O0O00000O000 ["fourfoldpre"]=[O000OO000O00OO0O0 ,O0000OO0OOOO0O00O ,OO00OO00OOO0OO00O ,OOOOO0OOO0000OOOO ]#line:999
            OOOO0O0O00000O000 ["fourfoldpost"]=[O0O00O0O00000O00O ,OOOO0O00O00OOOOOO ,OOO0O00OOOOOOOOOO ,O00O00O0OOO0OO0O0 ]#line:1000
        return OO00OO0OO0000O0OO ,OOOO0O0O00000O000 #line:1002
    def _verify_opt (OOOO0O0OOOOOO000O ,O0O00OO0O0OOO00OO ,OOO0O00O00O0OO0OO ):#line:1004
        OOOO0O0OOOOOO000O .stats ['total_ver']+=1 #line:1005
        O0OOO0O00O0OO0000 =False #line:1006
        if not (O0O00OO0O0OOO00OO ['optim'].get ('only_con')):#line:1009
            return False #line:1010
        if not (OOOO0O0OOOOOO000O .options ['optimizations']):#line:1013
            return False #line:1015
        O0OO000O00O00OO0O ={}#line:1017
        for O0O00OO0OOOOOOO00 in OOOO0O0OOOOOO000O .task_actinfo ['cedents']:#line:1018
            O0OO000O00O00OO0O [O0O00OO0OOOOOOO00 ['cedent_type']]=O0O00OO0OOOOOOO00 ['filter_value']#line:1020
        O000O0O000OOO00O0 =1 <<OOOO0O0OOOOOO000O .data ["rows_count"]#line:1022
        OO00OOOOOOO00O00O =O000O0O000OOO00O0 -1 #line:1023
        OO00OOO00O0O00OOO =""#line:1024
        OO00OO00OOO0O0O0O =0 #line:1025
        if (O0OO000O00O00OO0O .get ('ante')!=None ):#line:1026
            OO00OOOOOOO00O00O =OO00OOOOOOO00O00O &O0OO000O00O00OO0O ['ante']#line:1027
        if (O0OO000O00O00OO0O .get ('succ')!=None ):#line:1028
            OO00OOOOOOO00O00O =OO00OOOOOOO00O00O &O0OO000O00O00OO0O ['succ']#line:1029
        if (O0OO000O00O00OO0O .get ('cond')!=None ):#line:1030
            OO00OOOOOOO00O00O =OO00OOOOOOO00O00O &O0OO000O00O00OO0O ['cond']#line:1031
        OOO0OOO0O00O0O000 =None #line:1034
        if (OOOO0O0OOOOOO000O .proc =='CFMiner')|(OOOO0O0OOOOOO000O .proc =='4ftMiner')|(OOOO0O0OOOOOO000O .proc =='UICMiner'):#line:1059
            OO00O00O00OOOO00O =OOOO0O0OOOOOO000O ._bitcount (OO00OOOOOOO00O00O )#line:1060
            if not (OOOO0O0OOOOOO000O ._opt_base ==None ):#line:1061
                if not (OOOO0O0OOOOOO000O ._opt_base <=OO00O00O00OOOO00O ):#line:1062
                    O0OOO0O00O0OO0000 =True #line:1063
            if not (OOOO0O0OOOOOO000O ._opt_relbase ==None ):#line:1065
                if not (OOOO0O0OOOOOO000O ._opt_relbase <=OO00O00O00OOOO00O *1.0 /OOOO0O0OOOOOO000O .data ["rows_count"]):#line:1066
                    O0OOO0O00O0OO0000 =True #line:1067
        if (OOOO0O0OOOOOO000O .proc =='SD4ftMiner'):#line:1069
            OO00O00O00OOOO00O =OOOO0O0OOOOOO000O ._bitcount (OO00OOOOOOO00O00O )#line:1070
            if (not (OOOO0O0OOOOOO000O ._opt_base1 ==None ))&(not (OOOO0O0OOOOOO000O ._opt_base2 ==None )):#line:1071
                if not (max (OOOO0O0OOOOOO000O ._opt_base1 ,OOOO0O0OOOOOO000O ._opt_base2 )<=OO00O00O00OOOO00O ):#line:1072
                    O0OOO0O00O0OO0000 =True #line:1074
            if (not (OOOO0O0OOOOOO000O ._opt_relbase1 ==None ))&(not (OOOO0O0OOOOOO000O ._opt_relbase2 ==None )):#line:1075
                if not (max (OOOO0O0OOOOOO000O ._opt_relbase1 ,OOOO0O0OOOOOO000O ._opt_relbase2 )<=OO00O00O00OOOO00O *1.0 /OOOO0O0OOOOOO000O .data ["rows_count"]):#line:1076
                    O0OOO0O00O0OO0000 =True #line:1077
        return O0OOO0O00O0OO0000 #line:1079
        if OOOO0O0OOOOOO000O .proc =='CFMiner':#line:1082
            if (OOO0O00O00O0OO0OO ['cedent_type']=='cond')&(OOO0O00O00O0OO0OO ['defi'].get ('type')=='con'):#line:1083
                OO00O00O00OOOO00O =bin (O0OO000O00O00OO0O ['cond']).count ("1")#line:1084
                O0O0000O0OO00O0OO =True #line:1085
                for OO0OOOO0OOOOOO00O in OOOO0O0OOOOOO000O .quantifiers .keys ():#line:1086
                    if OO0OOOO0OOOOOO00O =='Base':#line:1087
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO00O00O00OOOO00O )#line:1088
                        if not (O0O0000O0OO00O0OO ):#line:1089
                            print (f"...optimization : base is {OO00O00O00OOOO00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1090
                    if OO0OOOO0OOOOOO00O =='RelBase':#line:1091
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO00O00O00OOOO00O *1.0 /OOOO0O0OOOOOO000O .data ["rows_count"])#line:1092
                        if not (O0O0000O0OO00O0OO ):#line:1093
                            print (f"...optimization : base is {OO00O00O00OOOO00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1094
                O0OOO0O00O0OO0000 =not (O0O0000O0OO00O0OO )#line:1095
        elif OOOO0O0OOOOOO000O .proc =='4ftMiner':#line:1096
            if (OOO0O00O00O0OO0OO ['cedent_type']=='cond')&(OOO0O00O00O0OO0OO ['defi'].get ('type')=='con'):#line:1097
                OO00O00O00OOOO00O =bin (O0OO000O00O00OO0O ['cond']).count ("1")#line:1098
                O0O0000O0OO00O0OO =True #line:1099
                for OO0OOOO0OOOOOO00O in OOOO0O0OOOOOO000O .quantifiers .keys ():#line:1100
                    if OO0OOOO0OOOOOO00O =='Base':#line:1101
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO00O00O00OOOO00O )#line:1102
                        if not (O0O0000O0OO00O0OO ):#line:1103
                            print (f"...optimization : base is {OO00O00O00OOOO00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1104
                    if OO0OOOO0OOOOOO00O =='RelBase':#line:1105
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO00O00O00OOOO00O *1.0 /OOOO0O0OOOOOO000O .data ["rows_count"])#line:1106
                        if not (O0O0000O0OO00O0OO ):#line:1107
                            print (f"...optimization : base is {OO00O00O00OOOO00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1108
                O0OOO0O00O0OO0000 =not (O0O0000O0OO00O0OO )#line:1109
            if (OOO0O00O00O0OO0OO ['cedent_type']=='ante')&(OOO0O00O00O0OO0OO ['defi'].get ('type')=='con'):#line:1110
                OO00O00O00OOOO00O =bin (O0OO000O00O00OO0O ['ante']&O0OO000O00O00OO0O ['cond']).count ("1")#line:1111
                O0O0000O0OO00O0OO =True #line:1112
                for OO0OOOO0OOOOOO00O in OOOO0O0OOOOOO000O .quantifiers .keys ():#line:1113
                    if OO0OOOO0OOOOOO00O =='Base':#line:1114
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO00O00O00OOOO00O )#line:1115
                        if not (O0O0000O0OO00O0OO ):#line:1116
                            print (f"...optimization : ANTE: base is {OO00O00O00OOOO00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1117
                    if OO0OOOO0OOOOOO00O =='RelBase':#line:1118
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO00O00O00OOOO00O *1.0 /OOOO0O0OOOOOO000O .data ["rows_count"])#line:1119
                        if not (O0O0000O0OO00O0OO ):#line:1120
                            print (f"...optimization : ANTE:  base is {OO00O00O00OOOO00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1121
                O0OOO0O00O0OO0000 =not (O0O0000O0OO00O0OO )#line:1122
            if (OOO0O00O00O0OO0OO ['cedent_type']=='succ')&(OOO0O00O00O0OO0OO ['defi'].get ('type')=='con'):#line:1123
                OO00O00O00OOOO00O =bin (O0OO000O00O00OO0O ['ante']&O0OO000O00O00OO0O ['cond']&O0OO000O00O00OO0O ['succ']).count ("1")#line:1124
                OOO0OOO0O00O0O000 =0 #line:1125
                if OO00O00O00OOOO00O >0 :#line:1126
                    OOO0OOO0O00O0O000 =bin (O0OO000O00O00OO0O ['ante']&O0OO000O00O00OO0O ['succ']&O0OO000O00O00OO0O ['cond']).count ("1")*1.0 /bin (O0OO000O00O00OO0O ['ante']&O0OO000O00O00OO0O ['cond']).count ("1")#line:1127
                O000O0O000OOO00O0 =1 <<OOOO0O0OOOOOO000O .data ["rows_count"]#line:1128
                OO000O000OO00O000 =bin (O0OO000O00O00OO0O ['ante']&O0OO000O00O00OO0O ['succ']&O0OO000O00O00OO0O ['cond']).count ("1")#line:1129
                OOOO0OO0OOO00O0O0 =bin (O0OO000O00O00OO0O ['ante']&~(O000O0O000OOO00O0 |O0OO000O00O00OO0O ['succ'])&O0OO000O00O00OO0O ['cond']).count ("1")#line:1130
                O0O00OO0OOOOOOO00 =bin (~(O000O0O000OOO00O0 |O0OO000O00O00OO0O ['ante'])&O0OO000O00O00OO0O ['succ']&O0OO000O00O00OO0O ['cond']).count ("1")#line:1131
                O0O00O0OO000OO00O =bin (~(O000O0O000OOO00O0 |O0OO000O00O00OO0O ['ante'])&~(O000O0O000OOO00O0 |O0OO000O00O00OO0O ['succ'])&O0OO000O00O00OO0O ['cond']).count ("1")#line:1132
                O0O0000O0OO00O0OO =True #line:1133
                for OO0OOOO0OOOOOO00O in OOOO0O0OOOOOO000O .quantifiers .keys ():#line:1134
                    if OO0OOOO0OOOOOO00O =='pim':#line:1135
                        O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OOO0OOO0O00O0O000 )#line:1136
                    if not (O0O0000O0OO00O0OO ):#line:1137
                        print (f"...optimization : SUCC:  pim is {OOO0OOO0O00O0O000} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1138
                    if OO0OOOO0OOOOOO00O =='aad':#line:1140
                        if (OO000O000OO00O000 +OOOO0OO0OOO00O0O0 )*(OO000O000OO00O000 +O0O00OO0OOOOOOO00 )>0 :#line:1141
                            O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=OO000O000OO00O000 *(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 +O0O00OO0OOOOOOO00 +O0O00O0OO000OO00O )/(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 )/(OO000O000OO00O000 +O0O00OO0OOOOOOO00 )-1 )#line:1142
                        else :#line:1143
                            O0O0000O0OO00O0OO =False #line:1144
                        if not (O0O0000O0OO00O0OO ):#line:1145
                            OOO0O00O0OO0O0O00 =OO000O000OO00O000 *(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 +O0O00OO0OOOOOOO00 +O0O00O0OO000OO00O )/(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 )/(OO000O000OO00O000 +O0O00OO0OOOOOOO00 )-1 #line:1146
                            print (f"...optimization : SUCC:  aad is {OOO0O00O0OO0O0O00} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1147
                    if OO0OOOO0OOOOOO00O =='bad':#line:1148
                        if (OO000O000OO00O000 +OOOO0OO0OOO00O0O0 )*(OO000O000OO00O000 +O0O00OO0OOOOOOO00 )>0 :#line:1149
                            O0O0000O0OO00O0OO =O0O0000O0OO00O0OO and (OOOO0O0OOOOOO000O .quantifiers .get (OO0OOOO0OOOOOO00O )<=1 -OO000O000OO00O000 *(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 +O0O00OO0OOOOOOO00 +O0O00O0OO000OO00O )/(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 )/(OO000O000OO00O000 +O0O00OO0OOOOOOO00 ))#line:1150
                        else :#line:1151
                            O0O0000O0OO00O0OO =False #line:1152
                        if not (O0O0000O0OO00O0OO ):#line:1153
                            O000O0OO000O0O00O =1 -OO000O000OO00O000 *(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 +O0O00OO0OOOOOOO00 +O0O00O0OO000OO00O )/(OO000O000OO00O000 +OOOO0OO0OOO00O0O0 )/(OO000O000OO00O000 +O0O00OO0OOOOOOO00 )#line:1154
                            print (f"...optimization : SUCC:  bad is {O000O0OO000O0O00O} for {OOO0O00O00O0OO0OO['generated_string']}")#line:1155
                O0OOO0O00O0OO0000 =not (O0O0000O0OO00O0OO )#line:1156
        if (O0OOO0O00O0OO0000 ):#line:1157
            print (f"... OPTIMALIZATION - SKIPPING BRANCH at cedent {OOO0O00O00O0OO0OO['cedent_type']}")#line:1158
        return O0OOO0O00O0OO0000 #line:1159
    def _print (OO0OOO00O000OO00O ,O00OOO0OOOOOOOO00 ,_O00OO0000OO00OO00 ,_OO0O0O0O0O00OO000 ):#line:1162
        if (len (_O00OO0000OO00OO00 ))!=len (_OO0O0O0O0O00OO000 ):#line:1163
            print ("DIFF IN LEN for following cedent : "+str (len (_O00OO0000OO00OO00 ))+" vs "+str (len (_OO0O0O0O0O00OO000 )))#line:1164
            print ("trace cedent : "+str (_O00OO0000OO00OO00 )+", traces "+str (_OO0O0O0O0O00OO000 ))#line:1165
        O0O00O0O0000OOO00 =''#line:1166
        OOO00O00O00000OOO ={}#line:1167
        OOOO0O0O0O0OOO0OO =[]#line:1168
        for OO0OOOO000O000000 in range (len (_O00OO0000OO00OO00 )):#line:1169
            OOO00O00OOOOO0OOO =OO0OOO00O000OO00O .data ["varname"].index (O00OOO0OOOOOOOO00 ['defi'].get ('attributes')[_O00OO0000OO00OO00 [OO0OOOO000O000000 ]].get ('name'))#line:1170
            O0O00O0O0000OOO00 =O0O00O0O0000OOO00 +OO0OOO00O000OO00O .data ["varname"][OOO00O00OOOOO0OOO ]+'('#line:1172
            OOOO0O0O0O0OOO0OO .append (OOO00O00OOOOO0OOO )#line:1173
            OO00000O0OOOO00OO =[]#line:1174
            for O0OO00OO0O0OO00OO in _OO0O0O0O0O00OO000 [OO0OOOO000O000000 ]:#line:1175
                O0O00O0O0000OOO00 =O0O00O0O0000OOO00 +str (OO0OOO00O000OO00O .data ["catnames"][OOO00O00OOOOO0OOO ][O0OO00OO0O0OO00OO ])+" "#line:1176
                OO00000O0OOOO00OO .append (str (OO0OOO00O000OO00O .data ["catnames"][OOO00O00OOOOO0OOO ][O0OO00OO0O0OO00OO ]))#line:1177
            O0O00O0O0000OOO00 =O0O00O0O0000OOO00 [:-1 ]+')'#line:1178
            OOO00O00O00000OOO [OO0OOO00O000OO00O .data ["varname"][OOO00O00OOOOO0OOO ]]=OO00000O0OOOO00OO #line:1179
            if OO0OOOO000O000000 +1 <len (_O00OO0000OO00OO00 ):#line:1180
                O0O00O0O0000OOO00 =O0O00O0O0000OOO00 +' & '#line:1181
        return O0O00O0O0000OOO00 ,OOO00O00O00000OOO ,OOOO0O0O0O0OOO0OO #line:1185
    def _print_hypo (O0OOOO00000OO0OOO ,OO000OO00OOOOOOO0 ):#line:1187
        O0OOOO00000OO0OOO .print_rule (OO000OO00OOOOOOO0 )#line:1188
    def _print_rule (OO00OO000OOOOOOOO ,OO00O0000OOO0OO0O ):#line:1190
        if OO00OO000OOOOOOOO .verbosity ['print_rules']:#line:1191
            print ('Rules info : '+str (OO00O0000OOO0OO0O ['params']))#line:1192
            for OO00OOOO000OO00O0 in OO00OO000OOOOOOOO .task_actinfo ['cedents']:#line:1193
                print (OO00OOOO000OO00O0 ['cedent_type']+' = '+OO00OOOO000OO00O0 ['generated_string'])#line:1194
    def _genvar (OO00000O00O00OOOO ,O0O0O0OO000OO00O0 ,O00O000OO0O000000 ,_O0O0O00OOOOO00O0O ,_O000OO0OO00O0OOO0 ,_OOO00O000O0O000O0 ,_O000000O000OO00OO ,_O0O00OOO0O000OOOO ,_OOO00OOO0OOOOO0OO ,_O0O00OOO00OO00O00 ):#line:1196
        _OOO00OOOOOOO00OOO =0 #line:1197
        if O00O000OO0O000000 ['num_cedent']>0 :#line:1198
            _OOO00OOOOOOO00OOO =(_O0O00OOO00OO00O00 -_OOO00OOO0OOOOO0OO )/O00O000OO0O000000 ['num_cedent']#line:1199
        for OO0O0O0O000OO0OOO in range (O00O000OO0O000000 ['num_cedent']):#line:1200
            if len (_O0O0O00OOOOO00O0O )==0 or OO0O0O0O000OO0OOO >_O0O0O00OOOOO00O0O [-1 ]:#line:1201
                _O0O0O00OOOOO00O0O .append (OO0O0O0O000OO0OOO )#line:1202
                O00OOOOO00OOOO000 =OO00000O00O00OOOO .data ["varname"].index (O00O000OO0O000000 ['defi'].get ('attributes')[OO0O0O0O000OO0OOO ].get ('name'))#line:1203
                _OOO0OOO000OO0O000 =O00O000OO0O000000 ['defi'].get ('attributes')[OO0O0O0O000OO0OOO ].get ('minlen')#line:1204
                _OO00000OO00O0O00O =O00O000OO0O000000 ['defi'].get ('attributes')[OO0O0O0O000OO0OOO ].get ('maxlen')#line:1205
                _OOOOOOOOOO0000OO0 =O00O000OO0O000000 ['defi'].get ('attributes')[OO0O0O0O000OO0OOO ].get ('type')#line:1206
                O0000000O00O000O0 =len (OO00000O00O00OOOO .data ["dm"][O00OOOOO00OOOO000 ])#line:1207
                _O0O0O00O00O0OO0OO =[]#line:1208
                _O000OO0OO00O0OOO0 .append (_O0O0O00O00O0OO0OO )#line:1209
                _O0000OO00OO0000O0 =int (0 )#line:1210
                OO00000O00O00OOOO ._gencomb (O0O0O0OO000OO00O0 ,O00O000OO0O000000 ,_O0O0O00OOOOO00O0O ,_O000OO0OO00O0OOO0 ,_O0O0O00O00O0OO0OO ,_OOO00O000O0O000O0 ,_O0000OO00OO0000O0 ,O0000000O00O000O0 ,_OOOOOOOOOO0000OO0 ,_O000000O000OO00OO ,_O0O00OOO0O000OOOO ,_OOO0OOO000OO0O000 ,_OO00000OO00O0O00O ,_OOO00OOO0OOOOO0OO +OO0O0O0O000OO0OOO *_OOO00OOOOOOO00OOO ,_OOO00OOO0OOOOO0OO +(OO0O0O0O000OO0OOO +1 )*_OOO00OOOOOOO00OOO )#line:1211
                _O000OO0OO00O0OOO0 .pop ()#line:1212
                _O0O0O00OOOOO00O0O .pop ()#line:1213
    def _gencomb (OO0OO0OO00000OO0O ,O0O0O00OOO0OOO00O ,O00O00OOO00OO0O00 ,_O00OO000O0OOO0OOO ,_O00O0OO0O0O0OO0OO ,_O000O0O000OO0OO0O ,_OO0O0000O00000O0O ,_OOOO0OOO00O00O0OO ,OO0O0000000OO0OO0 ,_O0OO00000OOO0OO00 ,_O00OOOO000O0O00OO ,_OO00000O00OO00O00 ,_O0OOOO00OOOO00OO0 ,_O0OO00OO00000OOOO ,_O0O0OOO00O00O0000 ,_O0OO00OOOO00O0O00 ):#line:1215
        _OO000OOOOO0O00OO0 =[]#line:1216
        if _O0OO00000OOO0OO00 =="subset":#line:1217
            if len (_O000O0O000OO0OO0O )==0 :#line:1218
                _OO000OOOOO0O00OO0 =range (OO0O0000000OO0OO0 )#line:1219
            else :#line:1220
                _OO000OOOOO0O00OO0 =range (_O000O0O000OO0OO0O [-1 ]+1 ,OO0O0000000OO0OO0 )#line:1221
        elif _O0OO00000OOO0OO00 =="seq":#line:1222
            if len (_O000O0O000OO0OO0O )==0 :#line:1223
                _OO000OOOOO0O00OO0 =range (OO0O0000000OO0OO0 -_O0OOOO00OOOO00OO0 +1 )#line:1224
            else :#line:1225
                if _O000O0O000OO0OO0O [-1 ]+1 ==OO0O0000000OO0OO0 :#line:1226
                    return #line:1227
                OOOO00O0OO00O0O0O =_O000O0O000OO0OO0O [-1 ]+1 #line:1228
                _OO000OOOOO0O00OO0 .append (OOOO00O0OO00O0O0O )#line:1229
        elif _O0OO00000OOO0OO00 =="lcut":#line:1230
            if len (_O000O0O000OO0OO0O )==0 :#line:1231
                OOOO00O0OO00O0O0O =0 ;#line:1232
            else :#line:1233
                if _O000O0O000OO0OO0O [-1 ]+1 ==OO0O0000000OO0OO0 :#line:1234
                    return #line:1235
                OOOO00O0OO00O0O0O =_O000O0O000OO0OO0O [-1 ]+1 #line:1236
            _OO000OOOOO0O00OO0 .append (OOOO00O0OO00O0O0O )#line:1237
        elif _O0OO00000OOO0OO00 =="rcut":#line:1238
            if len (_O000O0O000OO0OO0O )==0 :#line:1239
                OOOO00O0OO00O0O0O =OO0O0000000OO0OO0 -1 ;#line:1240
            else :#line:1241
                if _O000O0O000OO0OO0O [-1 ]==0 :#line:1242
                    return #line:1243
                OOOO00O0OO00O0O0O =_O000O0O000OO0OO0O [-1 ]-1 #line:1244
            _OO000OOOOO0O00OO0 .append (OOOO00O0OO00O0O0O )#line:1246
        elif _O0OO00000OOO0OO00 =="one":#line:1247
            if len (_O000O0O000OO0OO0O )==0 :#line:1248
                O00OOOOO00OOOOOOO =OO0OO0OO00000OO0O .data ["varname"].index (O00O00OOO00OO0O00 ['defi'].get ('attributes')[_O00OO000O0OOO0OOO [-1 ]].get ('name'))#line:1249
                try :#line:1250
                    OOOO00O0OO00O0O0O =OO0OO0OO00000OO0O .data ["catnames"][O00OOOOO00OOOOOOO ].index (O00O00OOO00OO0O00 ['defi'].get ('attributes')[_O00OO000O0OOO0OOO [-1 ]].get ('value'))#line:1251
                except :#line:1252
                    print (f"ERROR: attribute '{O00O00OOO00OO0O00['defi'].get('attributes')[_O00OO000O0OOO0OOO[-1]].get('name')}' has not value '{O00O00OOO00OO0O00['defi'].get('attributes')[_O00OO000O0OOO0OOO[-1]].get('value')}'")#line:1253
                    exit (1 )#line:1254
                _OO000OOOOO0O00OO0 .append (OOOO00O0OO00O0O0O )#line:1255
                _O0OOOO00OOOO00OO0 =1 #line:1256
                _O0OO00OO00000OOOO =1 #line:1257
            else :#line:1258
                print ("DEBUG: one category should not have more categories")#line:1259
                return #line:1260
        else :#line:1261
            print ("Attribute type "+_O0OO00000OOO0OO00 +" not supported.")#line:1262
            return #line:1263
        if len (_OO000OOOOO0O00OO0 )>0 :#line:1265
            _O00O00OO0O0O0OO0O =(_O0OO00OOOO00O0O00 -_O0O0OOO00O00O0000 )/len (_OO000OOOOO0O00OO0 )#line:1266
        else :#line:1267
            _O00O00OO0O0O0OO0O =0 #line:1268
        _O0O0O0000000OO000 =0 #line:1270
        for OO0O0OO00000000OO in _OO000OOOOO0O00OO0 :#line:1272
                _O000O0O000OO0OO0O .append (OO0O0OO00000000OO )#line:1274
                _O00O0OO0O0O0OO0OO .pop ()#line:1275
                _O00O0OO0O0O0OO0OO .append (_O000O0O000OO0OO0O )#line:1276
                _O0OO0OOO0O00000O0 =_OOOO0OOO00O00O0OO |OO0OO0OO00000OO0O .data ["dm"][OO0OO0OO00000OO0O .data ["varname"].index (O00O00OOO00OO0O00 ['defi'].get ('attributes')[_O00OO000O0OOO0OOO [-1 ]].get ('name'))][OO0O0OO00000000OO ]#line:1280
                _OOOOOOOO00O0O000O =1 #line:1282
                if (len (_O00OO000O0OOO0OOO )<_O00OOOO000O0O00OO ):#line:1283
                    _OOOOOOOO00O0O000O =-1 #line:1284
                if (len (_O00O0OO0O0O0OO0OO [-1 ])<_O0OOOO00OOOO00OO0 ):#line:1286
                    _OOOOOOOO00O0O000O =0 #line:1287
                _O0OOOOOOOO0O000OO =0 #line:1289
                if O00O00OOO00OO0O00 ['defi'].get ('type')=='con':#line:1290
                    _O0OOOOOOOO0O000OO =_OO0O0000O00000O0O &_O0OO0OOO0O00000O0 #line:1291
                else :#line:1292
                    _O0OOOOOOOO0O000OO =_OO0O0000O00000O0O |_O0OO0OOO0O00000O0 #line:1293
                O00O00OOO00OO0O00 ['trace_cedent']=_O00OO000O0OOO0OOO #line:1294
                O00O00OOO00OO0O00 ['traces']=_O00O0OO0O0O0OO0OO #line:1295
                O00000OO00OO00OOO ,OOO00OOOOOOOOO000 ,O0O0O0O0OO0OOOO00 =OO0OO0OO00000OO0O ._print (O00O00OOO00OO0O00 ,_O00OO000O0OOO0OOO ,_O00O0OO0O0O0OO0OO )#line:1296
                O00O00OOO00OO0O00 ['generated_string']=O00000OO00OO00OOO #line:1297
                O00O00OOO00OO0O00 ['rule']=OOO00OOOOOOOOO000 #line:1298
                O00O00OOO00OO0O00 ['filter_value']=_O0OOOOOOOO0O000OO #line:1299
                O00O00OOO00OO0O00 ['traces']=copy .deepcopy (_O00O0OO0O0O0OO0OO )#line:1300
                O00O00OOO00OO0O00 ['trace_cedent']=copy .deepcopy (_O00OO000O0OOO0OOO )#line:1301
                O00O00OOO00OO0O00 ['trace_cedent_asindata']=copy .deepcopy (O0O0O0O0OO0OOOO00 )#line:1302
                O0O0O00OOO0OOO00O ['cedents'].append (O00O00OOO00OO0O00 )#line:1304
                OOO00000OO0OO000O =OO0OO0OO00000OO0O ._verify_opt (O0O0O00OOO0OOO00O ,O00O00OOO00OO0O00 )#line:1305
                if not (OOO00000OO0OO000O ):#line:1311
                    if _OOOOOOOO00O0O000O ==1 :#line:1312
                        if len (O0O0O00OOO0OOO00O ['cedents_to_do'])==len (O0O0O00OOO0OOO00O ['cedents']):#line:1314
                            if OO0OO0OO00000OO0O .proc =='CFMiner':#line:1315
                                OOOO00OOO0OOO0O00 ,OO00OO00O000O0O00 =OO0OO0OO00000OO0O ._verifyCF (_O0OOOOOOOO0O000OO )#line:1316
                            elif OO0OO0OO00000OO0O .proc =='UICMiner':#line:1317
                                OOOO00OOO0OOO0O00 ,OO00OO00O000O0O00 =OO0OO0OO00000OO0O ._verifyUIC (_O0OOOOOOOO0O000OO )#line:1318
                            elif OO0OO0OO00000OO0O .proc =='4ftMiner':#line:1319
                                OOOO00OOO0OOO0O00 ,OO00OO00O000O0O00 =OO0OO0OO00000OO0O ._verify4ft (_O0OO0OOO0O00000O0 )#line:1320
                            elif OO0OO0OO00000OO0O .proc =='SD4ftMiner':#line:1321
                                OOOO00OOO0OOO0O00 ,OO00OO00O000O0O00 =OO0OO0OO00000OO0O ._verifysd4ft (_O0OO0OOO0O00000O0 )#line:1322
                            elif OO0OO0OO00000OO0O .proc =='NewAct4ftMiner':#line:1323
                                OOOO00OOO0OOO0O00 ,OO00OO00O000O0O00 =OO0OO0OO00000OO0O ._verifynewact4ft (_O0OO0OOO0O00000O0 )#line:1324
                            elif OO0OO0OO00000OO0O .proc =='Act4ftMiner':#line:1325
                                OOOO00OOO0OOO0O00 ,OO00OO00O000O0O00 =OO0OO0OO00000OO0O ._verifyact4ft (_O0OO0OOO0O00000O0 )#line:1326
                            else :#line:1327
                                print ("Unsupported procedure : "+OO0OO0OO00000OO0O .proc )#line:1328
                                exit (0 )#line:1329
                            if OOOO00OOO0OOO0O00 ==True :#line:1330
                                O00O00OOOOO00O00O ={}#line:1331
                                O00O00OOOOO00O00O ["rule_id"]=OO0OO0OO00000OO0O .stats ['total_valid']#line:1332
                                O00O00OOOOO00O00O ["cedents_str"]={}#line:1333
                                O00O00OOOOO00O00O ["cedents_struct"]={}#line:1334
                                O00O00OOOOO00O00O ['traces']={}#line:1335
                                O00O00OOOOO00O00O ['trace_cedent_taskorder']={}#line:1336
                                O00O00OOOOO00O00O ['trace_cedent_dataorder']={}#line:1337
                                for OO000OOO000OOO0O0 in O0O0O00OOO0OOO00O ['cedents']:#line:1338
                                    O00O00OOOOO00O00O ['cedents_str'][OO000OOO000OOO0O0 ['cedent_type']]=OO000OOO000OOO0O0 ['generated_string']#line:1340
                                    O00O00OOOOO00O00O ['cedents_struct'][OO000OOO000OOO0O0 ['cedent_type']]=OO000OOO000OOO0O0 ['rule']#line:1341
                                    O00O00OOOOO00O00O ['traces'][OO000OOO000OOO0O0 ['cedent_type']]=OO000OOO000OOO0O0 ['traces']#line:1342
                                    O00O00OOOOO00O00O ['trace_cedent_taskorder'][OO000OOO000OOO0O0 ['cedent_type']]=OO000OOO000OOO0O0 ['trace_cedent']#line:1343
                                    O00O00OOOOO00O00O ['trace_cedent_dataorder'][OO000OOO000OOO0O0 ['cedent_type']]=OO000OOO000OOO0O0 ['trace_cedent_asindata']#line:1344
                                O00O00OOOOO00O00O ["params"]=OO00OO00O000O0O00 #line:1346
                                OO0OO0OO00000OO0O ._print_rule (O00O00OOOOO00O00O )#line:1348
                                OO0OO0OO00000OO0O .rulelist .append (O00O00OOOOO00O00O )#line:1354
                            OO0OO0OO00000OO0O .stats ['total_cnt']+=1 #line:1356
                            OO0OO0OO00000OO0O .stats ['total_ver']+=1 #line:1357
                    if _OOOOOOOO00O0O000O >=0 :#line:1358
                        if len (O0O0O00OOO0OOO00O ['cedents_to_do'])>len (O0O0O00OOO0OOO00O ['cedents']):#line:1359
                            OO0OO0OO00000OO0O ._start_cedent (O0O0O00OOO0OOO00O ,_O0O0OOO00O00O0000 +_O0O0O0000000OO000 *_O00O00OO0O0O0OO0O ,_O0O0OOO00O00O0000 +(_O0O0O0000000OO000 +0.33 )*_O00O00OO0O0O0OO0O )#line:1360
                    O0O0O00OOO0OOO00O ['cedents'].pop ()#line:1361
                    if (len (_O00OO000O0OOO0OOO )<_OO00000O00OO00O00 ):#line:1362
                        OO0OO0OO00000OO0O ._genvar (O0O0O00OOO0OOO00O ,O00O00OOO00OO0O00 ,_O00OO000O0OOO0OOO ,_O00O0OO0O0O0OO0OO ,_O0OOOOOOOO0O000OO ,_O00OOOO000O0O00OO ,_OO00000O00OO00O00 ,_O0O0OOO00O00O0000 +(_O0O0O0000000OO000 +0.33 )*_O00O00OO0O0O0OO0O ,_O0O0OOO00O00O0000 +(_O0O0O0000000OO000 +0.66 )*_O00O00OO0O0O0OO0O )#line:1363
                else :#line:1364
                    O0O0O00OOO0OOO00O ['cedents'].pop ()#line:1365
                if len (_O000O0O000OO0OO0O )<_O0OO00OO00000OOOO :#line:1366
                    OO0OO0OO00000OO0O ._gencomb (O0O0O00OOO0OOO00O ,O00O00OOO00OO0O00 ,_O00OO000O0OOO0OOO ,_O00O0OO0O0O0OO0OO ,_O000O0O000OO0OO0O ,_OO0O0000O00000O0O ,_O0OO0OOO0O00000O0 ,OO0O0000000OO0OO0 ,_O0OO00000OOO0OO00 ,_O00OOOO000O0O00OO ,_OO00000O00OO00O00 ,_O0OOOO00OOOO00OO0 ,_O0OO00OO00000OOOO ,_O0O0OOO00O00O0000 +_O00O00OO0O0O0OO0O *(_O0O0O0000000OO000 +0.66 ),_O0O0OOO00O00O0000 +_O00O00OO0O0O0OO0O *(_O0O0O0000000OO000 +1 ))#line:1367
                _O000O0O000OO0OO0O .pop ()#line:1368
                _O0O0O0000000OO000 +=1 #line:1369
                if OO0OO0OO00000OO0O .options ['progressbar']:#line:1370
                    OO0OO0OO00000OO0O .bar .update (min (100 ,_O0O0OOO00O00O0000 +_O00O00OO0O0O0OO0O *_O0O0O0000000OO000 ))#line:1371
    def _start_cedent (OOOO00OO00OOO00O0 ,OO0OO0O0O0O00O0O0 ,_O0OO000O00OO0O000 ,_OOO000OOOO0OO0O0O ):#line:1374
        if len (OO0OO0O0O0O00O0O0 ['cedents_to_do'])>len (OO0OO0O0O0O00O0O0 ['cedents']):#line:1375
            _OOO0O0000OOOOO00O =[]#line:1376
            _O00OO00OOOOOOO00O =[]#line:1377
            OOO0OOO0O00O0OO0O ={}#line:1378
            OOO0OOO0O00O0OO0O ['cedent_type']=OO0OO0O0O0O00O0O0 ['cedents_to_do'][len (OO0OO0O0O0O00O0O0 ['cedents'])]#line:1379
            OOOO0O0OO0OOOO0OO =OOO0OOO0O00O0OO0O ['cedent_type']#line:1380
            if ((OOOO0O0OO0OOOO0OO [-1 ]=='-')|(OOOO0O0OO0OOOO0OO [-1 ]=='+')):#line:1381
                OOOO0O0OO0OOOO0OO =OOOO0O0OO0OOOO0OO [:-1 ]#line:1382
            OOO0OOO0O00O0OO0O ['defi']=OOOO00OO00OOO00O0 .kwargs .get (OOOO0O0OO0OOOO0OO )#line:1384
            if (OOO0OOO0O00O0OO0O ['defi']==None ):#line:1385
                print ("Error getting cedent ",OOO0OOO0O00O0OO0O ['cedent_type'])#line:1386
            _O0OO0OOO0O0O00OO0 =int (0 )#line:1387
            OOO0OOO0O00O0OO0O ['num_cedent']=len (OOO0OOO0O00O0OO0O ['defi'].get ('attributes'))#line:1394
            if (OOO0OOO0O00O0OO0O ['defi'].get ('type')=='con'):#line:1395
                _O0OO0OOO0O0O00OO0 =(1 <<OOOO00OO00OOO00O0 .data ["rows_count"])-1 #line:1396
            OOOO00OO00OOO00O0 ._genvar (OO0OO0O0O0O00O0O0 ,OOO0OOO0O00O0OO0O ,_OOO0O0000OOOOO00O ,_O00OO00OOOOOOO00O ,_O0OO0OOO0O0O00OO0 ,OOO0OOO0O00O0OO0O ['defi'].get ('minlen'),OOO0OOO0O00O0OO0O ['defi'].get ('maxlen'),_O0OO000O00OO0O000 ,_OOO000OOOO0OO0O0O )#line:1397
    def _calc_all (O0OOOO00OOOOO00OO ,**OO0OO0OOO0OOO000O ):#line:1400
        if "df"in OO0OO0OOO0OOO000O :#line:1401
            O0OOOO00OOOOO00OO ._prep_data (O0OOOO00OOOOO00OO .kwargs .get ("df"))#line:1402
        if not (O0OOOO00OOOOO00OO ._initialized ):#line:1403
            print ("ERROR: dataframe is missing and not initialized with dataframe")#line:1404
        else :#line:1405
            O0OOOO00OOOOO00OO ._calculate (**OO0OO0OOO0OOO000O )#line:1406
    def _check_cedents (OOO00OOOOO000O0O0 ,OO000OO00O0O00OO0 ,**OOO0OOO000OO00OO0 ):#line:1408
        OO00OOOOO0000OOOO =True #line:1409
        if (OOO0OOO000OO00OO0 .get ('quantifiers',None )==None ):#line:1410
            print (f"Error: missing quantifiers.")#line:1411
            OO00OOOOO0000OOOO =False #line:1412
            return OO00OOOOO0000OOOO #line:1413
        if (type (OOO0OOO000OO00OO0 .get ('quantifiers'))!=dict ):#line:1414
            print (f"Error: quantifiers are not dictionary type.")#line:1415
            OO00OOOOO0000OOOO =False #line:1416
            return OO00OOOOO0000OOOO #line:1417
        for O0O000O0O0OOO000O in OO000OO00O0O00OO0 :#line:1419
            if (OOO0OOO000OO00OO0 .get (O0O000O0O0OOO000O ,None )==None ):#line:1420
                print (f"Error: cedent {O0O000O0O0OOO000O} is missing in parameters.")#line:1421
                OO00OOOOO0000OOOO =False #line:1422
                return OO00OOOOO0000OOOO #line:1423
            O0O0O000O0O00OO00 =OOO0OOO000OO00OO0 .get (O0O000O0O0OOO000O )#line:1424
            if (O0O0O000O0O00OO00 .get ('minlen'),None )==None :#line:1425
                print (f"Error: cedent {O0O000O0O0OOO000O} has no minimal length specified.")#line:1426
                OO00OOOOO0000OOOO =False #line:1427
                return OO00OOOOO0000OOOO #line:1428
            if not (type (O0O0O000O0O00OO00 .get ('minlen'))is int ):#line:1429
                print (f"Error: cedent {O0O000O0O0OOO000O} has invalid type of minimal length ({type(O0O0O000O0O00OO00.get('minlen'))}).")#line:1430
                OO00OOOOO0000OOOO =False #line:1431
                return OO00OOOOO0000OOOO #line:1432
            if (O0O0O000O0O00OO00 .get ('maxlen'),None )==None :#line:1433
                print (f"Error: cedent {O0O000O0O0OOO000O} has no maximal length specified.")#line:1434
                OO00OOOOO0000OOOO =False #line:1435
                return OO00OOOOO0000OOOO #line:1436
            if not (type (O0O0O000O0O00OO00 .get ('maxlen'))is int ):#line:1437
                print (f"Error: cedent {O0O000O0O0OOO000O} has invalid type of maximal length.")#line:1438
                OO00OOOOO0000OOOO =False #line:1439
                return OO00OOOOO0000OOOO #line:1440
            if (O0O0O000O0O00OO00 .get ('type'),None )==None :#line:1441
                print (f"Error: cedent {O0O000O0O0OOO000O} has no type specified.")#line:1442
                OO00OOOOO0000OOOO =False #line:1443
                return OO00OOOOO0000OOOO #line:1444
            if not ((O0O0O000O0O00OO00 .get ('type'))in (['con','dis'])):#line:1445
                print (f"Error: cedent {O0O000O0O0OOO000O} has invalid type. Allowed values are 'con' and 'dis'.")#line:1446
                OO00OOOOO0000OOOO =False #line:1447
                return OO00OOOOO0000OOOO #line:1448
            if (O0O0O000O0O00OO00 .get ('attributes'),None )==None :#line:1449
                print (f"Error: cedent {O0O000O0O0OOO000O} has no attributes specified.")#line:1450
                OO00OOOOO0000OOOO =False #line:1451
                return OO00OOOOO0000OOOO #line:1452
            for O00OO000O0OOO0OOO in O0O0O000O0O00OO00 .get ('attributes'):#line:1453
                if (O00OO000O0OOO0OOO .get ('name'),None )==None :#line:1454
                    print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO} has no 'name' attribute specified.")#line:1455
                    OO00OOOOO0000OOOO =False #line:1456
                    return OO00OOOOO0000OOOO #line:1457
                if not ((O00OO000O0OOO0OOO .get ('name'))in OOO00OOOOO000O0O0 .data ["varname"]):#line:1458
                    print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} not in variable list. Please check spelling.")#line:1459
                    OO00OOOOO0000OOOO =False #line:1460
                    return OO00OOOOO0000OOOO #line:1461
                if (O00OO000O0OOO0OOO .get ('type'),None )==None :#line:1462
                    print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} has no 'type' attribute specified.")#line:1463
                    OO00OOOOO0000OOOO =False #line:1464
                    return OO00OOOOO0000OOOO #line:1465
                if not ((O00OO000O0OOO0OOO .get ('type'))in (['rcut','lcut','seq','subset','one'])):#line:1466
                    print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} has unsupported type {O00OO000O0OOO0OOO.get('type')}. Supported types are 'subset','seq','lcut','rcut','one'.")#line:1467
                    OO00OOOOO0000OOOO =False #line:1468
                    return OO00OOOOO0000OOOO #line:1469
                if (O00OO000O0OOO0OOO .get ('minlen'),None )==None :#line:1470
                    print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} has no minimal length specified.")#line:1471
                    OO00OOOOO0000OOOO =False #line:1472
                    return OO00OOOOO0000OOOO #line:1473
                if not (type (O00OO000O0OOO0OOO .get ('minlen'))is int ):#line:1474
                    if not (O00OO000O0OOO0OOO .get ('type')=='one'):#line:1475
                        print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} has invalid type of minimal length.")#line:1476
                        OO00OOOOO0000OOOO =False #line:1477
                        return OO00OOOOO0000OOOO #line:1478
                if (O00OO000O0OOO0OOO .get ('maxlen'),None )==None :#line:1479
                    print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} has no maximal length specified.")#line:1480
                    OO00OOOOO0000OOOO =False #line:1481
                    return OO00OOOOO0000OOOO #line:1482
                if not (type (O00OO000O0OOO0OOO .get ('maxlen'))is int ):#line:1483
                    if not (O00OO000O0OOO0OOO .get ('type')=='one'):#line:1484
                        print (f"Error: cedent {O0O000O0O0OOO000O} / attribute {O00OO000O0OOO0OOO.get('name')} has invalid type of maximal length.")#line:1485
                        OO00OOOOO0000OOOO =False #line:1486
                        return OO00OOOOO0000OOOO #line:1487
        return OO00OOOOO0000OOOO #line:1488
    def _calculate (O0O00000O0000O00O ,**O00OOOOOO0O0000OO ):#line:1490
        if O0O00000O0000O00O .data ["data_prepared"]==0 :#line:1491
            print ("Error: data not prepared")#line:1492
            return #line:1493
        O0O00000O0000O00O .kwargs =O00OOOOOO0O0000OO #line:1494
        O0O00000O0000O00O .proc =O00OOOOOO0O0000OO .get ('proc')#line:1495
        O0O00000O0000O00O .quantifiers =O00OOOOOO0O0000OO .get ('quantifiers')#line:1496
        O0O00000O0000O00O ._init_task ()#line:1498
        O0O00000O0000O00O .stats ['start_proc_time']=time .time ()#line:1499
        O0O00000O0000O00O .task_actinfo ['cedents_to_do']=[]#line:1500
        O0O00000O0000O00O .task_actinfo ['cedents']=[]#line:1501
        if O00OOOOOO0O0000OO .get ("proc")=='UICMiner':#line:1504
            if not (O0O00000O0000O00O ._check_cedents (['ante'],**O00OOOOOO0O0000OO )):#line:1505
                return #line:1506
            _O00O00000O0OOOOOO =O00OOOOOO0O0000OO .get ("cond")#line:1508
            if _O00O00000O0OOOOOO !=None :#line:1509
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1510
            else :#line:1511
                O00O0OOOOO0O0OOOO =O0O00000O0000O00O .cedent #line:1512
                O00O0OOOOO0O0OOOO ['cedent_type']='cond'#line:1513
                O00O0OOOOO0O0OOOO ['filter_value']=(1 <<O0O00000O0000O00O .data ["rows_count"])-1 #line:1514
                O00O0OOOOO0O0OOOO ['generated_string']='---'#line:1515
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1517
                O0O00000O0000O00O .task_actinfo ['cedents'].append (O00O0OOOOO0O0OOOO )#line:1518
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('ante')#line:1519
            if O00OOOOOO0O0000OO .get ('target',None )==None :#line:1520
                print ("ERROR: no succedent/target variable defined for UIC Miner")#line:1521
                return #line:1522
            if not (O00OOOOOO0O0000OO .get ('target')in O0O00000O0000O00O .data ["varname"]):#line:1523
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1524
                return #line:1525
            if ("aad_score"in O0O00000O0000O00O .quantifiers ):#line:1526
                if not ("aad_weights"in O0O00000O0000O00O .quantifiers ):#line:1527
                    print ("ERROR: for aad quantifier you need to specify aad weights.")#line:1528
                    return #line:1529
                if not (len (O0O00000O0000O00O .quantifiers .get ("aad_weights"))==len (O0O00000O0000O00O .data ["dm"][O0O00000O0000O00O .data ["varname"].index (O0O00000O0000O00O .kwargs .get ('target'))])):#line:1530
                    print ("ERROR: aad weights has different number of weights than classes of target variable.")#line:1531
                    return #line:1532
        elif O00OOOOOO0O0000OO .get ("proc")=='CFMiner':#line:1533
            O0O00000O0000O00O .task_actinfo ['cedents_to_do']=['cond']#line:1534
            if O00OOOOOO0O0000OO .get ('target',None )==None :#line:1535
                print ("ERROR: no target variable defined for CF Miner")#line:1536
                return #line:1537
            if not (O0O00000O0000O00O ._check_cedents (['cond'],**O00OOOOOO0O0000OO )):#line:1538
                return #line:1539
            if not (O00OOOOOO0O0000OO .get ('target')in O0O00000O0000O00O .data ["varname"]):#line:1540
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1541
                return #line:1542
            if ("aad"in O0O00000O0000O00O .quantifiers ):#line:1543
                if not ("aad_weights"in O0O00000O0000O00O .quantifiers ):#line:1544
                    print ("ERROR: for aad quantifier you need to specify aad weights.")#line:1545
                    return #line:1546
                if not (len (O0O00000O0000O00O .quantifiers .get ("aad_weights"))==len (O0O00000O0000O00O .data ["dm"][O0O00000O0000O00O .data ["varname"].index (O0O00000O0000O00O .kwargs .get ('target'))])):#line:1547
                    print ("ERROR: aad weights has different number of weights than classes of target variable.")#line:1548
                    return #line:1549
        elif O00OOOOOO0O0000OO .get ("proc")=='4ftMiner':#line:1552
            if not (O0O00000O0000O00O ._check_cedents (['ante','succ'],**O00OOOOOO0O0000OO )):#line:1553
                return #line:1554
            _O00O00000O0OOOOOO =O00OOOOOO0O0000OO .get ("cond")#line:1556
            if _O00O00000O0OOOOOO !=None :#line:1557
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1558
            else :#line:1559
                O00O0OOOOO0O0OOOO =O0O00000O0000O00O .cedent #line:1560
                O00O0OOOOO0O0OOOO ['cedent_type']='cond'#line:1561
                O00O0OOOOO0O0OOOO ['filter_value']=(1 <<O0O00000O0000O00O .data ["rows_count"])-1 #line:1562
                O00O0OOOOO0O0OOOO ['generated_string']='---'#line:1563
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1565
                O0O00000O0000O00O .task_actinfo ['cedents'].append (O00O0OOOOO0O0OOOO )#line:1566
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('ante')#line:1570
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('succ')#line:1571
        elif O00OOOOOO0O0000OO .get ("proc")=='NewAct4ftMiner':#line:1572
            _O00O00000O0OOOOOO =O00OOOOOO0O0000OO .get ("cond")#line:1575
            if _O00O00000O0OOOOOO !=None :#line:1576
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1577
            else :#line:1578
                O00O0OOOOO0O0OOOO =O0O00000O0000O00O .cedent #line:1579
                O00O0OOOOO0O0OOOO ['cedent_type']='cond'#line:1580
                O00O0OOOOO0O0OOOO ['filter_value']=(1 <<O0O00000O0000O00O .data ["rows_count"])-1 #line:1581
                O00O0OOOOO0O0OOOO ['generated_string']='---'#line:1582
                print (O00O0OOOOO0O0OOOO ['filter_value'])#line:1583
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1584
                O0O00000O0000O00O .task_actinfo ['cedents'].append (O00O0OOOOO0O0OOOO )#line:1585
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('antv')#line:1586
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('sucv')#line:1587
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('ante')#line:1588
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('succ')#line:1589
        elif O00OOOOOO0O0000OO .get ("proc")=='Act4ftMiner':#line:1590
            _O00O00000O0OOOOOO =O00OOOOOO0O0000OO .get ("cond")#line:1593
            if _O00O00000O0OOOOOO !=None :#line:1594
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1595
            else :#line:1596
                O00O0OOOOO0O0OOOO =O0O00000O0000O00O .cedent #line:1597
                O00O0OOOOO0O0OOOO ['cedent_type']='cond'#line:1598
                O00O0OOOOO0O0OOOO ['filter_value']=(1 <<O0O00000O0000O00O .data ["rows_count"])-1 #line:1599
                O00O0OOOOO0O0OOOO ['generated_string']='---'#line:1600
                print (O00O0OOOOO0O0OOOO ['filter_value'])#line:1601
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1602
                O0O00000O0000O00O .task_actinfo ['cedents'].append (O00O0OOOOO0O0OOOO )#line:1603
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('antv-')#line:1604
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('antv+')#line:1605
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('sucv-')#line:1606
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('sucv+')#line:1607
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('ante')#line:1608
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('succ')#line:1609
        elif O00OOOOOO0O0000OO .get ("proc")=='SD4ftMiner':#line:1610
            if not (O0O00000O0000O00O ._check_cedents (['ante','succ','frst','scnd'],**O00OOOOOO0O0000OO )):#line:1613
                return #line:1614
            _O00O00000O0OOOOOO =O00OOOOOO0O0000OO .get ("cond")#line:1615
            if _O00O00000O0OOOOOO !=None :#line:1616
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1617
            else :#line:1618
                O00O0OOOOO0O0OOOO =O0O00000O0000O00O .cedent #line:1619
                O00O0OOOOO0O0OOOO ['cedent_type']='cond'#line:1620
                O00O0OOOOO0O0OOOO ['filter_value']=(1 <<O0O00000O0000O00O .data ["rows_count"])-1 #line:1621
                O00O0OOOOO0O0OOOO ['generated_string']='---'#line:1622
                O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('cond')#line:1624
                O0O00000O0000O00O .task_actinfo ['cedents'].append (O00O0OOOOO0O0OOOO )#line:1625
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('frst')#line:1626
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('scnd')#line:1627
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('ante')#line:1628
            O0O00000O0000O00O .task_actinfo ['cedents_to_do'].append ('succ')#line:1629
        else :#line:1630
            print ("Unsupported procedure")#line:1631
            return #line:1632
        print ("Will go for ",O00OOOOOO0O0000OO .get ("proc"))#line:1633
        O0O00000O0000O00O .task_actinfo ['optim']={}#line:1636
        OO0O00O00O00000OO =True #line:1637
        for OOO0OOO00O000OO0O in O0O00000O0000O00O .task_actinfo ['cedents_to_do']:#line:1638
            try :#line:1639
                OO000O0OO00O00OOO =O0O00000O0000O00O .kwargs .get (OOO0OOO00O000OO0O )#line:1640
                if OO000O0OO00O00OOO .get ('type')!='con':#line:1644
                    OO0O00O00O00000OO =False #line:1645
            except :#line:1647
                O000OOO0OOO0000O0 =1 <2 #line:1648
        if O0O00000O0000O00O .options ['optimizations']==False :#line:1650
            OO0O00O00O00000OO =False #line:1651
        OOO000000O0O0OOO0 ={}#line:1652
        OOO000000O0O0OOO0 ['only_con']=OO0O00O00O00000OO #line:1653
        O0O00000O0000O00O .task_actinfo ['optim']=OOO000000O0O0OOO0 #line:1654
        print ("Starting to mine rules.")#line:1662
        sys .stdout .flush ()#line:1663
        time .sleep (0.01 )#line:1664
        if O0O00000O0000O00O .options ['progressbar']:#line:1665
            OO0OOOOOO0OO00OO0 =[progressbar .Percentage (),progressbar .Bar (),progressbar .Timer ()]#line:1666
            O0O00000O0000O00O .bar =progressbar .ProgressBar (widgets =OO0OOOOOO0OO00OO0 ,max_value =100 ,fd =sys .stdout ).start ()#line:1667
            O0O00000O0000O00O .bar .update (0 )#line:1668
        O0O00000O0000O00O .progress_lower =0 #line:1669
        O0O00000O0000O00O .progress_upper =100 #line:1670
        O0O00000O0000O00O ._start_cedent (O0O00000O0000O00O .task_actinfo ,O0O00000O0000O00O .progress_lower ,O0O00000O0000O00O .progress_upper )#line:1671
        if O0O00000O0000O00O .options ['progressbar']:#line:1672
            O0O00000O0000O00O .bar .update (100 )#line:1673
            O0O00000O0000O00O .bar .finish ()#line:1674
        O0O00000O0000O00O .stats ['end_proc_time']=time .time ()#line:1676
        print ("Done. Total verifications : "+str (O0O00000O0000O00O .stats ['total_cnt'])+", rules "+str (O0O00000O0000O00O .stats ['total_valid'])+", times: prep "+"{:.2f}".format (O0O00000O0000O00O .stats ['end_prep_time']-O0O00000O0000O00O .stats ['start_prep_time'])+"sec, processing "+"{:.2f}".format (O0O00000O0000O00O .stats ['end_proc_time']-O0O00000O0000O00O .stats ['start_proc_time'])+"sec")#line:1680
        O0O0O0O000O0O0O00 ={}#line:1681
        O0O0O0OO0OOOOOOOO ={}#line:1682
        O0O0O0OO0OOOOOOOO ["task_type"]=O00OOOOOO0O0000OO .get ('proc')#line:1683
        O0O0O0OO0OOOOOOOO ["target"]=O00OOOOOO0O0000OO .get ('target')#line:1685
        O0O0O0OO0OOOOOOOO ["self.quantifiers"]=O0O00000O0000O00O .quantifiers #line:1686
        if O00OOOOOO0O0000OO .get ('cond')!=None :#line:1688
            O0O0O0OO0OOOOOOOO ['cond']=O00OOOOOO0O0000OO .get ('cond')#line:1689
        if O00OOOOOO0O0000OO .get ('ante')!=None :#line:1690
            O0O0O0OO0OOOOOOOO ['ante']=O00OOOOOO0O0000OO .get ('ante')#line:1691
        if O00OOOOOO0O0000OO .get ('succ')!=None :#line:1692
            O0O0O0OO0OOOOOOOO ['succ']=O00OOOOOO0O0000OO .get ('succ')#line:1693
        if O00OOOOOO0O0000OO .get ('opts')!=None :#line:1694
            O0O0O0OO0OOOOOOOO ['opts']=O00OOOOOO0O0000OO .get ('opts')#line:1695
        if O0O00000O0000O00O .df is None :#line:1696
            O0O0O0OO0OOOOOOOO ['rowcount']=O0O00000O0000O00O .data ["rows_count"]#line:1697
        else :#line:1698
            O0O0O0OO0OOOOOOOO ['rowcount']=len (O0O00000O0000O00O .df .index )#line:1699
        O0O0O0O000O0O0O00 ["taskinfo"]=O0O0O0OO0OOOOOOOO #line:1700
        OOOO0O00000O0OOO0 ={}#line:1701
        OOOO0O00000O0OOO0 ["total_verifications"]=O0O00000O0000O00O .stats ['total_cnt']#line:1702
        OOOO0O00000O0OOO0 ["valid_rules"]=O0O00000O0000O00O .stats ['total_valid']#line:1703
        OOOO0O00000O0OOO0 ["total_verifications_with_opt"]=O0O00000O0000O00O .stats ['total_ver']#line:1704
        OOOO0O00000O0OOO0 ["time_prep"]=O0O00000O0000O00O .stats ['end_prep_time']-O0O00000O0000O00O .stats ['start_prep_time']#line:1705
        OOOO0O00000O0OOO0 ["time_processing"]=O0O00000O0000O00O .stats ['end_proc_time']-O0O00000O0000O00O .stats ['start_proc_time']#line:1706
        OOOO0O00000O0OOO0 ["time_total"]=O0O00000O0000O00O .stats ['end_prep_time']-O0O00000O0000O00O .stats ['start_prep_time']+O0O00000O0000O00O .stats ['end_proc_time']-O0O00000O0000O00O .stats ['start_proc_time']#line:1707
        O0O0O0O000O0O0O00 ["summary_statistics"]=OOOO0O00000O0OOO0 #line:1708
        O0O0O0O000O0O0O00 ["rules"]=O0O00000O0000O00O .rulelist #line:1709
        O0O00OOO000000000 ={}#line:1710
        O0O00OOO000000000 ["varname"]=O0O00000O0000O00O .data ["varname"]#line:1711
        O0O00OOO000000000 ["catnames"]=O0O00000O0000O00O .data ["catnames"]#line:1712
        O0O0O0O000O0O0O00 ["datalabels"]=O0O00OOO000000000 #line:1713
        O0O00000O0000O00O .result =O0O0O0O000O0O0O00 #line:1714
    def print_summary (O000O00OO0O0O0O0O ):#line:1716
        ""#line:1719
        if not (O000O00OO0O0O0O0O ._is_calculated ()):#line:1720
            print ("ERROR: Task has not been calculated.")#line:1721
            return #line:1722
        print ("")#line:1723
        print ("CleverMiner task processing summary:")#line:1724
        print ("")#line:1725
        print (f"Task type : {O000O00OO0O0O0O0O.result['taskinfo']['task_type']}")#line:1726
        print (f"Number of verifications : {O000O00OO0O0O0O0O.result['summary_statistics']['total_verifications']}")#line:1727
        print (f"Number of rules : {O000O00OO0O0O0O0O.result['summary_statistics']['valid_rules']}")#line:1728
        print (f"Total time needed : {strftime('%Hh %Mm %Ss', gmtime(O000O00OO0O0O0O0O.result['summary_statistics']['time_total']))}")#line:1729
        print (f"Time of data preparation : {strftime('%Hh %Mm %Ss', gmtime(O000O00OO0O0O0O0O.result['summary_statistics']['time_prep']))}")#line:1731
        print (f"Time of rule mining : {strftime('%Hh %Mm %Ss', gmtime(O000O00OO0O0O0O0O.result['summary_statistics']['time_processing']))}")#line:1732
        print ("")#line:1733
    def print_hypolist (OOOOO0OOOO0OO0OO0 ):#line:1735
        OOOOO0OOOO0OO0OO0 .print_rulelist ();#line:1736
    def print_rulelist (O00OO00OOOOO000O0 ,sortby =None ,storesorted =False ):#line:1738
        if not (O00OO00OOOOO000O0 ._is_calculated ()):#line:1739
            print ("ERROR: Task has not been calculated.")#line:1740
            return #line:1741
        def O00OOO0O00OOO000O (O0OO0OO0O0OOO0OOO ):#line:1742
            OO00OO0OO0000000O =O0OO0OO0O0OOO0OOO ["params"]#line:1743
            return OO00OO0OO0000000O .get (sortby ,0 )#line:1744
        print ("")#line:1746
        print ("List of rules:")#line:1747
        if O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1748
            print ("RULEID BASE  CONF  AAD    Rule")#line:1749
        elif O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="UICMiner":#line:1750
            print ("RULEID BASE  AAD_SCORE  Rule")#line:1751
        elif O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="CFMiner":#line:1752
            print ("RULEID BASE  S_UP  S_DOWN Condition")#line:1753
        elif O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1754
            print ("RULEID BASE1 BASE2 RatioConf DeltaConf Rule")#line:1755
        else :#line:1756
            print ("Unsupported task type for rulelist")#line:1757
            return #line:1758
        OOOOOOOOO0OO0O0OO =O00OO00OOOOO000O0 .result ["rules"]#line:1759
        if sortby is not None :#line:1760
            OOOOOOOOO0OO0O0OO =sorted (OOOOOOOOO0OO0O0OO ,key =O00OOO0O00OOO000O ,reverse =True )#line:1761
            if storesorted :#line:1762
                O00OO00OOOOO000O0 .result ["rules"]=OOOOOOOOO0OO0O0OO #line:1763
        for O0O0OO00O00000000 in OOOOOOOOO0OO0O0OO :#line:1765
            OO0OOOO0000O0OOOO ="{:6d}".format (O0O0OO00O00000000 ["rule_id"])#line:1766
            if O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1767
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["base"])+" "+"{:.3f}".format (O0O0OO00O00000000 ["params"]["conf"])+" "+"{:+.3f}".format (O0O0OO00O00000000 ["params"]["aad"])#line:1769
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +" "+O0O0OO00O00000000 ["cedents_str"]["ante"]+" => "+O0O0OO00O00000000 ["cedents_str"]["succ"]+" | "+O0O0OO00O00000000 ["cedents_str"]["cond"]#line:1770
            elif O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="UICMiner":#line:1771
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["base"])+" "+"{:.3f}".format (O0O0OO00O00000000 ["params"]["aad_score"])#line:1772
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +"     "+O0O0OO00O00000000 ["cedents_str"]["ante"]+" => "+O00OO00OOOOO000O0 .result ['taskinfo']['target']+"(*) | "+O0O0OO00O00000000 ["cedents_str"]["cond"]#line:1773
            elif O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="CFMiner":#line:1774
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["base"])+" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["s_up"])+" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["s_down"])#line:1775
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +" "+O0O0OO00O00000000 ["cedents_str"]["cond"]#line:1776
            elif O00OO00OOOOO000O0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1777
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["base1"])+" "+"{:5d}".format (O0O0OO00O00000000 ["params"]["base2"])+"    "+"{:.3f}".format (O0O0OO00O00000000 ["params"]["ratioconf"])+"    "+"{:+.3f}".format (O0O0OO00O00000000 ["params"]["deltaconf"])#line:1778
                OO0OOOO0000O0OOOO =OO0OOOO0000O0OOOO +"  "+O0O0OO00O00000000 ["cedents_str"]["ante"]+" => "+O0O0OO00O00000000 ["cedents_str"]["succ"]+" | "+O0O0OO00O00000000 ["cedents_str"]["cond"]+" : "+O0O0OO00O00000000 ["cedents_str"]["frst"]+" x "+O0O0OO00O00000000 ["cedents_str"]["scnd"]#line:1779
            print (OO0OOOO0000O0OOOO )#line:1781
        print ("")#line:1782
    def print_hypo (O000000O0OO000000 ,O0O0OOO0OOOOO0000 ):#line:1784
        O000000O0OO000000 .print_rule (O0O0OOO0OOOOO0000 )#line:1785
    def print_rule (OO0OOO000OOOO0OO0 ,OOOOOO0O0OO0O0000 ):#line:1788
        if not (OO0OOO000OOOO0OO0 ._is_calculated ()):#line:1789
            print ("ERROR: Task has not been calculated.")#line:1790
            return #line:1791
        print ("")#line:1792
        if (OOOOOO0O0OO0O0000 <=len (OO0OOO000OOOO0OO0 .result ["rules"])):#line:1793
            if OO0OOO000OOOO0OO0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1794
                print ("")#line:1795
                O0OOO0OO0000O0000 =OO0OOO000OOOO0OO0 .result ["rules"][OOOOOO0O0OO0O0000 -1 ]#line:1796
                print (f"Rule id : {O0OOO0OO0000O0000['rule_id']}")#line:1797
                print ("")#line:1798
                print (f"Base : {'{:5d}'.format(O0OOO0OO0000O0000['params']['base'])}  Relative base : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_base'])}  CONF : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['conf'])}  AAD : {'{:+.3f}'.format(O0OOO0OO0000O0000['params']['aad'])}  BAD : {'{:+.3f}'.format(O0OOO0OO0000O0000['params']['bad'])}")#line:1799
                print ("")#line:1800
                print ("Cedents:")#line:1801
                print (f"  antecedent : {O0OOO0OO0000O0000['cedents_str']['ante']}")#line:1802
                print (f"  succcedent : {O0OOO0OO0000O0000['cedents_str']['succ']}")#line:1803
                print (f"  condition  : {O0OOO0OO0000O0000['cedents_str']['cond']}")#line:1804
                print ("")#line:1805
                print ("Fourfold table")#line:1806
                print (f"    |  S  |  ¬S |")#line:1807
                print (f"----|-----|-----|")#line:1808
                print (f" A  |{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold'][0])}|{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold'][1])}|")#line:1809
                print (f"----|-----|-----|")#line:1810
                print (f"¬A  |{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold'][2])}|{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold'][3])}|")#line:1811
                print (f"----|-----|-----|")#line:1812
            elif OO0OOO000OOOO0OO0 .result ['taskinfo']['task_type']=="CFMiner":#line:1813
                print ("")#line:1814
                O0OOO0OO0000O0000 =OO0OOO000OOOO0OO0 .result ["rules"][OOOOOO0O0OO0O0000 -1 ]#line:1815
                print (f"Rule id : {O0OOO0OO0000O0000['rule_id']}")#line:1816
                print ("")#line:1817
                O00OO00000OOO0OOO =""#line:1818
                if ('aad'in O0OOO0OO0000O0000 ['params']):#line:1819
                    O00OO00000OOO0OOO ="aad : "+str (O0OOO0OO0000O0000 ['params']['aad'])#line:1820
                print (f"Base : {'{:5d}'.format(O0OOO0OO0000O0000['params']['base'])}  Relative base : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_base'])}  Steps UP (consecutive) : {'{:5d}'.format(O0OOO0OO0000O0000['params']['s_up'])}  Steps DOWN (consecutive) : {'{:5d}'.format(O0OOO0OO0000O0000['params']['s_down'])}  Steps UP (any) : {'{:5d}'.format(O0OOO0OO0000O0000['params']['s_any_up'])}  Steps DOWN (any) : {'{:5d}'.format(O0OOO0OO0000O0000['params']['s_any_down'])}  Histogram maximum : {'{:5d}'.format(O0OOO0OO0000O0000['params']['max'])}  Histogram minimum : {'{:5d}'.format(O0OOO0OO0000O0000['params']['min'])}  Histogram relative maximum : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_max'])} Histogram relative minimum : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_min'])} {O00OO00000OOO0OOO}")#line:1822
                print ("")#line:1823
                print (f"Condition  : {O0OOO0OO0000O0000['cedents_str']['cond']}")#line:1824
                print ("")#line:1825
                OO0OO0O00OO0O0OO0 =OO0OOO000OOOO0OO0 .get_category_names (OO0OOO000OOOO0OO0 .result ["taskinfo"]["target"])#line:1826
                print (f"Categories in target variable  {OO0OO0O00OO0O0OO0}")#line:1827
                print (f"Histogram                      {O0OOO0OO0000O0000['params']['hist']}")#line:1828
                if ('aad'in O0OOO0OO0000O0000 ['params']):#line:1829
                    print (f"Histogram on full set          {O0OOO0OO0000O0000['params']['hist_full']}")#line:1830
                    print (f"Relative histogram             {O0OOO0OO0000O0000['params']['rel_hist']}")#line:1831
                    print (f"Relative histogram on full set {O0OOO0OO0000O0000['params']['rel_hist_full']}")#line:1832
            elif OO0OOO000OOOO0OO0 .result ['taskinfo']['task_type']=="UICMiner":#line:1833
                print ("")#line:1834
                O0OOO0OO0000O0000 =OO0OOO000OOOO0OO0 .result ["rules"][OOOOOO0O0OO0O0000 -1 ]#line:1835
                print (f"Rule id : {O0OOO0OO0000O0000['rule_id']}")#line:1836
                print ("")#line:1837
                O00OO00000OOO0OOO =""#line:1838
                if ('aad_score'in O0OOO0OO0000O0000 ['params']):#line:1839
                    O00OO00000OOO0OOO ="aad score : "+str (O0OOO0OO0000O0000 ['params']['aad_score'])#line:1840
                print (f"Base : {'{:5d}'.format(O0OOO0OO0000O0000['params']['base'])}  Relative base : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_base'])}   {O00OO00000OOO0OOO}")#line:1842
                print ("")#line:1843
                print (f"Condition  : {O0OOO0OO0000O0000['cedents_str']['cond']}")#line:1844
                print (f"Antecedent : {O0OOO0OO0000O0000['cedents_str']['ante']}")#line:1845
                print ("")#line:1846
                print (f"Histogram                                        {O0OOO0OO0000O0000['params']['hist']}")#line:1847
                if ('aad_score'in O0OOO0OO0000O0000 ['params']):#line:1848
                    print (f"Histogram on full set with condition             {O0OOO0OO0000O0000['params']['hist_cond']}")#line:1849
                    print (f"Relative histogram                               {O0OOO0OO0000O0000['params']['rel_hist']}")#line:1850
                    print (f"Relative histogram on full set with condition    {O0OOO0OO0000O0000['params']['rel_hist_cond']}")#line:1851
                O0OOOO00OOOO0O000 =OO0OOO000OOOO0OO0 .result ['datalabels']['catnames'][OO0OOO000OOOO0OO0 .result ['datalabels']['varname'].index (OO0OOO000OOOO0OO0 .result ['taskinfo']['target'])]#line:1852
                print (" ")#line:1854
                print ("Interpretation:")#line:1855
                for O000000O00O00OOO0 in range (len (O0OOOO00OOOO0O000 )):#line:1856
                  O0000OO0OO0OO0OO0 =0 #line:1857
                  if O0OOO0OO0000O0000 ['params']['rel_hist'][O000000O00O00OOO0 ]>0 :#line:1858
                      O0000OO0OO0OO0OO0 =O0OOO0OO0000O0000 ['params']['rel_hist'][O000000O00O00OOO0 ]/O0OOO0OO0000O0000 ['params']['rel_hist_cond'][O000000O00O00OOO0 ]#line:1859
                  OOOOOOOO0O0000OO0 =''#line:1860
                  if not (O0OOO0OO0000O0000 ['cedents_str']['cond']=='---'):#line:1861
                      OOOOOOOO0O0000OO0 ="For "+O0OOO0OO0000O0000 ['cedents_str']['cond']+": "#line:1862
                  print (f"    {OOOOOOOO0O0000OO0}{OO0OOO000OOOO0OO0.result['taskinfo']['target']}({O0OOOO00OOOO0O000[O000000O00O00OOO0]}) has an occurrence of {'{:.1%}'.format(O0OOO0OO0000O0000['params']['rel_hist_cond'][O000000O00O00OOO0])}, with antecedent it has an occurrence of {'{:.1%}'.format(O0OOO0OO0000O0000['params']['rel_hist'][O000000O00O00OOO0])}, that is {'{:.3f}'.format(O0000OO0OO0OO0OO0)} times more.")#line:1864
            elif OO0OOO000OOOO0OO0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1865
                print ("")#line:1866
                O0OOO0OO0000O0000 =OO0OOO000OOOO0OO0 .result ["rules"][OOOOOO0O0OO0O0000 -1 ]#line:1867
                print (f"Rule id : {O0OOO0OO0000O0000['rule_id']}")#line:1868
                print ("")#line:1869
                print (f"Base1 : {'{:5d}'.format(O0OOO0OO0000O0000['params']['base1'])} Base2 : {'{:5d}'.format(O0OOO0OO0000O0000['params']['base2'])}  Relative base 1 : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_base1'])} Relative base 2 : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['rel_base2'])} CONF1 : {'{:.3f}'.format(O0OOO0OO0000O0000['params']['conf1'])}  CONF2 : {'{:+.3f}'.format(O0OOO0OO0000O0000['params']['conf2'])}  Delta Conf : {'{:+.3f}'.format(O0OOO0OO0000O0000['params']['deltaconf'])} Ratio Conf : {'{:+.3f}'.format(O0OOO0OO0000O0000['params']['ratioconf'])}")#line:1870
                print ("")#line:1871
                print ("Cedents:")#line:1872
                print (f"  antecedent : {O0OOO0OO0000O0000['cedents_str']['ante']}")#line:1873
                print (f"  succcedent : {O0OOO0OO0000O0000['cedents_str']['succ']}")#line:1874
                print (f"  condition  : {O0OOO0OO0000O0000['cedents_str']['cond']}")#line:1875
                print (f"  first set  : {O0OOO0OO0000O0000['cedents_str']['frst']}")#line:1876
                print (f"  second set : {O0OOO0OO0000O0000['cedents_str']['scnd']}")#line:1877
                print ("")#line:1878
                print ("Fourfold tables:")#line:1879
                print (f"FRST|  S  |  ¬S |  SCND|  S  |  ¬S |");#line:1880
                print (f"----|-----|-----|  ----|-----|-----| ")#line:1881
                print (f" A  |{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold1'][0])}|{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold1'][1])}|   A  |{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold2'][0])}|{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold2'][1])}|")#line:1882
                print (f"----|-----|-----|  ----|-----|-----|")#line:1883
                print (f"¬A  |{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold1'][2])}|{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold1'][3])}|  ¬A  |{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold2'][2])}|{'{:5d}'.format(O0OOO0OO0000O0000['params']['fourfold2'][3])}|")#line:1884
                print (f"----|-----|-----|  ----|-----|-----|")#line:1885
            else :#line:1886
                print ("Unsupported task type for rule details")#line:1887
            print ("")#line:1891
        else :#line:1892
            print ("No such rule.")#line:1893
    def get_rulecount (OOO0O00O0OOO0OO00 ):#line:1895
        if not (OOO0O00O0OOO0OO00 ._is_calculated ()):#line:1896
            print ("ERROR: Task has not been calculated.")#line:1897
            return #line:1898
        return len (OOO0O00O0OOO0OO00 .result ["rules"])#line:1899
    def get_ruletext (OO00O00O0000O0OO0 ,OO00OOO000OO00000 ):#line:1901
        ""#line:1907
        if not (OO00O00O0000O0OO0 ._is_calculated ()):#line:1908
            print ("ERROR: Task has not been calculated.")#line:1909
            return #line:1910
        if OO00OOO000OO00000 <=0 or OO00OOO000OO00000 >OO00O00O0000O0OO0 .get_rulecount ():#line:1911
            if OO00O00O0000O0OO0 .get_rulecount ()==0 :#line:1912
                print ("No such rule. There are no rules in result.")#line:1913
            else :#line:1914
                print (f"No such rule ({OO00OOO000OO00000}). Available rules are 1 to {OO00O00O0000O0OO0.get_rulecount()}")#line:1915
            return None #line:1916
        O0O000OO0OOOOOOOO =""#line:1917
        OO000OO0OO000O000 =OO00O00O0000O0OO0 .result ["rules"][OO00OOO000OO00000 -1 ]#line:1918
        if OO00O00O0000O0OO0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1919
            O0O000OO0OOOOOOOO =O0O000OO0OOOOOOOO +" "+OO000OO0OO000O000 ["cedents_str"]["ante"]+" => "+OO000OO0OO000O000 ["cedents_str"]["succ"]+" | "+OO000OO0OO000O000 ["cedents_str"]["cond"]#line:1921
        elif OO00O00O0000O0OO0 .result ['taskinfo']['task_type']=="UICMiner":#line:1922
            O0O000OO0OOOOOOOO =O0O000OO0OOOOOOOO +"     "+OO000OO0OO000O000 ["cedents_str"]["ante"]+" => "+OO00O00O0000O0OO0 .result ['taskinfo']['target']+"(*) | "+OO000OO0OO000O000 ["cedents_str"]["cond"]#line:1924
        elif OO00O00O0000O0OO0 .result ['taskinfo']['task_type']=="CFMiner":#line:1925
            O0O000OO0OOOOOOOO =O0O000OO0OOOOOOOO +" "+OO000OO0OO000O000 ["cedents_str"]["cond"]#line:1926
        elif OO00O00O0000O0OO0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1927
            O0O000OO0OOOOOOOO =O0O000OO0OOOOOOOO +"  "+OO000OO0OO000O000 ["cedents_str"]["ante"]+" => "+OO000OO0OO000O000 ["cedents_str"]["succ"]+" | "+OO000OO0OO000O000 ["cedents_str"]["cond"]+" : "+OO000OO0OO000O000 ["cedents_str"]["frst"]+" x "+OO000OO0OO000O000 ["cedents_str"]["scnd"]#line:1929
        return O0O000OO0OOOOOOOO #line:1930
    def get_fourfold (O000O0O0O0000O00O ,OO0OOO00O00O00OOO ,order =0 ):#line:1932
        if not (O000O0O0O0000O00O ._is_calculated ()):#line:1933
            print ("ERROR: Task has not been calculated.")#line:1934
            return #line:1935
        if (OO0OOO00O00O00OOO <=len (O000O0O0O0000O00O .result ["rules"])):#line:1936
            if O000O0O0O0000O00O .result ['taskinfo']['task_type']=="4ftMiner":#line:1937
                O000O000OOOOO00O0 =O000O0O0O0000O00O .result ["rules"][OO0OOO00O00O00OOO -1 ]#line:1938
                return O000O000OOOOO00O0 ['params']['fourfold']#line:1939
            elif O000O0O0O0000O00O .result ['taskinfo']['task_type']=="CFMiner":#line:1940
                print ("Error: fourfold for CFMiner is not defined")#line:1941
                return None #line:1942
            elif O000O0O0O0000O00O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1943
                O000O000OOOOO00O0 =O000O0O0O0000O00O .result ["rules"][OO0OOO00O00O00OOO -1 ]#line:1944
                if order ==1 :#line:1945
                    return O000O000OOOOO00O0 ['params']['fourfold1']#line:1946
                if order ==2 :#line:1947
                    return O000O000OOOOO00O0 ['params']['fourfold2']#line:1948
                print ("Error: for SD4ft-Miner, you need to provide order of fourfold table in order= parameter (valid values are 1,2).")#line:1949
                return None #line:1950
            else :#line:1951
                print ("Unsupported task type for rule details")#line:1952
        else :#line:1953
            print ("No such rule.")#line:1954
    def get_hist (OOO0O0O00O0O000O0 ,OO000O0000O00O0O0 ):#line:1956
        if not (OOO0O0O00O0O000O0 ._is_calculated ()):#line:1957
            print ("ERROR: Task has not been calculated.")#line:1958
            return #line:1959
        if (OO000O0000O00O0O0 <=len (OOO0O0O00O0O000O0 .result ["rules"])):#line:1960
            if OOO0O0O00O0O000O0 .result ['taskinfo']['task_type']=="CFMiner":#line:1961
                OO0OOOOOOOO00000O =OOO0O0O00O0O000O0 .result ["rules"][OO000O0000O00O0O0 -1 ]#line:1962
                return OO0OOOOOOOO00000O ['params']['hist']#line:1963
            elif OOO0O0O00O0O000O0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1964
                print ("Error: SD4ft-Miner has no histogram")#line:1965
                return None #line:1966
            elif OOO0O0O00O0O000O0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1967
                print ("Error: 4ft-Miner has no histogram")#line:1968
                return None #line:1969
            else :#line:1970
                print ("Unsupported task type for rule details")#line:1971
        else :#line:1972
            print ("No such rule.")#line:1973
    def get_hist_cond (OOOO0O0OOO0O00000 ,OOOOO0O0O00OOOOOO ):#line:1976
        if not (OOOO0O0OOO0O00000 ._is_calculated ()):#line:1977
            print ("ERROR: Task has not been calculated.")#line:1978
            return #line:1979
        if (OOOOO0O0O00OOOOOO <=len (OOOO0O0OOO0O00000 .result ["rules"])):#line:1980
            if OOOO0O0OOO0O00000 .result ['taskinfo']['task_type']=="UICMiner":#line:1981
                OO00O00OO00OO0OOO =OOOO0O0OOO0O00000 .result ["rules"][OOOOO0O0O00OOOOOO -1 ]#line:1982
                return OO00O00OO00OO0OOO ['params']['hist_cond']#line:1983
            elif OOOO0O0OOO0O00000 .result ['taskinfo']['task_type']=="CFMiner":#line:1984
                OO00O00OO00OO0OOO =OOOO0O0OOO0O00000 .result ["rules"][OOOOO0O0O00OOOOOO -1 ]#line:1985
                return OO00O00OO00OO0OOO ['params']['hist']#line:1986
            elif OOOO0O0OOO0O00000 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1987
                print ("Error: SD4ft-Miner has no histogram")#line:1988
                return None #line:1989
            elif OOOO0O0OOO0O00000 .result ['taskinfo']['task_type']=="4ftMiner":#line:1990
                print ("Error: 4ft-Miner has no histogram")#line:1991
                return None #line:1992
            else :#line:1993
                print ("Unsupported task type for rule details")#line:1994
        else :#line:1995
            print ("No such rule.")#line:1996
    def get_quantifiers (O0000O00000OO0O0O ,OO00O0OO00OOOO00O ,order =0 ):#line:1998
        if not (O0000O00000OO0O0O ._is_calculated ()):#line:1999
            print ("ERROR: Task has not been calculated.")#line:2000
            return #line:2001
        if (OO00O0OO00OOOO00O <=len (O0000O00000OO0O0O .result ["rules"])):#line:2002
            O000000O000000000 =O0000O00000OO0O0O .result ["rules"][OO00O0OO00OOOO00O -1 ]#line:2003
            if O0000O00000OO0O0O .result ['taskinfo']['task_type']=="4ftMiner":#line:2004
                return O000000O000000000 ['params']#line:2005
            elif O0000O00000OO0O0O .result ['taskinfo']['task_type']=="CFMiner":#line:2006
                return O000000O000000000 ['params']#line:2007
            elif O0000O00000OO0O0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:2008
                return O000000O000000000 ['params']#line:2009
            else :#line:2010
                print ("Unsupported task type for rule details")#line:2011
        else :#line:2012
            print ("No such rule.")#line:2013
    def get_varlist (OOOO0OO0O00OO0O00 ):#line:2015
        return OOOO0OO0O00OO0O00 .result ["datalabels"]["varname"]#line:2016
    def get_category_names (OOOOOOO0O000O00OO ,varname =None ,varindex =None ):#line:2018
        OO000O0O0000000O0 =0 #line:2019
        if varindex is not None :#line:2020
            if OO000O0O0000000O0 >=0 &OO000O0O0000000O0 <len (OOOOOOO0O000O00OO .get_varlist ()):#line:2021
                OO000O0O0000000O0 =varindex #line:2022
            else :#line:2023
                print ("Error: no such variable.")#line:2024
                return #line:2025
        if (varname is not None ):#line:2026
            OOO000O000OO0OOO0 =OOOOOOO0O000O00OO .get_varlist ()#line:2027
            OO000O0O0000000O0 =OOO000O000OO0OOO0 .index (varname )#line:2028
            if OO000O0O0000000O0 ==-1 |OO000O0O0000000O0 <0 |OO000O0O0000000O0 >=len (OOOOOOO0O000O00OO .get_varlist ()):#line:2029
                print ("Error: no such variable.")#line:2030
                return #line:2031
        return OOOOOOO0O000O00OO .result ["datalabels"]["catnames"][OO000O0O0000000O0 ]#line:2032
    def print_data_definition (OOO0OO0O000OO0O0O ):#line:2034
        OOO0O0000OO000000 =OOO0OO0O000OO0O0O .get_varlist ()#line:2035
        for O0000OO0O00000OO0 in OOO0O0000OO000000 :#line:2036
            OOO0000O0OO0O0O0O =OOO0OO0O000OO0O0O .get_category_names (O0000OO0O00000OO0 )#line:2037
            OOO0O00O0OO00O000 =""#line:2038
            for O00O0O0O00OOO0OO0 in OOO0000O0OO0O0O0O :#line:2039
                OOO0O00O0OO00O000 =OOO0O00O0OO00O000 +str (O00O0O0O00OOO0OO0 )+" "#line:2040
            OOO0O00O0OO00O000 =OOO0O00O0OO00O000 [:-1 ]#line:2041
            print (f"Variable {O0000OO0O00000OO0} has {len(OOO0000O0OO0O0O0O)} categories: {OOO0O00O0OO00O000}")#line:2042
    def _is_calculated (OO00OO00OO0O0OOOO ):#line:2044
        ""#line:2049
        O000O0000OOO0OO0O =False #line:2050
        if 'taskinfo'in OO00OO00OO0O0OOOO .result :#line:2051
            O000O0000OOO0OO0O =True #line:2052
        return O000O0000OOO0OO0O 