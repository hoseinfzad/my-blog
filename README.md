# My-blog
To run my-blog in development mode; Just use steps below:
<li>
      <ol>Install python3, pip, virtualenv in your system.</ol>
      <ol>Clone the project https://github.com/hoseinfzad/my-blog.</ol>
      <ol>Make development environment ready using commands below;</ol>
            `git clone https://github.com/hoseinfzad/my-blog && cd MyBlog
            python3.10 -m virtualenv venv  # Create virtualenv named venv
            venv/script/activate
            pip install -r requirements.txt
            python manage.py migrate  # Create database tables
            `
      <ol>Run MyBlog using python manage.py runserver</ol>
      <ol>Go to http://localhost:8000 to see your MyBlog version</ol>
      
</li>
