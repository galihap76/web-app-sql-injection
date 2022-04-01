<?php
session_start();
include_once "database.php";
$results = mysqli_query($conn, "SELECT * FROM posts");

if(!isset($_SESSION["login"])){
	header("Location: login.php");
	exit;
}

?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Dashboard</title>
    </head> 
<body>
   <h1>Hallo admin!</h1> 
    <?php foreach($results as $data): ?>
    <p>Data 1 : <?php echo $data['coffee']; ?></p>
    <p>Data 2 : <?php echo $data['tea']; ?></p>
    <p>Data 3 : <?php echo $data['orange']; ?></p>
    <?php endforeach; ?>
     <a href="logout.php">Logout</a>
</body>
</html>