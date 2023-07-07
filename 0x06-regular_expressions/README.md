This builds a regular expression program that prints takes a commandline argument which is printed out by the program if it is a match for the underlying regexp used in the program. it is buily using the Oniguruma library in Ruby.

Example:
the below code is has a regexp that checks the last value of a address is a number
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join

First test passes as it is printed
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2

Second test also passes as it is printed
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1

Last test fails as it's last value is a character
sylvain@ubuntu$ ./example.rb 127.0.0.a
