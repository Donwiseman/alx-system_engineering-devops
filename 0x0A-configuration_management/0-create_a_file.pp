#This creates a file called school in the /tmp folder with some contents.
file { '/tmp/school':
  ensure   => file,
  path     => '/tmp/school',
  checksum => md5,
  content  => 'I love Puppet',
  group    => 'www-data',
  mode     => '0744',
  owner    => 'www-data',
}
