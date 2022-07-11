from django.contrib import admin
from . models import Student,Address,Course,Session,Class,Student_class_mapper
# Register your models here.
admin.site.register(Student)
admin.site.register(Address)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Class)
admin.site.register(Student_class_mapper)
