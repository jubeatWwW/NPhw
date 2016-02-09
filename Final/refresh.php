<?php
    $NAME = $_GET['name'];
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
    
    $queryData = array($NAME);
    $query = 'SELECT refresh_token FROM Calendar WHERE email=?';
    $sth = $PDO->prepare($query);
    $sth->execute($queryData);
    $data = $sth->fetch(PDO::FETCH_ASSOC);
    //echo $data['refresh_token'];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://accounts.google.com/o/oauth2/token");
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(array("client_id"=>$CLIENT_ID,
    "client_secret"=>$CLIENT_SECRET,
    "grant_type"=>'refresh_token',
    "refresh_token"=>$data['refresh_token']) ));
    
    $result = curl_exec($ch);
    $status = curl_getinfo($ch);
    curl_close($ch);
    $jsonObject = json_decode($result);
    $reftok = $jsonObject->access_token;
    if(isset($reftok)){
        echo $jsonObject->access_token;
    } else{
        echo "Refresh Failed";
    }
    //echo $jsonObject->refresh_token;
    
    $updateData = array($jsonObject->access_token,$NAME);
    $query = "UPDATE Calendar SET access_token=? WHERE email=?";
    $sth = $PDO->prepare($query);
    try{
        if($sth->execute($updateData)){
            //echo "Succ";
        }
        else{
            echo "Refresh Failed";
        }
    } catch(PDOException $e){
        echo "Fuck";
    }
?>
