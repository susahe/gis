#Sri Lanka Goverment Service (Grama Niladari Information System here after GIS)
#Cleint Grama Niladari  Mr. Nishantha  (All iland Gramaniladari 1st Place in 2015)
#Project Manager (D.S.S Hettiarachchi - BIT Project )
#This is the Model File of GIS Project This Model Define all models. it consist of  7 Models Which are called
# 1. GramaSevaDivision - (Division which is Grama Nildari Owned )
# 2. Village
# 3. Person
# 4. House
# 5. Land
# 6. Business
# 7. Organization
from django.db import models
from django.utils.timezone import now

class GramasevaDivision(models.Model):
#models adttributes --------------------------------------------------------------------------------------------------------
        gs_division = models.CharField(max_length=300,verbose_name="ග්‍රාම නිලධාරි වසම") #Grama Seva Division
        gs_fname = models.CharField(max_length=100,verbose_name="ග්‍රාමසේවක මහතාගේ මුල් නම") # Person First Name
        gs_lname = models.CharField(max_length=300,verbose_name="ග්‍රාමසේවක මහතාගේ වාසගම") # Person Last Name
        gs_oname =  models.CharField(max_length=300,verbose_name="ග්‍රාමසේවක මහතාගේ අනිකුත් නම්") # Person Other Name
        gs_start_date = models.DateTimeField(default=now,verbose_name="සේවය පටන් ගත් දිනය")
        gs_end_date = models.DateTimeField(verbose_name="සේවය අවසන් කල දිනය ",blank=True)

#----------------------------------------------------------------------------------------------------------------------------
        def __str__(self):
                return self.gs_division
        def get_gs_division(self):
                return self.gs_division
        def set_gs_division(self,gs_d):
                gs_division = gs_d

class Village(models.Model):
#models adttributes --------------------------------------------------------------------------------------------------------
        v_list = (('MW','මහවත්ත'),('SW','සේදවත්ත'),('ER','ඇලකන්ද පාර'),('SR','සුරුවල පාර'),('RA','රදැල්ල'),('TH','තල්ගස්මුල්ල'))
        v_name = models.CharField(max_length=2,choices=v_list,default='MW',verbose_name='ගම') # v_name mean Village Name
        v_road = models.CharField(max_length=200,verbose_name='පාර')  # v_road mean Viallge Road
#----------------------------------------------------------------------------------------------------------------------------
        def __str__(self):
                return self.v_name
#get Methods ==================================================
        def get_v_name(self):
                return self.v_name
        def get_v_road(self):
                return self.v_road
#Set Method ===================================================
        def set_v_name(self,vname):
                v_name= vname
        def set_v_road(self,vroad):
                v_road = vroad


class Person(models.Model):
         v_list  = (('GM','ගෘහමූලික'),('WF','බිරිඳ'),('DT','දුව'),('SN','පුතා'),('MO','මව'),('FR','පියා'),('EB','අයියා'),('ES','අක්කා'),('ST','නංගි'),('BR','මල්ලි'),('SB','සහෝදරයා'),('SS','සහෝදරිය'),('UN','මාමා'),('AN','නැන්දා'),('SM','මෙහෙකරු'),('SF','මෙහකාරිය'),('MN','මුනුබුරා'),('MI','මිනිබිරිය'))
         n_list = (('SI','සිංහල'),('TA','ද්‍රවිඩ'),('MU','මුස්ලිම්'),('BR','බර්ගර්'),('MA','මැලේ'),('OT','වෙනත්'))
         r_list = (('BU','බෙද්ධ'),('RC','කතෝලික'),('HI','හින්දු'),('IS','ඉස්ලාම්'),('CH','ක්‍රිස්තියානි'),('OT','වෙනත්'))
         e_list = (('PS','පාසල් යාමට පෙර'),('PR','පෙර පාසැල්'),('OF','1-5 ශ්‍රේණිය දක්වා'),('FO','5 සිට සා/පෙළ දක්වා'),('OP','සාමන්‍ය පෙළ සමත්'),('UA','උසස් පෙළ දක්වා'),('AP','උසස් පෙළ සමත්'),('DG','උපාධි හා ඊට ඉහල'),('NS','කිසිදා පසැල් නොගිය'))
         d_list = (('SD','සමෘද්ධි සහනාධාරය'),('PD','මහජන ආධාර'),('DD','රෝගාධාර'),('SD','ශිෂ්‍යාධාර'),('ED','වැඩිහිටි ආධාර'))
#models adttributes --------------------------------------------------------------------------------------------------------
         p_fname = models.CharField(max_length=100,verbose_name="මුල්  නම") # Person First Name
         p_lname = models.CharField(max_length=300,verbose_name="වාසගම") # Person Last Name
         p_oname =  models.CharField(max_length=300,verbose_name="අනිකුත් නම්") # Person Other Name
         p_nic   = models.CharField(max_length=12,verbose_name="ජාතික හැඳුනුම්පත් අංකය") # Person National Identity card
         p_type  = models.CharField(max_length=2,choices=v_list,default='GM',verbose_name="ඟාති සම්බන්ධය") # Person Type
         p_edu   = models.CharField(max_length=10,verbose_name= "අධ්‍යාපන සුදුසුකම්",choices=e_list , default='OP')
         p_job   = models.CharField(max_length=10,verbose_name= "රැකියාව")
         p_job_position = models.CharField(max_length=20, verbose_name="තනතුර")
         p_nationality  = models.CharField(max_length=20,verbose_name="ජාතිය",choices = n_list,default='SI')
         p_religion     = models.CharField(max_length=20,verbose_name="ඇාගම",choices = r_list,default='BU')
         p_birthdate    = models.DateField(default="1/1/1977",verbose_name="උපන්දිනය")
         p_gender       = models.CharField(max_length=20,verbose_name="ස්ත්‍රී/ පුරුෂ භාවය")
         p_donation     = models.CharField(max_length=20,verbose_name="රජයෙන් ලබන ආධාර", choices=d_list, default='SD')

#----------------------------------------------------------------------------------------------------------------------------
         def __str__(self):
                return self.p_fname + " " + self.p_oname + " " + self.p_lname
         def get_p_fname(self):
                return self.p_fname


class House(models.Model):
#models adttributes --------------------------------------------------------------------------------------------------------
        h_rlist=(('UL','උළු'),('AS','ඇස්බැස්ටස්'),('TH','තහඩු'),('TS','තාරශීට්'),('CO','කොන්ක්‍රීෟට්'))
        h_flist=(('CE','සිමෙන්ති'),('TE','ටෙරාසෝ'),('MB','මාබල්'),('MT','මැටි'),('CO','කොන්ක්‍රීට්'))
        h_wlist=(('BG','බලොාක් ගල්'),('GD','ගඩොල්'),('MT','මැටි'),('LL','ලෑලි'),('TH','තහඩු'))
        h_shade = models.CharField(max_length=20,verbose_name="වහලය",choices=h_rlist,default="UL")
        h_floor = models.CharField(max_length=20,verbose_name="ගෙබිම",choices=h_flist,default="CE")
        h_wall = models.CharField(max_length=20,verbose_name="බිත්ති",choices=h_wlist,default="BG")
        h_water = models.BooleanField(default=False,verbose_name="ජලය")
        h_elec = models.BooleanField(default=False,verbose_name="විදුලිය")
        h_toilet = models.BooleanField(default=False,verbose_name="වැසිකිලි")
        h_lantel = models.BooleanField(default=False,verbose_name="නිවසේ දුරකථන අංකය")
#----------------------------------------------------------------------------------------------------------------------------

class Land(models.Model):
#models adttributes --------------------------------------------------------------------------------------------------------
        l_list = (('SI','සිංනක්කර'),('AN','අනවසර'),('WB','වාර්ෂික බලපත්‍ර'),('JB','ජයභූමි'),('SB','ස්වර්ණභූමි'),('KU','කුලීකරුවන්'))
        l_period = models.CharField(max_length=10,verbose_name="පදිංචි කාලය")
        l_type = models.CharField(max_length=10,verbose_name="ඉඩමේ වර්ගය",choices=l_list,default='SI')
        l_lno = models.CharField(max_length=10,verbose_name="බලපත්‍ර අංකය")
        l_kno = models.CharField(max_length=10,verbose_name="කට්ටි අංකය")
        l_size = models.CharField(max_length=10,verbose_name="ඉඩමේ ප්‍රමාණය")
#----------------------------------------------------------------------------------------------------------------------------

class Buisness(models.Model):
#models adttributes --------------------------------------------------------------------------------------------------------
        b_name = models.CharField(max_length=300,verbose_name="ව්‍යාපාර නාමය")#Business Name
        b_oname = models.CharField(max_length=100,verbose_name="අයිතිකරුගේ නම")#Business Ower Name
        b_paddress1 = models.CharField(max_length=100,verbose_name="අංකය")#Business Permanent Address
        b_paddress2 = models.CharField(max_length=100,verbose_name="ලිපිනය 1")#Business Permanent Address
        b_paddress3 = models.CharField(max_length=100,verbose_name="ලිපිනය 2")#Business Permanent Address
        b_type = models.CharField(max_length=300,verbose_name="ව්‍යාපාර ස්වභාවය")#Business Type
        b_sdate = models.CharField(max_length=10,verbose_name="ව්‍යාපාරය ආරම්භකල දිනය")#Business Start Date
        b_rnumber = models.CharField(max_length=100,verbose_name="ලියාපදිංචි අංකය")#Business Registration Number
        b_tnumber = models.CharField(max_length=10,verbose_name="ව්‍යාපාරයේ දුරකථන අංකය")#Business Telephone Number
#----------------------------------------------------------------------------------------------------------------------------

        def __str__(self):
                return self.b_name

class Organizations(models.Model):
#models adttributes --------------------------------------------------------------------------------------------------------
        o_name     = models.CharField(max_length=300,verbose_name="සංවිධානයේ නම")#Organization's Name
        o_purpose  = models.CharField(max_length=100,verbose_name="සංවිධානය වීමේ අරමුණ")#Organization's Purpose
        o_address1 = models.CharField(max_length=100,verbose_name="සංවිධානයේ ලිපිනය")#Oranization's Adress
        o_address2 = models.CharField(max_length=100,verbose_name="")#Organization's Address
        o_address3 = models.CharField(max_length=100,verbose_name="")#Organization's Address
        o_rnumber  = models.CharField(max_length=100,verbose_name="සංවිධානයේ ලියාපදිංචි අංකය")#Organization's Register Number
        o_sdate    = models.CharField(max_length=10,verbose_name="සංවිධානය ආරම්භක දිනය")#Organization's Start Date
        o_nmembers = models.CharField(max_length=300,verbose_name="සමාජික සංඛ්‍යාව")#Organization's Number Of Members
        o_sstaff   = models.CharField(max_length=300,verbose_name="ලේකම්ගේ නම")#Organization's Secretary
        o_pstaff   = models.CharField(max_length=300,verbose_name="සභාපතිගේ  නම")#Organization's Prsident
        o_asstaff  = models.CharField(max_length=300,verbose_name="උප ලේකම්ගේ නම")#Organization's Assistant Secretary
        o_apstaff  = models.CharField(max_length=300,verbose_name="උප සභාපතිගේ  නම")#Organization's Assistant President
        o_tstaff   = models.CharField(max_length=300,verbose_name="භාණ්ඩාගාරිකගේ නම")#Organization's Staff
#----------------------------------------------------------------------------------------------------------------------------

        def __str__(self):
                return self.o_name
