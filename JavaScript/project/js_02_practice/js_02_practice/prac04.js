const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  // solution 함수 완성
  function solution(K, N, M, chargers) {

    let start = 0
    let charge = 0
    while (start+K < N) {
        let i = start + K
        let flag = 0
        while (i > start) {
            
            if (chargers.includes(i)) {
                charge += 1
                start = i
                flag = 1
                
                break
              } 
              
              i--
              
        }
        if (flag === 0) {
            charge = 0
            break
        }
        
        }
    
    console.log(charge)
    
  }

  for (const input of inputs) {
    solution(...input)
  }



