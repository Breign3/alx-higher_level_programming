#!/usr/bin/node

const argument = process.argv[2];  
const num = parseInt(argument, 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences'); 
} else {
  (function printMessage(n, message) {  
    if (n > 0) { 
      console.log(message);
      printMessage(n - 1, message); 
    }
  })(num, 'C is fun');
}

