"""

description


author: 
date:
credit:
links:


Requirements - Must have pyad library installed.  To install run "pip install pyad" from a command prompt


"""
###### begin code ######
import pyad
from pyad import adbase, aduser

def create_ad_user(username, password, ou_path, first_name, last_name, email):
    # Connect to Active Directory
    pyad.set_defaults(ldap_server="your_ldap_server")  # Replace with your LDAP server address
    pyad.set_defaults(ldap_port=389)  # Replace with your LDAP server port

    # Create new user object
    new_user = aduser.ADUser.create(username,
                                    password,
                                    ou_path=ou_path,
                                    upn=f"{username}@your_domain.com",  # Replace with your domain
                                    enabled=True,
                                    optional_attributes={
                                        'givenName': first_name,
                                        'sn': last_name,
                                        'mail': email
                                    })

    print(f"User {username} created successfully!")

if __name__ == "__main__":
    # Provide the necessary information
    new_username = "new_user"
    new_password = "password123"
    ou_path = "OU=Users,DC=your_domain,DC=com"  # Replace with the desired Organizational Unit (OU) path
    new_first_name = "New"
    new_last_name = "User"
    new_email = "newuser@your_domain.com"  # Replace with the user's email

    create_ad_user(new_username, new_password, ou_path, new_first_name, new_last_name, new_email)



