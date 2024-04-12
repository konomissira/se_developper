APPLICANT_1 = "John"
APPLICANT_2 = "Robert"
APPLICANT_3 = "Fanny"
RECRUITER = "Rochelle"

print(APPLICANT_1)

applicant_name = input("Please, Enter your name: ")

if(applicant_name == APPLICANT_1):
    print("Welcome", APPLICANT_1)
elif(applicant_name == APPLICANT_2):
    print("Welcome", APPLICANT_2)
elif(applicant_name == APPLICANT_3):
    print("Welcome", APPLICANT_3)
elif(applicant_name == RECRUITER):
    print("Greetings", RECRUITER)
else:
    print("Your name is not on the list.")
