This is the README file for the pricing_v2 assignment. 

When you are in the mysite folder you can use the command **python3 manage.py runserver** to start the server and it runs in http://127.0.0.1:8000/

I have kept two options in the starting page, one is to enter the admin dashboard and the other is where the api is exposed. 

1. Admin Dashboard:-
     I have created some admin users and have shared some of the credentials below. Those credentials can be used for testing. So under successful login, admin users can see the dashboard
     where they can find the Pricing Configuration Section. This is where the admin users can do all the CRUD operations of the params that are involved in pricing API. The logged in user can
    change the configuration of the params and if they save, the modified_by changes. The site still shows options where the logged in user can change created_by and modified_by, that part is
    yet to be changed. But other than that everything works fine.

2. Pricing Api:-
    I have followed the same convention given in the assignment.
    1. Distance Base Price DBP e.g. (80rs  Upto 3KMs on (Tue, Wed, Thur), 85rs Upto 3.0KMs (Sat, Sun), 90rs Upto 3.5KMs (Mon,Fri))
    2. Distance Additional Price DAP e.g. (28rs/KMs)
    3. Time Multiplier Factor TMF e.g. (Under 1 hour - 1x, After the initial hour - 1.25x till 2 hour, After the previous tier calculation 2.2x till 3 hour and 4x after 3 hrs) 
    4. Waiting Charges WC e.g. (5rs/min after initial 3mins)

    $Price = (DBP + (Dn * DAP)) + (Tn * TMF) + WC$) where  D → Additional distance traveled

    My input will be total_distance travlled, total_time, waiting_time(before the passesger gets in the car)
    
    With this formula, I have modified it according to my understanding. When distance in less than 3kms I used the additonal price, whereas if it is greater than 3 the above formual works.
    DBP varies according to days of the week. This was also followed. Tn is taken as the total_time and (Tn*TMF) will be (total_time-waiting_time)(in mins)*factor.

    When the user presses the calculate button it gives the total price. All the calculations are mentioned thoroughly mentioned in views.py file under pricing_api_module. The formula I used
    might not be the best approach, but it can be chaged accordingly. Nothing is stored in the database in this module.
    
