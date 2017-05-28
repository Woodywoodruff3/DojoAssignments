function slotMachine(leave){
	var bank = 100;
	while(bank >= 1){
		var slotPull = Math.floor((Math.random() * 100) + 1);
		var randomNumber = Math.floor((Math.random() * 100) + 1);
		if(bank >= leave){
			console.log("You have collected enough to reach your limit which was " + leave +" quarters. You now have " + bank + " quarters!" )
			break;
		}
		else if(slotPull === randomNumber)
		{
			bank--;
			bank = bank + Math.floor((Math.random() * 50) + 50);
			console.log("DING DING DING, You have won! You now have " + bank + " quarters in your account.");
		}
		else
		{
			bank--;
			console.log("Your number didnt match. You have " + bank + " quarters left")
		}
	}
}
slotMachine();