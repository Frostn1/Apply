# Apply
The Apply programming language is a tiny in size, foolish language built for 1st of April.


## Conventions are as followed:
- extra points for no spaces and zero readabilty
- shut up i know i write perfect
- extra points for shitty code

## Specifications & Example Codes
- `$` printing expression coming infront of it<br>
  `$Hello world`<br>
  Prints the string "Hello world" to the screen.<br><br>
- `@` used for input<br>
  `@`<br>
  Takes input from the user<br><br>
- `|` used for assignment to variables
- `{}` used expression interpolation<br>
  `${@}`<br>
  Takes input from the user as an expression and then prints it back to the screen.<br><br>
- `?c>t~f` used for conditionals (c => conditional, t => true, f => false)<br>
  `?1>$yes~$no`<br>
  Checks wheter ***1*** is true or not and then prints ***yes*** if it is and ___no___ it is not,<br>
  in this case it will print ___yes___.<br><br>
  
- `'` single word string literal<br>
  Used for the confirmation that some constant are string literals,<br>
  instead of having the compiler deduct it
  For example the, if we take the previous code of the conditional:
  `?1>$yes~$no`
  And modify it slightly, so we use a single print command
  `${?1>yes~no}`
  This will throw an error, to be specific a<br>
  ```
  return variables[string]
  KeyError: 'yes'
  ```
  As the compiler things the following name ___yes___ is a variable name,<br>
  and tries the find its value in memory.
  To Overide this we will use the string literal specifier, as follows:
  `${?1>'yes~'no}`
  Which will now compile with out any errors,<br>and print the string ___yes___ to screen<br><br>
  
  
- `#` octothorpe is used for getting the length of a variable<br>
  Words as a builtin string utility function,<br>
  that will return the length of a given string.
  `${#'Hello}`
  Will print out ___5___ to screen.<br><br>
- `[value|identefier,...&expression(value,...)]` lambda function with self calling <br>
- `+ - * /` used for arithmetic operators
- `=` used for boolean equality
