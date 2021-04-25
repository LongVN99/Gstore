<p id="top"></p>

# Gstore
## Code Institute: Milestone Project 4 - Nguyen Truong Thai Long

[View live deployment of site here]()

![responsive]()

Marshal Unisex Collectibles is an E-Commerce website for wrist watch brands. Majority of consumers now use online and digital channels to research prices or find product information. Whatever your interest, we tell your time in an extraordinary digital experience!
Moreso the site provides the necessary modern functionalities for the shop owner to manage vital content for products and services.

# Table of Contents

- [Project Requirements](#project-requirements)
    - [Mandatory Requirements](#mandatory-requirements)
- [UX](#ux)
    - [UX Design](#ux-design)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
- [Features](#features)
    - [Existing Features](#existing-features)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Tools and Libraries](#tools-and-libraries)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [Local Deployment](#local-deployment)
- [Credits](#credits)
    - [Code and Content](#code-and-content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>


# Project Requirements
Build a full-stack site based around business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

Required Technologies : 
* HTML, CSS, JavaScript, Django + Django
* Relational database (MySQL or Postgres)
* Stripe Payments - Test card details can be found [HERE](#test-card)

Optional: Include use of additional libraries and external APIs.

## Mandatory Requirements

1. Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
2. Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
3. Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course
4. User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
5. User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
6. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout or single payments, or donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.
7. Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
8. Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
9. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
10. Version Control: Use Git & GitHub for version control.
11. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
12. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
13. Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.

# UX
## UX Design

The application was structured using bootstrap to maintain wide browser compatibility, consistency in design and extensibility to render responsive and modern website.

### Typography

### Colors


## User Stories

### User Stories for Customers

| **As a shopper or site user I would like to**             | **So that I can**                                       |
| --------------------------------------------------------- | ------------------------------------------------------- |
| Navigate throughout the site with ease                    | Find product to purchase in an organised format         |
| View each product as a single unit                        | Ascertain detailed content of a particular brand        |
| View my current bag total                                 | Keep track of my spending limit                         |
| Search the site quickly                                   | Locate a particular product of interest                 |
| Create my own account                                     | Have my profile with the option to login and logout     |
| Create my personal profile                                | Save my information for future delivery and easy entry  |
| Sort products by category, name, price or rating          | Make an informed decision before transaction            |
| Be able to add/remove or edit products in my bag          | Regulate my orders and checkout                         |
| Be able to select the quantity and wrist size             | Avoid being overcharged and ensure perfect fitting      |
| Ensure secure transactions                                | Be convinced about my payment                           |
| Receive a post email confirmation about my order          | Be assured and have records of my transactions          |
| Read input by reviewers                                   | Be preinformed about product and services               |
| Review purchased product                                  | Let prospective users know how I feel about the product |
| Be able to reset or recover my password                   | Retain my personal account                              |
| Be able to contact the company                            | Channel enquiries or seek solution to issues            |


### User Stories for Shop Administrators


## Wireframes

The skeletal framework of this website was designed using [Figma](https://www.figma.com/) as a visual guide to represent the page schematic and screen blueprint.

Links to final version of the wireframes can be found below:

* [Desktop Final Version]()
* [Mobile Final Version]()


## Database Schema

The database schema as it relates to each model is structured below:

![schema]()

<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>


# Features

### Home Page

### User Account

This provides interface for new users to register, then sign into already created account.
The creation of the account requires a valid email and a password.
Account owners can access the following features:

-   Update profile information
-   View order history
-   Review purchased product

### Shopping Bag

-   The shopping bag populates all purchased product details, subtotal for items purchased and a grand total.
-   Users can remove items from the shopping bag and update quantities before checkout.
-   Thereafter users have the option to continue shopping or proceed to payment.

### Search bar

-   The Search functionality is present on all pages to enable users narrow down their search. 

### Checkout

-   Checkout allow users to enter their delivery and payment details initially.
-   The checkout details and delivery information are pre-filled with the information provided in the user's profile which can also be edited.
-   A summary of the order is populated on the checkout page
-   Users also have the option to adjust their bag before completion of order
-   Payment is made by card using [Stripe](https://stripe.com/)

### Administrator features

-   The administrator has the sole right to product management section
-   An administrator can edit or delete a product to get users updated and engaged.


# Technologies Used

## Languages

* [HTML5:](https://www.w3schools.com/html/default.asp)
    - HTML5 was used to code the content of the website.
* [CSS:](https://www.w3schools.com/css/default.asp)
    - CSS3 was used to style the content.
* [JavaScript:](https://www.w3schools.com/js/default.asp)
    - JavaScript was used to style the significant interactive functionality.
* [Python:](https://www.w3schools.com/python/default.asp)
    - Python was used for the project back-end functions.

## Tools and Libraries




**External Hosting:**
* [GitHub:](https://github.com/)
    - The project used the GitHub hosting service to save the project in a repository. 
* [Heroku:](https://www.heroku.com/)
    - Heroku platform was used to deploy, manage, and scale the app. 

**Databases:**


# Testing


# Deployment

## GitPod
* The site was developed in GitPod and pushed to the following remote GitHub repository - [REPO](https://github.com/jamie120/ms4-wild-mile) -->
    * The following GIT commands were used throughout deployment:
        * **git status** ------ used to check the status of files and any changes made / untracked.
        * **git add**   ------ to stage files ready to commit.
        * **git commit -m " "**  ------ to commit the files.
        * **git push** ------ to push the files to the master branch of the GitHub repo.

## Deployment to Heroku

* This site is hosted using Heroku, deployed directly from the master branch via GitHub. - [LIVE SITE]() -->
    * The following steps were taken to complete the hosting process.
       
    1. Set **_debug=False_** in the app.py file.
    2. Created a requirements.txt file from the terminal, using **_pip3 freeze --local > requirements.txt_**, to allow Heroku to detect this project as a python app and any required package dependencies.
    3. Created a Procfile using **_echo web: python app.py > Procfile_** from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project.

    -   Add the following configuration variables to the application:

    | **VARIABLE**          | **VALUE**                                                          |
    | --------------------- | ------------------------------------------------------------------ |
    | AWS_ACCESS_KEY_ID     | The key provided by AWS                                            |
    | AWS_SECRET_ACCESS_KEY | The secret key provided by AWS for authentication                  |
    | DATABASE_URL          | Postgres Database url provided by the Add-ons                      |
    | EMAIL_HOST_PASSWORD   | Password for designated E-mail address                             |
    | EMAIL_HOST_USER       | The E-mail address used to authenticate to the SMTP server         |
    | SECRET_KEY            | Your Django secret key                                             |
    | STRIPE_PUBLIC_KEY     | The public key provided by Stripe to Identify your account         |
    | STRIPE_SECRET_KEY     | backend secret key provided by Stripe                              |
    | STRIPE_WH_SECRET      | The webhook secret provided by Stripe                              |
    | USE_AWS               | True                                                               |

### Setting-up Automatic Deployment from GitHub

To setup Automatic Deployment from GitHub:

-   Selected Deploy on Heroku dashboard.
-   Clicked on Connect to GitHub button.
-   Ensure GitHub profile is displayed, then add repository name (same as Heroku App), and clicked search.
-   Click connect button to find the repo.
-   Then now Enable Automatic Deployment.
-   Selected branch and clicked Deploy Branch button.
-   Once it's done, you'll see "Your App was successfully deployed!!!.
-   Click "View" to launch the new app. The deployed site is now available.

# Credits

## Code and Content

-   Inspiration and base code was derived from the Boutique Ado Project section of the Code Institute course. Code was modified to better fit my needs.

## Media

## Acknowledgements

<div align="right"><p style="text-align: right"><a href="#top">Back to top</a></p></div>