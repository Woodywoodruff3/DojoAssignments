var daysUntilMyBirthday = 60;
while (daysUntilMyBirthday > 1){
	daysUntilMyBirthday--;
	if(daysUntilMyBirthday === 1){
		console.log(daysUntilMyBirthday + " DAY UNTIL MY BIRTHDAY!!!");
	}
	else if(daysUntilMyBirthday <= 5 )
	{
		console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!!");
	}
	else if(daysUntilMyBirthday <=30)
	{
		console.log(daysUntilMyBirthday + " days til my party");
	}
	else
	{
		console.log(daysUntilMyBirthday + " days until my birthday. Such a long time to wait... :(");
	}
}
console.log("HAPPY BIRTHDAY!!!");