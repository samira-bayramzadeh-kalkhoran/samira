<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>کارت عروسی</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f8f4e3;
        }
        .container {
            position: relative;
            width: 300px;
            height: 400px;
        }
        .envelope {
            width: 100%;
            height: 100%;
            background: url('envelope.png') no-repeat center/cover;
            position: absolute;
            z-index: 2;
        }
        .card {
            width: 100%;
            height: 100%;
            background: url('card.png') no-repeat center/cover;
            position: absolute;
            bottom: 0;
            transition: transform 1s ease-in-out;
        }
    </style>
</head>
<body>
    <div class="container" onclick="revealCard()">
        <div class="card" id="card"></div>
        <div class="envelope"></div>
    </div>
    <audio id="weddingMusic" src="wedding.mp3"></audio>
    <script>
        function revealCard() {
            document.getElementById('card').style.transform = 'translateY(-150px)';
            document.getElementById('weddingMusic').play();
        }
    </script>
</body>
</html>
