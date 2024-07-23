from django.core.exceptions import ValidationError
import re

def validate_name_format(name): 
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    pattern = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'

    good_name = re.match(pattern, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name' : name })
    

def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    pattern = r'^.+@school\.com$'

    good_email= re.match(pattern, email)
    if good_email:
        return email
    else:
        raise ValidationError(error_message, params={'email': email})
    
def validate_personal_email(email):
    error_message = 'Enter a valid email address'
    pattern = r'^[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.com$'

    good_email= re.match(pattern, email)
    if good_email:
        return email
    else:
        raise ValidationError(error_message, params={'email': email})
    
    
def validate_combination_format(combo):
    pattern = r'^\d{2}-\d{2}-\d{2}$'
    error_message = 'Combination must be in the format "12-12-12"'

    good_combo = re.match(pattern, combo)
    if good_combo:
        return combo
    else:
        raise ValidationError(error_message, params= {'combo' : combo})
    
def validate_locker_number(number): 
    if number >= 1 and number <= 200:
        validation_error = ''
        return number 
    elif number < 1:
        error_message = 'Ensure this value is greater than or equal to 1.'
    else:
        error_message = 'Ensure this value is less than or equal to 200.'
    raise ValidationError(error_message, params = {'number': number})
   
