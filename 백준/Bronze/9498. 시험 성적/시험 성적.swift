if let input = readLine(), let score = Int(input){
    
    if score >= 90 && score <= 100{
        print("A")
    } else if score >= 80 && score < 90{
        print("B")
    } else if score >= 70 && score < 80 {
        print("C")
    } else if score >= 60 && score < 70 {
        print("D")
    } else {
        print("F")
    }
} else {
    print("err")
}