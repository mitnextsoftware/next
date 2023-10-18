from django.shortcuts import render, redirect

# Create your views here.

from .models import branchmaster, dailyattendancetransaction, daysaccumulation, divisionmaster, employeeexperience, \
    employeetypemaster, familydetail, grademaster, leaveencashmaster, proftaxrange, compinfo
from .forms import branchmasterform, designationmasterform, divisionmasterform, proftaxrangeform, daysaccumulationform, \
    dailyattendancetransactionform, familydetailform, employeeexperienceform, employeetypemasterform, grademasterform, \
    leaveencashmasterform, dailyattendanceform
from .models import departmentmaster
from .models import designationmaster
from .forms import departmentmasterform

from .forms import *
from .forms import branchmasterform
from .models import divisionmaster
from .forms import divisionmasterform
from .forms import shiftform


def create_branchmaster(request):
    # if request.method == "POST":
    # branchcode = request.POST['branchcode']
    # branchname = request.POST['branchname']

    context = {}
    bmasterform = branchmasterform(request.POST or None)
    if bmasterform.is_valid():
        bmasterform.save()

    context['form'] = bmasterform

    return render(request, "insertbranch.html", context)


def searchbranch(request):
    sal = branchmaster.objects.all()
    return render(request, "searchbranch.html", {'bran': sal})


def updatebranch(request, id):
    branch = branchmaster.objects.get(id=id)
    form = branchmasterform(
        initial={'branchcode': branch.branchcode, 'branchname': branch.branchname})
    if request.method == "POST":
        form = branchmasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchbranch')
            except Exception as e:
                pass
    return render(request, 'updatebranch.html', {'form': form})


def deletebranch(request, id):
    employee = branchmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchbranch')


def create_departmentmaster(request):
    context = {}
    dmasterform = departmentmasterform(request.POST or None)
    if dmasterform.is_valid():
        dmasterform.save()

    context['form'] = dmasterform

    return render(request, "insertdepartment.html", context)


def create_designationmaster(request):
    context = {}
    demasterform = designationmasterform(request.POST or None)
    if demasterform.is_valid():
        demasterform.save()

    context['form'] = demasterform

    return render(request, "insertdesignation.html", context)


def create_divisionmaster(request):
    context = {}
    dimasterform = divisionmasterform(request.POST or None)
    if dimasterform.is_valid():
        dimasterform.save()

    context['form'] = dimasterform

    return render(request, "insertdivision.html", context)


def create_proftaxrange(request):
    context = {}
    protaxrform = proftaxrangeform(request.POST or None)
    if protaxrform.is_valid():
        protaxrform.save()

    context['form'] = protaxrform

    return render(request, "insertproftax.html", context)


def create_daysacc(request):
    context = {}
    daysaccform = daysaccumulationform(request.POST or None)
    if daysaccform.is_valid():
        daysaccform.save()

    context['form'] = daysaccform

    return render(request, "insertdaysacc.html", context)


def create_dailyatttran(request):
    context = {}
    dailyatttranform = dailyattendancetransactionform(request.POST or None)
    if dailyatttranform.is_valid():
        dailyatttranform.save()

    context['form'] = dailyatttranform

    return render(request, "insertdatttran.html", context)


def create_familydetail(request):
    context = {}
    famdetailform = familydetailform(request.POST or None)
    if famdetailform.is_valid():
        famdetailform.save()

    context['form'] = famdetailform

    return render(request, "insertfamilydetail.html", context)


def create_employeeexperience(request):
    context = {}
    empexperform = employeeexperienceform(request.POST or None)
    if empexperform.is_valid():
        empexperform.save()

    context['form'] = empexperform

    return render(request, "insertempexperform.html", context)


def create_employeetypemaster(request):
    context = {}
    emptypemastform = employeetypemasterform(request.POST or None)
    if emptypemastform.is_valid():
        emptypemastform.save()

    context['form'] = emptypemastform

    return render(request, "insertemptypemaster.html", context)


def create_grademaster(request):
    context = {}
    grademastform = grademasterform(request.POST or None)
    if grademastform.is_valid():
        grademastform.save()

    context['form'] = grademastform

    return render(request, "insertgrademaster.html", context)


def create_leaveencashmaster(request):
    context = {}
    leavecashmastform = leaveencashmasterform(request.POST or None)
    if leavecashmastform.is_valid():
        leavecashmastform.save()

    context['form'] = leavecashmastform

    return render(request, "insertleavecashmaster.html", context)


def searchdayatttrans(request):
    sal = dailyattendancetransaction.objects.all()
    return render(request, "searchdayatttrans.html", {'dayatttrans': sal})


def updatedayatttrans(request, id):
    branch = dailyattendancetransaction.objects.get(id=id)
    form = dailyattendancetransactionform(
        initial={'RecordNo': branch.RecordNo, 'Month': branch.Month, 'Year': branch.Year, 'EmpCode': branch.EmpCode,
                 'PresentDays': branch.PresentDays, 'WeeklyOff': branch.WeeklyOff, 'EL': branch.EL, 'EOL': branch.EOL,
                 'Holiday': branch.Holiday, 'WP': branch.WP, 'HPRH': branch.HPRH, 'ExtraDuty': branch.ExtraDuty,
                 'Absent': branch.Absent, 'ESIL': branch.ESIL, 'LWP': branch.LWP, 'TotDays': branch.TotDays, })
    if request.method == "POST":
        form = dailyattendancetransactionform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchdayatttrans')
            except Exception as e:
                pass
    return render(request, 'updatedayatttrans.html', {'form': form})


def deletedayatttrans(request, id):
    employee = dailyattendancetransaction.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchdayatttrans')


def searchdaysacc(request):
    sal = daysaccumulation.objects.all()
    return render(request, "searchdaysacc.html", {'daysacc': sal})


def updatedaysacc(request, id):
    branch = daysaccumulation.objects.get(id=id)
    form = daysaccumulationform(
        initial={'SrNo': branch.SrNo, 'EmpCode': branch.EmpCode, 'EmpName': branch.EmpName, 'Desig': branch.Desig,
                 'Grade': branch.Grade, 'LeaveBalance': branch.LeaveBalance, 'LeaveAllotment': branch.LeaveAllotment,
                 'AllotmentMonth': branch.AllotmentMonth, })
    if request.method == "POST":
        form = daysaccumulationform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchdaysacc')
            except Exception as e:
                pass
    return render(request, 'updatedaysacc.html', {'form': form})


def deletedaysacc(request, id):
    employee = daysaccumulation.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchdaysacc')


def searchdepartment(request):
    sal = departmentmaster.objects.all()
    return render(request, "searchdepartment.html", {'depart': sal})


def updatedepartment(request, id):
    branch = departmentmaster.objects.get(id=id)
    form = departmentmasterform(
        initial={'departmentcode': branch.departmentcode, 'departmentname': branch.departmentname, })
    if request.method == "POST":
        form = departmentmasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchdepartment')
            except Exception as e:
                pass
    return render(request, 'updatedepartment.html', {'form': form})


def deletedepartment(request, id):
    employee = departmentmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchdepartment')


def searchdesignation(request):
    sal = designationmaster.objects.all()
    return render(request, "searchdesignation.html", {'design': sal})


def updatedesignation(request, id):
    branch = designationmaster.objects.get(id=id)
    form = designationmasterform(
        initial={'DesigCode': branch.DesigCode, 'DesigName': branch.DesigName, 'HRACnd': branch.HRACnd,
                 'CACnd': branch.CACnd, 'PACnd': branch.PACnd, 'EduCnd': branch.EduCnd, 'DACnd': branch.DACnd,
                 'BonusCnd': branch.BonusCnd, 'UniformCnd': branch.UniformCnd, 'VehicalCnd': branch.VehicalCnd,
                 'UtilityCnd': branch.UtilityCnd, 'DutyCnd': branch.DutyCnd, 'FieldCnd': branch.FieldCnd,
                 'WashCnd': branch.WashCnd, 'MedicalCnd': branch.MedicalCnd, 'PayScale': branch.PayScale, })
    if request.method == "POST":
        form = designationmasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchdesignation')
            except Exception as e:
                pass
    return render(request, 'updatedesignation.html', {'form': form})


def deletedesignation(request, id):
    employee = designationmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchdesignation')


def searchdivision(request):
    sal = divisionmaster.objects.all()
    return render(request, "searchdivision.html", {'divi': sal})


def updatedivision(request, id):
    branch = divisionmaster.objects.get(id=id)
    form = divisionmasterform(
        initial={'DivisionCode': branch.DivisionCode, 'DivisionName': branch.DivisionName,
                 'TransportAmt': branch.TransportAmt, 'FoodAmt': branch.FoodAmt, })
    if request.method == "POST":
        form = divisionmasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchdivision')
            except Exception as e:
                pass
    return render(request, 'updatedivision.html', {'form': form})


def deletedivision(request, id):
    employee = divisionmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchdivision')


def searchempexperience(request):
    sal = employeeexperience.objects.all()
    return render(request, "searchempexperience.html", {'experi': sal})


def updateempexperience(request, id):
    branch = employeeexperience.objects.get(id=id)
    form = employeeexperienceform(
        initial={'EmpCode': branch.EmpCode, 'PrvEmployer1': branch.PrvEmployer1, 'Designation1': branch.Designation1,
                 'EmpFromDate1': branch.EmpFromDate1, 'EmpToDate1': branch.EmpToDate1,
                 'PrvEmployer2': branch.PrvEmployer2, 'Designation2': branch.Designation2,
                 'EmpFromDate2': branch.EmpFromDate2, 'EmpToDate2': branch.EmpToDate2,
                 'PrvEmployer3': branch.PrvEmployer3, 'Designation3': branch.Designation3,
                 'EmpFromDate3': branch.EmpFromDate3, 'EmpToDate3': branch.EmpToDate3,
                 'PrvEmployer4': branch.PrvEmployer4, 'Designation4': branch.Designation4,
                 'EmpFromDate4': branch.EmpFromDate4, 'EmpToDate4': branch.EmpToDate4,
                 'PrvEmployer5': branch.PrvEmployer5, 'Designation5': branch.Designation5,
                 'EmpFromDate5': branch.EmpFromDate5, 'EmpToDate5': branch.EmpToDate5, })
    if request.method == "POST":
        form = employeeexperienceform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchempexperience')
            except Exception as e:
                pass
    return render(request, 'updateempexperience.html', {'form': form})


def deleteempexperience(request, id):
    employee = employeeexperience.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchempexperience')


def searchemptymast(request):
    sal = employeetypemaster.objects.all()
    return render(request, "searchemptymast.html", {'emptymast': sal})


def updateemptymast(request, id):
    branch = employeetypemaster.objects.get(id=id)
    form = employeetypemasterform(
        initial={'EmpTypeSrNo': branch.EmpTypeSrNo, 'EmpTypeName': branch.EmpTypeName,
                 'EmpTypeShortName': branch.EmpTypeShortName, })
    if request.method == "POST":
        form = employeetypemasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchemptymast')
            except Exception as e:
                pass
    return render(request, 'updateemptymast.html', {'form': form})


def deleteemptymast(request, id):
    employee = employeetypemaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchemptymast')


def searchfamilydetail(request):
    sal = familydetail.objects.all()
    return render(request, "searchfamilydetail.html", {'family': sal})


def updatefamilydetail(request, id):
    branch = familydetail.objects.get(id=id)
    form = familydetailform(
        initial={'EmpCode': branch.EmpCode, 'FatherName': branch.FatherName, 'FatherDob': branch.FatherDob,
                 'MotherName': branch.MotherName, 'MotherDob': branch.MotherDob, 'WifeorHsName': branch.WifeorHsName,
                 'wifeorHsdob': branch.wifeorHsdob, 'Son1Name': branch.Son1Name, 'Son1Dob': branch.Son1Dob,
                 'Son2Name': branch.Son2Name, 'Son2Dob': branch.Son2Dob, 'DaughterName': branch.DaughterName,
                 'daughterDob': branch.daughterDob, 'Daughter2Name': branch.Daughter2Name,
                 'Daughter2Dob': branch.Daughter2Dob, })
    if request.method == "POST":
        form = familydetailform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchfamilydetail')
            except Exception as e:
                pass
    return render(request, 'updatefamilydetail.html', {'form': form})


def deletefamilydetail(request, id):
    employee = familydetail.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchfamilydetail')


def searchgrademaster(request):
    sal = grademaster.objects.all()
    return render(request, "searchgrademaster.html", {'grade': sal})


def updategrademaster(request, id):
    branch = grademaster.objects.get(id=id)
    form = grademasterform(
        initial={'GradeCode': branch.GradeCode, 'GradeName': branch.GradeName, 'SrNo': branch.SrNo, 'Pay1': branch.Pay1,
                 'Incr1': branch.Incr1,
                 'Pay2': branch.Pay2, 'Incr2': branch.Incr2, 'Pay3': branch.Pay3, 'Incr3': branch.Incr3,
                 'Pay4': branch.Pay4, 'Incr4': branch.Incr4, 'Per_HRA': branch.Per_HRA,
                 'Per_CA': branch.Per_CA, 'Cash_CA': branch.Cash_CA, 'Per_PA': branch.Per_PA, 'Per_Edu': branch.Per_Edu,
                 'Cash_Edu': branch.Cash_Edu, 'Per_DA': branch.Per_DA, 'Per_Bonus': branch.Per_Bonus,
                 'Uniform_Allowance': branch.Uniform_Allowance, 'Vehical_Allowance': branch.Vehical_Allowance,
                 'Utility_Allowance': branch.Utility_Allowance, 'Duty_Allowance': branch.Duty_Allowance,
                 'Field_Allowance': branch.Field_Allowance, 'Washing_Allowance': branch.Washing_Allowance,
                 'Medical_Allowance': branch.Medical_Allowance,
                 })
    if request.method == "POST":
        form = grademasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchgrademaster')
            except Exception as e:
                pass
    return render(request, 'updategrademaster.html', {'form': form})


def deletegrademaster(request, id):
    employee = grademaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchgrademaster')


def searchleaveencashmaster(request):
    sal = leaveencashmaster.objects.all()
    return render(request, "searchleaveencashmaster.html", {'leavem': sal})


def updateleaveencashmaster(request, id):
    branch = leaveencashmaster.objects.get(id=id)
    form = leaveencashmasterform(
        initial={'EmpCode': branch.EmpCode, 'SrNo': branch.SrNo, })
    if request.method == "POST":
        form = leaveencashmasterform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchleaveencashmaster')
            except Exception as e:
                pass
    return render(request, 'updateleaveencashmaster.html', {'form': form})


def deleteleaveencashmaster(request, id):
    employee = leaveencashmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchleaveencashmaster')


def searchproftaxrange(request):
    sal = proftaxrange.objects.all()
    return render(request, "searchproftaxrange.html", {'protax': sal})


def updateproftaxrange(request, id):
    branch = proftaxrange.objects.get(id=id)
    form = proftaxrangeform(
        initial={'state_code': branch.state_code, 'range1': branch.range1, 'tax_amt1': branch.tax_amt1,
                 'range2': branch.range2, 'tax_amt2': branch.tax_amt2, 'range3': branch.range3,
                 'tax_amt3': branch.tax_amt3, 'range4': branch.range4,
                 'tax_amt4': branch.tax_amt4, 'once_amt': branch.once_amt, })
    if request.method == "POST":
        form = proftaxrangeform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchproftaxrange')
            except Exception as e:
                pass
    return render(request, 'updateproftaxrange.html', {'form': form})


def deleteproftaxrange(request, id):
    employee = proftaxrange.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchproftaxrange')


# *******************************************************************************************************

def create_employeenmaster(request):
    context = {}
    bemployeeform = employeemasterform(request.POST or None)
    if bemployeeform.is_valid():
        bemployeeform.save()
    context['form'] = bemployeeform
    return render(request, "insertemployee.html", context)


def searchemployee(request):
    bemployee = employeemaster.objects.all()
    return render(request, "searchemployee.html", {'employee': bemployee})


def updateemployee(request, id):
    employee = employeemaster.objects.get(id=id)
    form = employeemasterform(
        initial={'empname': employee.empname, 'empshortname': employee.empshortname})
    if request.method == "POST":
        form = employeemasterform(request.POST, instance=employee)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchemployee')
            except Exception as e:
                pass
    return render(request, 'updateemployee.html', {'form': form})


def deleteemployee(request, id):
    employee = employeemaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchemployee')


# *****************************************************************************************

def create_leaveemp(request):
    context = {}
    aleaveempform = leaveempform(request.POST or None)
    if aleaveempform.is_valid():
        aleaveempform.save()
    context['form'] = aleaveempform
    return render(request, "insertleaveemp.html", context)


def searchleaveemp(request):
    leave = leaveemp.objects.all()
    return render(request, "searcheleveemp.html", {'employee': leave})


def updateleaveem(request, id):
    employee = leaveemp.objects.get(id=id)
    form = leaveempform(
        initial={'basicpay': employee.basicpay, 'leaveencashdate': employee.leaveencashdate,
                 'leaveencashday': employee.leaveencashday, 'ltcblog': employee.ltcblog, 'ltcfrom': employee.ltcfrom,
                 'ltcto': employee.ltcto})
    if request.method == "POST":
        form = leaveempform(request.POST, instance=employee)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchleave')
            except Exception as e:
                pass
    return render(request, 'updateleaveemp.html', {'form': form})


def deleteleave(request, id):
    employee = leaveemp.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchleave')


# *****************************************************************************8

def create_statemaster(request):
    context = {}
    bstateform = statemasterform(request.POST or None)
    if bstateform.is_valid():
        bstateform.save()
    context['form'] = bstateform
    return render(request, "insertstatemaster.html", context)


def searchstate(request):
    leave = statemaster.objects.all()
    return render(request, "searchstate.html", {'state': leave})


def updatestate(request, id):
    state = statemaster.objects.get(id=id)
    form = statemasterform(
        initial={'empname': state.statecode, 'empshortname': state.statename})
    if request.method == "POST":
        form = statemasterform(request.POST, instance=state)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchstate')
            except Exception as e:
                pass
    return render(request, 'updatestate.html', {'form': form})


def deletestate(request, id):
    employee = statemaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchstate')


# *************************************************************

def create_usermaster(request):
    context = {}
    user = usermasterform(request.POST or None)
    if user.is_valid():
        user.save()
    context['form'] = user
    return render(request, "insertuser.html", context)


def searchuser(request):
    user = usermaster.objects.all()
    return render(request, "searchuser.html", {'master': user})


def updateuser(request, id):
    master = usermaster.objects.get(id=id)
    form = usermasterform(
        initial={'userid': master.userid, 'username': master.username, 'usertype': master.usertype,
                 'month': master.month, 'year': master.year, 'leavepostpassword': master.leavepostpassword})
    if request.method == "POST":
        form = usermasterform(request.POST, instance=master)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchuser')
            except Exception as e:
                pass
    return render(request, 'updateuser.html', {'form': form})


def deleteuser(request, id):
    master = usermaster.objects.get(id=id)
    try:
        master.delete()
    except:
        pass
    return redirect('/searchuser')


# ************************************************************************************************************

def create_shiftmaster(request):
    context = {}
    bshiftform = shiftform(request.POST or None)
    if bshiftform.is_valid():
        bshiftform.save()
    context['form'] = bshiftform
    return render(request, "insertshift.html", context)


def searchshift(request):
    leave = shiftmaster.objects.all()
    return render(request, "searchshift.html", {'employee': leave})


def updateshift(request, id):
    employee = shiftmaster.objects.get(id=id)
    form = shiftform(
        initial={'shiftname': employee.shiftname, 'shiftcode': employee.shiftcode, 'time': employee.time})
    if request.method == "POST":
        form = shiftform(request.POST, instance=employee)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searcshift')
            except Exception as e:
                pass
    return render(request, 'updateshift.html', {'form': form})


def deleteshift(request, id):
    employee = shiftmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searcshift')


# ********************************************************************************************************************

def create_otherfacilitie(request):
    context = {}
    botherform = otherfacilitiesform(request.POST or None)
    if botherform.is_valid():
        botherform.save()
    context['form'] = botherform
    return render(request, "insertotherfacilitiesmast.html", context)


def searchotherfacilitie(request):
    user = otherFacilitiesMast.objects.all()
    return render(request, "searchotherfacilities.html", {'facilities': user})


def updateotherfacilities(request, id):
    employee = otherFacilitiesMast.objects.get(id=id)
    form = otherfacilitiesform(
        initial={'EmpCode': employee.EmpCode, 'OfAmt1': employee.OfAmt1, 'OfDescription1': employee.OfDescription1,
                 'OfAmt2': employee.OfAmt2, 'OfDescription2': employee.OfDescription2, 'OfAmt3': employee.OfAmt3,
                 'OfDescription3': employee.OfDescription3, 'OfAmt4': employee.OfAmt4,
                 'OfDescription4': employee.OfDescription4, 'OfAmt5': employee.OfAmt5,
                 'OfDescription5': employee.OfDescription5})
    if request.method == "POST":
        form = otherfacilitiesform(request.POST, instance=employee)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchotherfacilities')
            except Exception as e:
                pass
    return render(request, 'updateotherfacilities.html', {'form': form})


def deleteotherfacilities(request, id):
    employee = otherFacilitiesMast.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchotherfacilities')


# **************************************************************************************************88
def create_saladvcal(request):
    context = {}
    bsalform = saladvcalform(request.POST or None)
    if bsalform.is_valid():
        bsalform.save()
    context['form'] = bsalform
    return render(request, "insertsaladvcal.html", context)


def searchsaladvcal(request):
    sal = saladvcalculation.objects.all()
    return render(request, "searchsaladvcal.html", {'cal': sal})


def updateosaladvcal(request, id):
    sal = saladvcalculation.objects.get(id=id)
    form = saladvcalform(
        initial={'SrNo': sal.SrNo, 'EmpCode': sal.EmpCode, 'Month': sal.Month, 'Year': sal.Year,
                 'BasicPay': sal.BasicPay, 'Attendance': sal.Attendance, 'DateOn': sal.DateOn,
                 'AccumulateSalAdv': sal.AccumulateSalAdv, 'SalAdv': sal.SalAdv})
    if request.method == "POST":
        form = saladvcalform(request.POST, instance=sal)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchsaladvcal')
            except Exception as e:
                pass
    return render(request, 'updatesaladvcal.html', {'form': form})


def deletesaladvcal(request, id):
    employee = saladvcalculation.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchsaladvcal')


# ***************************************

def create_brangr(request):
    context = {}
    bbrangrform = branchgrform(request.POST or None)
    if bbrangrform.is_valid():
        bbrangrform.save()
    context['form'] = bbrangrform
    return render(request, "insertbrangroup.html", context)


def searchbrangr(request):
    sal = brangroupmaster.objects.all()
    return render(request, "searchbrangr.html", {'bran': sal})


def updatebrangr(request, id):
    branch = brangroupmaster.objects.get(id=id)
    form = branchgrform(
        initial={'BranGrCode': branch.BranGrCode, 'BranGrName': branch.BranGrName})
    if request.method == "POST":
        form = branchgrform(request.POST, instance=branch)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchbrangr')
            except Exception as e:
                pass
    return render(request, 'updatebrangr.html', {'form': form})


def deletebrangr(request, id):
    employee = brangroupmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchbrangr')


# *******************************
def create_compinfo(request):
    context = {}
    compform = compinfoform(request.POST or None)
    if compform.is_valid():
        compform.save()
    context['form'] = compform
    return render(request, "insertcompinfo.html", context)


def searchcompinfo(request):
    info = compinfo.objects.all()
    return render(request, "searchcompinfo.html", {'comp': info})


def updatecompinfo(request, id):
    sal = compinfo.objects.get(id=id)
    form = compinfoform(
        initial={'compid': sal.compid, 'name': sal.name, 'address': sal.address, 'city': sal.city, 'pin': sal.pin,
                 'phoneno': sal.phoneno, 'fax': sal.fax, 'email': sal.email, 'website': sal.website,
                 'vattin': sal.vattin, 'csttin': sal.csttin, 'excise': sal.excise, 'pfno': sal.pfno, 'esino': sal.esino,
                 'EPFPER': sal.EPFPER, 'EPSPER': sal.EPSPER, 'MAXEPS': sal.MAXEPS, 'ESIPER': sal.ESIPER,
                 'LabourWealfare1': sal.LabourWealfare1, 'LabourWealfare2': sal.LabourWealfare2,
                 'LabourWealfare3': sal.LabourWealfare3, 'LabourWealfare4': sal.LabourWealfare4,
                 'LabourWealfare5': sal.LabourWealfare5, 'TaDaper': sal.TaDaper})
    if request.method == "POST":
        form = compinfoform(request.POST, instance=sal)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchcompinfo')
            except Exception as e:
                pass
    return render(request, 'updatecompinfo.html', {'form': form})


def deletecompinfo(request, id):
    employee = compinfo.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchcompinfo')


# ***********************************
def create_dailyattendance(request):
    context = {}
    dailyform = dailyattendanceform(request.POST or None)
    if dailyform.is_valid():
        dailyform.save()
    context['form'] = dailyform
    return render(request, "insertdailyattendance.html", context)


def searchdaily(request):
    leave = dailyattendancesmaster.objects.all()
    return render(request, "searchdailyattendance.html", {'daily': leave})


def updatedaily(request, id):
    attendance = dailyattendancesmaster.objects.get(id=id)
    form = dailyattendanceform(
        initial={'RecordNo': attendance.RecordNo, 'AttendanceDate': attendance.AttendanceDate})
    if request.method == "POST":
        form = dailyattendanceform(request.POST, instance=attendance)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchdailyattendance')
            except Exception as e:
                pass
    return render(request, 'updatedailyattendance.html', {'form': form})


def deletedaily(request, id):
    employee = dailyattendancesmaster.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchdailyattendance')


# *****************

def create_empf(request):
    context = {}
    empfform = empfandform(request.POST or None)
    if empfform.is_valid():
        empfform.save()
    context['form'] = empfform
    return render(request, "insertempfand.html", context)


def searchempf(request):
    emp = empfandf.objects.all()
    return render(request, "searchempfand.html", {'fand': emp})


def updateempf(request, id):
    emp = empfandf.objects.get(id=id)
    form = empfandform(
        initial={'EmpCode': emp.EmpCode, 'DateOfRelieve': emp.DateOfRelieve, 'ActualWorkDays': emp.ActualWorkDays,
                 'WeeklyOff': emp.WeeklyOff, 'CompanyOff': emp.CompanyOff, 'Holidays': emp.Holidays,
                 'ElBalance': emp.ElBalance, 'TotalDays': emp.TotalDays, 'NetPayable': emp.NetPayable,
                 'Remark': emp.Remark, 'RecoverBal': emp.RecoverBal, 'Note': emp.Note})
    if request.method == "POST":
        form = empfandform(request.POST, instance=emp)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchempfand')
            except Exception as e:
                pass
    return render(request, 'updateempfand.html', {'form': form})


def deleteempf(request, id):
    employee = empfandf.objects.get(id=id)
    try:
        employee.delete()
    except:
        pass
    return redirect('/searchempfand')


# ***************************************

def insertleavepost(request):
    context = {}
    lpostform = leavepostmastform(request.POST or None)
    print(lpostform.is_valid())
    if lpostform.is_valid():
        lpostform.save()

    context['form'] = lpostform
    return render(request, "insertleavepost.html", context)


def searchleavepost(request):
    leaveposts = leavepostmast.objects.all()
    return render(request, "searchleavepost.html", {'leavepost': leaveposts})


def updateleavepost(request, id):
    leavepost = leavepostmast.objects.get(id=id)
    form = leavepostmastform(
        initial={'recordid': leavepost.recordid, 'recorddate': leavepost.recorddate, 'month': leavepost.month,
                 'year': leavepost.year, 'time': leavepost.time})
    if request.method == "POST":
        form = leavepostmastform(request.POST, instance=leavepost)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchleavepost')
            except Exception as e:
                pass
    return render(request, 'updateleavepost.html', {'form': form})


def deleteleavepost(request, id):
    user = leavepostmast.objects.get(id=id)
    try:
        user.delete()
    except:
        pass
    return redirect('/searchleavepost')


# leaveposttran

def insertleaveposttran(request):
    context = {}
    lposttranform = leaveposttranform(request.POST or None)
    print(lposttranform.is_valid())
    if lposttranform.is_valid():
        lposttranform.save()

    context['form'] = lposttranform
    return render(request, "insertleaveposttran.html", context)


def searchleaveposttran(request):
    leavepostts = leaveposttran.objects.all()
    return render(request, "searchleaveposttran.html", {'leavepostt': leavepostts})


def updateleaveposttran(request, id):
    leavepost = leaveposttran.objects.get(id=id)
    form = leaveposttranform(
        initial={'recordid': leavepost.recordid, 'empcode': leavepost.empcode, 'leaveqty': leavepost.leaveqty})
    if request.method == "POST":
        form = leaveposttranform(request.POST, instance=leavepost)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchleaveposttran')
            except Exception as e:
                pass
    return render(request, 'updateleaveposttran.html', {'form': form})


def deleteleaveposttran(request, id):
    user = leaveposttran.objects.get(id=id)
    try:
        user.delete()
    except:
        pass
    return redirect('/searchleaveposttran')


def inserttemptbl(request):
    context = {}
    ttblform = temptblform(request.POST or None)
    print(ttblform.is_valid())
    if ttblform.is_valid():
        ttblform.save()

    context['form'] = ttblform
    return render(request, "inserttemptbl.html", context)


def searchtemptbl(request):
    tetbls = temptbl.objects.all()
    return render(request, "searchtemptbl.html", {'tetbl': tetbls})


def updatetemptbl(request, id):
    teptbl = temptbl.objects.get(id=id)
    form = temptblform(
        initial={'empcode': teptbl.empcode, 'empname': teptbl.empname, 'pfno': teptbl.pfno,
                 'payablepayment': teptbl.payablepayment, 'specialamt': teptbl.specialamt, 'ariasamt': teptbl.ariasamt,
                 'epfamt': teptbl.epfamt, 'epsamt': teptbl.epsamt, 'month': teptbl.month, 'year': teptbl.year})
    if request.method == "POST":
        form = temptblform(request.POST, instance=teptbl)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchtemptbl')
            except Exception as e:
                pass
    return render(request, 'updatetemptbl.html', {'form': form})


def deletetemptbl(request, id):
    user = temptbl.objects.get(id=id)
    try:
        user.delete()
    except:
        pass
    return redirect('/searchtemptbl')


# temptblii

def inserttemptblii(request):
    context = {}
    ttbliiform = temptbliiform(request.POST or None)
    print(ttbliiform.is_valid())
    if ttbliiform.is_valid():
        ttbliiform.save()

    context['form'] = ttbliiform
    return render(request, "inserttemptblii.html", context)


def searchtemptblii(request):
    tetbliis = temptblii.objects.all()
    return render(request, "searchtemptblii.html", {'tetblii': tetbliis})


def updatetemptblii(request, id):
    ttblii = temptblii.objects.get(id=id)
    form = temptbliiform(
        initial={'empcode': ttblii.empcode, 'totalearningamt': ttblii.totalearningamt, 'month': ttblii.month,
                 'year': ttblii.year})
    if request.method == "POST":
        form = temptbliiform(request.POST, instance=ttblii)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/searchtemptblii')
            except Exception as e:
                pass
    return render(request, 'updatetemptblii.html', {'form': form})


def deletetemptblii(request, id):
    user = temptblii.objects.get(id=id)
    try:
        user.delete()
    except:
        pass
    return redirect('/searchtemptblii')
