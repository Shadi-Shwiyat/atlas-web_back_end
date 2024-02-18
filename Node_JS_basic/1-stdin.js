// Executed in command line, prompts user for name
// if not passed in through cli

// Check if program is run without piped in command
if (process.argv.length == 2 && process.stdin.isTTY) {
  console.log("Welcome to Holberton School, what is your name?");

  // Listen for user input
  process.stdin.on('readable', () => {
      const userName = process.stdin.read();
      if (userName !== null) {
          process.stdout.write(`Your name is: ${userName}`);
      }
  });
} else {
  // Listen for data on stdin stream (echo command pipe)
  process.stdin.on('data', (data) => {
    // console.log('about to trim');
    const userName = data.toString().trim()

    console.log("Welcome to Holberton School, what is your name?");
    console.log('Your name is:', userName);
    console.log("This important software is now closing");
  });
}
