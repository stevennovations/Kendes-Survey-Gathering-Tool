<?php

require_once 'dbconnect.php'; //Database Connection
session_start();

/** Follows this format
        
        1. Get Connection
            1.5 Process any parameters that need processing
        2. Prepare the SQL Statements
        3. Bind to parameters if there are any
        4. Execute the query
        5. Return the Array of objects that you have queried
**/

	if (isset($_POST['type']) && !empty($_POST['type'])) {
     	$action = $_POST['type'];
     	switch ($action) {
     		case 'ksurvey': echo addSurveyAnswer($_POST['dats'], $_POST['usernme']); break;
     		case 'userProfile': addProfile(); break;

     	}
    }

	function addSurveyAnswer($items, $user_id) {
        //echo "hello";

        $conn = getConnection();
        $temp = json_decode($items);
        
        $stmtString = "INSERT INTO kanseitb (relax_refresh, cool_impress, light_interest, mystery_elegant, classic_creative, sexy_chic, klasiko_malikhain, fun_boring, M_F, pretty_adorable, beauty_cute, child_profe, calm_live, masikip_maayos, simple_luxury, crowded_neat, plain_sopshiticated, comfort_style, oldf_future, gorgeous_charm, masaya_nakakabagot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
        $stmt = $conn->prepare($stmtString);

        $a_params = array();
        $paramType = "iiiiiiiiiiiiiiiiiiiii";
        $a_params[] = & $paramType;

        for($x = 0; $x < count($temp); $x++){
        	$a_params[] = & $temp[$x];
        }

        call_user_func_array(array($stmt, 'bind_param'), $a_params);
        $ret = $stmt->execute();
        $last_id = $conn->insert_id;
        $varr = 3001;
        $stmtString2 = "INSERT INTO survey (kanseitb_idkanseitb, websitid, userid) VALUES (?,?,?)";
        $stmt2 = $conn->prepare($stmtString2);
        $stmt2->bind_param("iii", $last_id, $varr, $user_id);

        $ret = $stmt2->execute();

        echo  $last_id = $conn->insert_id;

        $conn->close();

        //echo $stmt->error;
        //var_dump($conn->error);

        return $ret;

    }


    //Function to add the user's Profile
    function addProfile(){

    	$conn = getConnection();
    	$stmtString = "INSERT INTO user_profile (username, birthdate, college, gender, highschool1, highschool2, device, hobbies, primaryshop, shopnumber, shophours, shopitems, products, price, designorfunctionality, homepage) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";

        // echo $_POST['USERNAME'] . "<br>";
        // echo $_POST['BIRTHDATE'] . "<br>";
        // echo $_POST['COLLEGE'] . "<br>";
        // echo $_POST['GENDER'] . "<br>";
        // echo $_POST['HIGHSCHOOL1'] . "<br>";
        // echo $_POST['HIGHSCHOOL2'] . "<br>";
        // echo $_POST['DEVICE'] . "<br>";
        // echo $_POST['HOBBIES'] . "<br>";
        // echo $_POST['PRIMARYSHOP'] . "<br>";
        // echo $_POST['SHOPNUMBERS'] . "<br>";
        // echo $_POST['SHOPHOURS'] . "<br>";
        // echo $_POST['SHOPITEMS'] . "<br>";
        // echo $_POST['PRODUCTS'] . "<br>";
        // echo $_POST['PRICE'] . "<br>";
        // echo $_POST['DESIGNORFUNCTIONALITY'] . "<br>";
        // echo $_POST['HOMEPAGE'] . "<br>";

    	$stmt = $conn->prepare($stmtString);
    	$stmt->bind_param("ssssssssssssssss", $_POST['USERNAME'], $_POST['BIRTHDATE'], $_POST['COLLEGE'], $_POST['GENDER'], $_POST['HIGHSCHOOL1'], $_POST['HIGHSCHOOL2'], $_POST['DEVICE'], $_POST['HOBBIES'], $_POST['PRIMARYSHOP'], $_POST['SHOPNUMBERS'], $_POST['SHOPHOURS'], $_POST['SHOPITEMS'], $_POST['PRODUCTS'], $_POST['PRICE'], $_POST['DESIGNORFUNCTIONALITY'], $_POST['HOMEPAGE']);

        $ret = $stmt->execute();

        $last_id = $conn->insert_id;
        if($_SESSION["PREQ"] == 0){
            $_SESSION['user_id'] = $last_id;
            $_SESSION["NAME"] = $_POST["USERNAME"];
            $_SESSION["BIRTHDAY"] = $_POST["BIRTHDATE"];
            $_SESSION["GENDER"] = $_POST["GENDER"];
        }

        $conn->close();

        //echo $stmt->error;
        //var_dump($conn->error);
    	//Return User Profile ID

        header("Location: ../survey.php"); /* Redirect browser */
        exit();
    }

    

