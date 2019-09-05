# twitter_sentiment_analysis

In this project we are doing sentiment analysis over tweets focused on specific keyword ( Hashtag or User).

The libraries which we are using in this project are:-

(1) NLTK :- It is a implementation of Stanford OpenSource NLP library for python. We are using it for doing sentimental
            analysis over the tweets For more information http://www.nltk.org

(2) Tweepy :- Its is a Python SDK for twitter api. We are using this to get the tweets regarding a specific keyword
            from twitter. For more information https://www.tweepy.org

(3) D3.js :- D3.js is a JavaScript library for manipulating documents based on data. D3 helps you bring data to life
            using HTML, SVG, and CSS. D3’s emphasis on web standards gives you the full capabilities of modern browsers
            without tying yourself to a proprietary framework, combining powerful visualization components and a
            data-driven approach to DOM manipulation. We are using to create the Word Cloud. For more information
            https://d3js.org

(4) Django :- Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
              Built by experienced developers, it takes care of much of the hassle of Web development, so you can
              focus on writing your app without needing to reinvent the wheel. It is the backbone of our project.
              For more information https://www.djangoproject.com

 Other needed libraries and dependencies are noted in requirements.txt.

 #### Project Structure

When you create a Django project, the Django framework itself creates a root directory of the project with the project
name on it. That contains some files and folder, which provide the very basic functionality to your website and on that
strong foundation you will be building your full scaled website.
After that it is our decision that we want to create different apps for different modules or single mega app for all.
We have created an app for sentimental analysis module and it contains all the model, view, urls, templates & extra
docs or code regarding sentimental analysis in it. In future wea can easily add a new sentimental analysis functionality
in it and if we plan for other modules like tweet streaming in future then we can create different app for it.
