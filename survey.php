<!DOCTYPE html>
<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html lang = "en">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>KANSEI DESIGN SURVEY</title>

        <!-- Bootstrap -->
        <link href="Assets/CSS/bootstrap-3.3.7-dist/css/bootstrap.min.css" rel="stylesheet">

        <!--Custom-->
        <link href="Assets/CSS/survey.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/9.4.1/css/bootstrap-slider.min.css" />

        
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>

    <body>

        <body>
        <!-- Trigger/Open The Modal -->

        <div class="container-fluid row-survey-opt-1">

            <div class="row">
                <div class="progress no-radius">
                    <div class="progress-bar progress-bar-success no-radius" role="progressbar" aria-valuenow="1"
                    aria-valuemin="0" aria-valuemax="3" style="width:40%">
                    1/3 Websites Complete
                    </div>
                </div>
            </div>
            
            <div class="row">
                <div class="col-lg-10 col-lg-offset-1">
                    <form class="form-inline">
                        <!--<span>-->
                        <h4 class="pull-left yay">
                            Hi, 
                            <?php

                            echo $_SESSION["NAME"] . "!";
                            ?>
                        </h4>
                        <!--</span>-->
                        <button type="button" class="btn btn-primary pull-right btn-userinfo-2" data-toggle="modal" data-target="#myModal">
                            Answer Survey Form
                        </button>

                        <select class="form-control pull-right select-test" id="select-url">
                            <?php
                                // add user info variables to the session
                                $arr = array();
                                
                                if($_SESSION["PREQ"] == 0){
                                    echo "<option>ENTER</option>";
                                    $rootpath = ".\\Assets\\Websites";
                                    $fileinfos = new RecursiveIteratorIterator(
                                            new RecursiveDirectoryIterator($rootpath)
                                    );

                                    foreach ($fileinfos as $pathname => $fileinfo) {
                                        $ctr = 0;
                                        if (!$fileinfo->isFile())
                                            continue;
                                        if (strpos($pathname, ".html")) {
                                            $LINK = substr($pathname, 2);
                                            $ctr = $ctr + 1;
                                            echo "<option value= ". $ctr .">" . $LINK . "</option>"; 
                                            array_push($arr, $LINK);
                                            foreach($arr as $key => $value)
                                            {
                                                echo "<option>" .$key." has the value". $value. "</option>";
                                            } 
                                        }
                                    }

                                    $_SESSION["WEBSITES"] = $arr;
                                    $_SESSION["PREQ"] = 1;
                                } else {
                                    
                                    $arr = $_SESSION["WEBSITES"];

                                    foreach($arr as $key => $value)
                                    {
                                        $LINK = $value;
                                        echo "<option>" .$value. "</option>";
                                    }
                                }

                            ?>
                        </select>

                    </form>

                </div>
            </div>
        </div>

        <?php
            echo "<div class='container-fluid row row-cust'>
                    
                        <iframe src='" . $LINK . "' class='iframe-custom' id='myFrame'></iframe>
                    </div>";
            if(($key = array_search($LINK, $arr)) !== false) {
                unset($arr[$key]);
            }

            $_SESSION["WEBSITES"] = $arr;
        ?>

        <!-- The Modal -->
        <div id="myModal" class="modal fade" role="dialog">
            <div class="container">
                <!-- Modal content -->
                <div class="modal-content col-lg-10 col-lg-offset-1">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        <h2 class="text-center t-title">Survey</h2>
                        <div class = "row">
                            <div class = "col-lg-6 col-lg-offset-3 text-center">
                                <h6>Based on the website you just viewed please adjust the slider's position to the word that best describes how you feel about the website.</h6>
                            </div>
                        </div>
                    </div>
                    <hr class="hr-custom-2">
                    <div class="modal-body">
                        <div class="row">
                            <!--<div class="col-lg-12">-->
                            <form id="kanseiForm" method="post" role="form" action="survey.php">
                                <?php
                                    echo "<input type='hidden' id='userid1' value= '" . $_SESSION['user_id'] . "''>";
                                ?>
                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Relaxing</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex1" data-slider-id='ex1' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider" 
                                                   />
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Refreshing</b></center>
                                        </div>
                                    </div>
                                </div>


                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Cool</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex2" data-slider-id='ex2' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Impressive</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Light</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex3" data-slider-id='ex3' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Interesting</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Mysterious</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex4" data-slider-id='ex4' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Elegant</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Classic</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex5" data-slider-id='ex5' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Creative</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Sexy</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex6" data-slider-id='ex6' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Chic</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Klasiko</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex7" data-slider-id='ex7' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Malikhain</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Fun</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex8" data-slider-id='ex8' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Boring</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Masculine</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex9" data-slider-id='ex9' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Feminine</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Pretty</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex10" data-slider-id='ex10' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Adorable</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Beautiful</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex11" data-slider-id='ex11' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Cute</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Childish</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex12" data-slider-id='ex12' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Professional</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Calm</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex13" data-slider-id='ex13' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Lively</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Masikip</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex14" data-slider-id='ex14' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Maayos</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Simple</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex15" data-slider-id='ex15' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Luxurious</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Crowded</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex16" data-slider-id='ex16' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Neat</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Plain</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex17" data-slider-id='ex17' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Sophisticated</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Comfortable</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex18" data-slider-id='ex18' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Stylish</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Old-Fashioned</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex19" data-slider-id='ex19' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Futuristic</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Gorgeous</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex20" data-slider-id='ex20' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Charming</b></center>
                                        </div>
                                    </div>
                                </div>

                                <hr class="hr-custom">

                                <div class="form-group text-center">
                                    <div class="row">
                                        <div class="col-lg-2 col-lg-offset-2">
                                            <center><b>Masaya</b></center>
                                        </div>
                                        <div class="col-lg-4">
                                            <input id="ex21" data-slider-id='ex21' 
                                                   type="text" data-slider-min="1" data-slider-max="5" data-slider-step="1" data-slider-value="3"
                                                   data-slider-handle="round" class="mySlider"/>
                                        </div>
                                        <div class="col-lg-2">
                                            <center><b>Nakakabagot</b></center>
                                        </div>
                                    </div>
                                </div>

                                

                                    <!--</div>-->
                            </div>

                        </div>
                        <div class="modal-footer">
                            <div class="row">
                                <hr class="hr-custom">
                                <div class="col-lg-6 col-lg-offset-3">
                                    <input type="submit" name="userinfo_submit" id="userinfo_submit" tabindex="4" class="form-control btn btn-userinfo" value="Proceed">
                                </div>
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </div>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="Assets/CSS/bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>
        <!--Custom-->
        <!--<script src="assets/js/main.js"></script>-->

        
    </body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/9.4.1/bootstrap-slider.min.js"></script>
    <script>
        var sliderSHIT = [];
        var ctr = 0;

        for (ctr = 1; ctr < 22; ctr++) {
            sliderSHIT[ctr-1] = 3;
        }

        $('.mySlider').slider();

        //console.log(sliderSHIT);
        $('#select-url').click(function () {
            //$('#myFrame').attr('src', $('#select-url').val());
            console.log($('#select-url').val())
            $('.mySlider').slider('refresh');

        });

         $('.mySlider').on('slide', function (ev) {
                console.log(ev.value);
                //console.log(ev.target.id);
                var str = ev.target.id;
                str = str.substring(2);
                console.log(str);
                var dex = str - 1;
                sliderSHIT[dex] = ev.value;
        });

        $('#userinfo_submit').on('click', function(e){
            e.preventDefault();
            console.log(sliderSHIT);

            var sendFile = JSON.stringify(sliderSHIT);
            alert($('#userid1').val());
             $.ajax({
                 url: "models/modelHandler.php",
                 type: "POST",
                 data: {"type": "ksurvey", "dats": sendFile, "usernme": $('#userid1').val()},
                 dataType: "html",
                 success: function(html){
                     console.log(html);
                     alert("Success");
                 }
             });

        });
    </script>
</html>



 