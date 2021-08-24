# Django-Realation-testing
Django Realation testing

***information Reagrading Problem***

Authtenticatin Used  : JWT authentication

Permission_Class Used: DjangoModelPermission

Customised User Model used as a User Model

**Teacher** and **Student** model are realaed to User Model by **foreign key**(OneToOne)

There are two groups in **Group Model Table**
1.Teacher (having Permission)

  ![image](https://user-images.githubusercontent.com/65783411/130676330-83d1b341-3680-4dd1-adf6-ec5f49925212.png)
 
2.Student (having Permission)  

![image](https://user-images.githubusercontent.com/65783411/130676495-26356257-527d-4631-8ea8-39940988992c.png)

**_Problem_**
Tacher is unable to add or update data neither of Student nor Teacher until it is has permissons of User Model
