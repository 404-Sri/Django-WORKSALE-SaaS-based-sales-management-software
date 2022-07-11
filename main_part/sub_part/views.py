from django.shortcuts import render
from . models import registration_table, contact_table, add_customer_table
from django.contrib import messages,auth


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def login_form_submission(request):
    if registration_table.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
        ex1=registration_table.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
        take_user_name=ex1.user_name
        print(take_user_name)
        logger_data=registration_table.objects.get(user_name=take_user_name)
        return render(request,'dashboard.html',{'logger_data':logger_data})
    else:
        messages.error(request,'Invalid email_id or password!',extra_tags='failed_login')
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')        



def register(request):
    return render(request,'register.html')

def register_form_submission(request):
    if request.method=='POST':
        if registration_table.objects.filter(email_id=request.POST['email_id']).exists():
            messages.error(request,'sorry, this email is already taken!!!',extra_tags='registration_failed')
            return render(request,'register.html')

        else:
            ex1=registration_table(user_name=request.POST.get('user_name'),
                                   email_id=request.POST.get('email_id'),
                                   password=request.POST.get('password'))
            ex1.save() 
            print('successfully saved')
            messages.error(request,'successfully registered!...',extra_tags='saved')
            return render(request,'login.html')      

    else:
        print('not saved')
        return render(request,'register.html')                       



def contact(request):
    return render(request,'contact.html')

def contact_form_submission(request):
    if request.method=='POST':
        if contact_table.objects.filter(email_id=request.POST['email_id']).exists():
            messages.error(request,'sorry, this email is already taken!!!',extra_tags='error_contact')
            return render(request,'contact.html')
        else:
            ex1=contact_table(name=request.POST.get('name'),
                              email_id=request.POST.get('email_id'),
                              subject=request.POST.get('subject'),
                              message=request.POST.get('message'))

            ex1.save()
            messages.error(request,'Thanks for your response, our team will contact you soon!...',extra_tags='success_contact')
            return render(request,'contact.html')
    else:
        return render(request,'contact.html')        

def dashboard(request):
    return render(request,'dashboard.html')

def add_product(request):
    return render(request,'add_product.html')

def edit_product(request):
    return render(request,'edit_product.html')        

def product_list(request):
    return render(request,'product_list.html')

def view_mail(request):
    return render(request,'view_mail.html')    

def compose(request):
    return render(request,'compose.html')

def font_awesome(request):
    return render(request,'font_awesome.html')

def inbox(request):
    return render(request,'inbox.html')

def material_icons(request):
    return render(request,'material_icons.html')

def simple_line_icons(request):
    return render(request,'simple_line_icons.html')

def themify(request):
    return render(request,'themify.html')

def tax(request):
    return render(request,'tax.html')

def users(request):
    return render(request,'users.html')

def vendors(request):
    return render(request,'vendors.html')

def add_brand(request):
    return render(request,'add_brand.html')

def add_category(request):
    return render(request,'add_category.html')

def add_customer_report(request):
    return render(request,'add_customer_report.html')

def add_customer(request):
    return render(request,'add_customer.html')

def add_customer_form_submission(request):
    if request.method=="POST":
        ex1=add_customer_table(name=request.POST.get('name'),
                               email_id=request.POST.get('email_id'),
                               phone_number=request.POST.get('phone_number'),
                               address=request.POST.get('address'),
                               city=request.POST.get('city'),
                               state=request.POST.get('state'),
                               country=request.POST.get('country'),
                               zipcode=request.POST.get('zipcode'))    
        ex1.save()
        messages.error(request,'successfully added the customer details!..',extra_tags='add_customer')
        view_data=add_customer_table.objects.all()
        return render(request,'customers.html',{'view_data':view_data})
    else:
        return render(request,'add_customer.html')


def add_expense_report(request):
    return render(request,'add_expense_report.html')

def add_expense(request):
    return render(request,'add_expense.html')

def add_purchase_tax(request):
    return render(request,'add_purchase_tax.html')

def add_quotation(request):
    return render(request,'add_quotation.html')

def add_return(request):
    return render(request,'add_return.html')

def add_role(request):
    return render(request,'add_role.html')

def add_sale(request):
    return render(request,'add_sale.html')

def add_stock(request):
    return render(request,'add_stock.html')

def add_tax(request):
    return render(request,'add_tax.html')

def add_user(request):
    return render(request,'add_user.html')

def add_vendor(request):
    return render(request,'add_vendor.html')

def brands(request):
    return render(request,'brands.html')

def calenders(request):
    return render(request,'calenders.html')

def chat(request):
    return render(request,'chat.html')

def customer_analysis(request):
    return render(request,'customer_analysis.html')

def customers(request):
    view_data=add_customer_table.objects.all()
    return render(request,'customers.html',{'view_data':view_data})

def edit_brand(request):
    return render(request,'edit_brand.html')

def edit_category(request):
    return render(request,'edit_category.html')

def edit_customer_report(request):
    return render(request,'edit_customer_report.html')

def customer_report(request,id):
    get_data=add_customer_table.objects.get()
    return render(request,'customer_report.html')    

def edit_customer(request):
    return render(request,'edit_customer.html')

def edit_expense_report(request):
    return render(request,'edit_expense_report.html')

def customer_report(request):
    return render(request,'customer_report.html') 

def edit_expense(request):
    return render(request,'edit_expense.html') 

def edit_purchase_tax(request):
    return render(request,'edit_purchase_tax.html')    

def edit_quotation(request):
    return render(request,'edit_quotation.html')     

def edit_return(request):
    return render(request,'edit_return.html')   

def edit_role(request):
    return render(request,'edit_role.html')      

def edit_sale(request):
    return render(request,'edit_sale.html') 

def edit_stock(request):
    return render(request,'edit_stock.html') 

def edit_tax(request):
    return render(request,'edit_tax.html') 

def edit_user(request):
    return render(request,'edit_user.html')      

def edit_vendor(request):
    return render(request,'edit_vendor.html') 

def edit_report(request):
    return render(request,'edit_report.html')            

def expense_category(request):
    return render(request,'expense_category.html') 

def expense_report(request):
    return render(request,'expense_report.html') 

def expense_list(request):
    return render(request,'expense_list.html') 

def purchase_tax_report(request):
    return render(request,'purchase_tax_report.html')     

def quotations(request):
    return render(request,'quotations.html')     

def stock_analysis(request):
    return render(request,'stock_analysis.html')     

def returns(request):
    return render(request,'returns.html')     

def roles(request):
    return render(request,'roles.html')     

def sales(request):
    return render(request,'sales.html')  

def profile(request):
    return render(request,'profile.html')                       