 ## Flask Application Design for a Site that Teaches the Basics of Github

### HTML Files

**1. index.html**
- This is the main page of the site.
- It should contain a brief introduction to the site and links to the other pages.

**2. basics.html**
- This page should cover the basics of Github, such as creating an account, creating a repository, and pushing code to a repository.

**3. advanced.html**
- This page should cover more advanced topics, such as branching, merging, and using the command line.

**4. resources.html**
- This page should list helpful resources for learning more about Github, such as tutorials, books, and online courses.

### Routes

**1. @app.route('/')**
- This route should render the index.html page.

**2. @app.route('/basics')**
- This route should render the basics.html page.

**3. @app.route('/advanced')**
- This route should render the advanced.html page.

**4. @app.route('/resources')**
- This route should render the resources.html page.

### Additional Notes

- The HTML files should be located in a templates folder within the Flask application.
- The routes should be defined in a routes.py file within the Flask application.
- The Flask application should be configured to use the templates folder and the routes.py file.
- The Flask application should be run on a local development server for testing purposes.