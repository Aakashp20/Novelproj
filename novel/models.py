from django.db import models

# Create your models here.
class UserTypeMaster(models.Model):
    UserTypeID = models.AutoField(primary_key=True)
    UserType = models.CharField(max_length=255,blank=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifiedAt = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=1)


    def __str__(self):
        return self.UserType

class UserMaster(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=25,help_text='Enter User Name: ', null=False, blank=False)
    UserTypeID = models.ForeignKey(UserTypeMaster,null=True,on_delete=models.SET_NULL)
    UserPassword = models.CharField(max_length=20,blank=False)
    UserEmail = models.EmailField(max_length=25,unique=True)
    UserMobile = models.BigIntegerField(blank=False)
    UserAddress = models.CharField(max_length=255,null=True,default='No Address')
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifiedAt = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=1)

    def __str__(self):
        return self.UserName

class CategoryMaster(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=25,help_text="what your book's category: ", null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=1)

    def __str__(self):
        return self.categoryName

class BookMaster(models.Model):
    BookID = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=25,help_text='Enter BookName: ', null=False, blank=False)
    UserID = models.ForeignKey(UserMaster,null=True,on_delete=models.SET_NULL)
    CategoryID = models.ForeignKey(CategoryMaster,null=True,on_delete=models.SET_NULL)
    CreateDate = models.DateTimeField(auto_now_add=True)
    ModifiedDate = models.DateTimeField(auto_now=True)
    BookImage = models.CharField(max_length=300,null=True)
    Description = models.CharField(max_length=1000,null=False,blank=False)
    IsCompleted = models.BooleanField(default=0)
    IsActive = models.BooleanField(default=1)

    def __str__(self):
        return self.BookName


class ChapterMaster(models.Model):
    ChapterID = models.AutoField(primary_key=True)
    ChapterNo = models.CharField(max_length=70,null=True,blank=False)
    ChapterName = models.CharField(max_length=70,null=True)
    ChapterData = models.CharField(max_length=5000,null=False,blank=False)
    BookID = models.ForeignKey(BookMaster,null=True,blank=False,on_delete=models.SET_NULL)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    ModifyAt = models.DateTimeField(auto_now=True)
    IsActive = models.BooleanField(default=1)

   # def __str__(self):
       # return self.CategoryID




