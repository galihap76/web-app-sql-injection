<?php
session_start();
include_once 'database.php';

  if(isset($_POST["login"])){
	 $username = $_POST["username"]; 
	 $password =  $_POST["password"]; 
	  
	  $login = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");
	  if(mysqli_num_rows($login) == 0){
          die('Username and password not valid!');    
    }else if(isset($_POST["login"]) && isset($_POST["remember"])){
     $username = $_POST["username"]; 
	 $password =  $_POST["password"];   
          
     $login = mysqli_query($conn, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");                 
     setcookie('id', 'administrator', time()+250);  
     $_SESSION['login'] = true;
     header('Location: index.php');
  }else{
        $_SESSION['login'] = true;
        header('Location: index.php');
      }
}
?>


<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Login</title>
    </head>
    
 <body>
     <h1>Please login!</h1>
    <form method="post" action="">
    <label for="username">Username :</label>
        <input type="text" id="username" name="username">
        <br>
        <br>
        <label for="password">Password :</label>
        <input type="password" id="password" name="password">
        <label for="remember">Remember :</label>
        <input type="checkbox" id="remember" name="remember">
        <br>
        <br>
        <button type="submit" name="login">login</button>
     </form>
    </body>   
</html>    