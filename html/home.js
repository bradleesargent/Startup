function load() {
var planningdir = "C:/Users/bradl/Dropbox/14 Planning/";
console.log(planningdir);
var d = new Date()
console.log(d);
var year=d.getFullYear();
var curr_month = d.getMonth() + 1;
var currday = ("0000" + d.getDate()).slice(-2) 
console.log("day:"+currday);
console.log("year:"+year);
var onedateelementdir=document.getElementById("datemmdir");
var onedateelement=document.getElementById("datemm");
var masterdir=document.getElementById("datemasterdir");
var datenewsubdir=document.getElementById("datenewsubdir");
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
onedateelement.value=months[d.getMonth()]+" "+d.getDate()+", " +year;
masterdir.value=planningdir+year+"/";
datenewsubdir.value=curr_month+" - "+months[d.getMonth()];
onedateelementdir.value=planningdir+"/"+year+"/"+curr_month+" - "+months[d.getMonth()]+"/"+currday+".mm";
}

function getyearly() {
		console.log("Hello");
		var hourly = document.getElementById("hourly");
		var yearly = document.getElementById("yearly");
		var monthly = document.getElementById("monthly");
		var weekly = document.getElementById("weekly");
		var daily = document.getElementById("daily");
		var hourlyvalue = hourly.value;
		console.log( hourly.value);
		yearly.value = hourlyvalue*40*52;
		monthly.value=yearly.value/12;
		weekly.value=hourlyvalue*40;
		daily.value=hourlyvalue*8;
		}