var names = ["James", "Jill", "Jane", "Jack"];

function fancy(symbol, reversed){
	//if reversed is true
	//sorts through names backwards
	if(reversed == true){
		for(var i = names.length -1; i >= 0; i--){
			console.log(names[i] + " " + symbol + " " + i);
		}
	}
	//if fancy is anonymous fancy();
	//sorts through array of names but adds default symbol
	else if (symbol === undefined && reversed === undefined){
		for(var i = 0; i < names.length; i++){
		console.log(i + " -> " + names[i]);
		}
	}	
	else
	{
	//If all arguments are filled out.
	//Sorts through array and adds symbol.  Reverse is false.
		for(var i = 0; i < names.length; i++){
		console.log(i + " " +symbol + " " + names[i]);
		}
	}
}
fancy("---->", true);