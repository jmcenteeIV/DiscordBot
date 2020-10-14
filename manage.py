#!/path/to/project/venv/bin/python
from locationsharinglib import Service
cookies_file = 'FILE_CREATED_BY_MAPSCOOKIEGETTERCLI_AUTHENTICATION_PROCESS'
vm = input
google_email = 'jmcenteeiv@gmail.com'
service = Service(cookies_file=cookies_file, authenticating_account=google_email)
vm = input
for person in service.get_all_people():
    print(person)
vm = input
