# Project Description

The goal of this project is to create a Portfolio Site for users. The site will allow users to sign up and enter their details, which will then be displayed in a visually appealing way. Users will also have access to an API for their information.

The project includes CRUD (Create/Retrieve/Update/Delete) functionality, which allows users to manage and update their information as needed. It is important to note that this project is not intended to be a social network or e-commerce site.

The application utilizes Django on the backend, including 6 models, and Javascript for the front-end. It is also designed to be mobile-responsive.



# Back End

The back end of the application includes the following files:
- views.py
- forms.py
- admin.py
- serializer.py
- urls.py
- models.py

The application includes the following models:
- User: A fully featured User model with admin-compliant permissions.
- InformationModel: Holds the regular information about the user.
- EducationModel: Holds the education-related information about the user.
- ExperienceModel: Holds the experience-related information about the user.
- SkillSetModel: Holds the skillsets related information about the user.
- ProjectModel: Holds the information related to projects done by the user.
- MessageModel: Used to hold the contact information so that anyone who wants to contact the user from the portfolio template can be done.
