
/*
let testScores = [7,8,1,2,3]
var teamScore = 0
for score in testScores{
    if score > 5{
        teamScore += 5
    }else{
        teamScore += 2
    }
    print(teamScore)
    // 5 10 12 14 16
}
*/

var optionNames:String? = "Kuehar"
var greeting:String? = "Hello!"

print(greeting)

if let name = optionNames{
    greeting = "Hello, \(name)"
}
print(greeting)