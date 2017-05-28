var HOUR = 4;
var MINUTE = 29;
var PERIOD = "PM";
var afterThirty = HOUR + 1;

if (MINUTE > 30)
{
	if(PERIOD == "AM")
	{
		console.log("It's almost " + afterThirty + " in the morning");
	}
	else
	{
		console.log("It's almost " + afterThirty + " in the evening");
	}
}
else if(MINUTE == 15)
{
	console.log("It's a quarter past " + HOUR + ".");
}
else if(MINUTE == 30)
{
	console.log("It's half past " + HOUR + ".");
}
else if(MINUTE == 05)
{
	console.log("It's 5 after " + HOUR + ":00" + PERIOD + ".");
}
else
{
	if(PERIOD == "AM")
	{
		console.log("It's " + HOUR + " in the morning");
	}
	else
	{
		console.log("It's " + HOUR + " in the evening");
	}
}

