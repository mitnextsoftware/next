from django import forms
from .models import branchmaster, divisionmaster, proftaxrange, daysaccumulation, dailyattendancetransaction, \
    familydetail, employeeexperience, employeetypemaster, grademaster, leaveencashmaster, employeemaster, leaveemp, \
    statemaster, usermaster, shiftmaster, otherFacilitiesMast, saladvcalculation, brangroupmaster, compinfo, \
    dailyattendancesmaster, empfandf, leavepostmast, leaveposttran, temptbl, temptblii
from .models import departmentmaster
from .models import designationmaster


class branchmasterform(forms.ModelForm):
    class Meta:
        model = branchmaster
        fields = ["branchcode", "branchname"]


class departmentmasterform(forms.ModelForm):
    class Meta:
        model = departmentmaster
        fields = ["departmentcode", "departmentname"]


class designationmasterform(forms.ModelForm):
    class Meta:
        model = designationmaster
        fields = ["DesigCode", "DesigName", "HRACnd", "CACnd", "PACnd", "DACnd", "BonusCnd", "UniformCnd", "VehicalCnd",
                  "UtilityCnd", "DutyCnd", "FieldCnd", "WashCnd", "MedicalCnd", "PayScale"]


class divisionmasterform(forms.ModelForm):
    class Meta:
        model = divisionmaster
        fields = ["DivisionCode", "DivisionName", "TransportAmt", "FoodAmt"]


class proftaxrangeform(forms.ModelForm):
    class Meta:
        model = proftaxrange
        fields = ["state_code", "range1", "tax_amt1", "range2", "tax_amt2", "range3", "tax_amt3", "range4", "tax_amt4",
                  "once_amt"]


class daysaccumulationform(forms.ModelForm):
    class Meta:
        model = daysaccumulation
        fields = ["SrNo", "EmpCode", "EmpName", "Desig", "Grade", "LeaveBalance", "LeaveAllotment", "AllotmentMonth"]


class dailyattendancetransactionform(forms.ModelForm):
    class Meta:
        model = dailyattendancetransaction
        fields = ["RecordNo", "Month", "Year", "EmpCode", "PresentDays", "WeeklyOff", "EL", "EOL", "Holiday", "WP",
                  "HPRH", "ExtraDuty", "Absent", "ESIL", "LWP", "TotDays"]


class familydetailform(forms.ModelForm):
    class Meta:
        model = familydetail
        fields = "__all__"


class employeeexperienceform(forms.ModelForm):
    class Meta:
        model = employeeexperience
        fields = "__all__"


class employeetypemasterform(forms.ModelForm):
    class Meta:
        model = employeetypemaster
        fields = "__all__"


class grademasterform(forms.ModelForm):
    class Meta:
        model = grademaster
        fields = "__all__"


class leaveencashmasterform(forms.ModelForm):
    class Meta:
        model = leaveencashmaster
        fields = "__all__"


class employeemasterform(forms.ModelForm):
    class Meta:
        model = employeemaster
        fields = ["empname", "empshortname"]


class leaveempform(forms.ModelForm):
    class Meta:
        model = leaveemp
        fields = ["basicpay", "leaveencashdate", "leaveencashday", "ltcblog", "ltcfrom", "ltcto"]


class statemasterform(forms.ModelForm):
    class Meta:
        model = statemaster
        fields = ["statecode", "statename"]


class usermasterform(forms.ModelForm):
    class Meta:
        model = usermaster
        fields = ["userid", "username", "usertype", "month", "year", "leavepostpassword"]


class shiftform(forms.ModelForm):
    class Meta:
        model = shiftmaster
        fields = "__all__"


class otherfacilitiesform(forms.ModelForm):
    class Meta:
        model = otherFacilitiesMast
        fields = "__all__"


class saladvcalform(forms.ModelForm):
    class Meta:
        model = saladvcalculation
        fields = "__all__"


class branchgrform(forms.ModelForm):
    class Meta:
        model = brangroupmaster
        fields = "__all__"


class compinfoform(forms.ModelForm):
    class Meta:
        model = compinfo
        fields = "__all__"


class dailyattendanceform(forms.ModelForm):
    class Meta:
        model = dailyattendancesmaster
        fields = "__all__"


class empfandform(forms.ModelForm):
    class Meta:
        model = empfandf
        fields = "__all__"


class leavepostmastform(forms.ModelForm):
    class Meta:
        model = leavepostmast
        fields = ["recordid", "recorddate", "month", "year", "time"]


class leaveposttranform(forms.ModelForm):
    class Meta:
        model = leaveposttran
        fields = ["recordid", "empcode", "leaveqty"]


class temptblform(forms.ModelForm):
    class Meta:
        model = temptbl
        fields = ["empcode", "empname", "pfno", "payablepayment", "specialamt", "ariasamt", "epfamt", "epsamt", "month",
                  "year"]


class temptbliiform(forms.ModelForm):
    class Meta:
        model = temptblii
        fields = ["empcode", "totalearningamt", "month", "year"]
