#Uses pkill comman to terminate the process killmenow
exec { 'Terminate killmenow':
  command => 'pkill killmenow',
}
