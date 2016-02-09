<?php
require_once 'googleapi/src/Google/autoload.php';

$client = new Google_Client();
$client->setClientId('965959505928-ort8ej02lkvro9dv9sp2kihel0iia1dl.apps.googleusercontent.com');
$client->addScope(Google_Service_Calendar::CALENDAR);
$client->setAccessType('offline');
$client->setApprovalPrompt('force');
$client->setRedirectUri('https://people.cs.nctu.edu.tw/~cwlin6104400/token.php');

$auth_url = $client->createAuthUrl();
header('Location: '. filter_var($auth_url,FILTER_SANITIZE_URL));
?>
