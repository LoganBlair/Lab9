############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.
keepgoing = True
print 'Welcome'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print 'What is your temperature?'
temp = int(raw_input())
print 'Have you been sick for the last 24 hours?'
wellness = raw_input()
print 'Have you been to West Africa in the past 21 days?'
africa = raw_input()
if temp > 105:
    print 'You should be sent to the hospital'
elif temp and wellness == 'yes':
    print 'You should be sent to the hospital'
elif temp > 100 and africa == 'yes':
    print 'You need to be sent to the hospital'
elif wellness == 'yes' and africa == 'yes':
    print 'You need to be sent to the hospital'
else:
    print 'You do not need to go to the hospital'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'Any other patients?'
    anotherpatient = raw_input()
    if anotherpatient == 'no':
        keepgoing = False
        print 'Have a good day!'
    if anotherpatient == 'yes':
        keepgoing = True
    

    














