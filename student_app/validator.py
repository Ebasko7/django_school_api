from django.core.exceptions import ValidationError
import re

def validate_name_format(name): 
    error_message = 'Name must be in the format "First Middle Initial. Last'
    pattern = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'

    good_name = re.match(pattern, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={ 'name' : name })