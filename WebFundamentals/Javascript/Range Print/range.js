function printRange(start, end, skip){
	if(end === undefined && skip === undefined){
		printRange(0, start, 1);
	}
	else if(skip === undefined){
		printRange(start, end, 1);
	
	}
	else if(start > end)
	{
		for(var i = start; i > end; i-=skip){
			console.log(i);
		}
	}
	else
	{
		for(var i = start; i < end; i+=skip){
			console.log(i);
		}
	}
}
printRange(5);