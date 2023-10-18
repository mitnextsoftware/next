from django.urls import path
from . import views

urlpatterns = [

    path('branchmaster', views.create_branchmaster),
    path('searchbranch', views.searchbranch),
    path('updatebranch/<int:id>', views.updatebranch),
    path('deletebranch/<int:id>', views.deletebranch),

    path('departmentmaster', views.create_departmentmaster),
    path('searchdepartment', views.searchdepartment),
    path('updatedepartment/<int:id>', views.updatedepartment),
    path('deletedepartment/<int:id>', views.deletedepartment),

    path('designationmaster', views.create_designationmaster),
    path('searchdesignation', views.searchdesignation),
    path('updatedesignation/<int:id>', views.updatedesignation),
    path('deletedesignation/<int:id>', views.deletedesignation),

    path('divisionmaster', views.create_divisionmaster),
    path('searchdivision', views.searchdivision),
    path('updatedivision/<int:id>', views.updatedivision),
    path('deletedivision/<int:id>', views.deletedivision),

    path('proftaxrangeform', views.create_proftaxrange),
    path('searchproftaxrange', views.searchproftaxrange),
    path('updateproftaxrange/<int:id>', views.updateproftaxrange),
    path('deleteproftaxrange/<int:id>', views.deleteproftaxrange),

    path('daysaccumulationform', views.create_daysacc),
    path('searchdaysacc', views.searchdaysacc),
    path('updatedaysacc/<int:id>', views.updatedaysacc),
    path('deletedaysacc/<int:id>', views.deletedaysacc),

    path('dailyattendancetransactionform', views.create_dailyatttran),
    path('searchdayatttrans', views.searchdayatttrans),
    path('updatedayatttrans/<int:id>', views.updatedayatttrans),
    path('deletedayatttrans/<int:id>', views.deletedayatttrans),

    path('familydetail', views.create_familydetail),
    path('searchfamilydetail', views.searchfamilydetail),
    path('updatefamilydetail/<int:id>', views.updatefamilydetail),
    path('deletefamilydetail/<int:id>', views.deletefamilydetail),

    path('employeeexperience', views.create_employeeexperience),
    path('searchempexperience', views.searchempexperience),
    path('updateempexperience/<int:id>', views.updateempexperience),
    path('deleteempexperience/<int:id>', views.deleteempexperience),

    path('employeetypemaster', views.create_employeetypemaster),
    path('searchemptymast', views.searchemptymast),
    path('updateemptymast/<int:id>', views.updateemptymast),
    path('deleteemptymast/<int:id>', views.deleteemptymast),

    path('grademaster', views.create_grademaster),
    path('searchgrademaster', views.searchgrademaster),
    path('updategrademaster/<int:id>', views.updategrademaster),
    path('deletegrademaster/<int:id>', views.deletegrademaster),

    path('leaveencashmaster', views.create_leaveencashmaster),
    path('searchleaveencashmaster', views.searchleaveencashmaster),
    path('updateleaveencashmaster/<int:id>', views.updateleaveencashmaster),
    path('deleteleaveencashmaster/<int:id>', views.deleteleaveencashmaster),

    path('createemployeemaster', views.create_employeenmaster),
    path('searchemployee', views.searchemployee),
    path('updateemployee/<int:id>', views.updateemployee),
    path('deleteemployee/<int:id>', views.deleteemployee),

    path('createleaveemp', views.create_leaveemp),  # leave en cash trans
    path('searchleave', views.searchleaveemp),
    path('updateleaveemp/<int:id>', views.updateleaveem),
    path('deleteleave/<int:id>', views.deleteleave),

    path('createstate', views.create_statemaster),
    path('searchstate', views.searchstate),
    path('updatestate/<int:id>', views.updatestate),
    path('deletestate/<int:id>', views.deletestate),

    path('createusermaster', views.create_usermaster),
    path('searchuser', views.searchuser),
    path('updateuser/<int:id>', views.updateuser),
    path('deleteuser/<int:id>', views.deleteuser),

    path('createshift', views.create_shiftmaster),
    path('searcshift', views.searchshift),
    path('updateshift/<int:id>', views.updateshift),
    path('deleteshfit/<int:id>', views.deleteshift),

    path('createothsrfacilitie', views.create_otherfacilitie),
    path('searchotherfacilities', views.searchotherfacilitie),
    path('updateotherfacilities/<int:id>', views.updateotherfacilities),
    path('deleteotherfacilities/<int:id>', views.deleteotherfacilities),

    path('createsaladvcal', views.create_saladvcal),
    path('searchsaladvcal', views.searchsaladvcal),
    path('updatesaladvcal/<int:id>', views.updateosaladvcal),
    path('deletesaladvcal/<int:id>', views.deletesaladvcal),

    path('createbrangr', views.create_brangr),
    path('searchbrangr', views.searchbrangr),
    path('updatebrangr/<int:id>', views.updatebrangr),
    path('deletebrangr/<int:id>', views.deletebrangr),

    path('createcomp', views.create_compinfo),
    path('searchcompinfo', views.searchcompinfo),
    path('updatecompinfo/<int:id>', views.updatecompinfo),
    path('deletecompinfo/<int:id>', views.deletecompinfo),

    path('createdailyattendance', views.create_dailyattendance),
    path('searchdailyattendance', views.searchdaily),
    path('updatedailyattendance/<int:id>', views.updatedaily),
    path('deletedailyattendance/<int:id>', views.deletedaily),

    path('createempfand', views.create_empf),
    path('searchempfand', views.searchempf),
    path('updateempfand/<int:id>', views.updateempf),
    path('deleteempfand/<int:id>', views.deleteempf),

    path('insertleavepost', views.insertleavepost),
    path('searchleavepost', views.searchleavepost),
    path('updateleavepost/<int:id>', views.updateleavepost),
    path('deleteleavepost/<int:id>', views.deleteleavepost),

    path('insertleaveposttran', views.insertleaveposttran),
    path('searchleaveposttran', views.searchleaveposttran),
    path('updateleaveposttran/<int:id>', views.updateleaveposttran),
    path('deleteleaveposttran/<int:id>', views.deleteleaveposttran),

    path('inserttemptbl', views.inserttemptbl),
    path('searchtemptbl', views.searchtemptbl),
    path('updatetemptbl/<int:id>', views.updatetemptbl),
    path('deletetemptbl/<int:id>', views.deletetemptbl),

    path('inserttemptblii', views.inserttemptblii),
    path('searchtemptblii', views.searchtemptblii),
    path('updatetemptblii/<int:id>', views.updatetemptblii),
    path('deletetemptblii/<int:id>', views.deletetemptblii),

]
