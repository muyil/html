<?php
  error_reporting(E_ALL);
  date_default_timezone_set('Europe/Berlin');
  $db = new mysqli('localhost', 'root', 'Samy0110', 'WillenDafoeDb');
  $db->set_charset('utf8');
  if ($db->connect_errno){
    die('Sorry - gerade gibt es ein Problem');
}
 ?>
