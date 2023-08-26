#Uses pkill comman to terminate the process killmenow
exec { 'Terminate_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
}
