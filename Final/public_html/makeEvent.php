<html>
    <head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>	    
        <link rel="stylesheet" type="text/css" href="Semantic/semantic.min.css">
        <link rel="stylesheet" type="text/css" href="datetimepicker/css/bootstrap-datetimepicker.min.css">
        <script src="Semantic/semantic.min.js"></script>
        <script src="datetimepicker/js/bootstrap-datetimepicker.min.js"></script>
        <script src="js/make.js"></script>
    </head>
    <body>
        <form class="ui form" style="margin-top:30px;margin-left:30px;margin-right:30px">
            <div class="field">
                <input type="text" style="text-align:center" placeholder="Summary"></input>
            </div>
            <div class="fields">
                <div class="six wide field">
                    <div id="datetimepicker1" class="input-append date" style="">
                        <input data-format="yyyy-MM-dd" type="text" style="text-align: center" placeholder="Start Date"></input>
                        <span class="add-on">
                            <i data-time-icon="icon-time" data-date-icon="icon-calendar" class="calendar icon" onclick="datepickerShow()"></i>
                        </span>
                    </div>
                </div>
                <div class="four wide field">
                    <i class="big long arrow right icon" style="position:relative;left:50%"></i>
                </div>
                <div class="six wide field">
                    <div id="datetimepicker2" class="input-append date">
                        <input data-format="yyyy-MM-dd" type="text" style="text-align: center" placeholder="End Date"></input>
                        <span class="add-on">
                            <i data-time-icon="icon-time" data-date-icon="icon-calendar" class="calendar icon" onclick="datepickerShow2()"></i>
                        </span>
                    </div>
                </div>
            </div>
        </form>
        <div class="ui buttons" style="width:80vw;position:relative;left:10%;top:20vw">
            <button class="ui button" onclick="$('input').val('')">Clear</button>
            <div class="or"></div>
            <button class="ui positive button" onclick="make()">Make!</button>
        </div>
        <div style="margin-top:50px;margin-left:30px;margin-right:30px" id="tblDiv"></div>

<script type="text/javascript">
  function datepickerShow() {
    $('#datetimepicker1').datetimepicker({
        pickTime: false
    });
  };

  function datepickerShow2(){
    $('#datetimepicker2').datetimepicker({
        pickTime: false
    });
  };
</script> 
    </body>
</html>
