
var isGenerated = false;

function addTableItem(name, weight, duration){
	var addItem = 
			"<tr>" +
				"<td>" +
					name +
				"</td>" +
				"<td>" +
					weight +
				"</td>" +
				"<td>" +
					duration +
				"</td>" +
			"</tr>";

	return addItem;
}

function taskItem(name, weight, duration){
	this.name = name;
	this.b = weight;
	this.w = duration;
}

var todoList = Array();

var yoh = Array();
function generateSchedule(){
	if(!isGenerated){
		$("#generate-form").addClass("hidden");
		$("#generate-table").removeClass("hidden");
		
		$("#generatedList").html("");
		$("#removedList").html("");

		//ENTER GENERATING CODE

		var timeAlot = parseInt($("#timeallot").val());
		//console.log(timeAlot);

		//ENTER ALGO
		var exportSched = knapsack(yoh, timeAlot);
		console.log(exportSched);

		var generatedSched = exportSched.set;

		//LOOP WHEN APPENDING ITEM TO TABLE

		for (var i = 0; i < generatedSched.length; i++) {
			var addItem = addTableItem(generatedSched[i].name, generatedSched[i].b, generatedSched[i].w);
			$("#generatedList").append(addItem);
		}

		//IF THERE ARE NO TASK USE THIS AS VIEW
		//var clearItem = addTableItem("&nbsp","&nbsp","&nbsp");
		//$("#generatedList").html(clearItem);
		//$("#removedList").html(clearItem);

		isGenerated = true;   
	}    
}

function changeAllottedTime(){
	if(isGenerated){
		$("#generate-table").addClass("hidden");
		$("#generate-form").removeClass("hidden");

		//STORE NEW ALLOTTED TIME

		isGenerated = false;
	}
}

function resetSchedule(){
	isGenerated = false;

	$("#taskList").html("");
	$("#generatedList").html("");
	$("#removedList").html("");

	yoh = Array();
	var clearItem = addTableItem("&nbsp","&nbsp","&nbsp");
	$("#taskList").html(clearItem);
	$("#removedList").html(clearItem);

	$("#generate-table").addClass("hidden");
	$("#generate-form").removeClass("hidden");

	//RESET ALL YOUR VARIABLES
}

function addTask(){
	
	var name = $("#name").val();
	var weight = $("#weight").val();
	var duration = $("#duration").val();

	//var addItem = addTableItem(name, weight, duration);
	var tItem = new taskItem(name, parseInt(weight), parseInt(duration));
	var clearItem = addTableItem("&nbsp","&nbsp","&nbsp");

	yoh.push(tItem);

	var addItem = addTableItem(tItem.name, tItem.b, tItem.w);
	$("#taskList").append(addItem);



	//CREATE OBJECT USING THE THREE INPUTS
}

