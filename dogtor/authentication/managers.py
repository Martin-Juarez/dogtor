from django.contrib.auth.models import BaseUserManager


class ModUserManager(BaseUserManager):
    '''mod user custom manager'''
    def create_user(self,email,user_name,first_name, password, **other_fields):
        '''overwrite create_user'''
        if not email:
            raise ValueError('You must provide an email')
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)

        user.set_password(password)

        user.save()
        return user
    
    def create_superuser(self,email, user_name,first_name, password, **other_fields):
        '''overwrite a superuser'''
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)

        return self.create_user(email, user_name,first_name, password, **other_fields)