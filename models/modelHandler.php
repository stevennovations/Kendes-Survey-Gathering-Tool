<?php

require_once 'dbconnect.php'; //Database Connection

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
     		case 'ksurvey': echo addSurveyAnswer($_POST['dats']); break;
     		case 'userProfile': addProfile($_POST['id']); break;

     	}
     }

	function addSurveyAnswer($items) {
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

        $conn->close();

        echo $stmt->error;
        var_dump($conn->error);

        return $ret;

    }


    //Function to add the user's Profile
    function addProfile(){

    	$conn = getConnection();
    	$stmtString = "INSERT INTO user_profile (name, birthday, gndr, HStype, HScd, college, hobby, online_retail, num_known_ec, num_items_ecb, num_hours_spent_ec, prod_purch_most, price_of_prod, design_fucntion, presentation) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";

    	$stmt = $conn->prepare($stmtString);
    	$stmt->bind_param("sssssssssssssss", $_POST['USERNAME'],$_POST['BIRTHDATE'],$_POST['COLLEGE'],$_POST['GENDER'],$_POST['HIGHSCHOOL1'],$_POST[''],$_POST[''],$_POST[''],$_POST[''],$_POST[''],$_POST[''],$_POST[''],$_POST[''],$_POST[''],$_POST[''])

    	//Return User Profile ID
    }

    

