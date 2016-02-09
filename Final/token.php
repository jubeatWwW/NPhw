<?php
    //echo "<h1>Hello</h1>";
    //echo $_GET['code'];
    $CODE = $_GET['code'];
    $CLIENT_ID = "965959505928-ort8ej02lkvro9dv9sp2kihel0iia1dl.apps.googleusercontent.com";
    $CLIENT_SECRET = "uk24HYv-6m52Te8uyTkEI4dJ";
    $REDIRECT_URI = "https://people.cs.nctu.edu.tw/~cwlin6104400/token.php";
    $GRANT_TYPE = "authorization_code";

    try{
        $PDO = new PDO('mysql:host=dbhome.cs.nctu.edu.tw;dbname=cwlin6104400_cs','cwlin6104400_cs','l5162891');
        $PDO->exec('SET CHARACTER SET utf8');
    }   catch(PDOException $e){
        throw new PDOException($e->getMessage());
    }
    
    $query = 'SELECT email FROM Calendar WHERE email=:username';
    $sth = $PDO->prepare($query);   
    $sth->bindValue(':username',$_COOKIE['user']);
    $sth->execute();
    $data = $sth->fetch(PDO::FETCH_ASSOC);

    if(isset($data['email'])){
        echo "User Exist";
    } else{

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://accounts.google.com/o/oauth2/token");
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(array("client_id"=>$CLIENT_ID,
        "client_secret"=>$CLIENT_SECRET,
        "redirect_uri"=>$REDIRECT_URI,
        "grant_type"=>$GRANT_TYPE,
        "code"=>$CODE) ));
    
        $result = curl_exec($ch);
        $status = curl_getinfo($ch);
        curl_close($ch);

        $jsonObject = json_decode($result);
        //echo "hahaha: ".$jsonObject->access_token;
        //echo $jsonObject->refresh_token;


        $insertData = array($_COOKIE['user'], $jsonObject->access_token, $jsonObject->refresh_token);
        $query = 'INSERT INTO Calendar (email, access_token, refresh_token) VALUES (?, ?, ?)';
        $sth = $PDO->prepare($query);
        try{
            if($sth->execute($insertData)){
                echo "Succ";
            }
            else{
                echo "Fail";
            }
        } catch(PDOException $e){
            echo "Fuck";
        }
    }
   //echo "<script>window.close();</script>";
?>
