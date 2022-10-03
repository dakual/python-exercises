<?php
function getPost()
{
    if (isset($_SERVER['PHP_AUTH_USER'])) {
      if ($_SERVER['PHP_AUTH_USER'] == 'login' && $_SERVER['PHP_AUTH_PW'] == 'password') {
        $result["status"] = 'Access granted.';
        $result["data"]   = $_POST;
        return $result;
      } else {
        return 'Access denied!';
      }
    }

    if(!empty($_POST)) {
        return $_POST;
    }

    if(!empty($_FILES)) {
      return "file uploaded!";
    }

    $rawData  = file_get_contents('php://input');
    $jsonData = json_decode($rawData, true);
    if(json_last_error() == JSON_ERROR_NONE) {
        return $jsonData;
    }

    $xmlData = new SimpleXMLElement($rawData);
    if($xmlData) {
      return $xmlData;
    }

    return [];
}

print_r(getPost());
?>