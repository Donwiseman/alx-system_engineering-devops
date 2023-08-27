# This configures the ssh_config file to ensure it does not allow password
# Authentication and uses the ~/.ssh/school private key.
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "Include /etc/ssh/ssh_config.d/*.conf\n
  Host *\n
    PasswordAuthentication no\n
    IdentityFile ~/.ssh/school\n
    SendEnv LANG LC_*\n
    HashKnownHosts yes\n
    GSSAPIAuthentication yes\n",
}
