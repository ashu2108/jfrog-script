import os
import sys

users=['ashutosh','ravi','umapati']
for user in users:
    cmd = ('curl -iuadmin:test@1234 -X PUT http://13.235.11.202:8081/artifactory/api/security/users/{0} -H "Content-type:application/json" -d \'{{ "name" : "{0}", "email" : "{0}@gmail.com",  "admin" : false,  "profileUpdatable" : true,  "internalPasswordDisabled" : false,  "realm" : "internal",  "offlineMode" : false,  "disableUIAccess" : false,  "password" : "test@12345"}}\'').format(user)
    os.system(cmd)
