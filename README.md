# My-blog
To run my-blog in development mode; Just use steps below:
<ol>
1.Install python3, pip, virtualenv in your system.
2.Clone the project https://github.com/hoseinfzad/my-blog.
3.Make development environment ready using commands below;
      `git clone https://github.com/hoseinfzad/my-blog && cd MyBlog
      python3.10 -m virtualenv venv  # Create virtualenv named venv
      venv/script/activate
      pip install -r requirements.txt
      python manage.py migrate  # Create database tables
      `
4.Run MyBlog using python manage.py runserver
5.Go to http://localhost:8000 to see your MyBlog version
</ol>
