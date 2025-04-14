# your_app/tests/test_models.py
import pytest
from django.core.exceptions import ValidationError
from cit410signupApp.models import RegisterCourse

@pytest.mark.django_db #Django's pytest.mark.django_db decorator, which allows it to interact with the database if needed.
def test_studentid_must_be_integer():
    """Test that studentID only accepts integer values"""
    # Test with valid integer
    valid_course = RegisterCourse(
        studentID=123456,
        firstName="John",
        lastName="Doe"
    )
    try:
        valid_course.full_clean()  # this is used to execute the test above - the above Should pass validation since integer field has the right value
    except ValidationError:
        pytest.fail("Valid integer for studentID raised ValidationError")


# Test with invalid non-integer (e.g., string)
    invalid_course = RegisterCourse(
        studentID="ABC123",  # Not an integer
        firstName="Jane",
        lastName="Doe"
    )
    with pytest.raises(ValidationError):# This context manager asserts that the code inside raises ValidationError
        invalid_course.full_clean()  # # This Django method validates all model fields - Should raise a ValidationError

"""
#To validate only the studentID field in Django (instead of using full_clean(), which validates all fields), you can use Django's field-specific validation. 
with pytest.raises(ValidationError):
    invalid_course.clean_fields(exclude=["firstName", "lastName"])  # Only validates studentID
"""

   
