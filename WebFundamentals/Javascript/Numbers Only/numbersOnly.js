function newNumbersArray(){
	var newArray = [1,"apple", -3, "orange", 0.5];
	var newNumbers=[];
	for(var i = 0; i< newArray.length; i++){
		if(typeof newArray[i] === "number"){
		newNumbers.push(newArray[i]);
		}
	}
	return newNumbers;
}
newNumbersArray();

function numbersOnly(){
	var newArray = [1,"apple", -3, "orange", 0.5];
	for(var i = 0; i< newArray.length; i++){
		if(typeof newArray[i] === "string"){
			newArray.splice(i,1);
		}
	} 
	return newArray;
}
numbersOnly();