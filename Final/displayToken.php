<?php
    try{
        $PDO = new PDO('mysql:host=dbhome.cs.nctu.edu.tw;dbname=cwlin6104400_cs','cwlin6104400_cs','l5162891');
        $PDO->exec('SET CHARACTER SET utf8');
    }   catch(PDOException $e){
        throw new PDOException($e->getMessage());
    }
    $query = 'SELECT * FROM Calendar';
    $sth = $PDO->prepare($query);
    $sth->execute();
    $data = $sth->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode($data);
    /*foreach($data as $value){
        echo $value['email']."  ".$value['access_token'];
        echo "<br>";
    }*/
?>
