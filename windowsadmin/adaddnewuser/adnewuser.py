"""

description


author: 
date:
credit:
links:


requirements - Must have pyad library installed.  To install run "pip install pyad" from a command prompt

notes
Replace the placeholder values with your specific Active Directory information. 
The create_ad_user function takes the necessary parameters and creates a new user with the provided details. 
Make sure to set the correct LDAP server, port, and domain information.

Note: Ensure that you have the necessary permissions to create new users in the specified Organizational Unit (OU) within Active Directory. 
Test this code in a safe environment before using it in a production setting.

"""
###### begin code ######
import pyad
from pyad import adbase, aduser

def create_ad_user(username, password, ou_path, first_name, last_name, email):
    # Connect to Active Directory
    pyad.set_defaults(ldap_server="your_ldap_server")  # !!! Replace with your LDAP server address
    pyad.set_defaults(ldap_port=389)  # !!! Replace with your LDAP server port

    # Create new user object
    new_user = aduser.ADUser.create(username,
                                    password,
                                    ou_path=ou_path,
                                    upn=f"{username}@your_domain.com",  # !!! Replace with your domain
                                    enabled=True,
                                    optional_attributes={
                                        'givenName': first_name,
                                        'sn': last_name,
                                        'mail': email
                                    })

    print(f"User {username} created successfully!")

if __name__ == "__main__":
    # Provide the necessary information
    new_username = input("enter username")
    new_password = input("enter password")
    ou_path = "OU=Users,DC=your_domain,DC=com"  # Replace with the desired Organizational Unit (OU) path
    new_first_name = input("first name")
    new_last_name = input("last name")
    new_email = input("email address") 

    create_ad_user(new_username, new_password, ou_path, new_first_name, new_last_name, new_email)



