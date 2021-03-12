from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserTypeMaster, UserMaster,BookMaster,CategoryMaster,ChapterMaster
from django.template import loader



# Create your views here
def chapter(request,id,chapid=0):
    book_name1 = BookMaster.objects.filter(BookID=id).values('BookID', 'BookName')

    if chapid == 0:
        chapter = ChapterMaster.objects.filter(BookID=id).values('ChapterID', 'ChapterName', 'ChapterData','ChapterNo')
        next_chapter=chapter[1]['ChapterID']
        #print(next_chapter)
    else:
        chapter = ChapterMaster.objects.filter(BookID=id).values('ChapterID', 'ChapterName', 'ChapterData')
        count=0
        for x in chapter:
            if count == 1:
                next_chapter=x['ChapterID']
                print(next_chapter)
                break
            if x['ChapterID'] == chapid:
                count = 1

        chapter = ChapterMaster.objects.filter(ChapterID=chapid).values('ChapterID', 'ChapterName', 'ChapterData','ChapterNo')
    return render(request, 'page.html',context={'book_name1': book_name1, 'chapter': chapter, 'next_chapter': next_chapter})


def page(request,id):
     book_name = BookMaster.objects.all().values('BookID','BookName')
     chapterdata = ChapterMaster.objects.filter(BookID=id).values('ChapterName','ChapterData')
     # book= BookMaster.objects.all().values('BookID', 'BookImage', 'BookName')
     # author=UserMaster.objects.filter(UserTypeID__UserType='author').values()
     # print((author))
     return render(request,'page.html',context={'book_name':book_name,'chapterdata':chapterdata})
def home(request):
    book_list=BookMaster.objects.all().values('BookID','BookImage','BookName')
    book_list1 = BookMaster.objects.filter(IsCompleted=True).values('BookID', 'BookImage', 'BookName')
    category_list=CategoryMaster.objects.all().values('categoryID','categoryName')
    chapter_list=ChapterMaster.objects.all().values('ChapterNo','ChapterName')
    list1=[]
    for x in range(0,len(book_list)):
        book_id=book_list[x]['BookID']
        book_name=book_list[x]['BookName']
        #print(book_name)
        category_id=BookMaster.objects.filter(BookID=book_id).values('CategoryID_id')[0]['CategoryID_id']
        category_name=CategoryMaster.objects.filter(categoryID=category_id).values('categoryName')[0]['categoryName']
        #print(category_name)
        chapter_name=ChapterMaster.objects.filter(BookID=book_id).values('ChapterNo','ChapterName')
        if chapter_name:
            chapter_no=chapter_name[0]['ChapterNo']
            chapter_name1=chapter_name[0]['ChapterName']
            print((chapter_no))
            temp_variable = {'BookID': book_id, 'BookName': book_name, 'categoryName': category_name,
                             'ChapterNo': chapter_no, 'ChapterName': chapter_name1}
        else:
            temp_variable = {'BookID': book_id, 'BookName': book_name, 'categoryName': category_name}
        #print(chapter_name1)

        list1.append(temp_variable)
        #print(list1)
    return render(request,'home.html',context={'list1':list1,'book_list':book_list,'book_list1':book_list1})

def bookdata(request,id):

    #print(request.GET.get('id'))
    #id =int(request.GET.get('id'))
    Bookdata=BookMaster.objects.filter(BookID=id).values('BookID','BookImage','BookName','Description','CategoryID','IsCompleted')
    #print(Bookdata)
    idbook=Bookdata[0]['BookID']
    #print(idbook)
    #list1 = []
    for x in range(0,idbook):

        bookdata1 = BookMaster.objects.filter(BookID=id).values('BookID', 'BookImage', 'BookName', 'Description',
                                                               'CategoryID', 'IsCompleted')[0]['BookID']
        #bookid=Bookdata1[0]['BookID']
        #print(bookdata1)
        chapterdata1=ChapterMaster.objects.filter(BookID=id).values('ChapterID','ChapterNo','ChapterName','ChapterData')[0]['ChapterID']
        #print(chapterdata)
        # tempvar = {'chapterdata':chapterdata,'bookdata1':bookdata1}
        # print(tempvar)
        #list1.append(tempvar)
        #print(list1)
    chapterdata =ChapterMaster.objects.filter(BookID=id).values('ChapterID', 'ChapterNo', 'ChapterName', 'ChapterData')
    category=CategoryMaster.objects.filter(categoryID=Bookdata[0]['CategoryID']).values('categoryName')[0]['categoryName']
    authorname1=BookMaster.objects.filter(UserID_id=id).values('UserID')[0]['UserID']
    authorname2=UserMaster.objects.filter(UserID=authorname1).values('UserName')[0]['UserName']
    #print(authorname2)
    return render(request,'bookdata.html',context={'Bookdata':Bookdata, 'chapterdata':chapterdata, 'category':category,'authorname2':authorname2,'bookdata1':bookdata1,'chapterdata1':chapterdata1})

def Register(request):
    if request.method == "POST":
        UserName1 = request.POST['UserName']
        UserType1 = request.POST['UserType']
        UserEmail1 = request.POST['UserEmail']
        UserMobile1 = request.POST['UserMobile']
        Password1 = request.POST['Password']
        UserTypeID_Instance=UserTypeMaster.objects.filter(UserTypeID=int(UserType1))[0]
        x=UserMaster.objects.create(UserName=UserName1,UserEmail=UserEmail1,UserMobile=UserMobile1,UserPassword=Password1,UserTypeID=UserTypeID_Instance)
        return redirect('login')
    else:
        a1 = UserTypeMaster.objects.all().values('UserType', 'UserTypeID')
        return render(request,'register.html',context={'a1':a1})

def login(request):
    if request.method == "POST":
        UserEmail1=request.POST['UserEmail']
        Password1 = request.POST['Password']
        if UserMaster.objects.filter(UserEmail=UserEmail1,UserPassword=Password1,UserTypeID=1).exists():
            user_id_session=UserMaster.objects.filter(UserEmail=UserEmail1).values('UserID')[0]['UserID']
            request.session['user_id_session']=user_id_session
            return redirect('author')
        else:
            return redirect('home')
    else:
        return render(request,'login.html')
def author(request):
     if request.method == "POST":
        print(request.FILES)
        product = request.FILES['BookImage']
        # print(product.name)
        img_save_path = 'media/' + product.name
        with open(img_save_path, 'wb+') as f:
            for chunk in product.chunks():
                f.write(chunk)
        CategoryName1=request.POST['CategoryName']
        UserMasterID_Intance=UserMaster.objects.filter(UserID=request.session['user_id_session'])[0]
        CategoryMaster_Intance=CategoryMaster.objects.filter(categoryID=int(CategoryName1))[0]
        q=BookMaster.objects.create(BookName=request.POST['BookName'],Description=request.POST['Description'],BookImage=product.name,CategoryID=CategoryMaster_Intance,UserID=UserMasterID_Intance,IsCompleted=0,IsActive=1)

        return redirect('home')
     else:
         b1=CategoryMaster.objects.all().values('categoryID','categoryName')
         return  render(request,'author.html',context={'b1':b1})


