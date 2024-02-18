// Executed in command line, prompts user for name
// if not passed in through cli

process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', function() {
  var userName = process.stdin.read();
  if (userName !== null) {
    process.stdout.write(`Your name is: ${userName}`);
  }
});

process.stdin.on('end', function() {
  process.stdout.write('This important software is now closing\n');
});
