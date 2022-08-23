from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
    {% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Mono&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Mono&family=Tapestry&display=swap" rel="stylesheet">
    <title>project home</title>
     <style>
       {% block css %} {% endblock %}
       .ul :hover{
           color: brown;
           background-color: aqua;
       }


    </style>
  </head>
  <body>
    <div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
crossorigin="anonymous"></script>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
            <div class="container-fluid">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/blog/home">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/blog/about">About the website</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/blog/aboutblogs">About the blogs</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/blog/contact">Contact us</a>
                        </li>
    
                        <li class="nav-item">
                            <a class="nav-link" href="/blog/signup">Sign-up new users</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/admin">Login</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
    <br>
    <br>
    <div class="out-box-redirectpage" style="width: 100vw; background-color: yellow;">
        <div style="width: max-content; height: 70vh; background-color: aqua; margin:auto; font-size:10vh;" >
            welcome to letsblog
            <br>
                <a class="nav-link" href="/admin">redirect to admin panel</a>
                <a class="nav-link" href="/blog/home">enter as reader</a>
                <a class="nav-link" href="/blog/login">enter as blogger</a>
        </div>
    </div>
    <br>
    <br>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <footer
    class="d-flex flex-wrap justify-content-between align-items-center py-3 my-0 border-top bg-dark text-light fixed-bottom">
    <div class="col-md-4 d-flex align-items-center">
        <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
            <svg class="bi" width="30" height="24">
                <use xlink:href="#bootstrap" />
            </svg>
        </a>
        <span class="text-muted">&copy; 2022 Company, Inc</span>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

</footer>

</body>
</html>


    ''')