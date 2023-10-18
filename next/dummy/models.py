from django.db import models


# Create your models here.

class branchmaster(models.Model):
    branchcode = models.CharField(max_length=10)
    branchname = models.CharField(max_length=10)


class departmentmaster(models.Model):
    departmentcode = models.CharField(max_length=10)
    departmentname = models.CharField(max_length=10)


class designationmaster(models.Model):
    DesigCode = models.CharField(max_length=10)
    DesigName = models.CharField(max_length=50)
    HRACnd = models.CharField(max_length=1)
    CACnd = models.CharField(max_length=1)
    PACnd = models.CharField(max_length=1)
    EduCnd = models.CharField(max_length=1)
    DACnd = models.CharField(max_length=1)
    BonusCnd = models.CharField(max_length=1)
    UniformCnd = models.CharField(max_length=1)
    VehicalCnd = models.CharField(max_length=1)
    UtilityCnd = models.CharField(max_length=1)
    DutyCnd = models.CharField(max_length=1)
    FieldCnd = models.CharField(max_length=1)
    WashCnd = models.CharField(max_length=1)
    MedicalCnd = models.CharField(max_length=1)
    PayScale = models.CharField(max_length=50)


class divisionmaster(models.Model):
    DivisionCode = models.CharField(max_length=10)
    DivisionName = models.CharField(max_length=50)
    TransportAmt = models.DecimalField(max_digits=10, decimal_places=2)
    FoodAmt = models.DecimalField(max_digits=10, decimal_places=2)


class proftaxrange(models.Model):
    state_code = models.CharField(max_length=30)
    range1 = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amt1 = models.DecimalField(max_digits=10, decimal_places=2)
    range2 = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amt2 = models.DecimalField(max_digits=10, decimal_places=2)
    range3 = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amt3 = models.DecimalField(max_digits=10, decimal_places=2)
    range4 = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amt4 = models.DecimalField(max_digits=10, decimal_places=2)
    once_amt = models.DecimalField(max_digits=10, decimal_places=2)


class daysaccumulation(models.Model):
    SrNo = models.IntegerField()
    EmpCode = models.CharField(max_length=10)
    EmpName = models.CharField(max_length=50)
    Desig = models.CharField(max_length=50)
    Grade = models.CharField(max_length=50)
    LeaveBalance = models.FloatField()
    LeaveAllotment = models.FloatField()
    AllotmentMonth = models.CharField(max_length=10)


class dailyattendancetransaction(models.Model):
    RecordNo = models.BigIntegerField()
    Month = models.IntegerField()
    Year = models.IntegerField()
    EmpCode = models.CharField(max_length=10)
    PresentDays = models.FloatField()
    WeeklyOff = models.FloatField()
    EL = models.FloatField()
    EOL = models.FloatField()
    Holiday = models.FloatField()
    WP = models.FloatField()
    HPRH = models.FloatField()
    ExtraDuty = models.FloatField()
    Absent = models.FloatField()
    ESIL = models.FloatField()
    LWP = models.FloatField()
    TotDays = models.FloatField()


class familydetail(models.Model):
    EmpCode = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=50)
    FatherDob = models.DateField()
    MotherName = models.CharField(max_length=50)
    MotherDob = models.DateField()
    WifeorHsName = models.CharField(max_length=50)
    wifeorHsdob = models.DateField()
    Son1Name = models.CharField(max_length=50)
    Son1Dob = models.DateField()
    Son2Name = models.CharField(max_length=50)
    Son2Dob = models.DateField()
    DaughterName = models.CharField(max_length=50)
    daughterDob = models.DateField()
    Daughter2Name = models.CharField(max_length=50)
    Daughter2Dob = models.DateField()


class employeeexperience(models.Model):
    EmpCode = models.CharField(max_length=50)
    PrvEmployer1 = models.CharField(max_length=50)
    Designation1 = models.CharField(max_length=50)
    EmpFromDate1 = models.DateField()
    EmpToDate1 = models.DateField()
    PrvEmployer2 = models.CharField(max_length=50)
    Designation2 = models.CharField(max_length=50)
    EmpFromDate2 = models.DateField()
    EmpToDate2 = models.DateField()
    PrvEmployer3 = models.CharField(max_length=50)
    Designation3 = models.CharField(max_length=50)
    EmpFromDate3 = models.DateField()
    EmpToDate3 = models.DateField()
    PrvEmployer4 = models.CharField(max_length=50)
    Designation4 = models.CharField(max_length=50)
    EmpFromDate4 = models.DateField()
    EmpToDate4 = models.DateField()
    PrvEmployer5 = models.CharField(max_length=50)
    Designation5 = models.CharField(max_length=50)
    EmpFromDate5 = models.DateField()
    EmpToDate5 = models.DateField()


class employeetypemaster(models.Model):
    EmpTypeSrNo = models.CharField(max_length=50)
    EmpTypeName = models.CharField(max_length=50)
    EmpTypeShortName = models.CharField(max_length=50)


class grademaster(models.Model):
    GradeCode = models.CharField(max_length=50)
    GradeName = models.CharField(max_length=50)
    SrNo = models.IntegerField()
    Pay1 = models.DecimalField(max_digits=10, decimal_places=2)
    Incr1 = models.DecimalField(max_digits=10, decimal_places=2)
    Pay2 = models.DecimalField(max_digits=10, decimal_places=2)
    Incr2 = models.DecimalField(max_digits=10, decimal_places=2)
    Pay3 = models.DecimalField(max_digits=10, decimal_places=2)
    Incr3 = models.DecimalField(max_digits=10, decimal_places=2)
    Pay4 = models.DecimalField(max_digits=10, decimal_places=2)
    Incr4 = models.DecimalField(max_digits=10, decimal_places=2)
    Per_HRA = models.FloatField()
    Per_CA = models.FloatField()
    Cash_CA = models.DecimalField(max_digits=10, decimal_places=2)
    Per_PA = models.FloatField()
    Per_Edu = models.FloatField()
    Cash_Edu = models.DecimalField(max_digits=10, decimal_places=2)
    Per_DA = models.FloatField()
    Per_Bonus = models.FloatField()
    Uniform_Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Vehical_Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Utility_Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Duty_Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Field_Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Washing_Allowance = models.DecimalField(max_digits=10, decimal_places=2)
    Medical_Allowance = models.DecimalField(max_digits=10, decimal_places=2)


class leaveencashmaster(models.Model):
    EmpCode = models.CharField(max_length=50)
    SrNo = models.IntegerField()


class employeemaster(models.Model):
    # srno = models.FloatField()
    empname = models.CharField(max_length=10)
    empshortname = models.CharField(max_length=10)


class leaveemp(models.Model):  # leave en cash trans
    basicpay = models.FloatField()
    leaveencashdate = models.DateField()
    leaveencashday = models.FloatField()
    ltcblog = models.IntegerField()
    ltcfrom = models.IntegerField()
    ltcto = models.IntegerField()


class statemaster(models.Model):
    statecode = models.IntegerField()
    statename = models.CharField(max_length=10)


class usermaster(models.Model):
    userid = models.IntegerField()
    username = models.CharField(max_length=10)
    usertype = models.CharField(max_length=10)
    month = models.IntegerField()
    year = models.IntegerField()
    leavepostpassword = models.CharField(max_length=10)


# *****************************************************************************************************************

class shiftmaster(models.Model):
    shiftname = models.CharField(max_length=10)
    shiftcode = models.CharField(max_length=10)
    time = models.TimeField()


class otherFacilitiesMast(models.Model):
    EmpCode = models.IntegerField()
    OfAmt1 = models.DecimalField(max_digits=10, decimal_places=2)
    OfDescription1 = models.CharField(max_length=10)
    OfAmt2 = models.DecimalField(max_digits=10, decimal_places=2)
    OfDescription2 = models.CharField(max_length=10)
    OfAmt3 = models.DecimalField(max_digits=10, decimal_places=2)
    OfDescription3 = models.CharField(max_length=10)
    OfAmt4 = models.DecimalField(max_digits=10, decimal_places=2)
    OfDescription4 = models.CharField(max_length=10)
    OfAmt5 = models.DecimalField(max_digits=10, decimal_places=2)
    OfDescription5 = models.CharField(max_length=10)


class saladvcalculation(models.Model):
    SrNo = models.IntegerField()
    EmpCode = models.IntegerField()
    Month = models.IntegerField()
    Year = models.IntegerField()
    BasicPay = models.DecimalField(max_digits=6, decimal_places=2)
    Attendance = models.IntegerField()
    DateOn = models.DateTimeField()
    AccumulateSalAdv = models.DecimalField(max_digits=6, decimal_places=2)
    SalAdv = models.DecimalField(max_digits=6, decimal_places=2)


class brangroupmaster(models.Model):
    BranGrCode = models.CharField(max_length=6)
    BranGrName = models.CharField(max_length=10)


class compinfo(models.Model):
    compid = models.IntegerField()
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    pin = models.IntegerField()
    phoneno = models.IntegerField()
    fax = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.CharField(max_length=30)
    vattin = models.CharField(max_length=10)
    csttin = models.CharField(max_length=10)
    excise = models.CharField(max_length=10)
    pfno = models.IntegerField()
    esino = models.IntegerField()
    EPFPER = models.FloatField()
    EPSPER = models.FloatField()
    MAXEPS = models.FloatField()
    ESIPER = models.FloatField()
    LabourWealfare1 = models.IntegerField()
    LabourWealfare2 = models.IntegerField()
    LabourWealfare3 = models.IntegerField()
    LabourWealfare4 = models.IntegerField()
    LabourWealfare5 = models.IntegerField()
    TaDaper = models.IntegerField()


class dailyattendancesmaster(models.Model):
    RecordNo = models.IntegerField()
    AttendanceDate = models.DateField()


class empfandf(models.Model):
    EmpCode = models.IntegerField()
    DateOfRelieve = models.DateTimeField()
    ActualWorkDays = models.IntegerField()
    WeeklyOff = models.IntegerField()
    CompanyOff = models.IntegerField()
    Holidays = models.IntegerField()
    ElBalance = models.IntegerField()
    TotalDays = models.IntegerField()
    NetPayable = models.DecimalField(max_digits=6, decimal_places=2)
    Remark = models.CharField(max_length=30)
    RecoverBal = models.DecimalField(max_digits=6, decimal_places=2)
    Note = models.CharField(max_length=40)


class leavepostmast(models.Model):
    recordid = models.IntegerField()
    recorddate = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    time = models.CharField(max_length=20)


class leaveposttran(models.Model):
    recordid = models.IntegerField()
    empcode = models.CharField(max_length=10)
    leaveqty = models.DecimalField(max_digits=10, decimal_places=2)


class temptbl(models.Model):
    empcode = models.CharField(max_length=10)
    empname = models.CharField(max_length=50)
    pfno = models.CharField(max_length=50)
    payablepayment = models.DecimalField(max_digits=10, decimal_places=2)
    specialamt = models.DecimalField(max_digits=10, decimal_places=2)
    ariasamt = models.DecimalField(max_digits=10, decimal_places=2)
    epfamt = models.DecimalField(max_digits=10, decimal_places=2)
    epsamt = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField()
    year = models.IntegerField()


class temptblii(models.Model):
    empcode = models.CharField(max_length=10)
    totalearningamt = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField()
    year = models.IntegerField()
