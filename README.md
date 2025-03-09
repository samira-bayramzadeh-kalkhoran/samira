<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>کارت عروسی دیجیتال</title>
    <style>
        body {
            font-family: 'Tahoma', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        .envelope {
            width: 400px;
            height: 250px;
            background-color: #e0e0e0;
            border-radius: 15px;
            padding: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .card {
            width: 100%;
            height: 100%;
            background-color: #fff;
            border-radius: 10px;
            position: absolute;
            bottom: -100%;
            transition: bottom 1s ease;
            padding: 20px;
            box-sizing: border-box;
        }
        .card-content {
            text-align: center;
        }
        .envelope .name {
            position: absolute;
            top: 10px;
            font-weight: bold;
            font-size: 18px;
        }
        .envelope:hover .card {
            bottom: 0;
        }
        .audio-player {
            display: none;
        }
    </style>
</head>
<body>

    <div class="envelope">
        <div class="name" id="recipient-name">نام گیرنده</div>
        <div class="card" id="wedding-card">
            <div class="card-content">
                <h2>دعوت نامه عروسی</h2>
                <p>با کمال افتخار از شما دعوت می‌کنیم تا در جشن عروسی ما شرکت کنید.</p>
                <p id="message-text">متن قابل تغییر شما اینجا نمایش داده می‌شود.</p>
            </div>
        </div>
        <audio id="wedding-audio" class="audio-player" autoplay>
            <source src="music.mp3" type="audio/mp3">
        </audio>
    </div>

    <script>
        // برای تغییر اسم گیرنده
        document.getElementById('recipient-name').innerText = "مریم عزیز";

        // برای تغییر متن کارت
        document.getElementById('message-text').innerText = "با حضور شما در این جشن، لحظات خاصی را به یاد می‌آوریم.";

        // برای پخش موسیقی
        document.getElementById('wedding-audio').play();
    </script>

</body>
</html>
