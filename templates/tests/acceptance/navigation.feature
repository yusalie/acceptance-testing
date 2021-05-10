Feature: test navigation between pages
    we can have a longer discription

        Scenario: homepage can go to the blog
            Given I am on the homepage
             When I click on the 'Go to blog' link
             Then I am on the blog page

        Scenario: blog can go to the homepage
            Given I am on the blog page
             When I click on the 'Go to home' link
             Then I am on the homepage
             