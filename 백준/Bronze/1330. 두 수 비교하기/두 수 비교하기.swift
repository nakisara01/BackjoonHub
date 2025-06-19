if let line = readLine() {
    let numbers = line.split(separator: " ").compactMap { Int($0) }
    
    if numbers.count == 2 {
        let a = numbers[0]
        let b = numbers[1]
        
        if a > b {
            print(">")
        } else if a < b {
            print("<")
        } else {
            print("==")
        }
    }
    else{
        print("err")
    }
}