<?php
    $startData = $_GET['start'];
    $endDate = $_GET['end'];
    $summary = $_GET['summary'];
    try{
        $PDO = new PDO('mysql:host=dbhome.cs.nctu.edu.tw;dbname=cwlin6104400_cs','cwlin6104400_cs','l5162891');
        $PDO->exec('SET CHARACTER SET utf8');
    }   catch(PDOException $e){
        throw new PDOException($e->getMessage());
    }
    
    $query = 'SELECT access_token FROM Calendar WHERE email=:username';
    $sth = $PDO->prepare($query);   
    $sth->bindValue(':username',$_COOKIE['user']);
    $sth->execute();
    $data = $sth->fetch(PDO::FETCH_ASSOC);
    $token = $data['access_token'];

    $payload = json_encode(array("summary"=>$summary,"start"=>array("date"=>$startData),"end"=>array("date"=>$endDate)));

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://www.googleapis.com/calendar/v3/calendars/primary/events/");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch,CURLOPT_HTTPHEADER, array("Authorization: Bearer ".$token,'Content-Type:application/json'));
    curl_setopt($ch,CURLOPT_POSTFIELDS, $payload);
    
    $result = curl_exec($ch);
    $status = curl_getinfo($ch);
    curl_close($ch);
        
    $jsonObject = json_decode($result);
    echo $jsonObject->id;
    /*$retData = array();
    if(isset($jsonObject->error)){
        $retData = array("error"=>"error");
    }else {
        foreach($jsonObject->items as $value){
            //echo $value->summary."   ".$value->start->dateTime."<br>";
            $data = array($value->summary);
            if(isset($value->start->dateTime)){
                array_push($data, $value->start->dateTime , $value->end->dateTime);
            } else{
                array_push($data, $value->start->date, $value->end->date);
            }
            array_push($retData, $data);
        }
    }
    echo json_encode($retData);*/
        //echo $jsonObject['items']
        //echo isset($jsonObject->error);
        //echo "hahaha: ".$jsonObject->access_token;
        //echo $jsonObject->refresh_token;
?>
