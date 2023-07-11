<!doctype html>
<html lang="en">
<?php
    include_once('header.php')
?>
<link href="assets/css/starter-template.css" rel="stylesheet">
<br><br><br>
<main role="main" class="container">
<div class="starter-template">
    <h1>Vertretung 12</h1>
    <br><br>
    <?php
      include_once('assets/content/crenew.php');
      //echo $s;
    if($s == true) {
        include_once('assets/content/v.php');
    }
    else{
        echo '<META HTTP-EQUIV="refresh" content="0;URL=login.php?r=/vertretung.php">';
    }
?>
</div>
Diese Seite dient ausschlie&szlig;lich zum Privatgebrauch.
<?php
    include_once('footer.php')
?>
      </div>
    </main>
  </body>
</html>
