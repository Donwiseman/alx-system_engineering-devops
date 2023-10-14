# This is a puppet command to correct an error in the wp settings.
file_line { 'replace_wp-locale':
  path    => '/var/www/html/wp-settings.php',
  line    => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );',
  match   => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );',
  replace => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
}

exec { 'restart_apache2':
  command     => '/usr/sbin/service apache2 restart',
  path        => '/usr/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'], # Ensure this file change triggers the restart
}

