//  //=============================\\
//  || data structures & algorithms ||
//  \\=============================//
//
//  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
//  ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
//  ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
//  ⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
//  ⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
//  ⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
//  ⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
//  ⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
//  ⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
//  ⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
//  ⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
//  ⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
//  ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
//  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
//  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁
//
//  ┌───────────────────────────────────┐
//  │ 1 Algorithmic Toolbox             │
//  │ 2 week                            │
//  │ 1 get fibonacci number last digit │
//  └───────────────────────────────────┘
//
const readline = require("readline");
function RunAfterGetData(Run) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.on("line", (line) => {
    Run(line, rl);
  });
}
RunAfterGetData(MyCode);

// my code start from here
function MyCode(line, r1) {
  let number = line.split(" ")[0];
  console.log(fibonacci(number));
  r1.close;
}

function fibonacci(number) {
  if (number <= 1) {
    return number;
  }
  let fibonacci_array = [0, 1];
  for (let i = 2; i <= number; i++) {
    fibonacci_array[i] = (fibonacci_array[i - 1] + fibonacci_array[i - 2]) % 10;
  }
  //console.log(fibonacci_array[number]);
  return fibonacci_array[number];
}



// ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
// ║                                                                                                                                                 ║
// ║ function fibonacci(number) {                                                                                                                    ║
// ║ if (number <= 1) {                                                                                                                              ║
// ║ return number;                                                                                                                                  ║
// ║ }                                                                                                                                               ║
// ║ let fibonacci_array = [0, 1];                                                                                                                   ║
// ║ for (let i = 2; i <= number; i++) {                                                                                                             ║
// ║ fibonacci_array[i] = (fibonacci_array[i - 1] + fibonacci_array[i - 2]) % 10;                                                                    ║
// ║ }                                                                                                                                               ║
// ║ //console.log(fibonacci_array[number]);                                                                                                         ║
// ║ return fibonacci_array[number];                                                                                                                 ║
// ║ }                                                                                                                                               ║
// ║ we should find the last digit of the sum of the first n Fibonacci numbers by above function                                                     ║
// ║ but in some programming languages, if you try to find the very large Fibonacci numbers, you may get a wrong answer because of integer overflow. ║
// ║ In such cases, you should use a more efficient algorithm to find the answer.                                                                    ║
// ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
