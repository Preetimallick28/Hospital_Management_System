# Hospital_Management_System

The project is based on djanggo framework and python technology

In this project i have created two users that is one for staff or management team and one is doctor 

responsibility of management team are:

1. Add patient
2. Crud operation on Patient like updating patient, view patient and delete patient
3. While adding patient , we have made the doctor as a foreign key
4. Add Appointment 
5. while adding appointment , i have kept patient and doctors as a foreign key
6. crud operation on appointment are , updating appointment , view appointment and deleting appointment
7. In admin dashboard, management can see how many doctors are there , how many patient is added and how many appointments have booked
8. for admin , profile of admin has been created in which we can update the profile , reset the password and logout button
9. Next i have kept search bar where we can search patients and appoinments
10. Next let see what are the features available in doctor dashboard

Responsibility of doctor are:

1. in the doctor dashboard i have used the specified user credetial , so that doctors can see thier patients and appointment only , and not other patient and appointment registered by doctor

2. then in doctor dashboard , there is option for view patient and in the view patient we can do update and delete

3. other than update and delete , we can search patient also

4. same as patient , in appointment section we can view appointment list , update appointments and delete appointment as well as we can do search .

5. we have doctor profile section , in profile section , we can do update , reset password

Benefiting of separating two different User -

1. For every single user doctor , they can see thier specific patient and specific appointment , no confusion will be thier and one doctor cannot see patients or appointment of another doctor

2. authentication and authorization have been included , before authorization user is not allowed to access 

