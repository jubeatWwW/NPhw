<html>
    <head>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script>
            function auth(){
                window.open("https://people.cs.nctu.edu.tw/~cwlin6104400/login.php",auth, "height=500,width=500");
                document.cookie = "user="+$("#email").val()+"; path=/~cwlin6104400/";
                //alert($("#email").val());
            }
        </script>            
    </head>
    <body>
    <div class="authBlock">
        <input type="text" name="email" id="email">
        <input type="submit" value="auth" onclick="auth()">
    </div>
</body>
</html>
