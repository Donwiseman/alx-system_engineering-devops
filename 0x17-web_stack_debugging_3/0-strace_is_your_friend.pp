# This is a puppet command to correct an error in the wp settings.
exec { 'edit_wp-settings.php':
  command => 'sed -i "s/require_once( ABSPATH . WPINC . \'\/class-wp-locale.phpp\' );/require_once( ABSPATH . WPINC . \'\/class-wp-locale.php\' );/" /var/www/html/wp-settings.php',
  path    => '/bin:/usr/bin', # Set the path to ensure the 'sed' command is found
  onlyif  => 'test -f /var/www/html/wp-settings.php', # Check if the file exists before running the command
}

exec { 'restart_apache2':
  command     => '/usr/sbin/service apache2 restart',
  path        => '/usr/bin',
  refreshonly => true,
}

