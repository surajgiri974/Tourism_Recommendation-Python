from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
import js2py, datetime
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def home(request):
    return render(request, 'Tourism/index.html')


def SessionUser(request):
    request.session['userName'] = 'User'
    s = request.session['userName']
    return HttpResponse(s)


def login(request):
    return render(request, 'Tourism/login.html')


def register(request):
    return render(request, 'Tourism/login.html')


def registered_check(request):
    try:
        username = request.POST['username']
        pw = request.POST['pw']
        pw1 = request.POST['pw1']
        email = request.POST['email']
        import re
        reg = re.compile('\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        if reg.match(email):
            if username != '':
                if pw == pw1:
                    q = 'INSERT INTO `trs_customer_login`(`customer_userid`, `customer_userpw`, `customer_email`) VALUES (%s,%s,%s)'
                    v = (username, pw, email)
                    cursor = connection.cursor()
                    cursor.execute(q, v)
                    messages.success(request, 'Successfully Registered')
                    return render(request, 'Tourism/index.html')
                else:
                    messages.warning(request, 'Password Do Not Match')
                    return render(request, 'Tourism/login.html')
            else:
                messages.warning(request, 'Username is Invalid')
                return render(request, 'Tourism/login.html')
        else:
            messages.warning(request,'Email is Invalid')
            return render(request,'Tourism/login.html')
    except:
        messages.warning(request, 'Having Trouble in Registering!!')
        return render(request, 'Tourism/login.html')


def login_check(request):
    try:
        trs_id = request.POST['useremail']
        trs_pw = request.POST['userpw']
        if trs_id == '' and trs_pw == '':
            messages.warning(request, 'Fields Are Empty !!')
            return render(request, 'Tourism/index.html')
        else:
            q = 'SELECT * FROM `trs_customer_login` WHERE `customer_userid` = %s and `customer_userpw` = %s '
            v = (trs_id, trs_pw)
            print(trs_id, trs_pw)
            cursor = connection.cursor()
            cursor.execute(q, v)
            messages.success(request, 'Login Successfully!!')
            del request.session['name']
            request.session['name1'] = trs_id
            return render(request, 'Tourism/index.html')
    except:
        messages.warning(request, "Invalid Username or Password")
        return render(request, 'Tourism/index.html')


def tour_page(request):
    return render(request, 'Tourism/Tour_Register_new.html')


def tour_register(request):
    try:
        cfname = request.POST.get('data_3', False)
        clname = request.POST.get('data_4', False)
        cname = str(cfname) + ' ' + str(clname)
        cemail = request.POST.get('data_5', False)
        cphone = request.POST.get('data_6', False)
        caddress = request.POST.get('data_18', False)
        cgender = request.POST.get('data_20', False)
        ccountry = request.POST.get('data_15', False)
        cstate = request.POST.get('data_16', False)
        cpassport = request.POST.get('data_19', False)
        cpackage = request.POST.get('data_21', False)
        cSelectdate = request.POST.get('data_22', False)
        print(cname, cemail, cphone, caddress, cgender, ccountry, cstate, cpassport, cpackage, cSelectdate)
        q = "INSERT INTO `tour_registration`(`customer_name`, `customer_email`, `customer_phone`, `customer_address`, " \
            "`customer_gender`, `customer_country`, `customer_state`, `customer_passport`, " \
            "`customer_selected_package`, `trip_startdate`, `trip_enddate`, `trip_amt`, `customer_payment`, " \
            "`trip_status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); "
        v = (cname, cemail, cphone, caddress, cgender, ccountry, cstate, cpassport, cpackage, cSelectdate, '2022-09-22',
             20000.89, 20000, 'Ongoing')
        cursor = connection.cursor()
        cursor.execute(q, v)

        messages.success(request, 'Successfully Registered')
        return render(request, 'Tourism/thanks.html')
    except:
        messages.success(request, 'Something Went Wrong')
        return render(request, 'Tourism/index.html')


def vehicle_page(request):
    return render(request, 'Tourism/vehicle_booking.html')


def vehicle_registration(request):
    try:
        username = request.POST['rental_user_name']
        userdl = request.POST['rental_user_dl']
        vtype = request.POST['vehicle_type']
        useremail = request.POST['rental_user_email']
        userphone = request.POST['rental_user_phone']
        pickup = request.POST['rental_user_pickD']
        drop = request.POST['rental_user_dropD']
        city = request.POST['city']
        amt = request.POST['vamt']
        print(username, userdl, useremail, userphone, vtype, pickup, drop, city, amt)
        q = 'INSERT INTO `vehicle_registration`(`customer_name`, `customer_license`, `customer_email`, ' \
            '`customer_phone`, `customer_pickup`, `customer_drop`, `vehicle_type`, `city`, `amount`) VALUES (%s,%s,' \
            '%s,%s,%s,%s,%s,%s,%s) '
        v = (username, userdl, useremail, userphone, pickup, drop, vtype, city, amt)
        cursor = connection.cursor()
        cursor.execute(q, v)
        messages.success(request, 'Confirmation Will be sent Soon')
        return render(request, 'Tourism/thanks.html')

    except:
        messages.success(request, 'Something Went Wrong')
        return render(request, 'Tourism/vehicle_booking.html')


def customer_contact(request):
    name = request.POST['name']
    cemail = request.POST['cemail']
    cnumber = request.POST['cnumber']
    cmsg = request.POST['cmsg']
    print(name, cemail, cnumber, cmsg)
    q = "INSERT INTO `customer_query`(`customer_name`, `customer_email`, `customer_number`, `customer_message`, " \
        "`employee_reply`) VALUES (%s,%s,%s,%s,%s) "
    v = (name, cemail, cnumber, cmsg, '')
    cursor = connection.cursor()
    cursor.execute(q, v)
    messages.success(request, 'Thank You For Enquiry!!')

    return render(request, 'Tourism/thanks.html')


def recommed(request):
    return render(request, 'Tourism/recommed.html')


def hotel_book(request):
    return render(request, 'Tourism/hotel_booking.html')


def hotel_booked(request):
    from datetime import date
    d=date.today()
    try:
        name = request.POST.get('custname')
        cemail = request.POST.get('cemail')
        cnumber = request.POST.get('cnumber')
        roombkd= request.POST.get('roombkd')
        people=request.POST.get('people')
        checkin=request.POST.get('checkindt')
        checkout=request.POST.get('checkoutdt')
        print(name,cemail,cnumber,roombkd,people,checkin,checkout)
        q = "INSERT INTO `hotel_booking`(`customer_name`, `customer_email`, `customer_number`, `room_booked`, `no_of_people`, `hotel_checkin`, `hotel_checkout`, `date_booked`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        v = (name,cemail,cnumber,roombkd,people,checkin,checkout,d)
        cursor = connection.cursor()
        cursor.execute(q, v)
        messages.success(request, 'Thank You For Hotel Booking We Will Reach Out to You Soon!!')
        return render(request, 'Tourism/index.html')
    except:
        messages.success(request, 'Something Went Wrong')
    return render(request, 'Tourism/hotel_booking.html')
