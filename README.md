
# Topic-based Research Paper Aggregator

This project presents a Research Paper Aggregator web application designed to 
help researchers and scholars discover and keep track of a vast collection of 
academic papers based on their interests. The application provides a user-friendly 
interface for searching, filtering, and saving papers based on user preferences. 
Users can save their preferences and view them later for a personalized search 
experience. The system is built using Django, a Python-based web framework, 
and incorporates Bootstrap and jQuery for the front end. It leverages the 
BeautifulSoup library for web scraping papers from ArXiv. Furthermore, the 
admin dashboard provides valuable insights such as user activity, popular search 
criteria, and papers viewed, which can be used to further improve the platform.
The system has been designed using the MVC architecture of Django, allowing 
it to be easily maintainable and scalable for future improvements and feature 
additions.



## Objectives

The objectives of this project are as follows:
1)  To develop a web application that aggregates research papers from ArXiv and presents them in a user-friendly manner.

2) To allow users to search for and filter papers based on their interests and preferences.

3) To provide a personalized search experience by allowing users to save their preferences and view them later.

4) To implement a scalable and maintainable system using the MVC architecture of Django.

5) To incorporate data analytics features in the admin dashboard to provide valuable insights for future improvements and feature additions.

## Implementation
The Research Paper Aggregator web application has been implemented using the Django web framework, which follows the Model-View-Controller (MVC) 
architectural pattern.

The project utilizes several libraries and packages such as BeautifulSoup, Django-Bootstrap, and jQuery. The web scraping of research papers is carried out using the BeautifulSoup library, which is a Python package for parsing HTML and XML documents. Django-Bootstrap is used to provide a responsive and visually appealing front end to the application, while jQuery is used for 
implementing dynamic behavior and handling user interactions. The application has been developed using Python 3.8.5 and Django 4.1.7. 

The database schema for the application consists of three models - User, Paper, and UserPaperPreference. The User model is provided by Django's built-in authentication system and is used to store user information such as username, email, and password. The Paper model is used to store information about each research paper, including its title, authors, summary, and URL. The UserPaperPreference model is used to store the user's preferred papers. 

The application's search functionality is implemented using Django's query API, which provides a powerful and flexible interface for searching the database. Users can search for papers by entering keywords or phrases in the search bar, and the application returns a list of papers that match the search criteria. 

The front-end interface of the application is designed using HTML, CSS, and 
JavaScript. Django-Bootstrap is used to provide responsive and visually appealing UI components, while jQuery is used to handle user interactions and implement dynamic behavior such as filtering and pagination.

The application's admin dashboard provides valuable insights such as user activity, popular search criteria, and papers viewed, which can be used to further improve the platform. The dashboard is implemented using Django's built-in admin site, which provides a user-friendly interface for managing the application's database.

The project's code is well-documented, and the development process follows best practices such as code reviews, testing, and continuous integration.
