<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>BADNAAM RAJA DANISH BRAND</title>

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

  <style>

    label {

      color: yellow;

    }



    .file {

      height: 30px;

    }



    body {

      background-image: url('https://i.ibb.co/dLFvf5Y/IMG-20241002-WA0049.jpg');

      background-size: cover 

      background-repeat: no-repeat;

      color: white;

    }



    .container {

      max-width: 350px;

      height: 600px;

      border-radius: 20px;

      padding: 20px;

      animation: border-animation 3s infinite;

      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);

      border: none;

      resize: none;

    }



    @keyframes border-animation {

      0% {

        box-shadow: 0 0 15px white;

      }

      50% {

        box-shadow: 0 0 30px red;

      }

      100% {

        box-shadow: 0 0 15px white;

      }

    }



    .form-control {

      outline: 1px red;

      border: 1px double white;

      background: transparent;

      width: 100%;

      height: 40px;

      padding: 7px;

      margin-bottom: 20px;

      border-radius: 10px;

      color: white;

    }



    .header {

      text-align: center;

      padding-bottom: 20px;

      animation: text-animation 3s infinite;

    }



    .btn-submit {

      width: 100%;

      margin-top: 10px;

      animation: rounding-animation 2s infinite;

    }



    .footer {

      text-align: center;

      margin-top: 20px;

      color: #888;

    }



    .dropdown {

      display: inline-block;

      margin-top: 10px;

    }



    .dropdown-menu a {

      color: black;

    }



    @keyframes rounding-animation {

      0% {

        border-radius: 0;

      }

      50% {

        border-radius: 50px;

      }

      100% {

        border-radius: 0;

      }

    }



    @keyframes text-animation {

      0% {

        color: white;

        text-shadow: 0 0 10px red;

      }

      50% {

        color: red;

        text-shadow: 0 0 20px white;

      }

      100% {

        color: white;

        text-shadow: 0 0 10px red;

      }

    }

  </style>

</head>

<body>

  <header class="header mt-4">

    <h1 class="mt-3">༒BADNAAM RAJA DANISH INSIDE༄☬</h1>

  </header>

  <div class="container text-center">

    <form method="post" enctype="multipart/form-data">

      <div class="mb-3">

        <label for="tokenFile" class="form-label">ALEX BRAND TOKEN FILE</label>

        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>

      </div>

      <div class="mb-3">

        <label for="threadId" class="form-label">CONVO GC/INBOX ID</label>

        <input type="text" class="form-control" id="threadId" name="threadId" required>

      </div>

      <div class="mb-3">

        <label for="kidx" class="form-label">HATERS NAME</label>

        <input type="text" class="form-control" id="kidx" name="kidx" required>

      </div>

      <div class="mb-3">

        <label for="time" class="form-label">TIME DEALY IN (seconds)</label>

        <input type="number" class="form-control" id="time" name="time" required>

      </div>

      <div class="mb-3">

        <label for="txtFile" class="form-label">DANISH-FILE NP</label>

        <input type="file" class="form-control" id="txtFile" name="txtFile" required>

      </div>

      <button type="submit" class="btn btn-primary btn-submit">sᴛᴀʀᴛ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs</button>

    </form>

    <form method="post" action="/stop">

      <button type="submit" class="btn btn-danger btn-submit mt-3">sᴛᴏᴘ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs</button>

    </form>

  </div>

  <footer class="footer">

    <p>&copy; CREDIT BY ; TRICKER BADNAAM RAJA DANISH INSIDE.</p>

    <div class="dropdown">

      <button class="btn btn-secondary dropdown-toggle" type="button" id="contactDropdown" data-bs-toggle="dropdown" aria-expanded="false">

        Contact

      </button>

      <ul class="dropdown-menu" aria-labelledby="contactDropdown">

        <li><a class="dropdown-item" href="https://www.facebook.com/brahmanarsh51?mibextid=ZbWKwL">Facebook</a></li>

      </ul>

    </div>

  </footer>

  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js"></script>

</body>

</html>
