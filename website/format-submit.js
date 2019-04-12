function convertArrayFormat()
{
    var i;
    var finalArr = [];
    for(i = 0; i < superArray.length; i++)
    {
        var lineX = [];
        var lineY = [];
        var j;
        for(j = 0; j < superArray[i].length; j++)
        {
            lineX.push(superArray[i][j].x);
            lineY.push(superArray[i][j].y);
        }
        var tempArr = [];
        tempArr.push(lineX);
        tempArr.push(lineY);
        finalArr.push(tempArr);
    }
    console.log(finalArr);
    return finalArr;
}