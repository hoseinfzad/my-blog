# My-blog
To run my-blog in development mode; Just use steps below:
<li>
      <ol>Install python3, pip, virtualenv in your system.</ol>
      <ol>Clone the project https://github.com/hoseinfzad/my-blog.</ol>
      <ol>Make development environment ready using commands below;</ol>
              
            1.git clone https://github.com/hoseinfzad/my-blog && cd MyBlog
            2.python3.10 -m virtualenv venv  # Create virtualenv named venv
            3.venv/script/activate
            4.pip install -r requirements.txt
            5.python manage.py migrate  # Create database tables
            
      
      Run MyBlog using python manage.py runserver
      <ol>Go to http://localhost:8000 to see your MyBlog version</ol>
      
</li>
